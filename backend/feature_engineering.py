import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def extract_full_features(df: pd.DataFrame) -> pd.DataFrame:
    required_cols = [
        "cycle",
        "Capacity",
        "Voltage_measured",
        "Current_measured",
        "Temperature_measured",
        "Time"
    ]

    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required raw columns: {missing}")

    df = df.copy()
    df = df.sort_values(["cycle", "Time"])

    # Capacity features
    df["initial_capacity"] = df.groupby("cycle")["Capacity"].transform("first")
    df["capacity_ratio"] = df["Capacity"] / df["initial_capacity"]
    df["capacity_diff"] = df.groupby("cycle")["Capacity"].diff().fillna(0)

    # Degradation slope per battery (using all cycles)
    cycle_capacity = df.groupby("cycle")["Capacity"].mean().reset_index()

    X_lr = cycle_capacity["cycle"].values.reshape(-1, 1)
    y_lr = cycle_capacity["Capacity"].values

    lr = LinearRegression()
    lr.fit(X_lr, y_lr)
    degradation_slope = lr.coef_[0]

    # Rolling slope 10
    rolling_slope_10 = (
        cycle_capacity["Capacity"]
        .rolling(10)
        .apply(lambda x: np.polyfit(range(len(x)), x, 1)[0], raw=False)
        .iloc[-1]
    )

    # Last cycle time-series features
    last_cycle = df["cycle"].max()
    df_last = df[df["cycle"] == last_cycle]

    discharge_time = df_last["Time"].iloc[-1] - df_last["Time"].iloc[0]
    temperature_variance = df_last["Temperature_measured"].var()

    X_time = df_last["Time"].values.reshape(-1, 1)
    y_volt = df_last["Voltage_measured"].values
    lr_v = LinearRegression()
    lr_v.fit(X_time, y_volt)
    voltage_slope = lr_v.coef_[0]

    v_std = df_last["Voltage_measured"].std()
    i_std = df_last["Current_measured"].std()
    internal_resistance_proxy = v_std / i_std if i_std != 0 else 0

    voltage_drop = (
        df_last["Voltage_measured"].iloc[0]
        - df_last["Voltage_measured"].iloc[-1]
    )

    mean_temperature = df_last["Temperature_measured"].mean()

    # Last cycle capacity values
    last_capacity = df_last["Capacity"].iloc[-1]
    last_capacity_ratio = df_last["capacity_ratio"].iloc[-1]
    last_capacity_diff = df_last["capacity_diff"].iloc[-1]

    feature_vector = pd.DataFrame([{
        "Capacity": last_capacity,
        "capacity_ratio": last_capacity_ratio,
        "capacity_diff": last_capacity_diff,
        "degradation_slope": degradation_slope,
        "avg_discharge_time": discharge_time,
        "temperature_variance": temperature_variance,
        "voltage_slope": voltage_slope,
        "internal_resistance_proxy": internal_resistance_proxy,
        "voltage_drop": voltage_drop,
        "mean_temperature": mean_temperature,
        "rolling_slope_10": rolling_slope_10
    }])

    return feature_vector
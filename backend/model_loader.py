import joblib
import os

def load_model():
    """
    Load the actual trained Random Forest model from the .pkl file.
    Falls back to DummyModel if the file doesn't exist or is corrupted.
    """
    model_path = os.path.join(os.path.dirname(__file__), "models", "secondspark_full_pipeline.pkl")
    
    try:
        if os.path.exists(model_path):
            pipeline = joblib.load(model_path)
            return pipeline["model"]
        else:
            print(f"Warning: Model file not found at {model_path}, using DummyModel")
            return DummyModel()
    except Exception as e:
        print(f"Error loading model: {e}, using DummyModel")
        return DummyModel()

class DummyModel:
    def predict(self, X):
        # Simple logic for demo:
        # More degradation slope → lower RUL
        slope = X[0][6] if len(X[0]) > 6 else 0
        base_rul = 5
        adjusted_rul = base_rul + slope * 10
        return [max(0.5, adjusted_rul)]
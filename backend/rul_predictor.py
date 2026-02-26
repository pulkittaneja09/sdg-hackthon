import numpy as np


def predict_rul_with_confidence(model, X):
    tree_preds = np.array([
        tree.predict(X) for tree in model.estimators_
    ])

    mean_pred = np.mean(tree_preds)
    std_pred = np.std(tree_preds)

    confidence = max(0, 100 - std_pred * 10)

    return {
        "predicted_rul": round(float(mean_pred), 2),
        "confidence_score": round(float(confidence), 2)
    }
# backend/deployment_engine.py

"""
Deployment Grading Engine

This module assigns:
- Grade (A / B / C)
- Risk level
- Recommended use case

Based on:
- Predicted RUL
- State of Health (SOH)
"""

def recommend_deployment(rul: float, soh: float) -> dict:
    """
    Assign grade and deployment recommendation
    based on predicted RUL and SOH.
    """

    if rul >= 60 and soh >= 0.85:
        return {
            "grade": "A",
            "risk_level": "Low",
            "recommendation": "Suitable for Community Solar Grid Storage"
        }

    elif rul >= 30 and soh >= 0.75:
        return {
            "grade": "B",
            "risk_level": "Moderate",
            "recommendation": "Suitable for Commercial Backup or Microgrid Storage"
        }

    else:
        return {
            "grade": "C",
            "risk_level": "High",
            "recommendation": "Recommended for Recycling"
        }
import pandas as pd
import numpy as np

from src.artifact_handling import detect_motion_artifacts, clean_vitals


def test_motion_artifact_detection():
    """
    High motion + sudden SpO2 drop should be flagged as artifact
    """
    data = {
        "heart_rate": [80, 82, 85, 88],
        "spo2": [98, 97, 80, 79],   # sudden drop
        "bp_sys": [120, 120, 118, 118],
        "bp_dia": [80, 80, 78, 78],
        "motion": [0.2, 0.3, 1.8, 1.9]
    }

    df = pd.DataFrame(data)
    result = detect_motion_artifacts(df, motion_threshold=1.0)
    print(result)

    assert result["artifact_detected"].iloc[2] == 1
    assert result["artifact_detected"].iloc[3] == 1


def test_cleaning_interpolates_missing_values():
    """
    Missing HR / SpO2 values should be interpolated
    """
    data = {
        "heart_rate": [80, np.nan, np.nan, 85],
        "spo2": [98, np.nan, 95, 94],
        "bp_sys": [120, 120, 120, 120],
        "bp_dia": [80, 80, 80, 80],
        "motion": [0.1, 0.1, 0.1, 0.1]
    }

    df = pd.DataFrame(data)
    cleaned = clean_vitals(df)

    assert cleaned["heart_rate"].isna().sum() == 0
    assert cleaned["spo2"].isna().sum() == 0

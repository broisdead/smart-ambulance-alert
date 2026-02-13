import pandas as pd
import numpy as np

def compute_anomaly_score(df, alpha=0.3):
    """
    EWMA-based anomaly score
    """
    df = df.copy()

    ewma_hr = df["heart_rate"].ewm(alpha=alpha).mean()
    ewma_spo2 = df["spo2"].ewm(alpha=alpha).mean()

    hr_dev = abs(df["heart_rate"] - ewma_hr)
    spo2_dev = abs(df["spo2"] - ewma_spo2)

    df["anomaly_score"] = hr_dev + (2 * spo2_dev)
    return df

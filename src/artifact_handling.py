import pandas as pd
import numpy as np

def detect_motion_artifacts(df, motion_threshold=1.0):
    df = df.copy()

    df["artifact_detected"] = (
        (df["motion"] > motion_threshold) &
        (df["spo2"].diff().abs() > 4)
    ).astype(int)

    return df



def clean_vitals(df):
    df = df.copy()
    df = detect_motion_artifacts(df)

    # Ensure numeric
    df["spo2"] = pd.to_numeric(df["spo2"], errors="coerce")
    df["heart_rate"] = pd.to_numeric(df["heart_rate"], errors="coerce")

    # Interpolate first
    df["spo2"] = df["spo2"].interpolate(limit_direction="both")

    # Smooth SpO2
    smooth = df["spo2"].rolling(
        window=15, center=True, min_periods=1
    ).median()

    # Replace only artifact rows
    mask = df["artifact_detected"] == 1
    df.loc[mask, "spo2"] = smooth.loc[mask]

    return df



if __name__ == "__main__":
    raw = pd.read_csv("/Users/aiyan/Desktop/smart-ambulance-alert/data/raw/synthetic_ambulance_vitals.csv")
    clean = clean_vitals(raw)
    clean.to_csv("/Users/aiyan/Desktop/smart-ambulance-alert/data/processed/vitals_cleaned.csv", index=False)

import pandas as pd

def add_rolling_features(df, window=30):
    df = df.copy()

    df["hr_mean"] = df["heart_rate"].rolling(window).mean()
    df["hr_trend"] = df["heart_rate"].diff(window)

    df["spo2_mean"] = df["spo2"].rolling(window).mean()
    df["spo2_trend"] = df["spo2"].diff(window)

    df["bp_sys_trend"] = df["bp_sys"].diff(window)

    return df

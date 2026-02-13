import numpy as np

def compute_risk_score(df):
    df = df.copy()

    hr_risk = np.clip((df["heart_rate"] - 100) / 40, 0, 1)
    spo2_risk = np.clip((95 - df["spo2"]) / 10, 0, 1)
    bp_risk = np.clip((110 - df["bp_sys"]) / 30, 0, 1)

    df["risk_score"] = (
        0.4 * hr_risk +
        0.4 * spo2_risk +
        0.2 * bp_risk
    )

    df["alert"] = (df["risk_score"] > 0.7).astype(int)
    return df

import pandas as pd

def analyze_alerts(alerts_df):
    summary = {}

    summary["total_alerts"] = alerts_df["alert_triggered"].sum()
    summary["alerts_during_artifacts"] = (
        (alerts_df["alert_triggered"] == 1) &
        (alerts_df["artifact_detected"] == 1)
    ).sum()

    summary["false_alerts"] = (
        (alerts_df["alert_triggered"] == 1) &
        (alerts_df["true_event"] == 0)
    ).sum()

    summary["missed_events"] = (
        (alerts_df["alert_triggered"] == 0) &
        (alerts_df["true_event"] == 1)
    ).sum()

    return summary


if __name__ == "__main__":
    df = pd.read_csv("data/evaluation/alerts_log.csv")
    results = analyze_alerts(df)

    for k, v in results.items():
        print(f"{k}: {v}")

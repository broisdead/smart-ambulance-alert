import pandas as pd
import numpy as np

def compute_metrics(alerts_df):
    """
    Computes alert quality metrics
    """
    tp = ((alerts_df["alert_triggered"] == 1) &
          (alerts_df["true_event"] == 1)).sum()

    fp = ((alerts_df["alert_triggered"] == 1) &
          (alerts_df["true_event"] == 0)).sum()

    fn = ((alerts_df["alert_triggered"] == 0) &
          (alerts_df["true_event"] == 1)).sum()

    precision = tp / (tp + fp + 1e-6)
    recall = tp / (tp + fn + 1e-6)

    false_alert_rate = fp / len(alerts_df)

    return {
        "precision": round(precision, 3),
        "recall": round(recall, 3),
        "false_alert_rate": round(false_alert_rate, 3)
    }


def compute_alert_latency(alerts_df):
    """
    Measures delay between true event start and first alert
    """
    latencies = []

    for pid in alerts_df["patient_id"].unique():
        patient = alerts_df[alerts_df["patient_id"] == pid]

        event_times = patient[patient["true_event"] == 1]["timestamp"]
        alert_times = patient[patient["alert_triggered"] == 1]["timestamp"]

        if not event_times.empty and not alert_times.empty:
            latency = alert_times.min() - event_times.min()
            if latency >= 0:
                latencies.append(latency)

    return {
        "mean_latency_sec": round(np.mean(latencies), 2) if latencies else None,
        "max_latency_sec": max(latencies) if latencies else None
    }


if __name__ == "__main__":
    df = pd.read_csv("/Users/aiyan/Desktop/smart-ambulance-alert/data/evaluation/alerts_log.csv")
    print(compute_metrics(df))
    print(compute_alert_latency(df))

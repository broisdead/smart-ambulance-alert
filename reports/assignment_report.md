# Smart Ambulance Alert System  
Gray Mobility – AI/ML Engineer Internship Assignment  

---

## 1. Problem Overview

This project implements a time-series monitoring and alerting system for
ambulance patient transport. Vital signs (HR, SpO₂, BP, motion) are streamed
at 1 Hz and must be analyzed in real-time under noisy conditions.

The goal is not perfect prediction accuracy, but robust and safe early warning
behavior under motion artifacts and sensor imperfections.

---

## 2. Data Generation

Synthetic data was generated for 30 minutes per patient, sampled at 1 Hz.
Each sequence includes:

- Normal transport
- Motion-induced sensor artifacts
- Gradual physiological deterioration
- Missing data segments

Distress scenarios include:
- HR increase (tachycardia trend)
- SpO₂ decline
- BP reduction

Motion artifacts include:
- Transient SpO₂ drops during high vibration
- HR spikes during bumps
- Short missing segments

Ground-truth labels (`true_event`, `artifact_flag`) were retained for evaluation
but not used during inference.

---

## 3. Artifact Handling

Artifact detection is performed before anomaly detection.

Detection logic:
- High motion + sudden SpO₂ drop
- Missing data segments

Correction strategy:
- Rolling median smoothing for artifacts
- Interpolation for short missing segments

Raw vs cleaned signal comparison confirms that:
- Non-physiological drops are suppressed
- True deterioration trends remain visible

This step is critical in preventing false alerts.

---

## 4. Anomaly Detection

Anomaly detection uses an EWMA-based deviation model.

Rationale:
- Interpretable
- Computationally lightweight
- Sensitive to trend deviations rather than static thresholds

Anomaly score combines:
- HR deviation
- Weighted SpO₂ deviation

This enables early detection of gradual deterioration.

---

## 5. Risk Scoring

A triage-style risk score combines:

- HR risk component
- SpO₂ risk component
- BP risk component

Risk score ∈ [0, 1]

Alerts trigger when:

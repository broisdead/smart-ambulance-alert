# Smart Ambulance Alert System  
AI/ML Engineer Intern Assignment – Gray Mobility

This project implements a safety-aware time-series alerting system for
ambulance patient monitoring.

It includes:
- Synthetic realistic ambulance vital generation
- Explicit artifact detection & correction
- Early anomaly detection (trend-based)
- Risk scoring logic for triage
- Alert quality evaluation
- FastAPI inference service
- Unit testing for artifact handling

---

## 📂 Project Structure

smart-ambulance-alert/
│
├── api/ # FastAPI service
├── data/ # Raw, processed & evaluation outputs
├── src/ # Core ML logic
├── evaluation/ # Metrics & failure analysis
├── tests/ # Unit tests
├── notebooks/ # Exploration (visual only)
└── reports/ # Figures & assignment report


---

## ⚙️ Setup Instructions

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt

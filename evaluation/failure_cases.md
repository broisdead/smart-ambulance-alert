# Failure Case Analysis

This section analyzes key failure modes observed during evaluation of the
ambulance alert system.

---

## Case 1: Motion-Induced False Alert

**What happened:**  
During high vehicle motion (speed bumps / turns), transient SpO₂ drops
combined with HR spikes triggered elevated anomaly scores.

**Why it failed:**  
Although artifact detection was present, the risk score aggregation
overweighted short-term deviations.

**Impact:**  
False alerts increase cognitive load on paramedics and may reduce trust.

**Mitigation:**  
- Increase minimum duration for alert confirmation  
- Suppress alerts when artifact confidence is high  
- Weight motion-aware confidence more strongly  

---

## Case 2: Late Detection of Gradual Deterioration

**What happened:**  
Slow HR rise and BP decline crossed risk thresholds several minutes
after the true deterioration onset.

**Why it failed:**  
EWMA smoothing delayed response to low-frequency trends.

**Impact:**  
Late alerts reduce available intervention time.

**Mitigation:**  
- Add slope-based trend features  
- Use multi-window anomaly scoring  
- Lower alert threshold during sustained trend detection  

---

## Case 3: Missed Alert During Data Dropout

**What happened:**  
Missing SpO₂ and HR data during critical periods suppressed anomaly scores.

**Why it failed:**  
Interpolation smoothed over clinically important uncertainty.

**Impact:**  
Missed alerts are the most dangerous failure mode.

**Mitigation:**  
- Treat prolonged missing data as a risk factor  
- Raise alert confidence uncertainty  
- Alert on data quality degradation  

---

## Safety Reflection

False positives are inconvenient but recoverable.
Missed detections during deterioration are unacceptable.

Human oversight must remain mandatory for all medical alerts.

# Cybersecurity Shield: ML Network Intrusion Detector 🛡️

An automated Machine Learning-based Network Intrusion Detection System (NIDS) designed to classify network packet flows in real-time. This system uses supervised machine learning to identify malicious traffic patterns (such as Port Scans, DoS attacks, and Data Exfiltration) and differentiate them from normal network activities.

---

## 📌 Project Overview
Traditional signature-based Firewalls and IDSs often fail to detect novel, zero-day attacks because they rely strictly on predefined rules. 

**Cybersecurity Shield** solves this problem by analyzing telemetry flow metrics—such as connection duration, bytes transferred, and host connection rates—using a **Random Forest Classifier** to continuously evaluate network posture and flag anomalous traffic.

---

## 🚀 Key Features
- **High Accuracy Classification:** Achieves **92.50%+ accuracy** on network flow evaluation.
- **Zero-Day Detection:** Leverages behavioral pattern recognition rather than static signatures.
- **Real-Time Predictions:** Classifies sample packet flows in sub-second timelines.
- **Clean Feature Processing:** Native support for structured feature data frames without runtime warnings.

---

## 📊 Feature Telemetry Schema

The ML classifier evaluates incoming traffic based on four core network metrics:

| Feature | Type | Description | Normal Range |
| :--- | :--- | :--- | :--- |
| `duration` | Integer | Connection length in seconds | `0 - 60 seconds` |
| `src_bytes` | Integer | Payload bytes sent from client to server | `100 - 3,000 bytes` |
| `dst_bytes` | Integer | Payload bytes returned from server | `100 - 8,000 bytes` |
| `count` | Integer | Host connection frequency in a 2-sec window | `1 - 20 connections` |

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.x
- **Libraries:**
  - `numpy` (Numerical operations)
  - `pandas` (Dataset structuring)
  - `scikit-learn` (Random Forest ML algorithm)

---

## 💻 Installation & Setup

### Option 1: Google Colab (Recommended)
1. Go to [Google Colab](https://colab.research.google.com/).
2. Click **New Notebook**.
3. Copy and paste the code from `intrusion_detector.py` into the cell.
4. Click **Play (▶️)** to train and test the model instantly.

### Option 2: Local Setup
1. Clone or download this repository.
2. Open terminal/command prompt and install dependencies:
   ```bash
   pip install numpy pandas scikit-learn
   ```
3. Run the Python script:
   ```bash
   python intrusion_detector.py
   ```

---

## 🧪 Example Output

```text
=== Cybersecurity Shield: Network Intrusion Detector ===

[*] Training Random Forest Classifier model...
[+] Model training completed successfully!

--- Model Evaluation Report ---
Accuracy Score: 92.50%

[*] Testing model with live network packet flows:
  - Packet 1 (Normal Flow) Prediction : Normal Traffic ✅
  - Packet 2 (Suspicious Flow) Prediction: Anomaly/Attack 🚨
```

---

## 📄 License
This project is open-source and intended for educational and bootcamp demonstration purposes.
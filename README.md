
# 🧠 SAP Log Intelligence Dashboard with Anomaly Detection

This project simulates a real-world SAP Basis log monitoring workflow and applies data science techniques to detect unusual system behaviors.

---

## 🚀 Project Overview

In SAP Basis administration, system logs are constantly reviewed to monitor:
- Login patterns
- System restarts
- Transport events
- Errors and failures

This project simulates SAP log data and applies **anomaly detection** using `Isolation Forest` to flag potentially suspicious events.

The dashboard is built using **Streamlit** with a modern UI, combining enterprise system simulation and machine learning.

---

## 🛠️ Tech Stack

- Python (Pandas, Scikit-learn, Matplotlib, Seaborn)
- Streamlit
- Isolation Forest (unsupervised anomaly detection)
- CSV simulation of SAP-like logs

---

## 📊 Dashboard Features

- KPI cards for total logs, users, and detected anomalies
- Event-type based filtering
- Color-coded anomaly highlighting
- Timeline plot of anomalies across different event types

---

## 📁 Files

| File | Description |
|------|-------------|
| `sap_logs_with_anomalies.csv` | Simulated SAP system log data with anomaly labels |
| `sap_log_anomaly_dashboard_modern.py` | Streamlit dashboard script (modern layout) |
| `sap_log_anomaly_dashboard.py` | Original version of the dashboard script |

---

## 🧪 How to Run

1. Clone/download the repo
2. Install dependencies:
   ```bash
   pip install streamlit pandas scikit-learn matplotlib seaborn
   ```
3. Run the dashboard:
   ```bash
   streamlit run sap_log_anomaly_dashboard_modern.py
   ```

---

## 📌 Use Case

This project bridges **Data Science and SAP Basis**, perfect for:
- Beginners exploring SAP + analytics
- Portfolio projects for consulting/infra/analytics roles
- Understanding real-world enterprise log monitoring

---

## 🙋‍♂️ Author

**Arkajyoti Sarkar**  
B.Tech in CSE (Data Science)  
[LinkedIn](https://www.linkedin.com/in/arkajyoti-sarkar-45254b219/) • [GitHub](https://github.com/ToX-09)

---



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="SAP Log Intelligence", layout="wide")

# Load dataset
df = pd.read_csv("sap_logs_with_anomalies.csv", parse_dates=["Timestamp"])

st.title("📊 SAP Log Intelligence Dashboard")
st.markdown("A hybrid SAP Basis + Data Science project for monitoring and anomaly detection in simulated enterprise logs.")

# KPI Cards
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Events", len(df))
with col2:
    st.metric("Unique Users", df['User'].nunique())
with col3:
    st.metric("Detected Anomalies", sum(df['Anomaly'] == 'Anomaly'))

st.markdown("---")

# Filter and table
st.subheader("🔎 Event Type Filter and Anomaly Tagging")
selected_event = st.selectbox("Select an Event Type", sorted(df['Event_Type'].unique()))
filtered_df = df[df['Event_Type'] == selected_event]

# Color tag for anomaly
def color_anomaly(val):
    return 'background-color: #ffcccc' if val == 'Anomaly' else ''

st.dataframe(filtered_df.style.applymap(color_anomaly, subset=['Anomaly']))

st.markdown("---")

# Anomaly distribution bar chart
st.subheader("📊 Anomaly vs Normal Log Count")
anomaly_counts = df['Anomaly'].value_counts()
st.bar_chart(anomaly_counts)

# Anomaly timeline
st.subheader("🧨 Anomaly Timeline")
anomaly_df = df[df['Anomaly'] == 'Anomaly']
fig, ax = plt.subplots()
sns.scatterplot(data=anomaly_df, x='Timestamp', y='Event_Type', hue='User', ax=ax, palette="tab10")
ax.set_title("Detected Anomalies Over Time")
st.pyplot(fig)

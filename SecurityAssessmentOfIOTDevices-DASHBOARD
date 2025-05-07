
import streamlit as st
import pandas as pd
from datetime import datetime
import random
import plotly.express as px

st.set_page_config(page_title="IoT Camera Intrusion Detection", layout="wide")

st.title("📹 IoT Camera Intrusion Detection Dashboard")
st.markdown("Real-time logging, alerting, and visualization of unauthorized access attempts.")

# Initialize log storage
if "log_data" not in st.session_state:
    st.session_state.log_data = []

# Simulate an access attempt
if st.button("🔍 Simulate Access Attempt"):
    ip = f"192.168.1.{random.randint(2, 254)}"
    status = random.choices(["SUCCESS", "FAILED", "BLOCKED"], weights=[0.3, 0.6, 0.1])[0]
    timestamp = datetime.now()
    st.session_state.log_data.append({"Timestamp": timestamp, "IP Address": ip, "Status": status})

# Convert to DataFrame
if st.session_state.log_data:
    df = pd.DataFrame(st.session_state.log_data)

    # Add risk score
    def risk_level(status):
        return {"SUCCESS": "🟢 Low", "FAILED": "🟠 Medium", "BLOCKED": "🔴 High"}.get(status, "Unknown")
    df["Risk Level"] = df["Status"].apply(risk_level)

    st.subheader("📋 Access Log")
    st.dataframe(df)

    # Alerts
    if (df["Status"] == "FAILED").sum() >= 3:
        st.warning("⚠️ Multiple failed access attempts detected! Possible brute-force attack.")
    if (df["Status"] == "BLOCKED").sum() > 0:
        st.error("⛔ IPs have been blocked due to suspicious behavior.")

    # Plot attacks over time
    st.subheader("📈 Access Attempt Timeline")
    timeline = df.copy()
    timeline["Minute"] = timeline["Timestamp"].dt.strftime("%H:%M:%S")
    count_by_minute = timeline.groupby(["Minute", "Status"]).size().reset_index(name="Count")
    fig = px.bar(count_by_minute, x="Minute", y="Count", color="Status", barmode="group", title="Access Attempts Over Time")
    st.plotly_chart(fig, use_container_width=True)

    # Download logs
    csv = df.to_csv(index=False)
    st.download_button("⬇️ Download Logs", csv, "access_logs.csv", mime="text/csv")
else:
    st.info("Click 'Simulate Access Attempt' to start logging activity.")


import streamlit as st
import pandas as pd
from datetime import datetime
import random

st.set_page_config(page_title="IoT Camera Security Dashboard", layout="wide")

st.title("📹 IoT Camera Intrusion Detection Dashboard")
st.markdown("Monitor and detect unauthorized access attempts on your smart camera.")

# Simulated log storage
if "log_data" not in st.session_state:
    st.session_state.log_data = []

# Simulate an access attempt
if st.button("🔍 Simulate Access Attempt"):
    ip = f"192.168.1.{random.randint(2, 254)}"
    status = random.choices(["SUCCESS", "FAILED", "BLOCKED"], weights=[0.3, 0.6, 0.1])[0]
    st.session_state.log_data.append({"Timestamp": datetime.now(), "IP Address": ip, "Status": status})

# Display access log
if st.session_state.log_data:
    df = pd.DataFrame(st.session_state.log_data)
    st.subheader("📄 Access Logs")
    st.dataframe(df)

    # Alerts
    failed_attempts = df[df["Status"] == "FAILED"]
    if len(failed_attempts) >= 3:
        st.warning("⚠️ Multiple failed access attempts detected! Possible brute-force attack.")
    blocked_attempts = df[df["Status"] == "BLOCKED"]
    if not blocked_attempts.empty:
        st.error("⛔ IPs have been blocked due to suspicious behavior.")

# Optional: Export logs
if st.session_state.log_data:
    st.download_button("⬇️ Download Logs", pd.DataFrame(st.session_state.log_data).to_csv(index=False), "camera_access_logs.csv")

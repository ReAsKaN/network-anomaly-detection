import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="SOC Monitor", layout="wide")

if "dataset" not in st.session_state:
    df = pd.read_csv("UNSW_NB15_testing-set.csv")
    df = df.sample(frac=1).reset_index(drop=True)
    st.session_state.dataset = df
    st.session_state.current_row = 0
    st.session_state.auto_mode = False

st.markdown("<h1 style='text-align: center; color: #00ffcc;'>🛡️ Zero-Trust Network Monitor</h1>", unsafe_allow_html=True)
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Inspect Next Packet", use_container_width=True):
        st.session_state.auto_mode = False
        if st.session_state.current_row < len(st.session_state.dataset) - 1:
            st.session_state.current_row += 1

with col2:
    if st.button("Start Auto Flow", use_container_width=True):
        st.session_state.auto_mode = True

with col3:
    if st.button("Stop Auto Flow", use_container_width=True):
        st.session_state.auto_mode = False

if st.session_state.current_row >= 0:
    processed_df = st.session_state.dataset.iloc[:st.session_state.current_row + 1].copy()
else:
    processed_df = st.session_state.dataset.iloc[0:0].copy()

total_analyzed = len(processed_df)
detected_anomalies = int(processed_df['label'].sum()) if total_analyzed > 0 else 0
secure_packets = total_analyzed - detected_anomalies
security_score = ((total_analyzed - detected_anomalies) / total_analyzed * 100) if total_analyzed > 0 else 100.0

stat1, stat2, stat3, stat4 = st.columns(4)

stat1.metric("Analyzed Packets", total_analyzed)
stat2.metric("Detected Anomalies", detected_anomalies)
stat3.metric("Secure Packets", secure_packets)
stat4.metric("Security Score %", f"{security_score:.2f}%")

st.markdown("<br>", unsafe_allow_html=True)

display_df = processed_df.copy()

def highlight_rows(row):
    if row['Threat Status'] == '🚨 ALERT':
        return ['background-color: rgba(255, 75, 75, 0.15)'] * len(row)
    return ['background-color: rgba(75, 255, 75, 0.1)'] * len(row)

if not display_df.empty:
    display_df['Threat Status'] = display_df['label'].apply(lambda x: "🚨 ALERT" if x == 1 else "✅ SECURE")
    
    display_columns = ['id', 'proto', 'service', 'state', 'dur', 'rate', 'sttl', 'dload', 'Threat Status']
    display_df = display_df[display_columns]
    
    styled_df = display_df.style.apply(highlight_rows, axis=1)
    st.dataframe(styled_df, use_container_width=True, height=500)
else:
    st.dataframe(display_df, use_container_width=True, height=500)

if st.session_state.auto_mode:
    if st.session_state.current_row < len(st.session_state.dataset) - 1:
        st.session_state.current_row += 1
        time.sleep(0.15)
        st.rerun()
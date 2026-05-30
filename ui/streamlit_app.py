"""Streamlit demo UI — engineer-facing dashboard.

Phase-7 stub. Implement in Week 11.

Will provide:
  - Scenario picker (50 faults)
  - Live agent reasoning log (think -> act -> observe)
  - Diff viewer for proposed config changes
  - Approval gate for high-risk actions
  - Audit log replay

Run with:
    streamlit run ui/streamlit_app.py
"""

import streamlit as st


st.set_page_config(page_title="NetAgent — Demo", page_icon="🤖", layout="wide")

st.title("🤖 NetAgent — Adaptive LLM Agent for Network Fault Remediation")
st.markdown(
    "_Adaptive Clarification for LLM Agents: A Risk-Weighted Approach to Network Fault Remediation_"
)

st.info("🚧 UI is a Phase-7 placeholder. Full implementation in Week 11.")

st.header("Pick a scenario")
scenarios = ["bgp_md5_mismatch_r1_r2", "ospf_mtu_mismatch_r1_r3", "vlan_trunk_mismatch_sw1_sw2"]
choice = st.selectbox("Fault scenario", scenarios)

if st.button("▶️  Run agent"):
    st.write(f"Would run NetAgent on scenario: **{choice}**")
    st.write("Live trace will appear here in Week 11.")

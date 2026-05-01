import streamlit as st

st.set_page_config(layout="wide", page_title="FitSync", page_icon="⚡")

st.markdown("""
<style>
.block-container {
    padding-top: 2.5rem;
    max-width: 1200px;
}

.hero {
    background: radial-gradient(circle at top left, #22c55e55, transparent 30%),
                linear-gradient(135deg, #020617, #0f172a, #064e3b);
    padding: 60px 50px;
    border-radius: 32px;
    border: 1px solid rgba(34,197,94,0.35);
    box-shadow: 0 0 45px rgba(34,197,94,0.18);
    margin-bottom: 35px;
}

.badge {
    display: inline-block;
    background: rgba(34,197,94,0.15);
    color: #86efac;
    border: 1px solid rgba(34,197,94,0.5);
    padding: 8px 18px;
    border-radius: 999px;
    font-weight: 700;
    margin-bottom: 20px;
}

.hero h1 {
    font-size: 70px;
    line-height: 1;
    font-weight: 900;
    color: white;
    margin: 0;
}

.hero h1 span {
    color: #22c55e;
}

.hero p {
    font-size: 22px;
    color: #d1fae5;
    margin-top: 18px;
    max-width: 760px;
}

.card {
    background: linear-gradient(145deg, #0f172a, #111827);
    border: 1px solid rgba(148,163,184,0.22);
    border-radius: 26px;
    padding: 32px;
    min-height: 250px;
    box-shadow: 0 14px 35px rgba(0,0,0,0.35);
    transition: all 0.25s ease;
}

.card:hover {
    transform: translateY(-7px);
    border-color: #22c55e;
    box-shadow: 0 18px 45px rgba(34,197,94,0.18);
}

.icon {
    font-size: 48px;
    margin-bottom: 14px;
}

.card h3 {
    color: #f8fafc;
    font-size: 30px;
    margin-bottom: 12px;
}

.card p {
    color: #cbd5e1;
    font-size: 16px;
    line-height: 1.6;
}

.tag {
    display: inline-block;
    margin-top: 18px;
    background: rgba(34,197,94,0.12);
    color: #86efac;
    padding: 7px 13px;
    border-radius: 999px;
    font-size: 14px;
    font-weight: 700;
}

.panel {
    margin-top: 35px;
    background: linear-gradient(90deg, #022c22, #0f172a);
    border: 1px solid rgba(34,197,94,0.25);
    padding: 26px 30px;
    border-radius: 24px;
    color: white;
}

.panel h3 {
    margin: 0 0 8px 0;
    color: #86efac;
    font-size: 26px;
}

.panel p {
    margin: 0;
    color: #d1fae5;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="badge">PERSONAL HEALTH ANALYTICS</div>
    <h1>⚡ Fit<span>Sync</span></h1>
    <p>
        Explore your wellness data with interactive dashboards, trend analysis,
        and time-range filters built to make your health patterns easier to understand.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="icon">📊</div>
        <h3>Dashboard</h3>
        <p>
            View your average steps, sleep, recovery score, calories burned,
            and health relationships in one clean analytics view.
        </p>
        <div class="tag">Main metrics</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="icon">📈</div>
        <h3>Trends</h3>
        <p>
            Review summary statistics, monthly recovery trends, and distribution
            charts to understand long-term progress.
        </p>
        <div class="tag">Insights over time</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="icon">🧭</div>
        <h3>Filters</h3>
        <p>
            Use the sidebar filter to change the time range and instantly update
            the dashboard and trend visualizations.
        </p>
        <div class="tag">All time / custom range</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="panel">
    <h3>Start exploring</h3>
    <p>
        Open the sidebar, choose a time range, then visit Dashboard or Trends
        to analyze your personal health data.
    </p>
</div>
""", unsafe_allow_html=True)

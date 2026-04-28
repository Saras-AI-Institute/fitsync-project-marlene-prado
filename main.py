import streamlit as st

st.set_page_config(layout="wide", page_title="FitSync", page_icon="⚡")

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}

.hero {
    background: linear-gradient(135deg, #052e16, #064e3b, #0f172a);
    padding: 55px 45px;
    border-radius: 30px;
    box-shadow: 0 0 35px rgba(34,197,94,0.25);
    text-align: center;
    margin-bottom: 45px;
    border: 1px solid rgba(34,197,94,0.35);
}

.hero h1 {
    font-size: 72px;
    font-weight: 900;
    color: #ffffff;
    margin-bottom: 5px;
}

.hero span {
    color: #22c55e;
}

.hero p {
    font-size: 22px;
    color: #d1fae5;
}

.badge {
    display: inline-block;
    background: rgba(34,197,94,0.15);
    color: #86efac;
    border: 1px solid #22c55e;
    padding: 8px 18px;
    border-radius: 999px;
    margin-bottom: 20px;
    font-weight: 600;
}

.card {
    background: rgba(15,23,42,0.95);
    padding: 32px;
    border-radius: 26px;
    border: 1px solid rgba(34,197,94,0.35);
    box-shadow: 0 12px 35px rgba(0,0,0,0.35);
    transition: all 0.25s ease;
    min-height: 230px;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 18px 45px rgba(34,197,94,0.25);
    border-color: #22c55e;
}

.icon {
    font-size: 48px;
    margin-bottom: 12px;
}

.card h3 {
    color: #22c55e;
    font-size: 30px;
    margin-bottom: 12px;
}

.card p {
    color: #e5e7eb;
    font-size: 16px;
    line-height: 1.6;
}

.metric-strip {
    display: flex;
    justify-content: space-around;
    background: linear-gradient(90deg, #022c22, #064e3b);
    padding: 24px;
    border-radius: 24px;
    margin-top: 35px;
    border: 1px solid rgba(34,197,94,0.3);
}

.metric {
    text-align: center;
    color: white;
}

.metric h2 {
    color: #86efac;
    margin: 0;
    font-size: 34px;
}

.metric p {
    margin: 0;
    color: #d1fae5;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="badge">LIVE WELLNESS ANALYTICS</div>
    <h1>⚡ Fit<span>Sync</span></h1>
    <p>Turn your daily health data into clear, motivating insights.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="icon">📊</div>
        <h3>Dashboard</h3>
        <p>See your steps, calories, workouts, sleep, and health summary in one clean view.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="icon">📈</div>
        <h3>Trends</h3>
        <p>Discover patterns in your health journey and understand what is improving over time.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="icon">🎯</div>
        <h3>Goals</h3>
        <p>Stay focused with wellness goals designed to keep you consistent and motivated.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="metric-strip">
    <div class="metric">
        <h2>7+</h2>
        <p>Health Metrics</p>
    </div>
    <div class="metric">
        <h2>24/7</h2>
        <p>Progress Tracking</p>
    </div>
    <div class="metric">
        <h2>100%</h2>
        <p>Personal Insights</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.success("Use the sidebar to explore your Dashboard and Trends pages.")
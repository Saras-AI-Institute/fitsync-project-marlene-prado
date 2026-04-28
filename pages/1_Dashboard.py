import streamlit as st
from streamlit import cache_data
import plotly.express as px
from modules.processor import process_data

# Use st.cache_data to cache the data loading function
@st.cache_data
def get_data():
    return process_data()

# Title
st.title("FitSync Personal Health Analytics")

# Load and process data
df = get_data()

# Sidebar filters with time range options: Last 7 Days, Last 30 Days, All Time
st.sidebar.header("Filters")
time_range = st.sidebar.selectbox("Select Time Range", options=["Last 7 Days", "Last 30 Days", "All time"], index=2)

# Filter the DataFrame based on the selected time range
if time_range == "Last 7 Days":
    filtered_df = df.sort_values(by='Date', ascending=False).head(7)
elif time_range == "Last 30 Days":
    filtered_df = df.sort_values(by='Date', ascending=False).head(30)
else:
    filtered_df = df

# Calculate key metrics
average_steps = filtered_df['Steps'].mean()
average_sleep = filtered_df['Sleep_Hours'].mean()
average_recovery_score = filtered_df['Recovery_Score'].mean()

# Display key metrics in three columns
metric_col1, metric_col2, metric_col3 = st.columns(3)
metric_col1.metric(label="Average Steps", value=f"{average_steps:.0f}")
metric_col2.metric(label="Average Sleep (Hours)", value=f"{average_sleep:.1f}")
metric_col3.metric(label="Average Recovery Score", value=f"{average_recovery_score:.1f}")

# Layout for the first pair of charts
chart_col1, chart_col2 = st.columns(2)

# Left Column: Dual Line Chart for Recovery Score and Sleep Hours Trend
with chart_col1:
    st.markdown("### Recovery Score & Sleep Trend")
    fig = px.line(filtered_df, x='Date', y=['Recovery_Score', 'Sleep_Hours'],
                  labels={'value': 'Values', 'variable': 'Metrics'},
                  title="Recovery Score & Sleep Trend")
    st.plotly_chart(fig, use_container_width=True)

# Right Column: Scatter Plot for Recovery Score vs Steps colored by Sleep Hours
with chart_col2:
    st.markdown("### Recovery Score vs Daily Steps")
    fig = px.scatter(filtered_df, x='Steps', y='Recovery_Score', color='Sleep_Hours',
                     labels={'Steps': 'Daily Steps', 'Recovery_Score': 'Recovery Score'},
                     title="Recovery Score vs Daily Steps")
    st.plotly_chart(fig, use_container_width=True)

# Layout for the second pair of charts
chart_col3, chart_col4 = st.columns(2)

# Left Column: Scatter Plot for Recovery Score vs Heart Rate
with chart_col3:
    st.markdown("### Recovery Score vs Resting Heart Rate")
    fig = px.scatter(filtered_df, x='Heart_Rate_bpm', y='Recovery_Score',
                     labels={'Heart_Rate_bpm': 'Heart Rate (bpm)', 'Recovery_Score': 'Recovery Score'},
                     title="Recovery Score vs Resting Heart Rate")
    st.plotly_chart(fig, use_container_width=True)

# Right Column: Line Chart for Calories Burned Trend
with chart_col4:
    st.markdown("### Daily Calories Burned Trend")
    fig = px.line(filtered_df, x='Date', y='Calories_Burned',
                  labels={'Calories_Burned': 'Calories Burned'},
                  title="Daily Calories Burned Trend")
    st.plotly_chart(fig, use_container_width=True)

# Display the filtered processed data
st.write("## Processed Health Data")
st.dataframe(filtered_df)


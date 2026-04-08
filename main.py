import streamlit as st
from modules.processor import process_data

# Title
st.title("FitSync Personal Health Analytics")

# Layout
col1, col2, col3 = st.columns(3)

# Get processed data
processed_data = process_data()

# Sidebar filters
st.sidebar.header("Filters")
time_range = st.sidebar.selectbox("Select Time Range", options=["Last 7 Days", "Last 30 Days", "All time"], index=2)

# Filter the DataFrame based on the time range selection
if time_range == "Last 7 Days":
    filtered_data = processed_data.sort_values(by='Date', ascending=False).head(7)
elif time_range == "Last 30 Days":
    filtered_data = processed_data.sort_values(by='Date', ascending=False).head(30)
else:
    filtered_data = processed_data

# Recalculate metrics based on the filtered data
average_steps = filtered_data['Steps'].mean()
average_sleep_hours = filtered_data['Sleep_Hours'].mean()
average_recovery_score = filtered_data['Recovery_Score'].mean()

# Update metrics display based on the filtered data
col1.metric(label="Average Steps", value=f"{average_steps:.0f}", delta=None)
col2.metric(label="Average Sleep Hours", value=f"{average_sleep_hours:.1f}", delta=None)
col3.metric(label="Average Recovery Score", value=f"{average_recovery_score:.1f}", delta=None)

# Display the filtered processed data
st.write("## Processed Health Data")
st.dataframe(filtered_data)

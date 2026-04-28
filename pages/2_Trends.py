import streamlit as st
from streamlit import cache_data
import plotly.express as px
from modules.processor import process_data

# Use st.cache_data to cache the data loading function
@st.cache_data
def get_data():
    return process_data()

# Title
st.title("Trends & Insights")

# Load data
df = get_data()

# Sidebar filters
st.sidebar.header("Filters")
time_range = st.sidebar.selectbox("Select Time Range", options=["Last 7 Days", "Last 30 Days", "All time"], index=2)

# Filter the DataFrame based on the time range selection
if time_range == "Last 7 Days":
    filtered_df = df.sort_values(by='Date', ascending=False).head(7)
elif time_range == "Last 30 Days":
    filtered_df = df.sort_values(by='Date', ascending=False).head(30)
else:
    filtered_df = df

# Display summary statistics
st.subheader("Summary Statistics")
summary = filtered_df[['Recovery_Score', 'Sleep_Hours', 'Steps', 'Calories_Burned']].agg(['mean', 'min', 'max'])
st.dataframe(summary)

# Line chart: Average Recovery Score month-wise
recovery_monthly_avg = filtered_df[['Date', 'Recovery_Score']].copy()
recovery_monthly_avg['Month'] = recovery_monthly_avg['Date'].dt.to_period('M')
avg_recovery_month = recovery_monthly_avg.groupby('Month').mean().reset_index()

# Convert 'Month' to string for JSON serialization
avg_recovery_month['Month'] = avg_recovery_month['Month'].astype(str)

st.subheader("Average Recovery Score - Monthly")
fig = px.line(avg_recovery_month, x='Month', y='Recovery_Score',
              labels={'Month': 'Month', 'Recovery_Score': 'Avg Recovery Score'},
              title="Average Recovery Score per Month")
st.plotly_chart(fig, use_container_width=True)

# Histograms
st.subheader("Distribution Histograms")

# Steps Histogram
fig_steps = px.histogram(filtered_df, x='Steps', nbins=20,
                         title='Distribution of Daily Steps')
st.plotly_chart(fig_steps, use_container_width=True)

# Calories Burned Histogram
fig_calories = px.histogram(filtered_df, x='Calories_Burned', nbins=20,
                            title='Distribution of Calories Burned')
st.plotly_chart(fig_calories, use_container_width=True)

# Recovery Score Histogram
fig_recovery = px.histogram(filtered_df, x='Recovery_Score', nbins=20,
                            title='Distribution of Recovery Score')
st.plotly_chart(fig_recovery, use_container_width=True)

# Sleep Hours Histogram
fig_sleep = px.histogram(filtered_df, x='Sleep_Hours', nbins=20,
                         title='Distribution of Sleep Hours')
st.plotly_chart(fig_sleep, use_container_width=True)


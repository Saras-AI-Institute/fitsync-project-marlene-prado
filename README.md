# FitSync - Health Analytics Platform 🚀

### Empower your personal health insights with streamlined data analytics.

## Project Overview
FitSync is a state-of-the-art personal health analytics platform designed to provide comprehensive insights into users' health metrics. Built using Python and Streamlit, the application features a 3-page dashboard that includes Main, Dashboard, and Trends pages. The Dashboard showcases key performance indicators and interactive charts, while the Trends page offers in-depth histograms and insights. To enhance the user experience, FitSync includes a dark theme and leverages `st.cache_data` for optimized performance.

## ✨ Key Features
- 📊 **Interactive Dashboard** – Displays key health metrics with dynamic visualizations  
- 📈 **Trend Analysis** – Histogram-based insights to identify patterns over time  
- 🌙 **Dark Theme UI** – Clean and modern interface for better user experience  
- ⚡ **Optimized Performance** – Uses `st.cache_data` for faster data processing  
- 📂 **Multi-Page Navigation** – Separate pages for Dashboard and Trends analysis  
- 🔄 **Custom Data Processing** – Modular data handling using reusable components  

## Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![GitHub Codespaces](https://img.shields.io/badge/GitHub%20Codespaces-181717?style=for-the-badge&logo=github&logoColor=white)

## 📂 Project Structure

```
fitsync/
│── main.py # Entry point for Streamlit app
│── pages/ # Multi-page app views
│ ├── 1_Dashboard.py # KPI dashboard and charts
│ ├── 2_Trends.py # Trend analysis and histograms
│── modules/ # Core logic and data processing
│ ├── processor.py # Data cleaning and transformations
│── data/ # Dataset files
│ ├── health_data.csv # Sample health dataset
│── .streamlit/ # Streamlit configuration
│ ├── config.toml # Theme and app settings
│── .devcontainer/ # Development container setup
│── requirements.txt # Python dependencies
│── runtime.txt # Deployment runtime config
│── generate_data.py # Script to generate synthetic data
│── sample_data.py # Sample dataset utilities
│── test.py # Testing script
│── README.md # Project documentation
```

## How to Run
1. **Clone the repository**: Use Git to clone the project to your local machine.
   ```bash
   git clone https://your-repo-url.git
   ```
2. **Open in GitHub Codespaces**: Navigate to your repository on GitHub and open a new Codespace.
3. **Run the Streamlit Application**: Once the Codespace is ready, execute the following command to start the application.
   ```bash
   streamlit run main.py
   ```

## 🔗 Live Demo Link 
 
https://fitsync-project-marlene-prado-89sd4tgf6oyqw2546hwkqj.streamlit.app/

## Built with AI
FitSync harnesses advancements in artificial intelligence to streamline the development process. By integrating the Continue Agent in GitHub Codespaces, the team accelerated code syntax decisions while maintaining full control over the architecture and data logic. This approach allowed for efficient development and deployment, ensuring a feature-rich and responsive health analytics platform.

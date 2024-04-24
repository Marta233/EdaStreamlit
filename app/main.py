# main.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data, basic_info, basic_desc, calculate_summary_stats, missing_values, count_negative_values, remove_negative_rows, plot_time_series, correlation_analysis

def main():
    st.title("Data Analysis App")

    # File upload
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        data = load_data(uploaded_file)

        # Sidebar options
        analysis_type = st.sidebar.selectbox("Select Analysis", ["Basic Info", "Summary Stats", "Missing Values", "Negative Values", "Time Series Plot", "Correlation Analysis"])
        if analysis_type == "Basic Info":
            basic_info(data)
        elif analysis_type == "Summary Stats":
            calculate_summary_stats(data)
        elif analysis_type == "Missing Values":
            missing_values(data)
        elif analysis_type == "Negative Values":
            count_negative_values(data)
        elif analysis_type == "Time Series Plot":
            cols = st.sidebar.multiselect("Select Columns for Time Series", data.columns)
            if cols:
                plot_data = data[cols]
                plot_time_series(plot_data)
        elif analysis_type == "Correlation Analysis":
            correlation_analysis(data)

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset into a Pandas DataFrame
df = pd.read_csv('/Users/bebi.a/project1/coaster_db.csv')

# Streamlit page configuration
st.set_page_config(page_title="Data Analysis App")

# Streamlit header
st.header("Exploratory Data Analysis")

# Check if the user wants to see a histogram
if st.checkbox('Show Histogram'):
    # Select a column to plot histogram
    column = st.selectbox('Select Column for Histogram', df.columns)
    # Create and display a histogram
    fig_hist = px.histogram(df, x=column)
    st.plotly_chart(fig_hist)

# Check if the user wants to see a scatter plot
if st.checkbox('Show Scatter Plot'):
    # Select columns for scatter plot
    x_column = st.selectbox('Select X-axis for Scatter Plot', df.columns, index=1)
    y_column = st.selectbox('Select Y-axis for Scatter Plot', df.columns, index=2)
    # Create and display a scatter plot
    fig_scatter = px.scatter(df, x=x_column, y=y_column)
    st.plotly_chart(fig_scatter)

# Footer or any additional text
st.write("This app provides a simple interface for basic exploratory data analysis.")

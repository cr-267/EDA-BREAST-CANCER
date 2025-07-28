import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Breast Cancer Detection - EDA")

uploaded_file = st.file_uploader("Upload data.csv file", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(data.head())

    st.subheader("Diagnosis Count")
    fig, ax = plt.subplots()
    sns.countplot(data['diagnosis'], ax=ax)
    st.pyplot(fig)

    st.subheader("Correlation Heatmap")
    fig2, ax2 = plt.subplots(figsize=(12, 10))
    sns.heatmap(data.corr(numeric_only=True), cmap='coolwarm', ax=ax2)
    st.pyplot(fig2)

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Breast Cancer EDA", layout="wide")

st.title("🩺 Breast Cancer Classification - EDA Dashboard")

# Sidebar
st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to", ["Upload File", "Data Preview", "Diagnosis Plot", "Correlation Heatmap", "Missing Values"])

# Upload file
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if option == "Upload File":
        st.subheader("✅ File uploaded successfully")
        st.success(f"File name: `{uploaded_file.name}`")
        st.write("Shape of the data:", df.shape)

    elif option == "Data Preview":
        st.subheader("📄 Data Preview")
        st.dataframe(df.head())

    elif option == "Diagnosis Plot":
        st.subheader("📊 Diagnosis Count Plot")
        fig, ax = plt.subplots()
        sns.countplot(data=df, x='diagnosis', palette='Set2', ax=ax)
        st.pyplot(fig)

    elif option == "Correlation Heatmap":
        st.subheader("🔥 Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(12, 10))
        sns.heatmap(df.corr(numeric_only=True), cmap='coolwarm', annot=False, ax=ax)
        st.pyplot(fig)

    elif option == "Missing Values":
        st.subheader("🧼 Missing Value Summary")
        missing = df.isnull().sum()
        st.write(missing[missing > 0] if missing.sum() > 0 else "No missing values found!")

else:
    st.warning("Please upload a CSV file using the sidebar.")

st.markdown("---")
st.markdown("💡 *This Streamlit app is built for visualizing Breast Cancer classification datasets*")

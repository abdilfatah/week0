import streamlit as st
import pandas as pd

st.set_page_config(page_title="File Uploader", page_icon="📂")


df = st.file_uploader("Upload a CSV file", type=["csv"])

if df:
    df = pd.read_csv(df)
    st.write("Uploaded data preview:")
    st.write(df.head())
    st.bar_chart(df["DNI"])
    st.line_chart(df["GHI"])
    st.dataframe(df)


else:
    st.warning("Please upload a CSV file.")


if __name__ == "__main__":
    st.title("Dashboard")

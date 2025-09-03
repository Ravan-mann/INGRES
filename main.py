import streamlit as st
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv 
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="Water Quality Expert")

st.title("Groundwater Quality Analysis Platform")
st.subheader("Professional water quality assessment and regional analysis")


df = pd.read_csv(f"F:\\ingres\\data\\final_nhs-wq_pre_2022_compressed.csv")

data_summary = f"""
Loaded groundwater quality dataset with samples.

Columns: {', '.join(df.columns.tolist())}

Coverage:
- States: {', '.join(df['STATE'].unique().astype(str)[:3])}
- Districts: {df['DISTRICT'].nunique()}
- Years: {df['Year'].min()}-{df['Year'].max()}

Sample data:
{df.head(3).to_string()}
"""

st.success(f"Dataset initialized: {len(df):,} groundwater samples loaded for analysis.")

prompt = st.chat_input("Ask questions about water quality ...")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Processing..."):
            model = genai.GenerativeModel("gemini-1.5-flash")
            
            context_prompt = f"""
            You are a professional water quality analyst. Provide technical analysis based exclusively on the provided dataset.
            Use scientific terminology appropriately. Do not reference external knowledge or general information.

            Dataset Specifications:
            {data_summary}

            Analysis Request: {prompt}

            Deliver a comprehensive analysis based solely on this dataset. If insufficient data exists 
            for the requested analysis, clearly state the limitations. Focus on quantitative findings,
            statistical patterns, and evidence-based regional comparisons.
            """
            
            response = model.generate_content(context_prompt)
            st.markdown(response.text)

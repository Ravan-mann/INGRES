import streamlit as st
import pandas as pd
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyDuSJ45-gcJxvcmNREoAMt1y4GBw0KQ_Hc")

st.set_page_config(page_title="Water Quality Expert")

st.title("Groundwater Quality Analysis Platform")
st.subheader("Professional water quality assessment and regional analysis")
try:
    df = pd.read_csv(""F:\ingres\temp_uploaded_file.csv"")
    st.success(f"Dataset initialized: {len(df):,} groundwater samples loaded for analysis.")
    
    data_summary = f"""
    Loaded groundwater quality dataset with {len(df)} samples.
    
    Columns: {', '.join(df.columns.tolist())}
    
    Coverage:
    - States: {', '.join(df['STATE'].unique().astype(str)[:3]) if 'STATE' in df.columns else 'N/A'}
    - Districts: {df['DISTRICT'].nunique() if 'DISTRICT' in df.columns else 'N/A'}
    - Years: {df['Year'].min()}-{df['Year'].max() if 'Year' in df.columns else 'N/A'}
    
    Sample data:
    {df.head(3).to_string()}
    """
except Exception as e:
    st.error(f"Data loading failed: {str(e)}")
    df = None
    data_summary = "No data available."

prompt = st.chat_input("ask  quesions about water quality ...")

if prompt:
    if df is not None:
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Processing..."):
                try:
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
                    
                except Exception as e:
                    error_msg = str(e)
                    if "429" in error_msg or "quota" in error_msg.lower():
                        st.error("API rate limit exceeded. Please retry after a brief interval.")
                    else:
                        st.error(f"Error: {error_msg}")
    else:
        st.error("Dataset unavailable. Analysis cannot proceed without loaded data.")


st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Evidence-based analysis from verified dataset"
    "</div>", 
    unsafe_allow_html=True
)

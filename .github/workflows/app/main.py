import streamlit as st
import pandas as pd
import os

# --- Page Config ---
st.set_page_config(page_title="COP32 Climate Portal", layout="wide")
st.title("🌍 Regional Climate Vulnerability Dashboard")

# --- DIRECT PATH DEFINITION ---
# Pointing specifically to your notebooks folder where the _clean.csv files are
DATA_DIR = r"C:\Users\HP\Desktop\10acadamey\week0\-climate-challenge-week0\notebooks"

@st.cache_data
def load_country_data(country):
    # Matches the 'country_clean.csv' format seen in your VS Code sidebar
    file_name = f"{country.lower()}_clean.csv"
    file_path = os.path.join(DATA_DIR, file_name)
    
    if os.path.exists(file_path):
        data = pd.read_csv(file_path)
        # Ensure 'Date' is reconstructed if it wasn't saved as a single column
        if 'YEAR' in data.columns and 'DOY' in data.columns:
            data['Date'] = pd.to_datetime(data['YEAR'] * 1000 + data['DOY'], format='%Y%j')
        return data
    return None

# --- Sidebar Filters ---
st.sidebar.header("Filter Options")
country_list = ["Ethiopia", "Kenya", "Nigeria", "Sudan", "Tanzania"]
selected_country = st.sidebar.selectbox("Select a Country", country_list)

df = load_country_data(selected_country)

if df is not None:
    st.success(f"✅ Data loaded successfully from: {selected_country}_clean.csv")
    
    # 1. Top Level Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Temp", f"{df['T2M'].mean():.1f} °C")
    col2.metric("Max Temp", f"{df['T2M_MAX'].max():.1f} °C")
    col3.metric("Avg Rain", f"{df['PRECTOTCORR'].mean():.2f} mm")

    # 2. Charts
    # Preparing monthly data for the charts
    df['Date'] = pd.to_datetime(df['Date'])
    monthly = df.set_index('Date').resample('ME').agg({
        'T2M': 'mean', 
        'PRECTOTCORR': 'sum'
    }).reset_index()
    
    st.subheader(f"Historical Trends: {selected_country}")
    
    tab1, tab2 = st.tabs(["🌡️ Temperature", "🌧️ Precipitation"])
    
    with tab1:
        st.line_chart(monthly.set_index('Date')['T2M'])
        
    with tab2:
        st.bar_chart(monthly.set_index('Date')['PRECTOTCORR'])

else:
    st.error(f"❌ Data file not found for {selected_country}.")
    st.info(f"The app is looking for `{selected_country.lower()}_clean.csv` in: `{DATA_DIR}`")
    st.warning("Double-check that the filenames in your 'notebooks' folder match this exactly!")
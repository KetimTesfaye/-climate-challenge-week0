import streamlit as st
import pandas as pd
import os

# --- Page Config ---
st.set_page_config(page_title="COP32 Climate Portal", layout="wide")
st.title("🌍 Regional Climate Vulnerability Dashboard")

# --- PATH CONFIG ---
# Using the notebook path where your _clean.csv files live
DATA_DIR = r"C:\Users\HP\Desktop\10acadamey\week0\-climate-challenge-week0\notebooks"

@st.cache_data
def load_all_data():
    countries = ["Ethiopia", "Kenya", "Nigeria", "Sudan", "Tanzania"]
    all_dfs = []
    for c in countries:
        file_path = os.path.join(DATA_DIR, f"{c.lower()}_clean.csv")
        if os.path.exists(file_path):
            temp_df = pd.read_csv(file_path)
            temp_df['Country'] = c
            # Ensure Date is datetime
            if 'YEAR' in temp_df.columns and 'DOY' in temp_df.columns:
                temp_df['Date'] = pd.to_datetime(temp_df['YEAR'] * 1000 + temp_df['DOY'], format='%Y%j')
            all_dfs.append(temp_df)
    return pd.concat(all_dfs, ignore_index=True) if all_dfs else None

# Load dataset
df_master = load_all_data()

if df_master is not None:
    # --- Sidebar Filters ---
    st.sidebar.header("Dashboard Controls")
    
    # 1. Country Multi-select
    selected_countries = st.sidebar.multiselect(
        "Select Countries to Compare", 
        options=df_master['Country'].unique(),
        default=["Ethiopia"]
    )
    
    # 2. Year Range Slider
    min_year = int(df_master['YEAR'].min())
    max_year = int(df_master['YEAR'].max())
    year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))

    # --- Data Filtering ---
    filtered_df = df_master[
        (df_master['Country'].isin(selected_countries)) & 
        (df_master['YEAR'] >= year_range[0]) & 
        (df_master['YEAR'] <= year_range[1])
    ]

    if not filtered_df.empty:
        # --- Visualizations ---
        
        # A. Temperature Trend Line Chart
        st.subheader("🌡️ Average Temperature Trends")
        # Resample to monthly for smoother lines
        line_data = filtered_df.groupby(['Country', pd.Grouper(key='Date', freq='ME')])['T2M'].mean().reset_index()
        st.line_chart(line_data, x='Date', y='T2M', color='Country')

        col1, col2 = st.columns([1, 1])
        
        with col1:
            # B. Precipitation Distribution Boxplot
            st.subheader("🌧️ Rainfall Distribution")
            import plotly.express as px
            fig_box = px.box(filtered_df, x="Country", y="PRECTOTCORR", color="Country",
                             title="Precipitation Spread (mm/day)",
                             labels={"PRECTOTCORR": "Precipitation (mm)"})
            st.plotly_chart(fig_box, use_container_width=True)

        with col2:
            st.info("""
            **Analysis Note:** The boxplot highlights precipitation volatility. Large "whiskers" or many outliers indicate erratic rainy seasons, 
            which is a primary indicator of climate vulnerability.
            """)
    else:
        st.warning("No data matches the selected filters.")
else:
    st.error("Could not find the cleaned data files. Please check your data directory.")
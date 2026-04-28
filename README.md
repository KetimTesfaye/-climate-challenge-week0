# EthioClimate Analytics - COP32 Climate Challenge
This project performs end-to-end data engineering and climate analysis on NASA POWER satellite data (2015–2026) for five African nations. The goal is to clean, visualize, and rank climate vulnerability to support policy narratives for COP32.
## Project Overview
The project involves:
- Infrastructure: Setting up a professional Git environment with CI/CD automation.
- Data Engineering: Sanitizing NASA sentinel values (-999) and handling outliers.
- EDA & Analytics: Performing individual and comparative analysis on temperature and rainfall trends.
- Visualization: Deploying an interactive Streamlit dashboard for regional benchmarking.

## Data Description
### Input Datasets
The project uses cleaned datasets for five countries:
- `ethiopia_clean.csv`
- `kenya_clean.csv`
- `nigeria_clean.csv`
- `sudan_clean.csv`
- `tanzania_clean.csv`

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/KetimTesfaye/-climate-challenge-week0.git
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate


### 3. Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn streamlit plotly
```

### 4. Run the Dashboard
```bash
streamlit run app/main.py
```

## EDA & Analysis Steps
### 1. Individual & Comparative Analysis
- Cleaning: Replaced NASA `-999` sentinels with `NaN` and applied forward-fill.
- Date Parsing:Standardized `YEAR` and `DOY` into proper datetime objects.
- Outliers: Flagged anomalies using Z-score filtering ($|Z| > 3$).
- Benchmarking: Combined data to rank vulnerability based on heat stress and rainfall volatility.

### 2. Visualizations
- Time Series: Monthly temperature and precipitation trends.
- Distributions:Boxplots showing rainfall spread across regions.
- Relationships: Heatmaps and bubble charts for humidity vs. temperature interaction.

## Dashboard Preview
I have placed my dashboard screenshot in: `dashboard_screenshots/`

---            

##  Dashboard Usage 
The Interactive Climate Vulnerability Dashboard allows for regional benchmarking across East Africa and Nigeria.

### Features:
- Multi-Country Selection: Compare temperature and rainfall trends between nations.
- Dynamic Year Scaling: Use the sidebar slider to focus on specific climate periods (2015-2026).
- Statistical Distributions: Boxplots are provided to visualize precipitation volatility—a key metric for flood and drought risk.

### Local Execution:
1. Ensure the cleaned data files reside in the `notebooks/` directory.
2. Run the following command:
   ```bash
streamlit run .github/workflows/app/main.py

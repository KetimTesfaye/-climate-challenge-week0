# EthioClimate Analytics - COP32 Climate Challenge

## Project Overview
This project focuses on the analysis of historical climate and weather data (2015–2026) for Ethiopia, Kenya, Sudan, Tanzania, and Nigeria. As part of the preparation for COP32 in Addis Ababa (2027), this analysis provides "negotiation-grade" evidence to highlight Africa's unique climate vulnerabilities.

The project evaluates key climate trends, seasonal patterns, and anomalies to support data-driven policy narratives for the Ethiopian Ministry of Planning and Development.            

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
   streamlit run app/main.py
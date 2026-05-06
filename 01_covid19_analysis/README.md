# COVID-19 Global Impact Analysis

## 📌 Overview
Comprehensive time-series analysis of the COVID-19 pandemic using the "Our World in Data" dataset. Covers daily case/death trends, fatality rate analysis, vaccination rollout patterns, testing effectiveness, and regional comparisons across continents and individual countries.
## 🎯 Problem Statement
The COVID-19 pandemic generated vast amounts of data. Understanding this data is crucial for policymakers and health organizations to make informed decisions. This project aims to:
- Identify global and regional trends in cases and deaths
- Analyze the correlation between different health metrics (e.g., cases vs. deaths)
- Visualize the spread and impact of the virus over time
- Derive actionable insights for pandemic response and preparedness

## 📂 Data Sources
| Data Source | Description | Size | Format | Access Date |
|-------------|-------------|------|--------|-------------|
| Our World in Data COVID-19 Dataset | Comprehensive global COVID-19 statistics including cases, deaths, tests, vaccinations, and demographics | ~50MB | CSV | 2023-05-15 |
| Source: https://github.com/owid/covid-19-data/tree/master/public/data | Official WHO and national health agency data aggregated by Our World in Data | | | |

## 🛠 Tools & Tech Stack
| Category | Tools & Libraries |
|----------|-------------------|
| Core | Python 3.9, Pandas 2.0, NumPy 1.24 |
| Visualization | Matplotlib 3.7, Seaborn 0.12, Plotly 5.13 |
| Data Analysis | SciPy 1.10, Statsmodels 0.14 |
| Development | Jupyter Notebook 6.5, Git |

## 📊 Methodology
### Exploratory Data Analysis (EDA)
- **Time-series aggregation**: Daily new cases/deaths, 7-day rolling averages
- **Regional comparisons**: Continental and country-level trend analysis
- **Fatality rate modeling**: Case Fatality Rate (CFR) and Infection Fatality Rate (IFR)
- **Vaccination analysis**: Doses administered, coverage rates, booster uptake
- **Testing effectiveness**: Correlation between testing rates and case detection

### Feature Engineering
- Created derived metrics: CFR, positivity rates, vaccination rates
- Generated rolling averages to smooth daily fluctuations
- Developed population-normalized metrics for cross-country comparison
- Created categorical variables for income levels and geographic regions

### Advanced Visualization
- Multi-axis time-series plots to compare cases vs. deaths
- Interactive choropleth maps for geographic distribution
- Heatmaps for weekly seasonality patterns
- Small multiples for regional trend comparison

## 🔑 Key Insights
### Technical Insights
- **Fatality trends**: Global Case Fatality Rate (CFR) decreased from ~3.5% to ~1.2% over the pandemic
- **Regional hotspots**: Different continents experienced waves at different times
- **Vaccine impact**: Countries with high vaccination rates showed significantly lower death rates
- **Data quality**: Missing testing data limited analysis of testing effectiveness

### Business Value
- **Policy recommendations**: Data-driven insights for resource allocation and intervention timing
- **Public communication**: Clear visualizations for public health messaging
- **Future preparedness**: Framework for rapid analysis of future pandemics

## 📁 Project Structure
```
01_covid19_analysis/
├── data/           # Raw and processed COVID-19 datasets
├── notebooks/      # Time-series analysis and visualizations
├── results/        # Generated plots and reports
└── README.md       # Project documentation
```

## 📚 References
- Our World in Data COVID-19 Dataset: https://github.com/owid/covid-19-data
- World Health Organization: https://covid19.who.int/
- Johns Hopkins Coronavirus Resource Center: https://coronavirus.jhu.edu/

## 🤝 License
MIT — See LICENSE file for details.

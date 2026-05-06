# Customer Segmentation (RFM Analysis)

## 📌 Overview
Recency-Frequency-Monetary (RFM) analysis to segment customers based on their purchasing behavior. By scoring customers on how recently they bought, how often they buy, and how much they spend, we classify them into distinct groups like "Most Valuable", "Loyal", and "Likely to Churn" for targeted marketing.

## 🎯 Problem Statement
Businesses need to understand their customer base to tailor marketing strategies effectively. Treating all customers the same leads to wasted resources. This project aims to identify high-value customers for retention and at-risk customers for re-engagement campaigns through data-driven segmentation.

## 📂 Data Sources
| Data Source | Description | Size | Format | Access Date |
|-------------|-------------|------|--------|-------------|
| Transaction History Dataset | Customer transactions with dates, amounts, and customer IDs | ~50,000 records | CSV | 2023-05-30 |

### Data Acquisition
Transaction data obtained from a retail database containing customer purchase history over a 12-month period. The dataset includes transaction dates, customer identifiers, and monetary values.

## 🔧 Preprocessing & Data Cleaning
### Data Quality Issues Identified
- **Missing customer IDs**: Transactions without customer identifiers
- **Date formatting**: Inconsistent date representations
- **Duplicate transactions**: Multiple entries for same transaction
- **Outliers**: Extremely high-value transactions
- **Data completeness**: Missing transaction amounts

### Cleaning Steps Applied
1. **Data validation**: Removed transactions with missing customer IDs
2. **Date standardization**: Converted all dates to datetime format
3. **Duplicate removal**: Identified and removed duplicate transaction records
4. **Outlier treatment**: Applied IQR method to detect and cap extreme values
5. **Aggregation**: Calculated customer-level metrics from transaction data
6. **Data type conversion**: Ensured proper numeric and datetime types

## 🛠 Tools & Tech Stack
| Category | Tools & Libraries |
|----------|-------------------|
| Core | Python 3.8, Pandas 2.0, NumPy 1.24 |
| Visualization | Matplotlib 3.7, Seaborn 0.12 |
| Statistics | SciPy 1.10 (optional) |
| Development | Jupyter Notebook 6.5, Git |

## 📊 Methodology
### RFM Metric Calculation
- **Recency (R)**: Days since last transaction (lower = better)
- **Frequency (F)**: Total number of transactions (higher = better)
- **Monetary (M)**: Total transaction value (higher = better)

### Scoring & Segmentation
1. **Quartile scoring**: Divided each metric into 4 quartiles (1-4 scale)
2. **RFM Score**: Sum of R, F, and M scores (range 3-12)
3. **Segment definition**:
   - **Most Valuable**: Score > 9
   - **Loyal Customers**: Score between 6-9
   - **At Risk**: Low recency, high frequency
   - **Needs Attention**: Low monetary, high recency

### Analysis Techniques
- **Quantile-based partitioning**: Using pd.qcut for equal-sized groups
- **Customer profiling**: Analyzing characteristics of each segment
- **Distribution analysis**: Visualizing RFM metric distributions
- **Business rule application**: Defining actionable customer segments

## 📈 Results & Business Insights
### Segment Analysis
- **Most Valuable**: 15% of customers, account for 45% of revenue
- **Loyal Customers**: 25% of customers, consistent repeat buyers
- **At Risk**: 10% of customers, high value but haven't purchased recently
- **Needs Attention**: 20% of customers, low engagement requiring re-engagement

### Actionable Strategies
- **Most Valuable**: VIP treatment, exclusive offers, loyalty programs
- **Loyal Customers**: Reward programs, early access to sales
- **At Risk**: Win-back campaigns, personalized outreach
- **Needs Attention**: Re-engagement offers, product recommendations

## 🚀 How to Run
### Setup
```bash
# Create virtual environment
python -m venv venv && source venv/bin/activate

# Install dependencies with pinned versions
pip install -r requirements.txt
```

### Execution
```bash
# Navigate to project
cd 05_customer_segmentation

# Launch Jupyter Notebook
jupyter notebook notebooks/05_customer_segmentation.ipynb
```

## 📁 Project Structure
```
05_customer_segmentation/
├── data/           # Transaction history datasets
├── notebooks/      # RFM analysis and segmentation notebook
├── results/        # Customer segment profiles and visualizations
└── README.md       # Project documentation
```

## 📝 Dependencies
- Python 3.8+
- pandas==2.0.3
- numpy==1.24.3
- matplotlib==3.7.1
- seaborn==0.12.2

## 📚 References
- RFM Analysis in Customer Segmentation (Berson, Smith, Thearling)
- Data-Driven Marketing: The 15 Metrics Everyone in Marketing Should Know
- Practical Retail Analytics: Using Data to Make Better Decisions

## 🤝 License
MIT — See LICENSE file for details.

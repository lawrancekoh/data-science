# Customer Segmentation (RFM Analysis)

## 📌 Overview
This project employs RFM (Recency, Frequency, Monetary) analysis to segment customers based on their purchasing behavior. By scoring customers on how recently they bought, how often they buy, and how much they spend, we classify them into distinct groups like "Most Valuable," "Loyal," and "Likely to Churn."

## 🎯 Problem Statement
Businesses need to understand their customer base to tailor marketing strategies effectively. Treating all customers the same leads to wasted resources. This project aims to identify high-value customers for retention and at-risk customers for re-engagement campaigns.

## 🛠 Tools & Tech Stack
- **Python**: Core language.
- **Pandas**: Used for data aggregation, grouping, and q-cut partitioning.
- **Seaborn & Matplotlib**: For visualizing the distributions of RFM metrics.
- **DateUtils**: Using `datetime` and `timedelta` to calculate Recency.

## 📊 Methodology
1. **Data Preprocessing**:
   - Parsed date columns to calculate "Recency".
   - Aggregated transaction data by `CardID` to determine "Frequency" (count of visits) and "MonetaryValue" (sum of spend).
2. **RFM Calculation**:
   - **Recency (R)**: Days since the last transaction.
   - **Frequency (F)**: Total number of transactions.
   - **Monetary (M)**: Total transaction value.
3. **Scoring & Segmentation**:
   - Divided each metric into quartiles (1-4) using `pd.qcut`.
   - Combined R, F, and M scores to create a composite "RFM Score".
   - Defined segments based on total score:
     - **Most Valuable**: Score > 9
     - **Loyal Members**: Score between 6 and 9
     - **Likely to Churn**: Score < 6

## 🔑 Key Insights
- **Segment Behavior**: The "Most Valuable" segment not only spends more but visits significantly more frequently with very low recency.
- **Actionable Strategy**: Marketing efforts can now be targeted—e.g., exclusive offers for "Most Valuable" customers and win-back campaigns for those "Likely to Churn."

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```
2. Navigate to the notebooks directory:
   ```bash
   cd notebooks
   ```
3. Open the analysis notebook:
   ```bash
   jupyter notebook "05_customer_segmentation.ipynb"
   ```

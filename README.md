# FinStatAnalysis

This project is based on [© NeuralNine's YouTube video](https://www.youtube.com/watch?v=ZAAuGEVJsH8), originally designed to analyze financial statements using Python and the FinancialModelingPrep API.

This version includes major improvements and restructuring, transforming it into a standalone project. The ultimate goal is to expand beyond the FinancialModelingPrep platform and enable support for Czech and Slovak companies, which are not publicly listed or available via FMP.

---

## 📁 `main.py`

The `main.py` script performs automated financial statement analysis using data fetched via API.

### 🔧 Key Features:
- Retrieves and processes the **Income Statement** (annual) for a selected company.
- Calculates key financial metrics:
  - **EBIT**
  - **EBITDA**
  - **Net Profit Margin**
  - **Operating Margin**
  - **Effective Tax Rate**
  - **R&D and SG&A ratios as % of revenue**
- Visualizes the following in separate graphs:
  - Revenue
  - Gross Profit
  - Earnings Per Share (EPS)

---

## ⚙️ How to Use

1. Create a file named `api_key.txt` in the project root and paste your API key from [FinancialModelingPrep](https://financialmodelingprep.com).
2. Run the script:
   ```bash
   python main.py

## 📊 Interpretation of Apple Inc. (AAPL) Financial Data

> **Note**: Due to the limitations of the FinancialModelingPrep **Free Plan**, only the most recent **4 years** of data (2020–2024) are available.

---

### 🔍 Key Financial Highlights (2024)

- **Revenue**: `$391.0B`  
- **Gross Profit**: `$180.7B`  
- **EBITDA**: `$134.7B`  
- **EBIT**: `$123.2B`  
- **EPS**: `6.11`

Apple has consistently demonstrated strong revenue growth and operational efficiency. Revenue has climbed steadily over the 4-year period, supported by robust profit margins and disciplined expense management.

---

### 📈 Financial Ratios with Benchmark Ranges

| Metric                  | Value     | Ideal Range         | Commentary                                         |
|-------------------------|-----------|----------------------|----------------------------------------------------|
| **Net Profit Margin**   | 23.97%    | 15% – 25%+           | Strong bottom-line profitability                   |
| **Operating Margin**    | 31.51%    | 10% – 25%+           | High operational efficiency                        |
| **Effective Tax Rate**  | 24.09%    | 20% – 25%            | Within normal range for a U.S. corporation         |
| **R&D Ratio**           | 8.02%     | 5% – 15% (for tech)  | Demonstrates sustained investment in innovation    |
| **SG&A Ratio**          | 6.67%     | 5% – 12%             | Indicates well-managed selling/admin expenses      |

---

### 💬 Summary

While EPS growth has leveled off slightly in the last two years, the company maintains strong profitability, efficient operations, and continued strategic investment in R&D.

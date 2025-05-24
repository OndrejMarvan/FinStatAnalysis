# Financial Statement Analysis
# Project made by NeuralNine, minor changes and code updates

# Website used:
# https://site.financialmodelingprep.com/

# Excessive requests in a short period may exceed API rate limits and require restarting the script

import matplotlib.pyplot as plt
import requests

# Load API key from file
with open("D:/Coding/GitHub/Python_Projects/FinStatAnalysis/api_key.txt", "r") as f:
    api_key = f.read().strip()

# Parameters
company = "AAPL"
years = 10  # requesting more, but will only receive last 4 if on Free plan

# API request
url = f"https://financialmodelingprep.com/api/v3/income-statement/{company}?limit={years}&period=annual&apikey={api_key}"
response = requests.get(url)
data = response.json()

# Check and print the latest income statement
if isinstance(data, list) and len(data) > 0:
    latest = data[0]
    print(f"Latest report for {company}:")
    print("Revenue:", latest.get('revenue'))
    print("Gross Profit:", latest.get('grossProfit'))
    print("EPS:", latest.get('eps'))
    print("EBITDA:", latest.get('ebitda'))

    # Additional financial metrics
    ebit = latest.get('operatingIncome')
    net_margin = latest.get('netIncome') / latest.get('revenue')
    operating_margin = latest.get('operatingIncome') / latest.get('revenue')
    effective_tax = latest.get('incomeTaxExpense') / latest.get('incomeBeforeTax')
    rnd_ratio = latest.get('researchAndDevelopmentExpenses') / latest.get('revenue')
    sga_ratio = latest.get('sellingGeneralAndAdministrativeExpenses') / latest.get('revenue')

    print(f"EBIT: {ebit:,}")
    print(f"Net Profit Margin: {net_margin:.2%}")
    print(f"Operating Margin: {operating_margin:.2%}")
    print(f"Effective Tax Rate: {effective_tax:.2%}")
    print(f"R&D Ratio: {rnd_ratio:.2%}")
    print(f"SG&A Ratio: {sga_ratio:.2%}")

else:
    print("❌ Failed to retrieve data:", data)

# Reverse order: oldest to newest
data = data[::-1]

# Extract data
years_labels = [entry['calendarYear'] for entry in data]
revenues = [entry['revenue'] for entry in data]
profits = [entry['grossProfit'] for entry in data]
eps = [entry['eps'] for entry in data]

# Plotting multiple subplots
plt.figure(figsize=(12, 10))

# Revenue plot
plt.subplot(3, 1, 1)
plt.plot(years_labels, revenues, marker='o', label="Revenue")
plt.title(f"{company} Revenue (USD)")
plt.ylabel("USD")
plt.grid(True)

# Profit plot
plt.subplot(3, 1, 2)
plt.plot(years_labels, profits, marker='o', color='green', label="Gross Profit")
plt.title(f"{company} Gross Profit (USD)")
plt.ylabel("USD")
plt.grid(True)

# EPS plot
plt.subplot(3, 1, 3)
plt.plot(years_labels, eps, marker='o', color='orange', label="EPS")
plt.title(f"{company} Earnings Per Share (EPS)")
plt.xlabel("Year")
plt.ylabel("USD")
plt.grid(True)

# Final layout adjustments
plt.tight_layout()
plt.show()

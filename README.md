# 📈 Stock Portfolio Tracker

A simple and interactive **Stock Portfolio Tracker** built using Python. This project helps users calculate the total value of their stock investments by entering stock symbols and quantities.

It provides a portfolio summary with individual stock values, calculates the total investment value, and allows users to export their results into TXT or CSV files.

## ✨ Features

- 📊 **Stock Selection:** Choose from available stock symbols.
- 🔢 **Quantity Management:** Enter the number of shares for each stock.
- 💰 **Investment Calculation:** Automatically calculate the value of individual stocks.
- 📈 **Portfolio Summary:** Display stock symbols, quantities, prices, and total values.
- 💾 **Save Results:** Export portfolio summaries into TXT or CSV files.
- ⚠️ **Input Validation:** Handle invalid stock symbols and quantities.
- 🔄 **Multiple Stock Entries:** Add quantities of the same stock across multiple entries.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Dictionary | Store stock prices and portfolio data |
| Functions | Organize program logic |
| File Handling | Save portfolio reports |
| CSV | Export portfolio data |

## 📋 Available Stocks

The project currently includes predefined stock prices for:

| Stock Symbol | Price (USD) |
|---|---:|
| AAPL | $180 |
| TSLA | $250 |
| GOOGL | $140 |
| MSFT | $410 |
| AMZN | $185 |
| NVDA | $120 |
| META | $480 |

**Note:** These are predefined sample prices, not live market prices.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Stock-Portfolio-Tracker.git
```

### 2. Navigate to the Project Directory

```bash
cd Stock-Portfolio-Tracker
```

### 3. Run the Python Program

```bash
python "stock portfolio tracker.py"
```

## 💻 Example Output

```text
=== Stock Portfolio Tracker ===

Available stocks: AAPL, TSLA, GOOGL, MSFT, AMZN, NVDA, META

Enter stock name and quantity (blank name to finish).

Stock symbol: AAPL
Quantity of AAPL: 5

Added 5 shares of AAPL.

Stock symbol: TSLA
Quantity of TSLA: 2

Added 2 shares of TSLA.

Stock symbol:

--- Portfolio Summary ---
Symbol  Qty   Price     Value
AAPL    5     $180      $900
TSLA    2     $250      $500
----------------------------------
Total Investment Value: $1,400.00
```

## 📂 Project Structure

```text
Stock-Portfolio-Tracker/
│
├── stock portfolio tracker.py
│
└── README.md
```

## 🧠 Python Concepts Used

- Variables and data types
- Dictionaries
- Functions
- Loops (`while` and `for`)
- Conditional statements (`if`, `elif`, `else`)
- User input and output
- Exception handling (`try-except`)
- File handling (`open`, `write`)
- CSV file generation

## 🔮 Future Improvements

- Integration with real-time stock market APIs.
- Interactive graphical user interface.
- Historical stock price tracking.
- Portfolio performance visualization.
- Profit and loss calculation.
- Database integration for saving portfolio history.

## 🎯 Project Objective

The objective of this project is to apply Python programming fundamentals to build a practical financial tracking application while developing skills in problem-solving, data management, functions, and file handling.

---

**Developed with Python 🐍**

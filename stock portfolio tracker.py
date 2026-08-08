STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 410,
    "AMZN": 185,
    "NVDA": 120,
    "META": 480,
}


def get_portfolio():
    """Prompt the user for stock names and quantities."""
    portfolio = {}
    print("Available stocks:", ", ".join(STOCK_PRICES.keys()))
    print("Enter stock name and quantity (blank name to finish).\n")

    while True:
        symbol = input("Stock symbol: ").strip().upper()
        if symbol == "":
            break
        if symbol not in STOCK_PRICES:
            print(f"  '{symbol}' not found in price list. Try again.")
            continue
        try:
            qty = int(input(f"Quantity of {symbol}: ").strip())
            if qty < 0:
                raise ValueError
        except ValueError:
            print("  Please enter a valid non-negative whole number.")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + qty
        print(f"  Added {qty} shares of {symbol}.\n")

    return portfolio


def calculate_total(portfolio):
    """Calculate total investment value and per-stock breakdown."""
    breakdown = []
    total = 0
    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        breakdown.append((symbol, qty, price, value))
    return breakdown, total


def display_results(breakdown, total):
    print("\n--- Portfolio Summary ---")
    print(f"{'Symbol':<8}{'Qty':<6}{'Price':<10}{'Value':<10}")
    for symbol, qty, price, value in breakdown:
        print(f"{symbol:<8}{qty:<6}${price:<9}${value:<9}")
    print("-" * 34)
    print(f"Total Investment Value: ${total:,.2f}")


def save_results(breakdown, total):
    """Optionally save results to a .txt or .csv file."""
    choice = input("\nSave results to a file? (txt/csv/no): ").strip().lower()
    if choice == "txt":
        filename = "portfolio_summary.txt"
        with open(filename, "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write(f"{'Symbol':<8}{'Qty':<6}{'Price':<10}{'Value':<10}\n")
            for symbol, qty, price, value in breakdown:
                f.write(f"{symbol:<8}{qty:<6}${price:<9}${value:<9}\n")
            f.write(f"\nTotal Investment Value: ${total:,.2f}\n")
        print(f"Saved to {filename}")
    elif choice == "csv":
        filename = "portfolio_summary.csv"
        with open(filename, "w") as f:
            f.write("Symbol,Quantity,Price,Value\n")
            for symbol, qty, price, value in breakdown:
                f.write(f"{symbol},{qty},{price},{value}\n")
            f.write(f"Total,,,{total}\n")
        print(f"Saved to {filename}")
    else:
        print("Results not saved.")


def main():
    print("=== Stock Portfolio Tracker ===\n")
    portfolio = get_portfolio()

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    breakdown, total = calculate_total(portfolio)
    display_results(breakdown, total)
    save_results(breakdown, total)


if __name__ == "__main__":
    main()
"""
Stock Portfolio Tracker
------------------------
A simple command-line tool that lets a user enter stock names and
quantities, looks up prices from a hardcoded dictionary, and
calculates the total investment value.

Key concepts used: dictionaries, input/output, basic arithmetic,
file handling.
"""

import csv
from datetime import datetime

# ---------------------------------------------------------
# Hardcoded stock prices (in USD). Add or edit as needed.
# ---------------------------------------------------------
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 410,
    "AMZN": 185,
    "NFLX": 640,
    "META": 480,
}


def show_available_stocks():
    """Print the list of stocks and prices the user can choose from."""
    print("\nAvailable stocks and prices (per share):")
    print("-" * 35)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<8} ${price}")
    print("-" * 35)


def get_portfolio_input():
    """
    Ask the user to enter stock symbols and quantities.
    Returns a dictionary: {symbol: quantity}
    """
    portfolio = {}

    print("\nEnter your stock holdings. Type 'done' when finished.\n")

    while True:
        symbol = input("Enter stock symbol (or 'done' to finish): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"  '{symbol}' not found in price list. Please choose from the list above.")
            continue

        qty_input = input(f"Enter quantity of {symbol}: ").strip()

        try:
            quantity = int(qty_input)
            if quantity <= 0:
                print("  Quantity must be a positive whole number.")
                continue
        except ValueError:
            print("  Invalid quantity. Please enter a whole number.")
            continue

        # If the stock is already in the portfolio, add to the existing quantity
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"  Added {quantity} share(s) of {symbol}.\n")

    return portfolio


def calculate_investment(portfolio):
    """
    Given a portfolio dictionary {symbol: quantity}, calculate
    the value of each holding and the total investment.

    Returns:
        details: list of tuples (symbol, quantity, price, value)
        total: total investment value (float)
    """
    details = []
    total = 0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        details.append((symbol, quantity, price, value))
        total += value

    return details, total


def display_summary(details, total):
    """Print a formatted summary of the portfolio to the console."""
    print("\n" + "=" * 45)
    print("PORTFOLIO SUMMARY")
    print("=" * 45)
    print(f"{'Symbol':<8}{'Qty':<8}{'Price':<10}{'Value':<10}")
    print("-" * 45)

    for symbol, quantity, price, value in details:
        print(f"{symbol:<8}{quantity:<8}${price:<9}${value:<10}")

    print("-" * 45)
    print(f"TOTAL INVESTMENT VALUE: ${total:,.2f}")
    print("=" * 45)


def save_to_txt(details, total, filename="portfolio_summary.txt"):
    """Save the portfolio summary to a .txt file."""
    with open(filename, "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 45 + "\n")
        f.write(f"{'Symbol':<8}{'Qty':<8}{'Price':<10}{'Value':<10}\n")
        f.write("-" * 45 + "\n")

        for symbol, quantity, price, value in details:
            f.write(f"{symbol:<8}{quantity:<8}${price:<9}${value:<10}\n")

        f.write("-" * 45 + "\n")
        f.write(f"TOTAL INVESTMENT VALUE: ${total:,.2f}\n")

    print(f"\nSummary saved to '{filename}'")


def save_to_csv(details, total, filename="portfolio_summary.csv"):
    """Save the portfolio summary to a .csv file."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Quantity", "Price", "Value"])

        for symbol, quantity, price, value in details:
            writer.writerow([symbol, quantity, price, value])

        writer.writerow([])
        writer.writerow(["", "", "Total", total])

    print(f"Summary saved to '{filename}'")


def main():
    print("=" * 45)
    print(" STOCK PORTFOLIO TRACKER")
    print("=" * 45)

    show_available_stocks()

    portfolio = get_portfolio_input()

    if not portfolio:
        print("\nNo stocks entered. Exiting program.")
        return

    details, total = calculate_investment(portfolio)
    display_summary(details, total)

    # Ask whether to save results
    save_choice = input(
        "\nSave results to a file? (txt / csv / no): "
    ).strip().lower()

    if save_choice == "txt":
        save_to_txt(details, total)
    elif save_choice == "csv":
        save_to_csv(details, total)
    else:
        print("Results not saved.")

    print("\nThank you for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()

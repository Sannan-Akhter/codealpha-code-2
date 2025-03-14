import yfinance as yf
from prettytable import PrettyTable

portfolio = {}

def add_stock():
    ticker = input("Enter stock ticker symbol (e.g., AAPL, TSLA): ").upper()
    shares = int(input("Enter number of shares: "))
    
    if ticker in portfolio:
        portfolio[ticker] += shares
    else:
        portfolio[ticker] = shares

    print(f"{shares} shares of {ticker} added to portfolio.")

def remove_stock():
    ticker = input("Enter stock ticker symbol to remove: ").upper()
    
    if ticker in portfolio:
        del portfolio[ticker]
        print(f"{ticker} removed from portfolio.")
    else:
        print("Stock not found in portfolio.")

def view_portfolio():
    if not portfolio:
        print("Your portfolio is empty.")
        return
    
    table = PrettyTable(["Stock", "Shares", "Current Price", "Total Value"])
    total_portfolio_value = 0

    for ticker, shares in portfolio.items():
        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")['Close'].iloc[-1]
        total_value = shares * price
        total_portfolio_value += total_value
        
        table.add_row([ticker, shares, f"${price:.2f}", f"${total_value:.2f}"])

    print("\nStock Portfolio:")
    print(table)
    print(f"Total Portfolio Value: ${total_portfolio_value:.2f}")

def main():
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_stock()
        elif choice == '2':
            remove_stock()
        elif choice == '3':
            view_portfolio()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

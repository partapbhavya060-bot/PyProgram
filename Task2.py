def stock_tracker():
    # Hardcoded stock prices
    prices = {"AAPL": 150, "TSLA": 250, "GOOGL": 140, "AMZN": 180}
    portfolio = {}

    print("Enter stocks and quantities (type 'done' to finish):")
    while True:
        ticker = input("Stock symbol: ").upper()
        if ticker == 'DONE': break
        if ticker not in prices:
            print("Stock not found.")
            continue
        
        qty = int(input(f"Quantity of {ticker}: "))
        portfolio[ticker] = portfolio.get(ticker, 0) + qty

    total_value = sum(prices[ticker] * qty for ticker, qty in portfolio.items())
    
    print(f"\nTotal Portfolio Value: ${total_value}")
    
    # Optional: Save to file
    with open("portfolio.txt", "w") as f:
        f.write(f"Total Value: ${total_value}")

if __name__ == "__main__":
    stock_tracker()
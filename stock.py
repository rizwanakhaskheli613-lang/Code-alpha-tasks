portfolio = {
    "AAPL": 10,   # Apple - 10 shares
    "TSLA": 5,    # Tesla - 5 shares
    "MSFT": 8     # Microsoft - 8 shares
}

stock_prices = {
    "AAPL": 210,
    "TSLA": 320,
    "MSFT": 500
}

total_value = 0

print("Stock Portfolio")
print("----------------")

for stock, shares in portfolio.items():
    value = shares * stock_prices[stock]
    total_value += value
    print(f"{stock}: {shares} shares × ${stock_prices[stock]} = ${value}")

print("----------------")
print(f"Total Portfolio Value = ${total_value}")
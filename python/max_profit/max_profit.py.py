def find_best_prices(prices):
    """
    Find the best buy and sell prices to maximize profit.
    Returns a tuple of (buy_price, sell_price, max_profit).
    """
    if not prices or len(prices) < 2:
        return None, None, 0
    
    # Initialize variables
    min_price = float('inf')
    max_profit = 0
    best_buy = None
    best_sell = None
    
    # Iterate through the prices
    for price in prices:
        # Update the minimum price seen so far
        if price < min_price:
            min_price = price
        
        # Calculate potential profit if we sell at current price
        current_profit = price - min_price
        
        # Update max profit if current profit is greater
        if current_profit > max_profit:
            max_profit = current_profit
            best_buy = min_price
            best_sell = price
    
    return best_buy, best_sell, max_profit


if __name__ == "__main__":
    # Loop until valid input is received
    while True:
        try:
            # Get price list from user
            user_input = input("Enter a list of prices separated by commas: ")
            
            # Check if input is empty
            if not user_input.strip():
                print("Input cannot be empty. Please try again.")
                continue
                
            # Convert input to list of integers
            prices = [int(price.strip()) for price in user_input.split(',')]
            
            # Check if list has at least two prices
            if len(prices) < 2:
                print("Please enter at least two prices to compare.")
                continue
                
            # Valid input received, break the loop
            break
            
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    # Calculate best prices
    buy_price, sell_price, profit = find_best_prices(prices)
    
    if profit > 0:
        print(f"Best buy price: {buy_price}")
        print(f"Best sell price: {sell_price}")
        print(f"Maximum profit: {profit}")
    else:
        print("No profit possible with the given prices.")
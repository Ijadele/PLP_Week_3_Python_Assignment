def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount is 20% or higher, apply it; otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount = (discount_percent / 100) * price
        final_price = price - discount
        return final_price
    else:
        return price
    
# prompt the user
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result
    if final_price < original_price:
        print(f"The final price after a {discount_percentage}% discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: ${original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")
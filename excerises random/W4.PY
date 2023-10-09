# Ask the user for the price of a child's meal and store it as a floating point number
child_meal_price = float(input("Enter the price of a child's meal:10.5 "))

# Ask the user for the price of an adult's meal and store it as a floating point number
adult_meal_price = float(input("Enter the price of an adult's meal:20.5 "))

# Ask the user for the number of children and store it as an integer
num_children = int(input("Enter the number of children:5 "))

# Ask the user for the number of adults and store it as an integer
num_adults = int(input("Enter the number of adults:5 "))

# Ask the user for the sales tax rate and store it as a floating point number
sales_tax_rate = float(input("Enter the sales tax rate (in percentage):8 ")) / 100

# Compute the subtotal
subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)

# Calculate the sales tax
sales_tax = subtotal * sales_tax_rate

# Calculate the total
total = subtotal + sales_tax

# Ask the user for the payment amount and store it as a floating point number
payment_amount = float(input("Enter the payment amount: "))

# Calculate the change
change = payment_amount - total

# Display the subtotal, sales tax, total, and change
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")
print(f"Change: ${change:.2f}")
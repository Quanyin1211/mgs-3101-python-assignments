# Store values into variables
shop_name = "Vera's Coffee"
number_of_drinks_sold = 165
price_per_drink = 4.25
number_of_pastries_sold = 90
price_per_pastry = 3.5

# Calculate revenue
drink_revenue = number_of_drinks_sold * price_per_drink
pastry_revenue = number_of_pastries_sold * price_per_pastry
total_revenue = drink_revenue + pastry_revenue
print(total_revenue)

# Read and print the txt file
with open("assignment1_salesAnalysis/report.txt", "r") as file:
    content = file.read()
    print(content)

    # Check if total revenue reaches $500 target
if total_revenue >= 500:
    print(f"Total revenue is ${total_revenue:.2f}. Great! Meets the $500 target.")
else:
    print(f"Total revenue is ${total_revenue:.2f}. Below the $500 target.")




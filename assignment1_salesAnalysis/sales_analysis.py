# MGS-3101 Assignment 1 - Sales Analysis
# Store: Lower Manhattan, Date: 2023-03-27


#store variables
shop_name = "Lower Manhattan"
number_of_drinks_sold = 369
price_per_drink = 2.96
number_of_pastries_sold = 45
price_per_pastry = 3.39

#caculate revenue
drink_revenue = number_of_drinks_sold * price_per_drink
pastry_revenue = number_of_pastries_sold * price_per_pastry
total_revenue = drink_revenue + pastry_revenue
print(drink_revenue)
print(pastry_revenue)
print(total_revenue)

#write a txt file
with open("sales_analysis.txt", "w") as f:
    f.write("Shop: " + shop_name + "\n")
    f.write("Drink revenue: $" + str(drink_revenue) + "\n")
    f.write("Pastry revenue: $" + str(pastry_revenue) + "\n")
    f.write("Total revenue: $" + str(total_revenue) + "\n")

#if/else
if total_revenue >= 500:
    print("Total revenue is at least $500.")
else:
    print("Total revenue is below $500.")


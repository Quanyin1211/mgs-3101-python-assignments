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

#print the txt file
with open("assignment1_salesAnalysis/sales_analysis.txt", "r") as f:
    print(f.read())

#if/else
if total_revenue >= 500:
    print("Total revenue is at least $500.")
else:
    print("Total revenue is below $500.")

#supporting data for recommendations
#1
bakery_attach_rate = 8040 / 57518
# sum(Coffee+Tea+Drinking Chocolate, 6 months)/sum(Bakery, 6 months)
#2
jan_sales = 8249
feb_sales = 7895
mar_sales = 10209
apr_sales = 12249
may_sales = 16175
jun_sales = 16965
growth = jun_sales / jan_sales
#3
coffee_count = 18204
tea_count = 13912
bakery_count = 7890
drinking_choco_count = 3405
flavours_count = 2930
coffee_beans_count = 531
loose_tea_count = 381
branded_count = 349
packaged_choco_count = 180




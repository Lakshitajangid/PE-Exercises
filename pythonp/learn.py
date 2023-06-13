def calculate_sales():
    print("Welcome to the Daily Sales Calculator!")
    sales_input = input("Please enter the sales amounts for today separated by spaces: ")

    sales_list = sales_input.split()
    
    sales_list = [int(amount) for amount in sales_list]
    
    total_sales = sum(sales_list)
    
    average_sales = total_sales / len(sales_list)
    
    print("Thank you for providing the sales data.")
    print("Today's total sales amount is: Rupees", total_sales)
    print("The average sales per transaction is:"(average_sales))

calculate_sales()

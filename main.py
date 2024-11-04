import datetime

# Create Order class
class Order:
    # Create constructor to initiate attributes
    def __init__(self, order_id, order_date, customer_name, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_amount = total_amount
    
    # Create calculate_tax method to return the amount of tax of each order
    def calculate_tax(self, tax_rate):
        self.tax_rate = tax_rate
        tax = self.total_amount * tax_rate
        return tax
    
    # Create display_order method to show the details of the order
    def display_order(self):
        print(f"Order ID: {self.order_id}")
        print(f"Order Date: {self.order_date}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Total Amount: {self.total_amount}")
    

# Create OrderProcessor class
class OrderProcessor:
    # Create constructor to initiate an empty list
    def __init__(self):
        self.order_list = []
    
    # Create add_order method to store the order to the list
    def add_order(self, order):
        self.order = order
        self.order_list.append(self.order)
    
    # Create calculate_total_revenue method to return total amount of revenue of all orders
    def calculate_total_revenue(self):
        total_revenue = 0
        for i in self.order_list:
            total_revenue = total_revenue + i.total_amount
            
        return total_revenue
    
    
    # Create calculate_total_tax method to return total amount of tax of all orders
    def calculate_total_tax(self, tax_rate):
        total_revenue = self.calculate_total_revenue()
        total_tax = total_revenue * tax_rate
        return total_tax
    
    
    # Create display_orders method to print out all orders
    def display_orders(self):
        for i in self.order_list:
            print(f"Order ID: {i.order_id}")
            print(f"Order Date: {i.order_date}")
            print(f"Customer Name: {i.customer_name}")
            print(f"Total Amount: {i.total_amount}")
            print("") # for space
    
    

# Create several Order Objects
order1 = Order(1, datetime.datetime(2024,11,1), "Angkasa",  250000)
order2 = Order(2, datetime.datetime(2024,11,2), "Buya",  200000)
order3 = Order(3, datetime.datetime(2024,11,3), "Caulkin",  320000)
order4 = Order(4, datetime.datetime(2024,11,4), "Dormamu",  170000)
order5 = Order(5, datetime.datetime(2024,11,5), "Ebenhaezer",  380000)

# Display the details of Order 1
order1.display_order()

# Get the amout of tax for Order 1 and Print It Out
tax_order1 = order1.calculate_tax(0.05)
print(f"Amount of Tax for Order {order1.order_id}: {tax_order1}")



# Create processor object to process the orders
processor = OrderProcessor()

# Add the orders
processor.add_order(order1)
processor.add_order(order2)
processor.add_order(order3)
processor.add_order(order4)
processor.add_order(order5)

# Calculate and print total revenue of all the orders
total_revenue = processor.calculate_total_revenue()
print(f"Total Revenue of All Orders: {total_revenue}")

# Calculate and print total revenue of all the orders
total_tax = processor.calculate_total_tax(0.05)
print(f"Total Tax of All Orders: {total_tax}")


# Display all the orders
processor.display_orders()
# Order Management System

A simple Python-based order management system that handles orders, calculates revenue, and processes taxes.

## Overview

This system consists of two main classes:
- `Order`: Represents individual orders with customer details and amounts
- `OrderProcessor`: Manages multiple orders and performs calculations across all orders

## Features

- Create and manage individual orders
- Calculate tax for individual orders
- Track multiple orders in a centralized processor
- Calculate total revenue across all orders
- Calculate total tax across all orders
- Display order details individually or in bulk

## Class Structure

### Order Class

The `Order` class represents a single order with the following attributes:
- `order_id`: Unique identifier for the order
- `order_date`: Date of the order (datetime object)
- `customer_name`: Name of the customer
- `total_amount`: Total amount of the order

Methods:
- `calculate_tax(tax_rate)`: Calculates tax for the order based on given tax rate (e.g. 0.05 for 5%)
- `display_order()`: Displays the order details

### OrderProcessor Class

The `OrderProcessor` class manages multiple orders with the following functionality:
- Maintains a list of orders
- Adds new orders to the system
- Calculates total revenue across all orders
- Calculates total tax across all orders
- Displays all orders in the system

Methods:
- `calculate_tax(tax_rate)`: Calculates tax for the order based on given tax rate (e.g. 0.05 for 5%)
- `display_order()`: Displays the order details


## Usage Examples

### 1. Creating Single Order

```python
import datetime

# Create a basic order
single_order = Order(
    order_id=1,
    order_date=datetime.datetime.now(),
    customer_name="John Doe",
    total_amount=100.00
)
```

#### 1a. Display the order details
```python
single_order.display_order()
```

#### 1b. Calculate tax (5% rate)
```python
tax_amount = single_order.calculate_tax(0.05)
print(f"Tax amount: ${tax_amount:.2f}")
```

### 2. Processing Multiple Orders
#### 2a. Create an order processor
```python
processor = OrderProcessor()
```

#### 2b. Create multiple orders
```python
order1 = Order(1, datetime.datetime(2024, 1, 1), "Alice Smith", 150.00)
order2 = Order(2, datetime.datetime(2024, 1, 2), "Bob Johnson", 200.00)
order3 = Order(3, datetime.datetime(2024, 1, 3), "Carol White", 175.00)
```

#### 2c. Add orders to processor
```python
processor.add_order(order1)
processor.add_order(order2)
processor.add_order(order3)
```

#### 2d. Display all orders
```python
processor.display_orders()
```


#### 2e. Calculate total revenue
```python
total_revenue = processor.calculate_total_revenue()
print(f"Total Revenue: ${total_revenue:.2f}")
```

#### 2f. Calculate total tax (5%)
```python
total_tax = processor.calculate_total_tax(0.05)
print(f"Total Revenue: ${total_tax:.2f}")
```
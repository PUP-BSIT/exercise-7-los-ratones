def get_order_details():
    orders = []
    user_input = "y"

    print("=-=-=ORDERS DETAILS=-=-=-")
    while user_input != "n":
        product_name = input("Enter item name: ")
        product_price = float(input(f"Enter price for {product_name}: "))
        product_quantity = int(input(f"Enter quantity for {product_name}: "))
        item = [product_name, product_price, product_quantity]
        orders.append(item)
        user_input = input("Do you want to add another item? (y/n): ").lower()

    return orders

def get_customer_details():
   print("\n=-=-=-CUSTOMER DETAILS-=-=-=")
   customer_name = input("Enter Customer Name: ")
   senior_id = input("Enter Senior ID Number here (blank if none): ")

   if not senior_id.strip():
        senior_id = None  
   else:
        senior_id = int(senior_id)
    
   customer = [customer_name, senior_id]

   return customer

def calculate_grand_total(orders, senior_id):
    grand_total = 0

    for item in orders:
        product_price = item[1]
        product_quantity = item[2]
        grand_total += product_price * product_quantity

    if senior_id != None:
        grand_total -= grand_total * 0.10 

    return grand_total

def display_order(orders, customer_name, senior_id, grand_total):
    print("\n=-=-= RECEIPT =-=-=")
    print("--------------------------------------------")
    print("Product Name      Price      Quantity  Total")
    print("--------------------------------------------")

    for product_name, product_price, product_quantity in orders:
        total_price = product_price * product_quantity
        
        print(f"{product_name:<15} {product_price:<10.2f} ", end = "")
        print(f"{product_quantity:<8} {total_price:<.2f}")

    print("--------------------------------------------")
    print(f"Customer Name: {customer_name}")
    print(f"Senior ID No.: {senior_id if senior_id else 'N/A'}")
    print(f"Grand Total: {grand_total:.2f}")

def main_function():
    print("=-=-=-Welcome to Ordering System!!-=-=-=")
    orders = get_order_details()
    customer = get_customer_details()
    customer_name = customer[0]
    senior_id = customer[1]
    grand_total = calculate_grand_total(orders, senior_id)
    display_order(orders, customer_name, senior_id, grand_total)

main_function()
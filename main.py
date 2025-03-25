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

def calculate_grand_total():
    """
    TODO(Kenji Enishi Campos): 
    Create a function that calculate the grand total of items.
    """
    pass

def display_receipt():
    """
    TODO(Dion Manicio):
    Create a function that displays the order information.
    """
    pass

def main_function():
    """
    TODO(Paul Benidict Reduta): 
    Create a function that integrates all the other functions.
    """
    pass

main_function()
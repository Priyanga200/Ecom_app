import sys

sys.path.append(r"D:\Hexaware\Ecom_app")
from datetime import datetime
from dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl
from entity.Customers import Customers
from entity.Products import Products
from entity.Cart import Cart
from entity.Orders import Orders
from entity.Order_items import Order_items
from exception.CustomerNotFoundException import CustomerNotFoundException
from exception.ProductNotFoundException import ProductNotFoundException
from exception.OrderNotFoundException import OrderNotFoundException
from util import DBConnUtil
from util import PropertyUtil

def main():
    repository = OrderProcessorRepositoryImpl()

    while True:
        print("\nE-commerce Application")
        print("1. Register Customer")
        print("2. Create Product")
        print("3. Delete Product")
        print("4. Add to Cart")
        print("5. View Cart")
        print("6. Place Order")
        print("7. View Customer Orders")
        print("8. Exit")
        
        try:
            choice = int(input("Choose an option: "))
            
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            
            customer_id = int(input("Customer ID: "))
            cname = input("Enter customer name: ")
            email = input("Enter customer email: ")
            passwords = input("Enter password: ")
            customers = Customers(customer_id, cname, email, passwords)
            
            if repository.createCustomer(customers):
                print("Customer registered successfully...")
            else:
                print("Error registering customer...")

        elif choice == 2:
            
            product_id = int(input("Enter Product ID: "))
            pname = input("Enter product name: ")
            price = float(input("Enter product price: "))
            descriptions = input("Enter product description: ")
            stockQuantity = int(input("Enter stock quantity: "))
            products = Products(product_id, pname, price, descriptions, stockQuantity)
            
            if repository.createProduct(products):
                print("Product created successfully...")
            else:
                print("Error creating product.")

        elif choice == 3:
            
            product_id = int(input("Enter product ID to delete: "))
            
            if repository.deleteProduct(product_id):
                print("Product deleted successfully!")
            else:
                print("Error deleting product.")

        elif choice == 4:
            
            cart_id = int(input("Enter Cart ID: "))
            customer_id = int(input("Enter customer ID: "))
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))
            
            if repository.addToCart(cart_id, customer_id, product_id, quantity):
                print("Product added to cart successfully...")
            else:
                print("Error adding product to cart.")

        elif choice == 5:
            
            customer_id = int(input("Enter customer ID to view cart: "))
            try:
                cart_items = repository.getAllFromCart(customer_id)
                if cart_items:
                    print("Cart items:")
                    for item in cart_items:
                        print(f"Product ID: {item[0]}, Name: {item[1]}, Price: {item[2]}, Quantity: {item[3]}")
                else:
                    print("Your cart is empty.")
            except Exception as e:
                print(f"Error retrieving cart items: {e}")
                
        elif choice == 6:
            
            customer_id = int(input("Enter customer ID: "))
            order_date = input("Enter order date (YYYY-MM-DD): ")
            total_price = int(input("Enter the price :"))
            shipping_address = input("Enter shipping address: ")
            try :
                repository.placeOrder(customer_id, order_date,total_price,shipping_address)
                print("order placed successfully...")
                
            except Exception as e:
                print(e)

        elif choice == 7:
            
            customer_id = int(input("Enter customer ID to view orders: "))
            try:
                results = repository.getOrdersByCustomer(customer_id)
                if results:
                    print("Customer orders:")
                    
                    for order in results:
                        print(f"Order ID: {order[0]}, Customer ID: {order[1]}, Order Date: {order[2]},Total Price: {order[3]}, Shipping Address: {order[4]}")
                else:
                    print("No orders found for the customer.")
            except OrderNotFoundException as e:
                print(f"Error retrieving orders: {e}")

        elif choice == 8:
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again!!!")

if __name__ == "__main__":
    main()




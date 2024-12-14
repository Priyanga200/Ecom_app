import pyodbc
import sys
from datetime import datetime
sys.path.append(r"D:\Hexaware\Ecom_app")

from dao.OrderProcessorRepository import OrderProcessorRepository
from util.DBConnUtil import DBConnUtil
from util.PropertyUtil import PropertyUtil
from exception.CustomerNotFoundException import CustomerNotFoundException
from exception.ProductNotFoundException import ProductNotFoundException
from exception.OrderNotFoundException import OrderNotFoundException


class OrderProcessorRepositoryImpl(OrderProcessorRepository):
     def __init__(self):
        self.connection = DBConnUtil.get_connection()

     #createProduct
     def createProduct(self, products):
        cursor=self.connection.cursor()
        
        try:
            cursor.execute("INSERT INTO Products(product_id, pname, price, descriptions, stockQuantity) VALUES (?, ?, ?, ?, ?)", 
                      (products.product_id,products.pname,products.price,products.descriptions,products.stockQuantity))
            self.connection.commit()
            return True
        
        except Exception as e:
            print(f"Error inserting Product: {e}")
            
     #createCustomer       
     def createCustomer(self, customers):
        cursor=self.connection.cursor()
        
        try:
            cursor.execute("INSERT INTO Customers (customer_id, cname, email, passwords) VALUES (?, ?, ?, ?)", 
                      (customers.customer_id, customers.cname, customers.email, customers.passwords))
            self.connection.commit()
            return True
           
        except Exception as e:
             print(f"Error inserting customer: {e}")

     #deleteProduct
     def deleteProduct(self, product_id):
        cursor=self.connection.cursor()
        
        try:
            cursor.execute("DELETE FROM Order_items where product_id=?",(product_id)) 
            cursor.execute("DELETE FROM Cart where product_id= ?",(product_id))
            cursor.execute("DELETE FROM Products where product_id= ?",(product_id))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)

     #deleteCustomer   
     def deleteCustomer(self,customer_id):
        cursor=self.connection.cursor()
        
        try:
            cursor.execute("DELETE FROM Customers where customer_id= ?",(customer_id))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)

     #addToCart
     def addToCart(self, cart_id, customer_id, product_id, quantity):
         try:
             cursor = self.connection.cursor()
             cursor.execute(
                 "INSERT INTO Cart (cart_id, customer_id, product_id, quantity) VALUES (?, ?, ?, ?)",
                 (cart_id,customer_id, product_id, quantity))
             self.connection.commit()
             return True
         except Exception as e:
             print(f"Error adding to cart: {e}")
             
     #removeFromCart
     def removeFromCart(self,customers,products):
        cursor=self.connection.cursor()
        
        try:
            cursor.execute("DELETE FROM Carts where customer_id= ? AND product_id= ?"),(customers.customer_id,products.product_id)
            self.connection.commit()
            return True
        except Exception as e:
            print(e)

     #placeOrder
     def placeOrder(self, customer_id, order_date,total_price, shipping_address: str):
        cursor = self.connection.cursor()
        
        try:
            cursor.execute("INSERT INTO Orders VALUES (?, ?, ?, ?) ", (customer_id, order_date, total_price, shipping_address))
            self.connection.commit()
        except Exception as e:
            print(f"Error placing order: {e}")
            raise

     #getAllFromCart
     def getAllFromCart(self, customer_id):
         cursor = self.connection.cursor()
         cursor.execute("SELECT p.product_id, p.pname, p.price, c.quantity FROM Products AS p JOIN Cart AS c ON p.product_id = c.product_id WHERE c.customer_id = ?", (customer_id,))
         cart_items = cursor.fetchall()
         return cart_items
    
     #getOrdersByCustomer
     def getOrdersByCustomer(self, customer_id: int):
          if not self.customerExists(customer_id):
             raise CustomerNotFoundException("Customer not found")
    
          cursor = self.connection.cursor()
          try:
             cursor.execute("SELECT * FROM orders WHERE customer_id = ?", (customer_id,))
             results = cursor.fetchall()
             return results   
          except Exception as e:
             print(f"Error fetching orders: {e}")
             raise e

     #customerExists
     def customerExists(self, customer_id: int):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,))
        return cursor.fetchone() is not None

     #findProductById
     def findProductById(self, product_id: int):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM products WHERE product_id = ?", (product_id,))
        result = cursor.fetchone()
        
        if result is None:
            raise ProductNotFoundException(f"Product with ID {product_id} not found")
        return result























    

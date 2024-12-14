from abc import ABC, abstractmethod
import sys
sys.path.append(r"D:\Hexaware\Ecom_app")

from entity import Customers
from entity import Products
from entity import Cart
from entity import Orders
from entity import Order_items 

class OrderProcessorRepository(ABC):
    @abstractmethod
    def createProduct(self,products:Products): pass
    
    @abstractmethod
    def createCustomer(self,customers: Customers): pass
    
    @abstractmethod
    def deleteProduct(self, product_id: int): pass

    @abstractmethod
    def deleteCustomer(self,customer_id: int): pass

    @abstractmethod
    def addToCart(self, cart_id:Cart,customer_id:Customers, product_id:Products,quantity): pass 

    @abstractmethod
    def removeFromCart(self,customers:Customers, products:Products): pass

    @abstractmethod
    def getAllFromCart(self,customers:Customers ,products: list[dict[str]]): pass

    @abstractmethod
    def placeOrder(self, customer_id:Customers, order_date ,total_price , shipping_address: str):pass
    
    @abstractmethod
    def getOrdersByCustomer(self, customer_id :int):pass

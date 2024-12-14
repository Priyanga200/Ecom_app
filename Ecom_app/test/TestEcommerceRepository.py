import unittest
import sys
sys.path.append(r"D:\Hexaware\Ecom_app")
from dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl
from entity.Products import Products
from entity.Cart import Cart
from entity.Orders import Orders
from exception.CustomerNotFoundException import CustomerNotFoundException
from exception.ProductNotFoundException import ProductNotFoundException

class TestEcommerceRepository(unittest.TestCase):
    
    def setUp(self):
               self.repository = OrderProcessorRepositoryImpl()
    
    # Test Case 1: Test Product Created Successfully
    
    def test_createProduct(self):
        product = Products(126, "Laptop", 75000.0, "Gaming Laptop", 10)
        result = self.repository.createProduct(product)
        
        self.assertTrue(result, "Failed to create the product.")
    
    # Test Case 2: Test Product Added to Cart Successfully
    
    def test_addToCart(self):
        cart = Cart(1028, 4, 104, 5) 
        result = self.repository.addToCart(cart.cart_id,cart.customer_id,cart.product_id,cart.quantity)
        
        self.assertTrue(result, "Failed to add the product to the cart.")

    # Test Case 3: Test Product Ordered Successfully
    
    def test_placeOrder(self):
        orders = Orders(6, '2024-01-05', 50000 , "Bangalore")
        result = self.repository.placeOrder(orders.customer_id, orders.order_date,orders.total_price, orders.shipping_address)

        self.assertTrue(result, "Failed to place the order.")

    
    # Test Case 4: Test Exception Thrown When Customer/Product Not Found
    
    def test_CustomerNotFoundException_or_ProductNotFoundException(self):
    
        with self.assertRaises(CustomerNotFoundException):
            self.repository.getOrdersByCustomer(-1)
        
        with self.assertRaises(ProductNotFoundException):
            self.repository.findProductById(-1)

if __name__ == '__main__':
    unittest.main()

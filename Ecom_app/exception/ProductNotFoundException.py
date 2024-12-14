import sys
sys.path.append(r"D:\Hexaware\Ecom_app\dao")

class ProductNotFoundException(Exception):
    def __init__(self, message="Product not found"):
        self.message = message
        super().__init__(self.message)


import sys
sys.path.append(r"D:\Hexaware\Ecom_app\dao")

class CustomerNotFoundException(Exception):
    def __init__(self, message="Customer not found"):
        self.message = message
        super().__init__(self.message)

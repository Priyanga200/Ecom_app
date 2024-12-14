import pyodbc

import sys
sys.path.append(r"D:\Hexaware\Ecom_app")

from util.PropertyUtil import PropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection():
        connection_string = PropertyUtil.get_property_string()
        return pyodbc.connect(connection_string)

    




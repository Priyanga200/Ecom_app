import sys
sys.path.append(r"D:\Hexaware\Ecom_app")


import pyodbc
import configparser

driver_name='SQL Server'
server= 'localhost\SQLEXPRESS' 
database='Ecom'


class PropertyUtil:
    @staticmethod
    def get_property_string():
        connection_string = (
            f'Driver={driver_name};'
            f'Server={server};'
            f'Database={database};'
            f'Trusted_Connection=yes;')
        return connection_string

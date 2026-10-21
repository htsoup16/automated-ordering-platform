# Miriam Rose CIS 345 online Final Project Classes

from os import path
import csv

# dictionary for cost of menu items
items = {'1': 8.00, '2': 10.00, '3': 10.00, '4': 7.00,
         '5': 8.00, '6': 9.00, '7': 5.00, '8': 4.00}


class Order:
    def __init__(self, name, time, address, order_type, location, orders=None):
        """Initialize Order initial values"""
        self.name = name
        self.time = time
        self.address = address
        self.order_type = order_type
        self.cost = 0.00
        self.location = location
        if orders is None:
            self._orders = []
        else:
            self._orders = orders

    @property
    def name(self):
        return self.__name.capitalize()

    @name.setter
    def name(self, new_name):
        if new_name.isalpha() and len(new_name) >= 1:
            self.__name = new_name
        else:
            self.__name = 'Invalid'

    @property
    def orders(self):
        return self._orders

    @orders.setter
    def orders(self, orders):
        self.orders = orders

    def add_order(self):
        for i in self.orders:
            self.cost += items[str(i)]

        if not path.isfile('orders.csv'):
            with open('orders.csv', 'w') as fp:
                data = csv.writer(fp)
                data.writerow(['Name', 'Time', 'Address', 'Order Type', 'Orders', 'Cost', 'Location'])

        # Convert list to string
        orderstring = ' '.join(str(order) for order in self.orders)

        with open('orders.csv', 'a') as fp:
            data = csv.writer(fp)
            if self.order_type == 1:
                self.order_type = 'Pickup'
            else:
                self.order_type = 'Delivery'
            data.writerow([self.name, self.time, self.address, self.order_type,
                           orderstring, self.cost, self.location])
        return self.cost


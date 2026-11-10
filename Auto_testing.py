# Miriam Rose CIS 345 online Final Project Auto testing

from Class import Order
import time


class TestOrder:
    def test_detail(self):
        print('Test Case 1: can create a new Order Instance')
        p1 = Order('Test', time.ctime(), '123 Any St', '2', 'Mesa')
        assert ('Test', time.ctime(), '123 Any St', '2', 'Mesa') == \
            (p1.name, p1.time, p1.address, p1.order_type, p1.location)

    def test_invalid(self):
        print('Test Case 2: test invalid')
        p2 = Order('Invalid', time.ctime(), '123 Any St', '2', 'Mesa')
        assert ('Invalid', time.ctime(), '123 Any St', '2', 'Mesa') == \
               (p2.name, p2.time, p2.address, p2.order_type, p2.location)

    def test_firstname(self):
        print('Test Case 3: test single letter first name')
        p3 = Order('T', time.ctime(), '123 Any St', '2', 'Mesa')
        assert ('T', time.ctime(), '123 Any St', '2', 'Mesa') == \
               (p3.name, p3.time, p3.address, p3.order_type, p3.location)

    def test_number(self):
        print('Test Case 4: test first name entered with numbers')
        p4 = Order('1234', time.ctime(), '123 Any St', '2', 'Mesa')
        assert ('Invalid', time.ctime(), '123 Any St', '2', 'Mesa') == \
               (p4.name, p4.time, p4.address, p4.order_type, p4.location)

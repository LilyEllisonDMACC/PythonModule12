"""
Program: test_customer_exceptions.py
Author: Lily Ellison
Last date modified: 04/06/2023

The purpose of this program is to test a class, customer_exceptions.py.

"""

import unittest
from custom_exceptions.customer_exceptions import Customer as cust
from custom_exceptions.test_custom_exceptions import InvalidCustomerIdException, InvalidNameException, InvalidPhoneNumberFormat


class CustomerExceptionsTest(unittest.TestCase):
    def setUp(self):
        self.Customer = cust(1230, 'Smith', 'Joe', '555-552-5599')

    def tearDown(self):
        del self.Customer

    def test_object_created_required_attributes(self):
        self.assertEqual(self.Customer.customer_id, 1230)
        self.assertEqual(self.Customer.last_name, 'Smith')
        self.assertEqual(self.Customer.first_name, 'Joe')
        self.assertEqual(self.Customer.phone_number, '555-552-5599')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(InvalidNameException):
            cust(1230, '456', 'Daisy', '555-552-5599')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(InvalidNameException):
            cust(1230, 'Duck', '123', '555-552-5599')

    def test_object_not_created_error_phone_number(self):
        with self.assertRaises(InvalidPhoneNumberFormat):
            cust(1230, 'Duck', 'Daisy', 'ABC')

    def test_object_not_created_error_cust_id(self):
        with self.assertRaises(InvalidCustomerIdException):
            cust('*knh', 'Duck', 'Daisy', '555-552-5599')

    def test_object_not_created_error_cust_id_too_high(self):
        with self.assertRaises(InvalidCustomerIdException):
            cust(10000, 'Duck', 'Daisy', '555-552-5599')

    def test_object_not_created_error_cust_id_too_low(self):
        with self.assertRaises(InvalidCustomerIdException):
            cust(123, 'Duck', 'Daisy', '555-552-5599')
    def test_Customer_str(self):
        self.assertEqual(str(self.Customer), "1230: Smith, Joe Phone: 555-552-5599")  # Uses person from setUp()

if __name__ == '__main__':
    unittest.main()

"""
Testing:

Ran 8 tests in 0.004s

OK

Process finished with exit code 0

"""

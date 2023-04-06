"""
Program: customer_exceptions.py
Author: Lily Ellison
Last date modified: 04/06/2023

The purpose of this program is to create a customer class that has custom exceptions.

"""
from custom_exceptions.test_custom_exceptions import InvalidCustomerIdException, InvalidNameException, InvalidPhoneNumberFormat


class Customer:
    """Customer class"""

    def __init__(self, cid, lname, fname, pnumber, ):  # Constructor sets all to no value
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        phone_number_characters = set("1234567890-()")

        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise InvalidNameException
        if not phone_number_characters.issuperset(pnumber):
            raise InvalidPhoneNumberFormat
        if type(cid) != int:
            raise InvalidCustomerIdException
        if cid > 9999 or cid < 1000:
            raise InvalidCustomerIdException

        self.customer_id = cid
        self.last_name = lname
        self.first_name = fname
        self.phone_number = pnumber


    def __str__(self):
        return str(self.customer_id) + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number

    def __repr__(self):
        return 'Customer({},{},{},{})'.format(str(self.customer_id), self.last_name, self.first_name, self.phone_number)

    def change_last_name(self, name):
        self.last_name = name

    def change_first_name(self, name):
        self.first_name = name

    def change_phone_number(self, number):
        self.phone_number = number

    def display(self):
        return str(self.customer_id) + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number

#Driver
if __name__ == '__main__':
    customer01 = Customer(1001, "Ellison", "Hazel", "555-555-5555")
    print(customer01.display())

    try:
        customer02 = Customer(1002, "Ellison", "Hercules", "ABCDEFG")
        print(customer02.display())
    except InvalidPhoneNumberFormat:
        print("Error found: Invalid phone number")

    try:
        customer03 = Customer(1003, "Ellison", "P3ga5u5", "555-555-5555")
        print(customer03.display())
    except InvalidNameException:
        print("Error found: Invalid name")

    try:
        customer04 = Customer(1004, "E11is0n", "Pegasus", "555-555-5555")
        print(customer04.display())
    except InvalidNameException:
        print("Error found: Invalid name")

    try:
        customer05 = Customer(105, "Ellison", "Ash", "555-555-5555")
        print(customer05.display())
    except InvalidCustomerIdException:
        print("Error found: Invalid customer ID")

"""
Testing:

1001: Ellison, Hazel Phone: 555-555-5555
Error found: Invalid phone number
Error found: Invalid name
Error found: Invalid name
Error found: Invalid customer ID

Process finished with exit code 0

"""
"""
Program: test_custom_exceptions.py
Author: Lily Ellison
Last date modified: 04/06/2023

The purpose of this program is to create custom exceptions for the customer class.

"""


class InvalidCustomerIdException(Exception):
    "Raised when customer ID is not a number between 1000 and 10000."
    pass


class InvalidNameException(Exception):
    "Raised when name contains characters outside the alphabet and ' and - symbols."
    pass


class InvalidPhoneNumberFormat(Exception):
    "Raised when phone number is not in (XXX)XXX-XXXX format."
    pass

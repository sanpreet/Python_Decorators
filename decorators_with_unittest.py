"""
This code is about usage of decorators in python
Code will be implemented using unit test
"""
import unittest
def check_two_numbers(funct):
    
    
    def wrapper_function(arg1, arg2):
        first_value, second_value = funct(arg1, arg2)   
        if first_value > second_value:
            return first_value
        else:
            return second_value 

    return wrapper_function


@check_two_numbers
def function_to_store_values(a, b):
    return a, b


class Check_Number_unit_test(unittest.TestCase):

    def check_result(self):
        
        a1 = 10
        b1 = 20
        message1 = "message1: First value and second value are not equal !"
        self.assertEqual(20, function_to_store_values(a1, b1), message1)
        print("Test one is passed................")

        a2 = 100
        b2 = 20
        message2 = "\nmessage2: First value and second value are not equal !"
        self.assertEqual(20, function_to_store_values(a2, b2), message2)

        return "Success"


object_check_numbers = Check_Number_unit_test()
print(object_check_numbers.check_result()) 

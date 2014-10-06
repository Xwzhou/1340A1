#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

list_upc = []
def checksum (upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a strong
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    # check type of input
    if type(upc) == str:

        #  check length of string
        if len(upc) == 12:
                print(upc)
                # convert string to array
                # hint: use the list function
                for number in range(0,12):
                    list_upc.append(int(upc[number]))
        # raise ValueError if not 12
        else:
            raise ValueError("Not 12 digit")
    # raise TypeError if not string
    else:
        raise TypeError("Not String")
    # generate checksum using the first 11 digits provided
    #First process Adding the odd numbered digitas and multiplying by three
    odd_sum = sum(list_upc[0:11:2]) * 3
    #Second procedure Add the digits in the even numbered positions to the result
    even_sum = sum(list_upc[1:10:2])
    total_sum = odd_sum+even_sum
    #Third procedure Find the result modulo 10
    modulo_result = total_sum % 10
    #Fourth Procedure if the result is not zero, subtract the result from ten
    def modulo_check(modulo):
        """
        :param modulo: Integer value
        :return: Integer value after UPC checksum
        """
        if(modulo_result) != 0:
            return (10-modulo_result)
        else:
            return modulo_result
    final_result = modulo_check(modulo_result)
    if final_result == list_upc[11]:
        return True
    # return True if they are equal, False otherwise
    else:
        return False
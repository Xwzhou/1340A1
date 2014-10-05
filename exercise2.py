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


def checksum (upc):

    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a string
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    # check type of input
    if type(upc) is str
    else:
        raise TypeError("The type of input is not accepted.")

    # raise TypeError if not string

    # check length of string
    if len(upc) is 12
    else:
        raise ValueError("The length of input is not accepted.")
    # raise ValueError if not 12

    # convert string to array
    list_upc=list(upc)
    # hint: use the list function

    # generate checksum using the first 11 digits provided

    odd_list_upc=list_upc[::2]
    odd= sum(odd_list_upc)*3

    even_list_upc=list_upc[1::2]
    even= sum(even_list_upc)

    checksum=(odd+even)%10

    # check against the the twelfth digit
    if checksum==list_upc[12]:
        return True
      else
        return False

    # return True if they are equal, False otherwise




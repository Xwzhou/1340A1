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


def checksum(upc):
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
    # convert string to array
    # check type of input
    # raise TypeError if not string
    # check length of string
    if type(upc) is str:
        if len(upc) == 12:
            list_upc = []
            for digit in list(upc):
                list_upc.append(int(digit))
            # generate checksum using the first 11 digits provided

            # pick out all the odd-numbered digit
            odd_list_upc = list_upc[::2]
            #sum up all the odd-numbered digit and multiply by 3
            odd = sum(odd_list_upc) * 3
            #pick out all the even-numbered digit
            even_list_upc = list_upc[1:11:2]
            #sum up all the even-numbered digit
            even = sum(even_list_upc)
            #calculate checksum
            checksum = (odd + even) % 10
            if checksum != 0:
                checksum = 10 - checksum
                # check against the the twelfth digit
            if checksum == list_upc[11]:
                # return True if they are equal, False otherwise
                return True
            else:
                return False
        else:
            raise ValueError("The length of input is not accepted.")
    else:
        raise TypeError("The type of input is not accepted.")


# raise ValueError if not 12


# hint: use the list function




#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.

    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """

    letter_grade = ""
    gpa = 0.0

    if type(grade) is str:
        print ("letter")

        # check that the grade is one of the accepted values
        def check_grade_string(str_grade):
            '''
            :param str_grade(string): input value to be compared with accepted values
            :return: Value or error
            '''
            accepted_values = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'FZ']
            if str_grade in accepted_values:
                print("Letter grade is ", str_grade)
            else:
               raise ValueError("Letter grade is not one of the accepted values")
        # assign grade to letter_grade
        check_grade_string(grade)
        letter_grade = grade

    elif type(grade) is int:
        print("mark") # remove this line once the code is implemented
        # check that grade is in the accepted range
        def check_grade_integer(int_grade):
            '''
            :param int_grade(Integer): input value to be compared with accepted values
            :return: Print input value or error
            '''
            accepted_values = range(0, 101)
            if int_grade in accepted_values:
                print("Integer grade is ", int_grade)
            else:
                raise ValueError("Integer grade is not one of the accepted values")
        check_grade_integer(grade)

        # convert the numeric grade to a letter grade
        def mark_to_letter(int_grade):
            '''
            :param int_grade(integer):
            :return: Str value. Converted letter grade from integer grade.
            '''
            if int_grade in range(90,101):
                return "A+"
            elif int_grade in range(85,90):
                return "A"
            elif int_grade in range(80,85):
                return "A-"
            elif int_grade in range(77,80):
                return "B+"
            elif int_grade in range(73,77):
                return "B"
            elif int_grade in range(70,73):
                return "B-"
            else:
                return "FZ"

        # assign the value to letter_grade
        # hint: letter_grade = mark_to_letter(grade)
        letter_grade = mark_to_letter(grade)
        print(letter_grade)

    else:
        # raise a TypeError exception
        raise TypeError("Invalid type passed as parameter")

    # write a long if-statement to convert letter_grade
    if letter_grade == "A+":
        gpa = 4.0
    elif letter_grade == "A":
        gpa = 4.0
    elif letter_grade == "A-":
        gpa = 3.7
    elif letter_grade == "B+":
        gpa = 3.3
    elif letter_grade == "B":
        gpa = 3.0
    elif letter_grade == "B-":
        gpa = 2.7
    else:
        gpa = 0.0
   # assign the value to gpa

    return gpa

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

    gpa = 0.0
    letter_range = ["A+","A","A-","B+","B","B-","FZ"]
    letter_grade = ""

    if type(grade) is str:
        print ("letter") # remove this line once the code is implemented
        if grade in letter_range:
            print ("yes")
        else:
            print ("Invalid type passed as parameter1")# check that the grade is one of the accepted values
        # assign grade to letter_grade
    elif type(grade) is int:
        print("mark") # remove this line once the code is implemented

    mark_range=range(0, 101, 1)

    def mark_to_letter(grade):
        # assign the value to letter_grade
        # hint: letter_grade = mark_to_letter(grade)
        # check that grade is in the accepted range

        if grade in mark_range:
            print("grade in mark range")
        # convert the numeric grade to a letter grade
        if grade in mark_range[91:102]:
            return "A+"
        if grade in mark_range[86:91]:
            return "A"
        if grade in mark_range[81:86]:
            return "A-"
        if grade in mark_range[78:81]:
            return "B+"
        if grade in mark_range[74:78]:
            return "B"
        if grade in mark_range[71:74]:
            return "B-"
        if grade in mark_range[0:71]:
            return "FZ"
        else: raise ValueError("the mark is out of range")

    letter_grade = mark_to_letter(grade)
    print(letter_grade)
    gpa = 0.0
    # write a long if-statement to convert letter_grade
    # assign the value to gpa
    if letter_grade == "A+":
        gpa = 4.0
    elif letter_grade=="A":
        gpa = 4.0
    elif letter_grade=="A-":
        gpa = 3.7
    elif letter_grade=="B+":
        gpa = 3.3
    elif letter_grade=="B":
        gpa = 3.0
    elif letter_grade=="B-":
        gpa = 2.7
    elif letter_grade=="FZ":
        gpa = 0.0
    else:
        # raise a TypeError exception
        raise TypeError("Invalid type passed as parameter3")
    print(gpa)

"""list.py
This module contains several functions for practicing working with lists.
"""

def sum_list(lst):
    """Function returns sum of elements of alist given in parameter"""
    total = 0
    for element in lst:
        total = total + element
    return total


def find_largest(lst):
    """Function returns largest element in the list specified as a
    parameter.

    Args:
        param1 (list): A list of numbers.

    Returns:
        int: The largest element of the list.
    """
    lst.sort()
    return lst[-1]

def find_smallest(lst):
    """Function returns smallest element in the list specified as a
    parameter.

    Args:
        param1 (list): A list of numbers.

    Returns:
        int: The smallest element of the list.
    """
    lst.sort()
    return lst[0]

def get_even(lst):
    """Function returns a list containing only even number from the list
       given as a parameter.

    Params
        list: A list of integers

    Returns
        list: A list of even numbers from the parameter list.
    """
    even_lst = []
    for element in lst:
        if element % 2 == 0:
            even_lst.append(element)
    return even_lst


def print_positive(lst):
    """Function traverses list given as a parameter and prints positive
       entries.

    Params
        list: A list of numbers.
    """
    for element in lst:
        if element > 0:
            print element

def return_positive(lst):
    """Function traverses list given as a parameter and returns a list
       containing only the positive entries.

    Params
        list: A list of numbers.

    Returns
        list: A list of positive numbers from the parameter list.
    """
    new_list = []
    for element in lst:
        if element > 0:
            new_list.append(element)
    return new_list


def scale_list(lst, scale):
    """Function scales a vector(list) by the specified amount.

    Params
        list: A list of numbers, basically a vector.
        scale: An integer that will be multiplied to every entry of the
               list.

    Returns
        list: The scaled list.
    """
    new_list = []
    for element in lst:
        new_list.append(element * scale)
    return new_list


def mult_vectors(vec_a, vec_b):
    """Function multiplies two vectors together.

    Params
        vec_a(list): A list of integers, a vector.
        vec_b(list): A list of integers, a vector.

    Returns
        new_list(list): A list of integers, a new vector.
    """
    index = 0
    new_list = []
    while index < len(vec_a):
        new_list.append(vec_a[index] * vec_b[index])
    return new_list

def size_square_matrix(matrix_a):
    """Function is a helper function, main goal is to check if a given
    matrix(2d list) is square or not.

    Params
        matrix_a(list 2d): Should be a two dimensional list or matrix.

    Returns
        int: Returns a positive integer that represents the size of the
             matrix if the matrix is square. If the matrix is not square
             then -1 is returned.
    """
    row_length = len(matrix_a)
    col_height = len(matrix_a[0])
    if row_length != col_height:
        return -1
    return row_length

def matrix_add_2d(matrix_a, matrix_b):
    """Function adds two matrices together.

    Params
        matrix_a(2d list): A matrix.
        matrix_b(2d list): A matrix.

    Returns
        matrix(2d list): A matrix, the result of adding the two parameters
                         together.
    """
    if size_square_matrix(matrix_a) != size_square_matrix(matrix_b):
        print "These matrices are not the same size"
        return
    matrix_sum = []
    for i in range(len(matrix_a)):
        new_row = []
        for j in range(len(matrix_a[i])):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
            matrix_sum.append(new_row)
    return matrix_sum

matrix_first = [[1, 3], [2, 4]]
matrix_sec = [[5, 2], [1, 0]]
print matrix_add_2d(matrix_first, matrix_sec)


matrix_first = [[1, 3, 1], [2, 4, 2], [1, 1, 1]]
matrix_sec = [[5, 2], [1, 0]]

print matrix_first
print matrix_sec
print matrix_add_2d(matrix_first, matrix_sec)


def dedup(lst):
    """Function is given a list of numbers or strings, then returns a list
       minus any duplicates.

    Params
        param1 (list): The list of items that we are checking for
                       duplicates.

    Returns
        list: A list with only unique elements.
    """
    new_lst = []
    for element in lst:
        if element not in new_lst:
            new_lst.append(element)
    print new_lst

sample_list = [1, 1, 2, 3, 4, 4]
dedup(sample_list)


def matrix_mult(mat_a, mat_b):
    """Function multiplies two matrices toegether,
       Great deal of help from this site.
       https://www.programiz.com/python-programming/examples/multiply-matrix
    """
    answer = []
    # iterate through rows of first matrix
    for i in range(len(mat_a)):
        newrow = []
        # iterate through columns of second matrix
        for j in range(len(mat_b[0])):
            # iterate through rows of second matrix
            temp = 0
            for k in range(len(mat_b)):
                temp += mat_a[i][k] * mat_b[k][j]
            newrow.append(temp)
        answer.append(newrow)
    return answer

matrix1 = [[1, 1], [1, 1]]
matrix2 = [[2, 1], [1, 1]]

print matrix_mult(matrix1, matrix2)

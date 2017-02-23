#! /bin/python3

"""
No. 16 - Maximal Length of Incremental Subsequences
Problem: Given an unsorted array, find the max length of subsequence in which the
numbers are in incremental order.

For example: If the input array is {7, 2, 3, 1, 5, 8, 9, 6}, a subsequence with
the most numbers in incremental order is {2, 3, 5, 8, 9} and the expected output is 5.
"""

def incremental_seq(array):
    """
    Find the subset of the given array with incremental subsequence
    """
    size = len(array)
    result = [[0 for i in range(size)] for j in range(size)]
    result[0][0] = array[0]
    max_len = 0
    for i in range(1, size-1):
        for row in range(size):
            flag = True
            column = 0
            while flag:
                if result[row][column] != 0:
                    column += 1
                else:
                    flag = False
            if column == 0:
                result[row][column] = array[i]
                break
            if array[i] >= result[row][column-1]:
                result[row][column] = array[i]
                if column > max_len:
                    max_len = column

    return max_len+1, result

def main():
    """
    Main func
    """
    seq = [7, 2, 3, 1, 5, 8, 9, 6]
    max_len, matrix = incremental_seq(seq)
    print(max_len)
    print(matrix)

if __name__ == '__main__':
    main()

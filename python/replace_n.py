#!/bin/python3

def replace(n, array):
    end = len(array) - 1
    i = 0
    while True:
        if array[i] == n:
            if array[end] == n:
                while array[end] == n:
                    end -= 1
                    if i == end:
                        return end
            temp = array[end]
            array[end] = array[i]
            array[i] = temp
        i += 1
        if i == end:
            break
    return end

print(replace(2, [2, 3, 2, 1, 2, 3, 2]))

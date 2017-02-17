"""
You have a string, , of lowercase English alphabetic letters. You can perform two types of operations on :

Append a lowercase English alphabetic letter to the end of the string.
Delete the last character in the string. Performing this operation on an empty string results in an empty string.
Given an integer, , and two strings,  and , determine whether or not you can convert  to  by performing exactly  of the above operations on . If it's possible, print Yes; otherwise, print No.

Input Format

The first line contains a string, , denoting the initial string. 
The second line contains a string, , denoting the desired final string. The third line contains an integer, , denoting the desired number of operations.

Constraints and consist of lowercase English alphabetic letters.
Output Format

Print Yes if you can obtain string  by performing exactly  operations on ; otherwise, print No.

Sample Input 0

hackerhappy
hackerrank
9
Sample Output 0

Yes
Explanation 0

We perform  delete operations to reduce string  to hacker. Next, we perform  append operations (i.e., r, a, n, and k), to get hackerrank. Because we were able to convert  to  by performing exactly operations, we print Yes.

Sample Input 1

aba
aba
7
Sample Output 1

Yes
Explanation 1

We perform  delete operations to reduce string  to the empty string (recall that, though the string will be empty after  deletions, we can still perform a delete operation on an empty string to get the empty string). Next, we perform  append operations (i.e., a, b, and a). Because we were able to convert  to  by performing exactly  operations, we print Yes.
"""

def check_convert(original_string, target_string, n_operations):
    """
    check if the original_string can be converted to target_string in n_operations
    """
    len_original = len(original_string)
    len_target = len(target_string)
    similar_index = 0
    #import pdb;pdb.set_trace()
    flag = True
    while flag:
        #special cases
        if n_operations > (len_original + len_target):
            return True
        if original_string[similar_index] == target_string[similar_index]   \
                and similar_index < len_original:
            similar_index += 1
        else:
            similar_index -= 1
            flag = False

    if (len_original+len_target-(2*similar_index)-2) < n_operations:
        possible_operations = len_original+len_target-(2*similar_index)-2
        while True:
            possible_operations += 2
            similar_index -= 1
            if possible_operations > n_operations:
                return False
            elif possible_operations == n_operations:
                return True
            if similar_index == -1:
                return True

    if (len_original+len_target-(2*similar_index)-2) == n_operations:
        return True

def main():
    if check_convert("qwerty", "zxcvbn", 100):
        print("True")
    else:
        print("False")

if __name__ == '__main__':
    main()
         
#! /bin/python3

# Find maximum size subset of the given set of numbers wher none of the pairs in the subset result in the sum divisible by number n
# Imput: set S, integer n

def max_subset(S, n):
    len_subset = 0
    for element in S:
        temp_S = list(S)
        temp_S.remove(element)
        print("current_element {}".format(element))
        len_temp_subset = subset(element, temp_S, n)
        if len_temp_subset > len_subset:
            len_subset = len_temp_subset
    return len_subset

def subset(ele, set, n):
    len_subset = 1
    for element in set:
        if (element + ele)%n != 0:
            len_subset += 1
    return len_subset

def main():
    # S = [1, 7, 2, 4]
    # n = 3
    S = [770528134, 663501748, 384261537, 800309024, 103668401, 538539662, 385488901, 101262949, 557792122, 46058493]
    n = 5
    # x, y = input().split(" ")
    # n, k = [int(x), int(y)]
    # set = input().split(" ")
    # S = []
    # for i in range(0, k):
    #     S.append(int(set[i]))
    print(max_subset(S, n))
    
if __name__ == '__main__':
    main()

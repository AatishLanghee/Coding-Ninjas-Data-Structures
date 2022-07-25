# Question: First Index of Number

# Given an array of length N and an integer x, you need to find and return the first index of
# integer x present in the array. Return -1 if it is not present in the array.
# First index means, the index of first occurrence of x in the input array.
# Do this recursively. Indexing in the array starts from 0.

# Input Format :
# Line 1 : An Integer N i.e. size of array
# Line 2 : N integers which are elements of the array, separated by spaces
# Line 3 : Integer x

# Output Format : first index or -1
# Constraints : 1 <= N <= 10^3

# Sample Input :
# 4
# 9 8 10 8
# 8

# Sample Output : 1


def find_first_index(arr: list, index: int, q_element: int) -> int:
    # Base case
    if index == len(arr):
        return -1

    if arr[index] == q_element:
        return index

    # Smaller Output ( Induction Hypothesis or Assumption)
    small_output: int = find_first_index(arr, index + 1, q_element)

    return small_output


if __name__ == "__main__":
    size: int = int(input("Enter the size of array: "))
    input_array: list = []
    for i in range(size):
        ele: int = int(input(f"Enter the {i+1} element of array: "))
        input_array.append(ele)

    print("Input array : ", input_array)
    query_element: int = int(input("Enter the element to search for :"))
    print(find_first_index(input_array, 0, query_element))

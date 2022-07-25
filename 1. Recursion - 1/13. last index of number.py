# Question: Last Index of Number

# Given an array of length N and an integer x, you need to find and return the last index of
# integer x present in the array. Return -1 if it is not present in the array.
# Last index means - if x is present multiple times in the array, return the index at which x comes last in the array.
# You should start traversing your array from 0, not from (N - 1).
# Do this recursively. Indexing in the array starts from 0.

# Input Format :
# Line 1 : An Integer N i.e. size of array
# Line 2 : N integers which are elements of the array, separated by spaces
# Line 3 : Integer x

# Output Format : last index or -1
# Constraints : 1 <= N <= 10^3

# Sample Input :
# 4
# 9 8 10 8
# 8

# Sample Output : 3

def find_last_index(arr: list, index: int, q_element: int, found: int) -> int:
    # Base case
    if index == len(arr):
        if found != -1:
            return found
        return -1

    if arr[index] == q_element:
        found = index

    # Smaller Output ( Induction Hypothesis or Assumption)
    small_output: int = find_last_index(arr, index + 1, q_element, found)

    return small_output


if __name__ == "__main__":
    size: int = int(input("Enter the size of array: "))
    input_array: list = []
    for i in range(size):
        ele: int = int(input(f"Enter the {i+1} element of array: "))
        input_array.append(ele)

    print("Input array : ", input_array)
    query_element: int = int(input("Enter the element to search for :"))
    print(find_last_index(input_array, 0, query_element, -1))

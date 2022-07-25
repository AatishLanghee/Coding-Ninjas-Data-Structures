# Question: All Indices of Number

# Given an array of length N and an integer x, you need to find all the indexes where x is present in the
# input array. Save all the indexes in an array (in increasing order).
# Do this recursively. Indexing in the array starts from 0.

# Input Format :
# Line 1 : An Integer N i.e. size of array
# Line 2 : N integers which are elements of the array, separated by spaces
# Line 3 : Integer x

# Output Format : indexes where x is present in the array (separated by space)
# Constraints : 1 <= N <= 10^3

# Sample Input :
# 5
# 9 8 10 8 8
# 8

# Sample Output : 1 3 4

def find_last_index(arr: list, index: int, q_element: int, op_list_t: list) -> list:
    # Base case
    if index == len(arr):
        return op_list_t

    if arr[index] == q_element:
        op_list_t.append(index)

    # Smaller Output ( Induction Hypothesis or Assumption)
    small_output: list = find_last_index(arr, index + 1, q_element, op_list_t)

    return small_output


if __name__ == "__main__":
    size: int = int(input("Enter the size of array: "))
    input_array: list = []
    for i in range(size):
        ele: int = int(input(f"Enter the {i+1} element of array: "))
        input_array.append(ele)

    print("Input array : ", input_array)
    query_element: int = int(input("Enter the element to search for :"))
    op_list = []
    print(find_last_index(input_array, 0, query_element, op_list))

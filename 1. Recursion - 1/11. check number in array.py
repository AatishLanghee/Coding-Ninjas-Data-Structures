# Question: Check number in Array

# Given an array of length N and an integer x, you need to find if x is present in the array or not.
# Return true or false. Do this recursively.

# Input Format :
# Line 1 : An Integer N i.e. size of array
# Line 2 : N integers which are elements of the array, separated by spaces
# Line 3 : Integer x

# Output Format : 'true' or 'false'

# Constraints : 1 <= N <= 10^3

# Sample Input 1 :
# 3
# 9 8 10
# 8
# Sample Output 1 : true

# Sample Input 2 :
# 3
# 9 8 10
# 2
# Sample Output 2 : false


def find_element(arr: list, index: int, q_element: int) -> bool:
    # Base case
    if index == len(arr) - 1:
        if arr[index] == q_element:
            return True
        return False

    if arr[index] == q_element:
        return True

    # Smaller Output ( Induction Hypothesis or Assumption)
    small_output: bool = find_element(arr, index + 1, q_element)

    return small_output


if __name__ == "__main__":
    size: int = int(input("Enter the size of array: "))
    input_array: list = []
    for i in range(size):
        ele: int = int(input(f"Enter the {i+1} element of array: "))
        input_array.append(ele)

    print("Input array : ", input_array)
    query_element: int = int(input("Enter the element to search for :"))
    print(find_element(input_array, 0, query_element))

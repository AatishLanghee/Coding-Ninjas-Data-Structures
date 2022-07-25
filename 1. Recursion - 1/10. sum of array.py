# Question: Sum of Array

# Given an array of length N, you need to find and return the sum of all elements of the array.
# Do this recursively.

# Input Format :
# Line 1 : An Integer N i.e. size of array
# Line 2 : N integers which are elements of the array, separated by spaces

# Output Format : Sum
# Constraints : 1 <= N <= 10^3

# Sample Input 1 :
# 3
# 9 8 9

# Sample Output 1 : 26

# Sample Input 2 :
# 3
# 4 2 1

# Sample Output 2 : 7

def sum_of_array(arr: list, index: int) -> int:
    # Base case
    if index == len(arr) - 1:
        return arr[index]

    # Smaller Output ( Induction Hypothesis or Assumption)
    small_output: int = sum_of_array(arr, index + 1)

    return arr[index] + small_output


if __name__ == "__main__":
    size: int = int(input("Enter the size of array: "))
    input_array: list = []
    for i in range(size):
        ele: int = int(input(f"Enter the {i+1} element of array: "))
        input_array.append(ele)

    print("Input array : ", input_array)
    print(sum_of_array(input_array, 0))

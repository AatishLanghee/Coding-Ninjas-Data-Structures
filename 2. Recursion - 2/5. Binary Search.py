# Question: Binary search

# Given an integer sorted array (sorted in increasing order) and an element x, find the x in given array
# using binary search. Return the index of x. Return -1 if x is not present in the given array.
# Note : If given array size is even, take first mid.

# Input format :
# Line 1 : Array size
# Line 2 : Array elements (separated by space)
# Line 3 : x (element to be searched)

# Sample Input : 6
# 2 3 4 5 6 8
# 5

# Sample Output: 3

def first_solution(array_t: list, query: int, start: int, end: int) -> int:
    # Base case
    if start > end:
        return -1

    # Small output (Induction Hypothesis or Assumption)
    mid: int = (start + end) // 2
    if array_t[mid] == query:
        return mid

    if query > array_t[mid]:
        start = mid + 1
    else:
        end = mid - 1

    return first_solution(array_t, query, start, end)


if __name__ == "__main__":
    size_t: int = int(input("Enter the length of the sorted array :"))
    input_array: list = []
    for i in range(size_t):
        elem: int = int(input(f"Enter {i+1} element of the sorted array :"))
        input_array.append(elem)

    print("Input Array :", input_array)

    search_query: int = int(input(f"Enter the search element :"))

    print(first_solution(input_array, search_query, 0, size_t - 1))

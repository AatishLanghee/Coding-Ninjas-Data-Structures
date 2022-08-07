# Question: Sort an array A using Quick Sort.

# Change in the input array itself. So no need to return or print anything.

# Input format :
# Line 1 : Integer n i.e. Array size
# Line 2 : Array elements (separated by space)

# Output format : Array elements in increasing order (separated by space)

# Constraints : 1 <= n <= 10^3

# Sample Input 1 : 6
# 2 6 8 5 4 3

# Sample Output 1 : 2 3 4 5 6 8

# Sample Input 2 : 5
# 1 5 2 7 3

# Sample Output 2 :
# 1 2 3 5 7

def partition(arr: list, s: int, e: int) -> int:
    pivot_ele: int = arr[s]
    count: int = 0

    for _ in range(s, e + 1):
        if arr[_] < pivot_ele:
            count += 1

    pivot_id: int = s + count
    arr[s], arr[pivot_id] = arr[pivot_id], arr[s]

    while s < e:
        if arr[s] < pivot_ele:
            s += 1
        elif arr[e] > pivot_ele:
            e -= 1
        else:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1

    return pivot_id


def first_solution(array_t: list, start: int, end: int) -> None:
    # Base case
    if start >= end:
        return

    # Small output (Induction Hypothesis or Assumption)
    pivot_index: int = partition(array_t, start, end)

    first_solution(array_t, start, pivot_index - 1)
    first_solution(array_t, pivot_index + 1, end)


if __name__ == "__main__":
    size_t: int = int(input("Enter the length of the sorted array :"))
    input_array: list = []
    for i in range(size_t):
        elem: int = int(input(f"Enter {i+1} element of the sorted array :"))
        input_array.append(elem)

    print("Input Array :", input_array)

    first_solution(input_array, 0, size_t - 1)

    print("Output Array :", input_array)

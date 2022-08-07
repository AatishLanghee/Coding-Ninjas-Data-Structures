# Question: Merge Sort

# Sort an array A using Merge Sort.
# Change in the input array itself. So no need to return or print anything.

# Input Format :
# Line 1 : Integer n i.e. Array size
# Line 2 : Array elements (separated by space)

# Output format : Array elements in increasing order (separated by space)
# Constraints : 1 <= n <= 10^3

# Sample Input 1 :
# 6
# 2 6 8 5 4 3

# Sample Output 1 : 2 3 4 5 6 8

# Sample Input 2 :
# 5
# 2 1 5 2 3

# Sample Output 2 : 1 2 2 3 5

def merge_array(a: list, b: list, ip: list) -> None:
    x: int = 0
    y: int = 0
    z: int = 0
    while x < len(a) and y < len(b):
        if a[x] < b[y]:
            ip[z] = a[x]
            x = x + 1
            z = z + 1
        else:
            ip[z] = b[y]
            y = y + 1
            z = z + 1

    while x < len(a):
        ip[z] = a[x]
        x = x + 1
        z = z + 1

    while y < len(b):
        ip[z] = b[y]
        y = y + 1
        z = z + 1


def first_approach(ip_array: list) -> None:
    # Base case
    if len(ip_array) == 0 or len(ip_array) == 1:
        return

    # Calculate mid
    mid: int = len(ip_array) // 2
    if len(ip_array) % 2 == 1:
        mid = mid + 1

    small_array_1: list = ip_array[0:mid]
    small_array_2: list = ip_array[mid:]

    # Induction Hypothesis (Assumption)
    first_approach(small_array_1)
    first_approach(small_array_2)

    merge_array(small_array_1, small_array_2, ip_array)


if __name__ == "__main__":
    size: int = int(input("Enter the size of the array :"))
    input_array: list = []
    for i in range(size):
        ele: int = int(input(f"Enter the {i+1} element of the array :"))
        input_array.append(ele)

    print("Input Array :", input_array)
    first_approach(input_array)
    print("Sorted Array :", input_array)

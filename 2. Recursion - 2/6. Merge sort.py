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

def merge_array(a: list, b: list) -> list:
    pass


def first_approach(ip_array: list) -> list:
    pass


if __name__ == "__main__":
    size: int = int(input("Enter the size of the array :"))
    input_array: list = []
    for i in range(size):
        ele: int = int(input(f"Enter the {i+1} element of the array :"))
        input_array.append(ele)

    print("Input Array :", input_array)
    print(first_approach(input_array))

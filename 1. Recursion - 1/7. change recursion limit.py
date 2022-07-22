# Question: Change Recursion limit

# We can set the maximum recursion limit using sys module in python
# But it is not recommended as it can take (eat up) more memory space
import sys


def fibonacci(num: int) -> int:
    # Base case
    if num == 1 or num == 2:
        return num

    # Smaller output (Induction Hypothesis or Assumption)
    small_output = fibonacci(num - 1) + fibonacci(num - 2)

    return small_output


if __name__ == "__main__":
    # Set the recursion limit to whatever number you want (Not recommended)
    sys.setrecursionlimit(3000)
    
    number: int = int(input("Enter the number :"))
    print(fibonacci(number,))

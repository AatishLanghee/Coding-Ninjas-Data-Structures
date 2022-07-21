# Question: Fibonacci Series

# Given is the code to get fibonacci number recursively.

# Input Format :Integer n
# Output Format : Fibonacci series output
# Constraints : 1 <= n <= 100

# Sample Input 1 : 4
# Sample Output 1 : 5

# Sample Input 2 : 5
# Sample Output 2 : 8

def fibonacci(num: int) -> int:
    # Base case
    if num == 1 or num == 2:
        return num

    # Smaller output (Induction Hypothesis or Assumption)
    small_output = fibonacci(num - 1) + fibonacci(num - 2)

    return small_output


if __name__ == "__main__":
    number: int = int(input("Enter the number :"))
    print(fibonacci(number,))

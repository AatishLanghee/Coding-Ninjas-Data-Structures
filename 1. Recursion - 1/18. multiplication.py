# Question: Multiplication

# Given two integers M & N, calculate and return their multiplication using recursion.
# You can only use subtraction and addition for your calculation. No other operators are allowed.

# Input format :
# Line 1 : Integer M
# Line 2 : Integer N

# Output format : M x N

# Constraints : 0 <= M <= 1000
# 0 <= N <= 1000

# Sample Input 1 :3  5
# Sample Output 1 :15

# Sample Input 2 :4  0
# Sample Output 2 : 0


def multiplication(num1: int, num2: int) -> float:
    # Base case
    if num2 == 0:
        return 0

    # Smaller Output ( Induction Hypothesis or Assumption)
    small_output: float = multiplication(num1, num2 - 1)
    return num1 + small_output


if __name__ == "__main__":
    number1: int = int(input("Enter the number 1: "))
    number2: int = int(input("Enter the number 2: "))
    print(multiplication(number1, number2))

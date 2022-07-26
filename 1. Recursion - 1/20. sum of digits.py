# Question: sum of Digits

# Write a recursive function that returns the sum of the digits of a given integer.

# Input format : Integer N
# Output format : Sum of digits of N
# Constraints : 0 <= N <= 10^9

# Sample Input 1 : 12345
# Sample Output 1 : 15

# Sample Input 2 : 9
# Sample Output 2 : 9


def sum_digits(num1: int) -> float:
    # Base case
    if num1 // 10 == 0:
        return num1

    # Smaller Output ( Induction Hypothesis or Assumption)
    small_output: float = sum_digits(num1 // 10)
    return (num1 % 10) + small_output


if __name__ == "__main__":
    number1: int = int(input("Enter the number 1: "))
    print(sum_digits(number1, ))

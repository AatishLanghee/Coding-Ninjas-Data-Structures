# Question: Number of Digits

# Given the code to find out and return the number of digits present in a number recursively.
# But it contains few bugs, that you need to rectify such that all the test cases should pass.

# Input Format : Integer n
# Output Format : Count of digits
# Constraints : 1 <= n <= 10^6

# Sample Input 1 : 156
# Sample Output 1 : 3

# Sample Input 2 : 7
# Sample Output 2 : 1


def num_digit(num1: int) -> float:
    # Base case
    if num1 == 0:
        return 0

    # Smaller Output ( Induction Hypothesis or Assumption)
    small_output: float = num_digit(num1 // 10)
    return 1 + small_output


if __name__ == "__main__":
    number1: int = int(input("Enter the number 1: "))
    print(num_digit(number1, ))

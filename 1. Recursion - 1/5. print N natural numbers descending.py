# Question: Print N natural number in descending order.

# Given is the code to print numbers from n to 1 in decreasing order recursively.
# But it contains few bugs that you need to rectify such that all the test cases pass.

# Input Format :Integer n
# Output Format : Numbers from n to 1 (separated by space)
# Constraints : 1 <= n <= 10000

# Sample Input 1 : 6
# Sample Output 1 : 6 5 4 3 2 1

# Sample Input 2 : 4
# Sample Output 2 : 4 3 2 1


def natural_numbers(num: int,) -> None:
    # Base case
    if num == 0:
        return

    print(num, end=" ")

    # Smaller output (Induction Hypothesis or Assumption)
    natural_numbers(num - 1)

    return


if __name__ == "__main__":
    number: int = int(input("Enter the number :"))
    natural_numbers(number,)

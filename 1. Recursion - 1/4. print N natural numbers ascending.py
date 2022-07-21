# Question: Print N natural number in ascending order.

# Given is the code to print numbers from 1 to n in increasing order recursively.
# But it contains few bugs that you need to rectify such that all the test cases pass.

# Input Format :Integer n
# Output Format : Numbers from 1 to n (separated by space)
# Constraints : 1 <= n <= 10000

# Sample Input 1 : 6
# Sample Output 1 : 1 2 3 4 5 6

# Sample Input 2 : 4
# Sample Output 2 : 1 2 3 4


def natural_numbers(num: int,) -> None:
    # Base case
    if num == 0:
        return

    # Smaller output (Induction Hypothesis or Assumption)
    natural_numbers(num - 1)

    print(num, end=" ")
    return


if __name__ == "__main__":
    number: int = int(input("Enter the number :"))
    natural_numbers(number,)

# Question: Sum of N natural numbers.

# Calculate the sum of N natural numbers using recursion.


def sum_of_natural_numbers(num: int) -> int:
    # Base case
    if num == 1:
        return 1

    # Smaller output (Induction Hypothesis or Assumption)
    small_output: int = sum_of_natural_numbers(num - 1)

    return num + small_output


if __name__ == "__main__":
    number: int = int(input("Enter the number :"))
    print(sum_of_natural_numbers(number))

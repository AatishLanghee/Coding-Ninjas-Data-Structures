# Question: Factorial

# Calculate the factorial of given number using recursion.
# By default, python has 1000 maximum recursion depth.
# We can change the depth if we want to.

def factorial(num: int) -> int:
    # Base Case
    if num == 0:
        return 1

    # Smaller Output (Induction Hypothesis or Assumption)
    small_output: int = factorial(num - 1)

    return num * small_output


if __name__ == "__main__":
    number: int = int(input("Enter the number :"))
    print(factorial(number))

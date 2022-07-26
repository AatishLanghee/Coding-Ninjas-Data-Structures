# Question: Geometric sum

# Given k, find the geometric sum i.e. 1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k)  using recursion.

# Input format : Integer k
# Output format : Geometric sum (upto 5 decimal places)
# Constraints : 0 <= k <= 1000

# Sample Input 1 : 3
# Sample Output 1 : 1.87500

# Sample Input 2 : 4
# Sample Output 2 : 1.93750

def geometric_sum(index: int) -> float:
    # Base case
    if index == 0:
        return 1

    # Smaller Output ( Induction Hypothesis or Assumption)
    small_output: float = geometric_sum(index - 1)
    return 1/2**index + small_output


if __name__ == "__main__":
    number: int = int(input("Enter the number: "))
    print(geometric_sum(number,))

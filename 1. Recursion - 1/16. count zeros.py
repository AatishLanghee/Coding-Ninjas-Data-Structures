# Question: Count zeros

# Given an integer N, count and return the number of zeros that are present
# in the given integer using recursion.

# Input Format : Integer N
# Output Format : Number of zeros in N
# Constraints : 0 <= N <= 10^9

# Sample Input 1 : 0
# Sample Output 1 : 1

# Sample Input 2 : 00010204
# Sample Output 2 : 2

# Explanation for Sample Output 2 :
# Even though "00010204" has 5 zeros, the output would still be 2 because
# when you convert it to an integer, it becomes 10204.

# Sample Input 3 : 708000
# Sample Output 3 : 4

def count_zeros(num: str, index: int, count: int) -> int:
    # Base case
    if index == len(num):
        return count

    # Smaller Output ( Induction Hypothesis or Assumption)
    if int(num[index]) == 0:
        count += 1

    small_output: int = count_zeros(num, index + 1, count)

    return small_output


def second_approach(num: int) -> int:
    # Base case
    if num < 10:
        if num == 0:
            return 1
        return 0

    # Smaller Output ( Induction Hypothesis or Assumption)
    if num % 10 == 0:
        small_output: int = second_approach(num // 10) + 1
        return small_output
    else:
        small_output: int = second_approach(num // 10)
        return small_output


if __name__ == "__main__":
    number: int = int(input("Enter the number: "))
    print(count_zeros(str(number,), 0, 0))
    print(second_approach(number,))

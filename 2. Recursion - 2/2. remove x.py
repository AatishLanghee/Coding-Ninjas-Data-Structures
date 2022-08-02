# Question: Remove X

# Given a string, compute recursively a new string where all 'x' chars have been removed.

# Input format : String S
# Output format : Modified String
# Constraints : 1 <= |S| <= 10^3
# where |S| represents the length of string S.

# Sample Input 1 : xaxb
# Sample Output 1: ab

# Sample Input 2 : abc
# Sample Output 2: abc

# Sample Input 3 : xx
# Sample Output 3:

def solution(str1: str, index: int, op_str: str) -> str:
    # Base case
    if index == len(str1):
        return op_str

    # Smaller output (Induction Hypothesis or Assumption)
    if str1[index] != "x":
        op_str += str1[index]

    return solution(str1, index + 1, op_str)


def second_solution(str1: str) -> str:
    # Base case
    if len(str1) == 0:
        return str1

    # Small Output (Induction Hypothesis or Assumption)
    small_output: str = second_solution(str1[1:],)

    if str1[0] != "x":
        return str1[0] + small_output

    return small_output


if __name__ == "__main__":
    string: str = input("Enter a string :")
    print(solution(string, 0, ""))
    print(second_solution(string,))

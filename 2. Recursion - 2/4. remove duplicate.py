# Question: Remove Duplicates Recursively

# Given a string S, remove consecutive duplicates from it recursively.

# Input Format : String S
# Output Format : Output string
# Constraints : 1 <= |S| <= 10^3
#                 where |S| represents the length of string

# Sample Input 1 : aabccba
# Sample Output 1 : abcba

# Sample Input 2 : xxxyyyzwwzzz
# Sample Output 2 : xyzwz

def first_solution(str1: str, index: int) -> str:
    # Base case
    if index == len(str1) - 1:
        return str1[index]

    # Small output (Induction Hypothesis or Assumption)
    if str1[index] == str1[index+1]:
        return first_solution(str1, index+1)

    return str1[index] + first_solution(str1, index+1)


def second_approach(str1: str, index: int, op_str: str) -> str:
    # Base Case
    if index == len(str1) - 1:
        return str1[index]

    # Small output (Induction Hypothesis or Assumption)
    if str1[index] == str1[index+1]:
        return op_str + second_approach(str1, index+1, op_str)
    else:
        return op_str + str1[index] + second_approach(str1, index + 1, op_str)


if __name__ == "__main__":
    string: str = input("Enter a string :")
    print(first_solution(string, 0))
    print(second_approach(string, 0, ""))

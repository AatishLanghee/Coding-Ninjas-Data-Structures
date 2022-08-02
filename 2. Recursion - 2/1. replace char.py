# Question: Replace Character Recursively

# Given an input string S and two characters c1 and c2, you need to replace every occurrence
# of character c1 with character c2 in the given string. Do this recursively.
#
# Input Format :
# Line 1 : Input String S
# Line 2 : Character c1 and c2 (separated by space)

# Output Format : Updated string
# Constraints : 1 <= Length of String S <= 10^6
# Sample Input : abacd
#                 a x

# Sample Output : xbxcd

def solution(str1: str, chr_1: str, chr_2: str, index: int, op_str: str) -> str:
    # Base case
    if index == len(str1):
        return op_str

    # Smaller output (Induction Hypothesis or Assumption)
    if str1[index] == chr_1:
        op_str += chr_2
    else:
        op_str += str1[index]

    return solution(str1, chr_1, chr_2, index + 1, op_str)


def second_solution(str1: str, chr_1: str, chr_2: str) -> str:
    # Base case
    if len(str1) == 0:
        return str1

    # Small Output (Induction Hypothesis or Assumption)
    small_output: str = second_solution(str1[1:], chr_1, chr_2)

    if str1[0] == chr_1:
        return chr_2 + small_output

    return str1[0] + small_output


if __name__ == "__main__":
    string: str = input("Enter a string :")
    char_1: str = input("Enter first character :")
    char_2: str = input("Enter second character :")
    print(solution(string, char_1, char_2, 0, ""))
    print(second_solution(string, char_1, char_2))

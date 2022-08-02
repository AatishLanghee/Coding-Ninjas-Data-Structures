# Question: Replace pi with 3.14

# Given an input string S, you need to replace every occurrence
# of pi with 3.14 in the given string. Do this recursively.

# Input Format :
# Line 1 : Input String S

# Output Format : Updated string
# Constraints : 1 <= Length of String S <= 10^6

# Sample Input : abapicdpiacd
# Sample Output : aba3.14cd3.14acd

def solution(str1: str, index: int, op_str: str) -> str:
    # Base case
    if index == len(str1):
        return op_str

    # Smaller output (Induction Hypothesis or Assumption)
    if str1[index] == "p" and str1[index+1] == "i":
        op_str += "3.14"
        index = index + 1
    else:
        op_str += str1[index]

    return solution(str1, index + 1, op_str)


def second_solution(str1: str) -> str:
    # Base case
    if len(str1) == 0:
        return str1

    # Small Output (Induction Hypothesis or Assumption)
    small_output: str = second_solution(str1[1:],)

    if str1[0] == "p" and str1[1] == "i":
        return "3.14" + small_output[1:]

    return str1[0] + small_output


if __name__ == "__main__":
    string: str = input("Enter a string :")
    print(solution(string, 0, ""))
    print(second_solution(string,))

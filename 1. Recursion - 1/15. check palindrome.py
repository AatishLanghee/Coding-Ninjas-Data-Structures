# Question: Check Palindrome.

# Check whether a given String S is a palindrome using recursion. Return true or false.
# Input Format : String S
# Output Format : 'true' or 'false'
# Constraints : 0 <= |S| <= 1000
# where |S| represents length of string S.

# Sample Input 1 : racecar
# Sample Output 1: true

# Sample Input 2 : ninja
# Sample Output 2: false

def check_palindrome(string_: str, index: int, op_str: str) -> bool:
    # Base Case
    if index == 0:
        op_str += string_[index]
        if op_str == string_:
            return True
        return False

    # Smaller Output ( Induction Hypothesis or Assumption)
    op_str += string_[index]
    small_output: bool = check_palindrome(string_, index - 1, op_str)

    return small_output


if __name__ == "__main__":
    string: str = input("Enter the string to check if it is palindrome :")
    print(check_palindrome(string, len(string) - 1, ""))

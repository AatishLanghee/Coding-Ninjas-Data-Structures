# Question: Find power of a number

# You are given a number x and another number n. You have to print xn (x raised to the power n).
# For example, if x=3 and n=2 then, you have to print 9 ( 32 ).


def sum_of_natural_numbers(num: int, r_num: int) -> int:
    # Base case
    if r_num == 1:
        return num

    # Smaller output (Induction Hypothesis or Assumption)
    small_output: int = sum_of_natural_numbers(num, r_num - 1)

    return num * small_output


if __name__ == "__main__":
    number: int = int(input("Enter the number :"))
    raise_number: int = int(input("Enter the raise number :"))
    print(sum_of_natural_numbers(number, raise_number))

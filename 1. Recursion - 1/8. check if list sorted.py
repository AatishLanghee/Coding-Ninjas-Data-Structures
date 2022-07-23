# Question: Check if list is sorted or not.

def sorted_array(arr: list, ) -> bool:
    # Base Case
    if len(arr) == 1:
        return True

    if arr[0] < arr[1]:
        # Smaller Output ( Induction Hypothesis or Assumption)

        # Here we are creating copy of array in every call as arr[1:] which is not recommended
        small_output: bool = sorted_array(arr[1:])

        return small_output
    else:
        return False


if __name__ == "__main__":
    size: int = int(input("Enter the size of array: "))
    input_array: list = []
    for i in range(size):
        ele: int = int(input(f"Enter the {i+1} element of array: "))
        input_array.append(ele)

    print("Input array : ", input_array)
    print(sorted_array(input_array))

# Question: Check if list is sorted or not.

def sorted_array(arr: list, s_index: int) -> bool:
    # Base Case
    if s_index == len(arr) - 1:
        return True

    if arr[s_index] < arr[s_index+1]:
        # Smaller Output ( Induction Hypothesis or Assumption)
        small_output: bool = sorted_array(arr, s_index+1)
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
    print(sorted_array(input_array, 0))

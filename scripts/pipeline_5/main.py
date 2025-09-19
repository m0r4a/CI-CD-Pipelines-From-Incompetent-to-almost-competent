from platform import system, python_version

def binary_search(objective, array):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        medium_value = array[mid]

        if medium_value == objective:
            return mid
        elif medium_value < objective:
            low = mid + 1
        else:
            high = mid - 1

    return None
  
array = [1, 3, 6, 7, 17, 18, 26, 29, 33, 36, 55, 59, 81, 121, 184, 188]

value_to_find = 59

print(f"--- Code running on {system()} using the version {python_version()} of Python ---\n")

print(f"The value {value_to_find} is in the position {binary_search(value_to_find, array)}")


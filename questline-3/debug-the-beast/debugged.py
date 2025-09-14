def second_largest(arr):
    if len(arr) < 2:
        return None  # Not enough elements for a second largest

    largest = second = float('-inf')  # Safest way to initialize
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second if second != float('-inf') else None


n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter numbers: ").split()))

result = second_largest(arr)
if result is None:
    print("No second largest number found")
else:
    print("Second largest:", result)

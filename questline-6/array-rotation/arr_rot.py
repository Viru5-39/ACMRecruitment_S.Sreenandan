def rotate(arr, k):
    n=len(arr)
    k=k % n  # handle cases where k > n
    return arr[-k:]+arr[:-k]
nums=eval(input("Enter your desired list:"))
a=int(input("Enter number of steps:")) 
result=rotate(nums, a)
print("Input array:", nums)
print("Rotated by", a, "steps:", result)


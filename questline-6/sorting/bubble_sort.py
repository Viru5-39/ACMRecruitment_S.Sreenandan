def bubble_sort(arr):
    n=len(arr) # Initializes the length of the list
    for i in range(n): # Outer loop iterates through each element in the list. Largest element get bubbled up to correct position
        flag=False # Just a flag to check whether the list is already sorted
        for j in range(0, n - i - 1): # Here we use n-i-1 since the last i elements are already sorted
            if arr[j]>arr[j + 1]: #Compares an element with its neighboring one
                arr[j],arr[j + 1]=arr[j + 1],arr[j] #Swapping the elements if given condition is true
                flag=True # Setting the flag to true if since a swap occured
        if not flag: #If swap not happened, exits the outer loop
            break
array=[5, 2, 9, 1, 5, 6]
print(f"Original array: {array}") # Printing original array for reference
bubble_sort(array) #Function call
print(f"Sorted array: {array}") #Printing sorted array

#Approach:-Using slicing method

1. Take the length of array as n
2. Take k%n to handle cases where k>n
3. Split the array into two parts:
    1. The last k elements
    2. The first n-k elements
4. Concatenate them in reverse order to get final result 

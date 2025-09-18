#Iterative method

In this method, we "iterate" or "traverse" through each character in a string with a loop. It is done in the following manner:

Start with an empty string.
Loop through the original string character by character.
Instead of appending each character at the end, place it in front of the result string.
By the end of the loop, the result string contains the characters in reverse order.

#Recursive method

In this method, the function calls itself repeatedly to reach the base case. It works like:

Define a base case: if the string length is 0 or 1, just return it (already reversed).
Otherwise, reverse the substring starting from the second character, and then add the first character at the end.
This keeps reducing the problem until it reaches the base case.
The reversed substrings are then combined back together, producing the final reversed string.

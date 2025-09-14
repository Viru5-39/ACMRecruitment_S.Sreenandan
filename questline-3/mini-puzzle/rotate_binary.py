#rotate_binary.py
'''
Function name: rotate_binary
Arguments: bin_str= The binary string subject to rotation
           k= Number of times of rotation
Returns: The final rotated decimal value(integer)

'''
def rotate_binary(bin_str,k):
  n=len(bin_str)
  k%=n #Handles cases where k>n
  rotated=bin_str[-k:]+bin_str[:-k] #Rotating from right
  dec_val=int(rotated,2) #Converts to decimal
  return dec_val

print(rotate_binary("1011",1))#Rotated -> 1101  Decimal -> 13
print(rotate_binary("1011",2))#Rotated -> 1110  Decimal -> 14
print(rotate_binary("1010",3))#Rotated -> 0101  Decimal -> 5
print(rotate_binary("1010",4))#Rotated -> 1010  Decimal -> 10

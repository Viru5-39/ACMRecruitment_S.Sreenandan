#Iterative method
def rev_iter(s):
    res = ""
    for char in s:
        res=char+res # prepend each char
    return res
ch=input("Enter the string you want to reverse:")
print(rev_iter(ch))

#Recursive method
def rev_recur(s):
    if len(s) <= 1:       # base case
        return s
    else:
        return rev_recur(s[1:]) + s[0]
st=input("Enter the string to be reversed:")
print(rev_recur(st))

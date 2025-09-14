def long_pal_st(s):
    if len(s)<2:
      return s
    result=""
    s=s.lower()
    #For odd length, the center is a single character and the loop expands outward from centre
    for i in range(len(s)):
      left,right=i,i
      while left>=0 and right<len(s) and s[left]==s[right]:
        cur_len=right-left+1
        if cur_len>len(result):
          result=s[left:right+1]
        left-=1
        right+=1
    #For even length, the center is between two characters and the loop expands outward from centre
    for i in range(len(s)):
      left,right=i,i+1
      while left>=0 and right<len(s) and s[left]==s[right]:
        cur_len=right-left+1
        if cur_len>len(result):
          result=s[left:right+1]
        left-=1
        right+=1
    return result
string="I am Navan. I speak Malayalam"
print(long_pal_st(string))

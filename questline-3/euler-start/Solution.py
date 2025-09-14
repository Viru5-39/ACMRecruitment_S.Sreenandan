#Sum of multiples of 3 and 5 less than 1000
s=0
for i in range(1000):
 if i%3==0 or i%5==0:
  s+=i
print(f"Sum of multiples of 3 and 5 below 1000={s}")



#Sum of even Fibonacci numbers less than 4 million
a,b=1,2
s=0

while a<=4000000:
 if a%2==0:
  s+=a
 a,b=b,a+b

print(f"Sum of even fibonacci nbrs below 4 mill={s}")

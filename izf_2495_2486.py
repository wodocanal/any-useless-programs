
'''
  def f(x):
    N = x
    S = 1 
    while N > 0 :
        S = S * (N % 10)
        N //= 10
    return S

for i in range(1000, 10000):
    a = f(i)
    if a == 9:
        print(i)



def f(n):
    if n == 0:
        return 0
    ff = 1 + f(n/5)
    if n > 0 and n % 5 == 0:
        return ff
    fff = f(n//5)
    if n > 0 and n % 5 != 0:
        return fff
for i in range(1000):
    a = f(i)
    if a == 3:
        
        print(i, a)
'''



def f(n):
    if n == 0:
        return 0
    
    if n > 0 and n % 7 == 1:
        ff = 1 + f((n-1)/7)
        return ff
    
    if n > 0 and n % 7 != 1:
        fff = f(n//7)
        return fff
    
for i in range(1000):
    a = f(i)
    if a == 3:
        
        print(i, a)


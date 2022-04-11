def f(n):
    if n == 0:
        return 11
    if n>0 and n%7 < f(int(n /7)):
        return f(int(n /7))
    if n>0 and n%7 >= f(int(n/7)):
        return n % 7
    else:
        return False


x = [1,2,3,4,5,6,7,8,9,10]
for i in range(1, 10000):
    c = f(i)
    
    if c in x:
        x[x.index(c)]=0
print(x)
        
print(sum(x))

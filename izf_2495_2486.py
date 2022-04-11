
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




def f(n):
    if n == 0:
        return 11
    if n>0 and n%7 < f(int(n /7)):
        return f(int(n /7))
    if n>0 and n%7 >= f(int(n/7)):
        return n % 7
    else:
        return False


cache = {}


def can_win(a, b, depth):
    if (a, b) in cache.keys():
        return cache[(a, b)]

    if a + b >= 30:
        cache[(a, b)] = [False, [], 0, 0]
        return cache[(a, b)]

    wins = []

    a3b = can_win(a + 3, b, depth + 1)
    if a3b[0] == False:
        wins.append([True, [f'(+3,) = ({a + 3}, {b})'] + a3b[1], a3b[2] + 1, a3b[3] + 1])

    ab3 = can_win(a, b + 3, depth + 1)
    if ab3[0] == False:
        wins.append([True, [f'(,+3) = ({a}, {b + 3})'] + ab3[1], ab3[2] + 1, ab3[3] + 1])

    a2b = can_win(a + 2, b, depth + 1)
    if a2b[0] == False:
        wins.append([True, [f'(+2,) = ({a + 2}, {b})'] + a2b[1], a2b[2] + 1, a2b[3] + 1])

    ab2 = can_win(a, b + 2, depth + 1)
    if ab2[0] == False:
        wins.append([True, [f'(,+2) = ({a}, {b + 2})'] + ab2[1], ab2[2] + 1, ab2[3] + 1])

    abb = can_win(a + b, b, depth + 1)
    if abb[0] == False:
        wins.append([True, [f'(+b,) = ({a + b}, {b})'] + abb[1], abb[2] + 1, abb[3] + 1])

    aab = can_win(a, b + a, depth + 1)
    if aab[0] == False:
        wins.append([True, [f'(,+a) = ({a}, {b + a})'] + aab[1], aab[2] + 1, aab[3] + 1])

    if len(wins) > 0:
        minlen_i = 0
        for i in range(len(wins)):
            if wins[minlen_i][2] > wins[i][2]:
                minlen_i = i
        cache[(a, b)] = wins[minlen_i]
        return cache[(a, b)]

    cache[(a, b)] = [False, [f'и даже если (+3,) = ({a + 3},{b}), то будет ответ ', a3b[1],
                             f'и даже если (,+3) = ({a},{b + 3}), то будет ответ ', ab3[1],
                             f'и даже если (+2,) = ({a + 2},{b}), то будет ответ ', a2b[1],
                             f'и даже если (,+2) = ({a},{b + 2}), то будет ответ ', ab2[1],
                             f'и даже если (+b,) = ({a + b},{b}), то будет ответ ', abb[1],
                             f'и даже если (,+a) = ({a},{b + a}), то будет ответ ', aab[1]],
                     min(a3b[2], ab3[2], a2b[2], ab2[2], aab[2], abb[2]) + 1,
                     max(a3b[3], ab3[3], a2b[3], ab2[3], aab[3], abb[3]) + 1]
    return cache[(a, b)]


for i in range(1, 44):
    for j in range(1, 44):
        print(i, j, can_win(i, j, 0))
        print()
'''


def f(n):
    if n == 0:
        return 0
    if n%7== 1 and n>0:
        return 1 + f((n-1)/7)
    if n%7 != 1 and n>0:
        return f(n//7)
for i in range(1000):
    c = f(i)
    if c == 3:
        print(i, c)
'''
'''   
def can_win(x):
    if x>= 56:
        return [False, []]
    plus3 = can_win(x+3)
    if plus3[0] == False:
        return [True, [f'+3 = {x+3}'] + plus3[1]]
    by3 = can_win(x*3)
    if by3[0] == False:
        return [True, [f'*3 = {x*3}'] + by3[1]]
    by4 = can_win(x*4)
    if by4[0] == False:
        return [True, [f'*4 = {x*4}'] + by4[1]]
    return [False, [f'если +3 = {x+3}, то ', plus3[1], f'если *3 = {x*3}, то ', by3[1], f'если *4 = {x*4}, то ', by4[1]]]

for i in range(1, 56):
    print(i, can_win(i))
    print()'''

#f function 2495
'''
def f(n):
    if n == 0:
        return 0

    if n > 0 and n % 9 == 0:
        ff = 1+f(n / 9)
        return ff

    if n > 0 and n % 9 != 0:
        fff = f(n // 9)
        return fff

for i in range(2000):
    a = f(i)
    if a == 3:
        print(a, i)
        
  '''  


#can_win function with Two ctones heaps

cache = {}


def can_win(a, b, depth):
    if (a, b) in cache.keys():
        return cache[(a, b)]

    if a + b >= 38:
        cache[(a, b)] = [False, [], 0, 0]
        return cache[(a, b)]

    wins = []

   
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

    cache[(a, b)] = [False, [f'если (+2,) = ({a + 2},{b}), то ', a2b[1],
                             f'если (,+2) = ({a},{b + 2}), то ', ab2[1],
                             f'если (+b,) = ({a + b},{b}), то ', abb[1],
                             f'если (,+a) = ({a},{b + a}), то ', aab[1]],
                     min(a2b[2], ab2[2], aab[2], abb[2]) + 1,
                     max(a2b[3], ab2[3], aab[3], abb[3]) + 1]
    return cache[(a, b)]


for i in range(1, 31):
    print(i, can_win(i, 7, 0))
    print()


#can_win function with one ctones heap
'''
def can_win(x):
    if x>= 43:
        return [False, []]
    plus4 = can_win(x+4)
    if plus4[0] == False:
        return [True, [f'+4 = {x+4}'] + plus4[1]]
    by3 = can_win(x*3)
    if by3[0] == False:
        return [True, [f'*3 = {x*3}'] + by3[1]]
    by2 = can_win(x*2)
    if by2[0] == False:
        return [True, [f'*2 = {x*2}'] + by2[1]]
    return [False, [f'если +4 = {x+4}, то ', plus4[1], f'если *3 = {x*3}, то ', by3[1], f'если *2 = {x*2}, то ', by2[1]]]

for i in range(1, 43):
    print(i, can_win(i))
    print()
'''

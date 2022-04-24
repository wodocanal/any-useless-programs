cache = {}

def can_win(m, depth):
    if (m, depth) in cache:
        return cache[(m, depth)]
    
    if m == 1 or m == 3:
        cache[(m, depth)] = [False, ["you, last"], depth + 1]
        return cache[(m, depth)]

    if m <= 0:
        cache[(m, depth)] = [True, ["last, opponent"], depth]
        return cache[(m, depth)]

    wins = []
    fails = []
    fails_len = []

    m3 = can_win(m - 3, depth + 1)
    if m3[0] == False:      #enemy is promised to lose
        wins.append([True, [f"-3: {m-3}"] + m3[1], m3[2]])
    else:
        fails.append([f"even if -3: {m-3}, opponent will "])
        fails.append([f"-3: {m-3}"] + m3[1])
        fails_len.append(m3[2])

    m4 = can_win(m - 4, depth + 1)
    if m4[0] == False:
        wins.append([True, [f"-4: {m-4}"] + m4[1], m4[2]])
    else:
        fails.append([f"even if -4: {m-4}, opponent will "])
        fails.append([f"-4: {m-4}"] + m4[1])
        fails_len.append(m4[2])

     

    if m% 2 == 0:
        b2 = can_win(m // 2, depth + 1)
        if b2[0] == False:
            wins.append([True, [f"/2: {m//2}"] + b2[1], b2[2]])
        else:
            fails.append([f"even if /2: {m//2}, opponent will "])
            fails.append([f"/2: {m//2}"] + b2[1])
            fails_len.append(b2[2])

    if len(wins) > 0:
        minlen_i = 0
        
        for i in range(len(wins)):
            if wins[i][2] < wins[minlen_i][2]:
                minlen_i = i
        cache[(m, depth)] = wins[minlen_i]
        return cache[(m, depth)]

    cache[(m, depth)] = [False, fails, max(fails_len)]
    return cache[(m, depth)]

for m in range(33, 0, -1):

    ans = can_win(m, 0)
    print(m, ans[0], ans[2])
    print()

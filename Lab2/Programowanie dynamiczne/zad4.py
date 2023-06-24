def wsp(n,m):
    tab = [[0] * (m+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, m)+1):
            if j == 0 or i == j:
                tab[i][j] = 1
            else:
                tab[i][j] = tab[i-1][j] + tab[i-1][j-1]

    return tab[n][m]

n = 6
m = 4
result = wsp(n, m)
print(result)
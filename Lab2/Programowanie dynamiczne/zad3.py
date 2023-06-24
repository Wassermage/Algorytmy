def solve(n):
    if n == 0 or n == 1:
        return 1

    seq = [1, 1]

    for i in range(2, n + 1):
        seq.append(1)

    return seq[n]

result = solve(10)
print(result)
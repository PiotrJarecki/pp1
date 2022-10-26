def sum(N):
    if N < 1:
        return 0
    
    return N + sum(N - 1)

print(sum(10))
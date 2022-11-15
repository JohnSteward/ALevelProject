from random import randint


def PQueue(M, N):
    total = 0
    print(M, N)
    X = []
    for i in range(M):
        x = randint(1, 10)
        X.append(x)
    print(X)    
    for i in range(N):
        biggest = max(X)
        for j in range(len(X)):
            y = X[j]
            if y == biggest:
                X[j] -= 1
                break
        total += biggest
        X[j] -= 1
    return total


M = randint(1, 10)
N = randint(1, 3)
total = PQueue(M, N)
print(total)

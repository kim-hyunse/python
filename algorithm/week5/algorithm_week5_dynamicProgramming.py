import sys
read = sys.stdin.readline

N, K = map(int, read().split())
cache = [0] * (K+1)

for _ in range(N):
    x, y = map(int, read().split())
    for j in range(K, x-1, -1):
        cache[j] = max(cache[j], cache[j-x] + y)
print(cache[-1])


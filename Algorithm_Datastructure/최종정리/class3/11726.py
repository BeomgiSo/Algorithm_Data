N = int(input())9

cache = [0]
cache.append(1)

for i in range(2,N):
    cache.append(cache[i-2]+cache[i-1])

print(cache[N])

K,N = list(map(int,input().split()))

data = []
for _ in range(K):
    data.append(int(input()))

start = 1
end = max(data)

while start <= end:
    mid = (start+end) // 2
    cnt = 0
    for i in data:
        cnt += i // mid

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1


print(end)



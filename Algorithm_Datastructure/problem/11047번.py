N , target = list(map(int,input().split()))

M = []

for _ in range(N):
    x = int(input())
    M.append(x)

count = 0

for i in range(len(M)-1,-1,-1):
    print(target // M[i])
    if target // M[i] != 0:
        target = target - M[i]*(target//M[i])
        count = count + (target//M[i])
    
    if target == 0:
        break

print(count)
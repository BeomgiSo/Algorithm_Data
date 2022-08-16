import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    x = int(input())
    cache = []
    cache.append((1,0)) #0
    cache.append((0,1)) #1
    cache.append((1,1)) #2
    cache.append((1,2)) #3
    for i in range(4,x+1):
        cnt_0 = cache[i-1][0]+cache[i-2][0]
        cnt_1 = cache[i-1][1]+cache[i-2][1]
        cache.append((cnt_0,cnt_1))
    print(*cache[x])

    # 0 (1 0)
    # 1 (0 1)
    # 2 1 0 => 1 0 ( 1, 1)
    # 3 2 1 => 1 0// 1 ( 1 , 2)
    # 4 3 2 => 1 0 1 // 0 1 (2 ,3)
    # 5 4 3 => 1 0 1 0 1 // 1 0 1 (3,5)
    # 6 5 4 => 1 0 1 0 1 1 0 1 // 1 0 1 0 1 (5 8) 

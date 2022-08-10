import sys

input = sys.stdin.readline

# k n : k층에 n호에는 몇명이 살고있는지 확인
# “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 
#  단,아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
# 2 3
# 2층 3호 0 : 1 2 3 1: 1 3 6 // 2: 1 4 10

N = int(input())

for _ in range(N):
    # K층
    K = int(input())
    # N호
    N = int(input())
    # 0층 사람
    inital_floor = [ x for x in range(1,N+1)]

    for _ in range(K):
        upfloor = []
        for i in range(1,N+1):
            print(inital_floor[:i])
            upfloor.append(sum(inital_floor[:i]))
        inital_floor=upfloor
    print(inital_floor[N-1])


    

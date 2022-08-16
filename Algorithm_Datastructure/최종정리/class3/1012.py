'''
력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.

''' 
# M 가로 N 세로 K 배추 심어져있는 위치
M,N,K = list(map(int,input().split()))

graph = [[0]*M for _ in range(N)]

for _ in range(K):
    x,y = list(map(int,input().split())) 
    
    graph[x][y] = 1

for i in graph:
    print(i)

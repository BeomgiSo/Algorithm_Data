N = 4
def getPowerSet(n,k):
    # 1부터 n까지의 자연수의 원소가 있을때 k를 가장 처음 선택하는 경우
    # 3 2
    # [2],[2,3]

    if n == k:
        return [[k]]
    
    result = [[k]]
    temp = []
    for i in range(k+1,n+1):
        temp = temp + getPowerSet(n,i)

A = "mef"
B = "myself"

def IsAInB(A,B):

    if len(A) == 0:
        return True
    
    if A[0] in B: # 시작점
        # 그외 있는지 확인
        A = A[1:-1]
        return IsAInB(A, B)
    else:
        return False

    return False

print(IsAInB(A,B))
N = 3

def getPower(n,k):
    if n == k:
        return  [[k]]

    result = [[k]]
    temp = []
    for i in range(k+1,n+1):
        temp = temp + getPower(n, i)

    for i in range(len(temp)):
        temp[i] = [k]+temp[i]

    return result + temp


def powerset(n):
    result = []
    for i in range(1,n+1):
        result +=getPower(n, i)
    return result

print(powerset(3))
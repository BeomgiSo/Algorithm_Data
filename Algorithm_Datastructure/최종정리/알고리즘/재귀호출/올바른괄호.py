import sys
sys.setrecursionlimit(10**6)
data = "(())()"

def is_correct(data):
    if len(data) == 0:
        return "YES"
    elif len(data) == 1:
        return "NO"

    for i in range(len(data)-1):
        if data[i] == "(" and data[i+1] == ")":
            data = data[:i] + data[i+2:]
            
            return is_correct(data)

    # "( )"이 없을 경우 is_correct가 진행되지 않기 떄문에 이럴 경우 No를 반환해 주어야 한다.
    return 'NO'

print(is_correct(data)) 
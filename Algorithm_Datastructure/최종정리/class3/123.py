
T = int(input())
for test_case in range(1, T + 1):
    a,b = list(map(int,input().split()))
    if a>=10 or b>=10:
        result = 1
    else:
        result = a*b
    print("#%d %d"%(test_case,result))
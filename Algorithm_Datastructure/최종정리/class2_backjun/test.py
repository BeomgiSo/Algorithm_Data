N = int(input())
for _ in range(N):
    x=input().rstrip()
    stack=[]
    sum = 0
    for i in x:
        if i =="O":
            stack.append(i)
        else:
            for j in range(1,len(stack)+1):
                sum+=j
            stack = []
    if len(stack) !=0:
        for j in range(1,len(stack)+1):
            sum+=j

    print(sum)
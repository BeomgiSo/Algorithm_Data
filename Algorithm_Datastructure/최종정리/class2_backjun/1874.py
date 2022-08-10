N = int(input())
x = int(input())
stack = [x]
for i in range(1,N):
    x = int(input())
    
    if i > x:
        print("No")
        
    if x > stack[-1]:
        stack.append(x)
    elif x < stack[-1]:
        stack.pop()
N =int(input())
data = []
for _ in range(N):
    data.append(int(input()))

current = 0
stack = [1]
print("+")
for i in range(2,N+1):
    while len(stack) > 0 and stack[-1] == data[current] :
        print("-")
        stack.pop()
        current =current + 1 # 스텍의 맨 마지막 인자가 일치할경우의 로직
    # [4]    
    if len(stack) == 0 or stack[-1] < data[current] :
        print("+")
        stack.append(i)
    else :
        print(clear)
        print("NO")
        
n = int(input())

count = 1
stack = []
result = []

for _ in range(n):
    data = int(input())

    while count <= data:
        stack.append(count)
        result.append('+')
        count += 1

    if stack.pop() == data:
        result.append('-')

    else:
        print("NO")
        exit(0)

print("\n".join(result))
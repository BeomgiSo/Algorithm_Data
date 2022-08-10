import sys
def checkpara(data):
    stack = []
    for i in data:
        if i == "[" or i == "(":
            stack.append(i)
        
        if i == "]":
            if len(stack) == 0:
                return "no"
            elif stack[-1] == "[":
                stack.pop()
        
        if i == ")":
            if len(stack) == 0:
                return "no"
            elif stack[-1] == "(":
                stack.pop()

    if len(stack) == 0:
        return 'yes'
    else:
        return 'no'

input = sys.stdin.readline

while True:
    data = input().rstrip()
    if data == ".":
        break
    print(checkpara(data))



# def checkpara(data):
#     stack = []
#     for i in data:
#         if i == "[" or i == "(":
#             stack.append(i)

#         if i == "]":
#             try:
#                 stack.remove("[")
#             except:
#                 return 'no'
#                 break

#         if i == ")":
#             try:
#                 stack.remove("(")
#             except:
#                 return 'no'
#                 break
            
#     if len(stack) == 0:
#         return 'yes'
#     else:
#         return 'no'

    

# import sys
# input = sys.stdin.readline

# while True:
#     data = input()

#     if data == ".":
#         break

#     stack = []
#     for i in data:
#         if i == "[" or i == "(":
#             stack.append(i)
        
#         if i == "]":
#             if len(stack) == 0:
#                  print("no")
#                  break
#             elif stack[-1] == "[":
#                 stack.pop()
        
#         if i == ")":
#             if len(stack) == 0:
#                  print("no")
#                  break
#             elif stack[-1] == "(":
#                 stack.pop()

#     if len(stack) == 0:
#         print("yes")
#     else:
#         print("no")

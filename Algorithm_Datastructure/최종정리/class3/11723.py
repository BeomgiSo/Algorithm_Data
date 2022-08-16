import sys
input = sys.stdin.readline

N = int(input())
set_=set()
for _ in range(N):
    order = list(input().split())
    if order[0] == "add":
        set_.add(int(order[1]))
    elif order[0] == "remove":
        set_.remove(int(order[1]))
    elif order[0] == "check":
        if int(order[1]) in set_:
            print(1)
        else:
            print(0)
    elif order[0] == "toggle":
        if int(order[1]) in set_:
            set_.remove(int(order[1]))
        else:
            set_.add(int(order[1]))
    elif order[0] =="all":
        set_=set([i for i in range(1,21)])
    elif order[0] == "empty":
        set_=set()
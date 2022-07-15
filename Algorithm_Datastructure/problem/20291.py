'''
8
sbrus.txt
spc.spc
acm.icpc
korea.icpc
sample.txt
hello.world
sogang.spc
example.txt
'''
import sys
from collections import Counter
input = sys.stdin.readline
    
def solution(_str):
    cnt = Counter(_list)
    ordering = sorted(cnt, key=lambda x : x[0])
    
    for i in range(len(cnt)):
        x= ordering[i]
        print(x,cnt[x])
    
if __name__=="__main__":
    N = int(input())
    _list = []

    for _ in range(N):
        M = input().split('.')
        _list.append(M[1][:-1])
        
    solution(_list)


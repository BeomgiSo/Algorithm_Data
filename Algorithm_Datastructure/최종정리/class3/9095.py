'''
1 1   (1,0,0) 1
2 1 1 // 2 (2,1) 2
3 1 1 1 // 1 2 2 1 // 3  4
4 111 1 , 12 1 , 3 1, // 1 1 2, 2 2 // 3 1
'''
cache = [0, 1, 2, 4]
i=3
while len(cache) != 12:
    cache.append(cache[i]+cache[i-1]+cache[i-2])
    i+=1
   
N = int(input())
for _ in range(N):
    X = int(input())
    print(cache[X])
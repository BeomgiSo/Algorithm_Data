N = int(input())
if N == 1:
    print(0)
else:
    cache = [[N]]
    t=0
    while True:
        set_ = set()
        for i in cache[t]:
            #print(i)
            if i % 3 == 0: 
                set_.add(i//3)
            if i % 2 == 0 : 
                set_.add(i//2)
            set_.add(i-1)
        t +=1
        if 1 in set_:
            print(t)
            break
  
        cache.append(list(set_))
        #print(cache)





data = [1,2,-4,5,3,-2,9,-10]

def getSubsum(data):

    result = -float("inf")
    for start in range(len(data)):
        for end in range(start,len(data)):
            sum_ = 0
            for j in range(start,end):
                sum_+=data[j]

            result = max(sum_,result)
    
    return result

print(getSubsum(data))
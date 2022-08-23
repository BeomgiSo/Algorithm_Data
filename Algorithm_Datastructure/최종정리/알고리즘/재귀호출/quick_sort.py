import sys
sys.setrecursionlimit(10**6)
data = [10,2,3,4,5,6,9,7,8,1]

def quickSort(data):

    if len(data) <= 1:
        return data

    pivot = data[0]

    # if data < pivot
    left_side = []
    right_side = []
    for i in data[1:]:
        if pivot > i:
            left_side.append(i)
        else:
            right_side.append(i)
    #print(pivot,left_side)
    return quickSort(left_side)+[pivot]+quickSort(right_side)

print(quickSort(data))
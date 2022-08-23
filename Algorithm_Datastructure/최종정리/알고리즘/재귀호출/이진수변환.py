n =  19
def convertToBinary(n):
    if n < 2:
        return str(n)
    a = n // 2
    b = n % 2
    
    return convertToBinary(a) + str(b)

print(convertToBinary(19))


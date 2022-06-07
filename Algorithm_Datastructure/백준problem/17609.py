'''
회문(回文) 또는 팰린드롬(palindrome)은 앞 뒤 방향으로 볼 때 같은 순서의 문자로 구성된 문자열을 말한다. 예를 들어 ‘abba’ ‘kayak’, ‘reviver’, ‘madam’은 모두 회문이다. 만일 그 자체는 회문이 아니지만 한 문자를 삭제하여 회문으로 만들 수 있는 문자열이라면 우리는 이런 문자열을 “유사회문”(pseudo palindrome)이라고 부른다. 예를 들어 ‘summuus’는 5번째나 혹은 6번째 문자 ‘u’를 제거하여 ‘summus’인 회문이 되므로 유사회문이다.

여러분은 제시된 문자열을 분석하여 그것이 그 자체로 회문인지, 또는 한 문자를 삭제하면 회문이 되는 “유사회문”인지, 아니면 회문이나 유사회문도 아닌 일반 문자열인지를 판단해야 한다. 만일 문자열 그 자체로 회문이면 0, 유사회문이면 1, 그 외는 2를 출력해야 한다. 


7
abba
summuus
xabba
xabbay
comcom
comwwmoc
comwwtmoc


0
1
1
2
2
0
1
'''
# import sys
# input = sys.stdin.readline
# N = int(input())
# for _ in range(N):
#     a = list(input().rstrip())

#     mid = len(a)//2
#     n = 0
#     m = 0

#     count = 0

#     for _ in range(mid):
#         if a[n] == a[-(m+1)]:
#             n = n+1
#             m = m+1
#         elif a[n+1] == a[-(m+1)]:
#             count+=1
#             n = n+2
#             m = m+1
#         elif a[n+1] == a[-(m+2)]:
#             count+=1
#             n = n+1
#             m = m+2
        
#         if count == 2:
#             print(2)
#             break
            
#     if count == 1:
#         print(1)
#     elif count == 0:
#         print(0)
    

import sys
input = sys.stdin.readline
N = int(input().rstrip())
for _ in range(N):
    checkString = list(input().rstrip())

    right = 0
    left = len(checkString)-1

    count = 0
    while right<left:
        if checkString[right] == checkString[left]:
            right+=1
            left-=1
        else:
            if checkString[right+1] == checkString[left]:
                right+=2
                left-=1
                count+=1
            elif checkString[right] == checkString[left-1]:
                right+=1
                left-=2
                count+=1
            else:
                count = 2
        if count == 2:
            break

    print(count)


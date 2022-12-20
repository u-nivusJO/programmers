# def solution(n):
#     answer = 0
#     arr=[]
#     for i in str(n):
#         arr.append(i)
#     arr.sort()
#     cnt=0
#     for a in arr:
#         answer+=int(a)*(10**cnt)
#         cnt+=1
#     return answer


def solution(n):
    answer=0
    arr=list(str(n))
    arr.sort(reverse=True)
    answer=int(''.join(arr))    
# def solution(x, n):
#     answer = []
#     if x==0:
#         answer=[0]*n
#         return answer
#     elif x>0:
#         y=(x*n)+1
#     else:
#         y=(x*n)-1    
#     for i in range(x,y,x):
#         answer.append(i)
#     return answer

def solution(x, n):
    answer = []
    for i in range(1,n+1):
        answer.append(x*i)
    return answer
# def solution(n):
#     answer=0
#     n3=''
#     while True:
#         n3+=str(n%3)
#         n=n//3
#         if n==0:
#             break
#     n3=''.join(reversed(n3))    
#     for i in range(len(n3)):
#         answer+=int(n3[i])*(3**i)  
#     return answer

def solution(n):
    n3=''
    while True:
        n3+=str(n%3)
        n=n//3
        if n==0:
            break
    answer=int(n3, 3)    
    return answer
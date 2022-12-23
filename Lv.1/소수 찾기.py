# def solution(n):
#     answer = 1
#     if n==2:
#         return 1

#     def prime(num):
#         for i in range(2, int(num**(1/2))+1):
#             if num%i==0:
#                 return False
#         return True

#     for j in range(3,n+1):
#         if prime(j):
#             answer+=1            
#     return answer

def solution(n):
    num=[False, False]+[True]*(n-1)

    for i in range(2,(n//2)+1):
        if num[i]==True:
            for j in range(i*2,n+1,i):
                num[j]=False
    return num.count(True)    
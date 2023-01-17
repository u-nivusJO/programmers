# def solution(s):
#     cnt=0
#     zero=0
#     while s!='1':
#         cnt+=1
#         num=0
#         for i in range(len(s)):
#             if s[i]=='1':
#                 num+=1
#         zero+=len(s)-num        
#         s=str(bin(num))[2:]        
#     return [cnt, zero]

def solution(s):
    cnt=0
    zero=0
    while s!='1':
        cnt+=1
        num=s.count('1')
        zero+=len(s)-num        
        s=str(bin(num))[2:]        
    return [cnt, zero]
# def solution(s):
#     s=s.lower()
#     p_cnt=0
#     y_cnt=0
#     print(s)
#     for i in s:
#         if i=='p':
#             p_cnt+=1
#         elif i=='y':
#             y_cnt+=1
#     if p_cnt == y_cnt:
#         return True
#     else:
#         return False                

def solution(s):
    if s.lower().count('p')==s.lower().count('y'):
        return True
    else:
        return False
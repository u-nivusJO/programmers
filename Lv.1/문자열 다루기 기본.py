# import string

# def solution(s):
#     answer = True
#     alpha=[i for i in string.ascii_lowercase]
#     s=s.lower()
#     if len(s)==4 or len(s)==6:    
#         for i in s:
#             if i in alpha:
#                 return False
#         return answer
#     return False

def solution(s):
    if len(s) in (4,6) and s.isdigit():
        return True 
    return False        
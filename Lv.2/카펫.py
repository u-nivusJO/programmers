# def solution(brown, yellow):
#     def check_mid(w,h):
#         if (w-2)*(h-2)==yellow:
#             return True
#         return False    

#     total=brown+yellow
#     w=1
#     h=total
#     while True:
#         w+=1
#         if total%w==0:
#             h=total//w
#             if check_mid(w, h):
#                 break  
    
#     return [max(w, h), min(w, h)]

def solution(brown, yellow):
    total=brown+yellow
    for w in range(2, total):
        if total%w==0 and (w-2)*(total//w-2)==yellow :
            return [total//w, w]

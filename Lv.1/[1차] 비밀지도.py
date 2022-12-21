# def solution(n, arr1, arr2):
#     answer = []
#     for i in range(n):
#         arr1[i]=list((format(arr1[i], 'b')).zfill(n))
#         arr2[i]=list((format(arr2[i], 'b')).zfill(n))
#         password=''
#         for j in range(n):
#             if arr2[i][j]=='1':
#                 arr1[i][j]='1'
#             if arr1[i][j]=='0':
#                 password+=' '
#             else:
#                 password+='#'    
#         answer.append(password)    
#     return answer   

def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        password=str(bin(i|j)[2:])
        password=password.zfill(n)
        password=password.replace('1','#')
        password=password.replace('0',' ')
        answer.append(password)
    return answer 

# def solution(numbers):
#     answer = ''
#     numbers_str=[]
#     for number in numbers:
#         numbers_str.append(str(number))
#     numbers_str.sort(reverse=True, key=lambda x:x*3)
    
#     for num in numbers_str:
#         answer+=num    
#     return str(int(answer))   # 예외 [0,0,0]

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True ,key=lambda x:x*3)
    return str(int(''.join(numbers)))
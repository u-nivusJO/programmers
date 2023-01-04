# 1
# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     for i,j in zip(phone_book, phone_book[1:]):
#         if j.startswith(i):
#             return False
#     return answer

# 2 해시
def solution(phone_book):
    hashdict={}
    for number in phone_book:
        hashdict[number]=1
    for number in phone_book:
        check=''
        for n in number:
            check+=n
            if check in hashdict and check != number:
                return False   
    return True




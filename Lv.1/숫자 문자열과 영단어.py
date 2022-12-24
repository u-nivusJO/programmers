# def solution(s):
#     answer = ''
#     word=['zero', 'one' ,'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     def num(n):
#         if n.isdigit():
#             return True
#         return False    

#     for _ in range(len(s)):
#         if num(s[0]):
#             answer+=s[0]
#             s=s[1:]
#         else:
#             for w in range(len(word)):
#                 if s[0:2]==word[w][0:2]:
#                     answer+= str(w)
#                     s=s[len(word[w]):]
#         if len(s)==0:
#             break                         
#     return int(answer)

def solution(s):
    word=['zero', 'one' ,'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for w in range(len(word)):
        s=s.replace(word[w], str(w))
    return int(s) 

print(solution("one4seveneight"))    
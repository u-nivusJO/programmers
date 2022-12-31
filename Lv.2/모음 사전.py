# def solution(word):
#     all=[]
#     words=['A', 'E', 'I', 'O', 'U']
#     from itertools import product
#     for i in range(1,6):
#         for p in product(words, repeat=i):
#             all.append(''.join(list(p)))
#     all.sort()        
#     return all.index(word)+1

def solution(word):
    answer = len(word)
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n)
        print((5 ** (5 - i) - 1) / (5 - 1), "AEIOU".index(n))
    return int(answer)

# 1. sort 후 loop
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     completion.append(' ')
#     for p, c in zip(participant, completion):
#         if p!=c:
#             return p

# 2. hash
def solution(participant, completion):
    hashdict={}
    hashcnt=0
    for p in participant:
        hashdict[hash(p)]=p
        hashcnt+=hash(p)
    for c in completion:
        hashcnt-=hash(c)    
    return hashdict[hashcnt]

# 3. counter
# from collections import Counter
# def solution(participant, completion):
#     answer = Counter(participant) - Counter(completion)
#     return list(answer)[0]

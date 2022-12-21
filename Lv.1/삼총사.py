from itertools import combinations

def solution(number):
    answer = 0
    candidate= list(combinations(number, 3))
    for c in candidate:
        if sum(c)==0:
            answer+=1
    return answer

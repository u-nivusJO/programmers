from itertools import combinations
def solution(numbers):
    answer = []
    twonum=list(combinations(numbers, 2))
    for t in twonum:
        if sum(t) not in answer:
            answer.append(sum(t))
    answer.sort()        
    return answer
 
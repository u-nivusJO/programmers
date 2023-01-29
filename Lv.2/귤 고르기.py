from collections import Counter
def solution(k, tangerine):
    answer = 0
    c_tangerine=Counter(tangerine).most_common()
    for t, v in c_tangerine:
        k-=v
        answer+=1
        if k<=0:
            break
    return answer
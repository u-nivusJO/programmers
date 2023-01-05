def solution(clothes):
    answer = 1
    hashdict={}
    # for c in clothes:
    #     if hash(c[1]) in hashdict:
    #         hashdict[hash(c[1])]+=1
    #     else:
    #         hashdict[hash(c[1])]=1
    for c in clothes:
        hashdict[c[1]]=hashdict.get(c[1],0) +1    
    for v in hashdict.values():
        answer*=(v+1)
    return answer-1
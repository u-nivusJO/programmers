def solution(k, dungeons):
    answer = -1

    def dungeon(d, k):
        cnt=0
        for dd in d:
            if dd[0]<=k:
                k-=dd[1]
                cnt+=1
        return cnt             

    from itertools import permutations
    for p in permutations(dungeons):
        if dungeon(p, k)>=answer:
            answer=dungeon(p, k)
    return answer
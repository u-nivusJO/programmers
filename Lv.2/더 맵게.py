import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville)>=2:
        a=heapq.heappop(scoville)
        if a>=K:
            return answer
        b=heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)
        answer+=1
    if scoville[0]>=K:
        return answer
    else:
        return -1
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  
    while len(scoville)>=2:
        a=heapq.heappop(scoville) # 가장 작은 값
        if a>=K:
            return answer
        b=heapq.heappop(scoville) # 두 번째로 작은 값   
        heapq.heappush(scoville,a+b*2)
        answer+=1
    if scoville[0]>=K:
        return answer
    else:
        return -1 
# 1. 이분탐색
# def solution(citations):
#     answer = 0
#     citations=sorted(citations)
#     start, end=0, citations[-1] # start=citations[0]의 반례 [4,4,4]
#     while start<=end:
#         mid=(start+end)//2
#         h_down=0 # h번 이하 인용된 논문 수=len(citations)-h_up
#         h_up=0 # h번 이상 인용된 논문 수=h 이상
#         for c in citations:
#             if c>mid:
#                 h_up+=1
#             elif c<mid:
#                 h_down+=1
#             else:
#                 h_up+=1
#                 h_down+=1 
#         if mid<=h_up:
#             answer=mid
#             start=mid+1
#         else:            
#             end=mid-1

#     return answer

# 2. 정렬
def solution(citations):
    citations.sort()
    for num, citation in enumerate(citations):
        if citation>=(len(citations)-num):
            return len(citations)-num
# 1
# def solution(nums):
#     answer = 0
#     if len(set(nums)) < (len(nums)//2) :
#         answer=len(set(nums))
#     else:
#         answer=len(nums)//2    
#     return answer

# 2
# def solution(nums):
#     answer=min(len(nums)/2, len(set(nums)))
#     return answer

# 3 해시
def solution(nums):
    answer = 0
    hashdict={}
    for n in nums:
        hashdict[hash(n)]=n   
    return min(len(nums)//2, len(hashdict))
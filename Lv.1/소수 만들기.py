from itertools import combinations
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True    

def solution(nums):
    answer = 0
    three=list(combinations(nums,3))
    for t in three:
        if isprime(sum(t)):
            answer+=1
    return answer
import math
def solution(n, k):
    answer=[]
    people=[i for i in range(1,n+1)]
    k-=1
    for _ in range(n,0,-1):
        cnt=math.factorial(n)
        section=cnt//n
        answer.append(people[k//section])
        people.pop(k//section)
        k=k%section
        n-=1  
    return answer
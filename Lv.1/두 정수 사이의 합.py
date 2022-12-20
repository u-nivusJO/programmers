def solution(a, b):
    answer = 0
    c=min(a,b)
    d=max(a,b)
    answer=(c+d)*(d-c+1)*(1/2)
    return answer
def solution(price, money, count):
    answer = -1
    for c in range(1, count+1):
        money-=c*price
    if money<0:
        answer=-money
    else:
        answer=0        
    return answer
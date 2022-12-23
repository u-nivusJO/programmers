def solution(a, b, n):
    answer = 0
    cola=0
    while n>=a:
        answer+=(n//a)*b
        cola=(n//a)*b
        n=(n%a)+cola
    return answer   
def solution(a, b):
    answer = ''
    day=['THU','FRI','SAT','SUN','MON','TUE','WED']
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(a-1):
        b+=month[i]
    answer=day[b%7]        
    return answer   
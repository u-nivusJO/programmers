def solution(n):
    answer = 1
    for i in range(1,n):
        for j in range(i+1,n):
            i+=j
            if i == n:
                answer+=1
                break
            elif i>n:
                break    
    return answer

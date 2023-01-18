def solution(people, limit):
    answer = 0
    people=sorted(people) # 몸무게 가벼운 순
    left, right=0, len(people)-1
    while left<=right:
        if people[left]+people[right]<=limit:
            answer+=1
            left+=1
            right-=1
        else:
            answer+=1
            right-=1
    return answer
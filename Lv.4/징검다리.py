def solution(distance, rocks, n):
    answer = 0
    left, right = 0, distance
    rocks.sort()
    while left<=right:
        mid=(left+right)//2
        del_rock=0
        now_rock=0
        for rock in rocks:
            if rock-now_rock<mid:
                del_rock+=1
            else:
                now_rock=rock
            if del_rock>n:
                break
        if del_rock<=n:
            answer=mid
            left=mid+1
        else:
            right= mid-1
    return answer
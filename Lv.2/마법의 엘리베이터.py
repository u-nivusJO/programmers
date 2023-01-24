def solution(storey):
    answer=0
    while storey>0:
        temp=storey%10
        if temp>5 or (temp==5 and (storey%100)-temp>=50):
            answer+=10-temp
            storey=(storey+10-temp)//10
        else:
            answer+=temp
            storey=(storey-temp)//10    
    return answer
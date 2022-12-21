def solution(s):
    answer=''
    cnt=0
    for i in range(len(s)):
        if s[i]==' ':
            cnt=0
        else:    
            if cnt%2==0:
                s=s.upper()
            else:
                s=s.lower()
            cnt+=1    
        answer+=s[i]
    return answer
 
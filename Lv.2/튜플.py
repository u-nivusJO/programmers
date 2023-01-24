from collections import Counter
def solution(s):
    answer=[]
    s=list(map(str, s.split('},{')))
    s[0]=s[0][2:]
    s[-1]=s[-1][:-2]
    s=sorted(s, key=lambda x:len(x))
    for i in s:
        i=list(map(str, i.split(',')))
        temp=list(Counter(i)-Counter(answer))
        if temp[0]==',':
            answer.append(temp[-1])
        else:
            answer.append(temp[0])   
    return tuple(int(a) for a in answer)
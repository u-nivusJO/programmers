def solution(input_string):
    answer = ''
    check=set(input_string)
    check=sorted(check)
    for c in check:
        temp=[]
        for i in range(len(input_string)):
            if c==input_string[i]:
                temp.append(i)
        for j in range(1,len(temp)):
            if temp[j]-1!=temp[j-1]:
                answer+=c
                
                break
    if answer=='':
        answer='N'
    return answer
def solution(answers):
    answer = []
    stu1=[1, 2, 3, 4, 5]
    stu2=[2, 1, 2, 3, 2, 4, 2, 5]
    stu3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt=[0,0,0]
    for a in range(len(answers)):
        if answers[a]==stu1[a%5]:
            cnt[0]+=1
        if answers[a]==stu2[a%8]:
            cnt[1]+=1
        if answers[a]==stu3[a%10]:
            cnt[2]+=1
    for c in range(len(cnt)):
        if max(cnt)==cnt[c]:        
            answer.append(c+1)
    return answer 
def solution(arr1, arr2):
    answer=[]
    for i in range(len(arr1)):
        answer.append([])
        for a2 in range(len(arr2[0])):
            ans=0
            for a1 in range(len(arr1[0])):
                ans+=arr1[i][a1]*arr2[a1][a2]
            answer[i].append(ans)
    return answer
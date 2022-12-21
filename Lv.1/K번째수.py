def solution(array, commands):
    answer = []
    for i, j, k in commands:
        array_m=array[i-1:j]
        array_m.sort()
        answer.append(array_m[k-1])
    return answer
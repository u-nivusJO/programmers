def solution(elements):
    answer = set()
    n=len(elements)
    elements+=elements
    for i in range(n):
        temp_elements=elements[i:i+n]
        for j in range(n):
            answer.add(sum(temp_elements[:j+1]))
    return len(answer)
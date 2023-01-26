def solution(tickets):
    answer = []
    flight={}
    for d,a in tickets:
        flight[d]=flight.get(d,[])+[a]
    stack=['ICN']
    for f in flight.keys():
        flight[f]=sorted(flight[f])
    while stack:
        temp=stack[-1]
        if temp not in flight or  flight[temp]==[] :
            answer.append(temp)
            stack.pop()
        else:
            stack.append(flight[temp][0])
            del flight[temp][0]              
    return answer[::-1]

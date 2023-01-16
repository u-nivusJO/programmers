from itertools import accumulate
def solution(bell):
    answer=0
    bell_dict={0:[0]}
    for i in range(len(bell)):
        if bell[i]==2:
            bell[i]=-1
    bell=list(accumulate(bell))
    for i, b in enumerate(bell):
        if b in bell_dict:
            bell_dict[b].append(i+1)
        else:
            bell_dict[b]=[i+1]       
    for v in bell_dict.values():
        if len(v)>1:
            answer=max(v[-1]-v[0],answer)
    return answer
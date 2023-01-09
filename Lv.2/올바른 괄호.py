def solution(s):
    answer = True
    stack=[]
    for ss in s:
        if ss=='(':
            stack.append(ss)
        else:
            if stack==[]:
                return False
            else:
                stack.pop()
    if stack!=[]:
        return False                    
    return True
def solution(s):
    if len(s)%2!=0:
        return 0 
    else:
        stack=[]
        for ss in s:
            if not stack:
                stack.append(ss)
            else:
                if stack[-1]==ss:
                    stack.pop()
                else:
                    stack.append(ss)
        if stack:
            return 0
        else:
            return 1    
def check(ss):
    stack=[]
    for k in ss:
        if len(stack)!=0:
            if k==')' and stack[-1]=='(':
                stack.pop()
            elif k==']' and stack[-1]=='[':
                stack.pop()
            elif k=='}' and stack[-1]=='{':
                stack.pop()  
            else:
                stack.append(k)   
        else:
            stack.append(k)        
    if len(stack)!=0:                  
        return 0
    else:
        return 1 

def solution(s):
    answer = 0
    for i in range(len(s)):
        if s[i]!=')' and s[i]!=']' and s[i]!='}':
            ss=s[i:]+s[:i]
            answer+=check(ss)
    return answer 
def solution(s):
    s=s.lower()
    for i in range(len(s)):
        if i==0 and s[i] not in ['0','1','2','3','4','5','6','7','8','9']:
            s_=s[i].upper()
            s=s_+s[1:]
        if s[i]!=' ' and s[i] not in ['0','1','2','3','4','5','6','7','8','9'] and s[i-1]==' ':
            s_=s[i].upper()
            s=s[:i]+s_+s[i+1:]
    return s
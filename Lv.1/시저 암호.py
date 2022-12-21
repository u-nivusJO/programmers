def solution(s, n):
    answer = ''
    for i in s:
        if i==' ':
            answer+=' '
        else:
            if ord(i)<=90 and 90<(ord(i)+n):
                answer+=chr(ord(i)+(n-1)-25)
            elif 122<(ord(i)+n):
                answer+=chr(ord(i)+(n-1)-25)
            else:
                answer+=chr(ord(i)+n)
    return answer 
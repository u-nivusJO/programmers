def solution(n):
    cnt=str(bin(n)[2:]).count('1') # bin(n).count('1') 도 가능
    while True:
        n+=1
        if str(bin(n)[2:]).count('1')==cnt:
            return n
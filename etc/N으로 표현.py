def solution(N, number):
    answer = 0
    dp=[set() for i in range(9)]
    for i in range(1,9):
        dp[i].add(int(str(N)*i))
        for j in range(i//2+1):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a+b)
                    dp[i].add(a-b)
                    dp[i].add(b-a)
                    dp[i].add(a*b)
                    if b!=0:
                        dp[i].add(a//b)
                    if a!=0:
                        dp[i].add(b//a)
        if number in dp[i]:
            return i                    
    return -1
def solution(numbers):
    answer = 0
    check=set()
    from itertools import permutations

    def prime(num):
        if num<=1:
            return False
        for n in range(2, int(num**(1/2))+1):
            if num%n==0:
                return False
        return True

    for i in range(len(numbers)):
        for p in permutations(list(numbers), i+1):
            add=''
            for pp in p:
                if pp=='0' and add=='':
                    pass
                else:
                    add=add+pp
            check.add(add)
    if ''in check:
        check.remove('')
    for c in list(check):
        if prime(int(c)):
            answer+=1
    return answer  
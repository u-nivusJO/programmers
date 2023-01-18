import math
def lcm(a,b):
    return a*b//math.gcd(a,b)
def solution(arr):
    last=arr[0]
    for i in range(1,len(arr)):
        last=lcm(arr[i],last)
    return last
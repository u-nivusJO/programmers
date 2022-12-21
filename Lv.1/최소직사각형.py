# def solution(sizes):
#     max1=0
#     max2=0
#     for a in sizes:
#         a.sort()
#         if max1<a[0]:
#             max1=a[0]
#         if max2<a[1]:
#             max2=a[1]       
#     return max1*max2   

def solution(sizes):
    return max(max(x) for x in sizes)*max(min(x) for x in sizes)

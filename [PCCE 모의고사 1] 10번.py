def solution(text, anagram, sw):
    answer = ''
    dict={}
    if sw==True:
        for i in range(len(text)):
            dict[anagram[i]]=text[i]
        dict=sorted(dict.items())
        for d in dict:    
            answer+=''.join(d[1]) 
    else:
        for a in range(len(anagram)):
            dict[a]=text[anagram[a]]
        for d in dict.items():
            answer+=''.join(d[1])
            
    return answer
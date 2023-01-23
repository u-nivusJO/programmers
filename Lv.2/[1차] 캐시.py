def solution(cacheSize, cities):
    answer = 0
    cities=[c.lower() for c in cities]
    city_cache=[]
    if cacheSize==0:
        return len(cities)*5  
    for c in cities:
        if c in city_cache:
            city_cache.remove(c)
            answer-=4
        elif len(city_cache)==cacheSize:
            city_cache.pop(0) 
        city_cache.append(c)
        answer+=5    
    return answer
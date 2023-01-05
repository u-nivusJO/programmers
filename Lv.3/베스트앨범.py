def solution(genres, plays):
    answer = []
    genre_dict={} # {장르:{고유번호:재생횟수}}
    playcnt_dict={} # 장르별 총 재생횟수
    for i in range(len(genres)):
        if genres[i] in genre_dict:
            genre_dict[genres[i]][i]=plays[i]
        else:
            genre_dict[genres[i]]={i:plays[i]} 
        playcnt_dict[genres[i]]=playcnt_dict.get(genres[i], 0) +plays[i]
    playcnt_dict=dict(sorted(playcnt_dict.items(), key=lambda x:x[1], reverse=True))
    for g in playcnt_dict:
        genre2= genre_dict[g]
        genre2=sorted(genre2.items(), key=lambda x:x[1], reverse=True)
        answer.append(genre2[0][0])
        if len(genre2)!=1:
            answer.append(genre2[1][0])  
    return answer

# 장르별로 재생횟수의 합 구하기
# 재생횟수가 많은 장르에서 많이 재생된 노래의 고유 번호 출력(같은 경우 고유번호가 낮은 곡)
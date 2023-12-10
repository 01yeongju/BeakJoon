# 1417. 국회의원 선거

N = int(input())    # 후보 수
me = int(input())   # 다솜의 득표 수
rank = [int(input()) for _ in range(N-1)]   # 다른 후보들의 득표 수
cnt = 0     # 다솜의 매수인원

rank.sort(reverse=True)     # 득표 순대로 정렬

if N == 1:
    print(0)    # 후보가 1명이면 매수 필요x
else:
    while rank[0] >= me:    # 후보가 여러명이면 최다 득표 수를 가진 후보의 표를 매수
        me += 1
        cnt += 1
        rank[0] -= 1
        rank.sort(reverse=True)     # 정렬을 통해 최다 특표 후보와 다솜의 득표 수를 비교
    print(cnt)

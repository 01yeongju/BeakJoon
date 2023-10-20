# 11650. 좌표 정렬하기

N = int(input())
spot = [list(map(int, input().split())) for _ in range(N)]

spot.sort()

for i in spot:
    print(*i)

'''
입력:
5
3 4
1 1
1 -1
2 2
3 3

출력:
1 -1
1 1
2 2
3 3
3 4
'''
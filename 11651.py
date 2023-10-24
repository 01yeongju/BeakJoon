# 11651. 좌표 정렬하기 2

N = int(input())
spot = [list(map(int, input().split())) for _ in range(N)]

spot.sort(key=lambda x: (x[1], x[0]))

for i in spot:
    print(*i)

'''
5
0 4
1 2
1 -1
2 2
3 3

1 -1
1 2
2 2
3 3
0 4
'''
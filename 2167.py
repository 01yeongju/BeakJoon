# 2167. 2차원 배열의 합
# 누적합

n, m = map(int, input().split())
num_list = [list(map(int, input().split())) for _ in range(n)]

# 누적합 배열 생성
dp = [[0] * (m + 1) for _ in range(n + 1)] 
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = num_list[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
# print(dp)

# (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합 구하기        
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    result = dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1]
    print(result)


''' 시간초과
n, m = map(int, input().split())
num_list = [list(map(int, input().split())) for _ in range(n)]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    result = 0 
    
    for row in range(i-1, x):
        for col in range(j-1, y):
            result += num_list[row][col]
        
    print(result)
    
'''
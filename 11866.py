# 11688. 요세푸스 문제 0

from collections import deque

N, K = map(int, input().split())
queue = deque()
for i in range(1, N+1):
    queue.append(i)

result = []
while queue:
    for i in range(K-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())
    
# 출력
print("<",end="")
for i in range(N-1):
    print(result[i],end=", ")
print(result[N-1], end = "")
print(">")

'''
7 3

<3, 6, 2, 7, 5, 1, 4>
'''
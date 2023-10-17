# 16435. 스네이크버드

N, L = map(int, input().split())        # N:과일의 개수, L:스네이크버드 초기길이
num_list = list(map(int, input().split()))      # 과일 높이 리스트

num_list.sort()     # 과일 높이 낮으순으로 정렬

# 먹을 수 있으면 L +1, 먹을 수 없으면 반복문 종료
for i in num_list:
    if i <= L:
        L+=1
    else:
        break
        
print(L)
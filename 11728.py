# 11728. 배열 합치기

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list += list(map(int, input().split()))
num_list.sort()

print(*num_list)
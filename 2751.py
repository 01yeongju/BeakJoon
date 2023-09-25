# 2751.py
import sys

N = int(input())
num_list = [int(sys.stdin.readline()) for _ in range(N)]     # int(input()) : input은 \n을 제거하므로 시간 ↑

for i in sorted(num_list):  # print(*sorted(num_list), sep='\n')
    print(i)

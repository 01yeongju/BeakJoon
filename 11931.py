# 11931. 수 정렬하기4
import sys

N = int(input())
num_list = [int(sys.stdin.readline()) for _ in range(N)]

num_list.sort(reverse=True)
print(*num_list, sep='\n')

'''
5
1
2
3
4
5


5
4
3
2
1
'''
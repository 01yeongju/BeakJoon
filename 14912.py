# 14912. 숫자 빈도수

n, find_num = input().split()       # n: n까지의 자연수, find_num: 빈도수를 확인할 숫자
cnt = 0     # 총 빈도수

for i in range(1, int(n)+1):    # 1~n까지 반복
    cnt += str(i).count(find_num)       # 각 자연수마다 찾는 수의 개수 확인 후 cnt에 합
print(cnt)
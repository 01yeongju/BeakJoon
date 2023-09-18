# 1094. 막대기

N = int(input())    # 만들고 싶은 막대의 길이

stick_len = 64      # 처음 막대의 길이
cnt = 0             # 필요한 막대의 개수

while N > 0:
    if stick_len > N:       # 가진 막대의 길이가 길면 절반으로 자르기
        stick_len //= 2
    else:                   # 가진 막대의 길이가 짧으면 cnt 1증가, 만들고싶은 막대길이 감소
        cnt += 1
        N -= stick_len
        
print(cnt)

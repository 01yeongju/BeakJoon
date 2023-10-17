# 1789. 수들의 합

S = int(input())    # 서로 다른 N개의 자연수의 합
cnt = 1

while cnt*(cnt+1)/2<=S:     # 합의 공식
    cnt += 1
    
print(cnt-1)
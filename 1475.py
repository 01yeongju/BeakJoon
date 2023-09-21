# 1475. 방 번호
N = input()
num_cnt = [0] * 10      # 0~9 각각의 개수 카운트

for i in N:     # 입력된 방번호의 각 자리에 대해 반복

    if i == '6' or i == '9':            # 6, 9인 경우
        if num_cnt[6] <= num_cnt[9]:    # 6과 9중 사용횟수가 적은 수의 사용횟수를 증가
            num_cnt[6] +=1
        else:
            num_cnt[9] += 1
    else:                               # 6, 9가 아닌 경우
        num_cnt[int(i)] += 1            # 사용횟수 증가
        
print(max(num_cnt))
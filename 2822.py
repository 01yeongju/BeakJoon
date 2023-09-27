# 2822. 점수 계산

score = [int(input()) for _ in range(8)]    # 8개의 정수 저장
temp = []   # 위치정보 저장
answer = 0  # 참가자의 총점 저장

for i in range(5):
    answer += max(score)        # 최대값을 찾아 누적합
    temp.append(score.index(max(score)) + 1)        # 최대값의 인덱스값 저장
    score[score.index(max(score))] = -1      # 최대값을 최소값으로 변경
temp.sort()     # 문제 번호가 증가하는 순으로 정렬

print(answer)
print(*temp)
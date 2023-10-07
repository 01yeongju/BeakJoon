# 5800. 성적 통계

K = int(input())        # 반의 수

score_list = [list(map(int, input().split())) for _ in range(K)]
cnt = 1

for score in score_list:
    score = sorted(score[1:])       # 학생수를 제외한 후 점수 정렬

    max_score,  min_score = score[-1], score[0]     # 최고, 최저 점수
    
    largest_gap = score[1] - score[0]       # 점수차이 초기화
    
    for i in range(2, len(score)):          # 가장 큰 입접한 점수차이 구하기
        if score[i] - score[i-1] > largest_gap:
            largest_gap = score[i] - score[i-1]
            
    print(f"Class {cnt}")
    print(f"Max {max_score}, Min {min_score}, Largest gap {largest_gap}")
    
    cnt += 1
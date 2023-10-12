# 10815. 숫자 카드
N = int(input())    # 상근이가 가지고 있는 숫자 카드의 개수
have_card = set(map(int, input().split()))   # 상근이가 가지고 있는 카드의 정수
M = int(input())    # 구별해야 할 숫자 카드의 개수
diff_card = list(map(int, input().split()))   # 비교해야 할 카드의 정수

for i in diff_card:
    if i in have_card:
        print(1, end=" ")    # 가지고 있으면 1, 없으면 0 출력
    else:
        print(0, end=" ")

'''
have_card = list(map(int, input().split()))  -> 시간초과

순서, 중복에 대한 특성을 사용하지 않을 때는 set을 사용하는 것이 좋음.
why? 리스트는 시간복잡도 O(n), set은 O(1)이므로.

'''
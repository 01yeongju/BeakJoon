# 1181. 단어 정렬

N = int(input())        # 단어의 개수 
word_list = [input() for _ in range(N)]     # 알파벳 단어

word_list = list(set(word_list))        # 중복 제거
word_list.sort()                        # 알파벳 사전순 정렬
word_list.sort(key=lambda x : len(x))   # 알파벳 길이순 정렬

for i in word_list:     # 출력
    print(i)
# 1543. 문서 검색

word = input()      # 주어진 문서
search = input()    # 찾을 단어

location = 0     # 검색 위치
search_len = len(search)    # 찾을 단어의 길이
last_location = len(word)-search_len    # 검사할 마지막 위치
# print(last_location)

cnt = 0         # 찾은 개수

# 같은 단어를 찾으면 word에서의 검색위치를 search_len만큼 증가, 못찾으면 검색위치 1 증가
while  last_location >= location:
    if search == word[location:location+search_len]:
        cnt += 1
        location += search_len
    else:
        location += 1
        
print(cnt)


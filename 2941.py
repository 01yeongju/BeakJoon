# 2941. 크로아티아 알파벳

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']     # 크로아디아 알파벳
word = input() 

for i in croatia:
    word = word.replace(i, '*') # 알파벳 찾으면 *로 변경

print(len(word))    # 알파벳의 개수 출력
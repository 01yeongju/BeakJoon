# 10814. 나이순 정렬

N = int(input())
member = []
for _ in range(N):
    age, name = input().split()
    member.append([int(age), name])

member.sort(key=lambda x: x[0])

for i in member:
    print(*i)

'''
3
21 Junkyu
21 Dohyun
20 Sunyoung


20 Sunyoung
21 Junkyu
21 Dohyun
'''
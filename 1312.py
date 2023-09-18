# 1312. 소수

A, B, N = map(int, input().split())     # A:피제수(분자), B:제수(분모), N:소숫점 아래 N번째 자리수

A %= B      # A를 B로 나눈 나머지를 A에 저장

# N번 반복하여 원하는 소수 자릿수까지 계산
for i in range(N):
    result = (A*10) // B
    A = (A*10) % B

print(result)
    
    
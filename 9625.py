# 9625. BABBA

K = int(input())

word = [0, 1]       # A:0, B:1

for i in range(1, K) :
  word.append(word[i] + word[i-1])

print(word[K-1], word[K])


''' 메모리 초과
K = int(input())
word = ['A', 'B']

for i in range(1, K):
    word.append(word[i]+word[i-1])
    
print(word[-1].count('A'), word[-1].count('B'))
'''
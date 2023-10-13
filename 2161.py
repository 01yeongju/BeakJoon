# 2161.카드1

N = int(input())
result = []
card = list(range(N,0,-1))
# print(card)

while card != []:
    result.append(card.pop())
    if card == []:
        break
    card.insert(0, card.pop())

print(result)
import sys
from collections import deque

input = sys.stdin.readline

cards = deque([])

num = int(input())
if num == 1:
    print(1)
    sys.exit(0)
for i in range(num):
    cards.append(i+1)

while True:
    cards.popleft()
    if len(cards) == 1:
        end_card = cards.popleft()
        break
    cards.append(cards.popleft())
print(end_card)
import sys
import heapq

N = int(sys.stdin.readline())
decks = []
result = 0

for _ in range(N):
    deck = int(sys.stdin.readline().rstrip())
    decks.append(deck)

heapq.heapify(decks)

while len(decks) >= 2:
    min_deck = heapq.heappop(decks)
    min_deck2 = heapq.heappop(decks)

    temp = min_deck+min_deck2
    result += temp
    heapq.heappush(decks, temp)

print(result)
import sys

N, M = map(int, sys.stdin.readline().split())
pokemon_dic = {}

for i in range(N):
    pokemon = sys.stdin.readline().rstrip()
    pokemon_dic[pokemon] = str(i+1)
    pokemon_dic[str(i+1)] = pokemon

for _ in range(M):
    que = sys.stdin.readline().rstrip()
    print(pokemon_dic[que])
K, N = map(int, input().split())
lines = []
result = []

for _ in range(K):
    lines.append(int(input()))

min_val = 1
max_val = max(lines)
mid = (min_val + max_val) // 2

while min_val <= max_val:
    cnt = 0

    for line in lines:
            cnt += (line // mid)
    
    if cnt < N:
        max_val = mid - 1
        mid = (min_val + max_val) // 2
    
    else:
        min_val = mid + 1
        mid = (min_val + max_val) // 2

print(mid)
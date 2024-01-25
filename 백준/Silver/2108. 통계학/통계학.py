import sys
from collections import Counter

N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

arm = 0
mid = 0
mod = 0
rng = 0

def merge_sort(L):
    if len(L) <= 1:
       return L
    mid = len(L) // 2
    L1 = merge_sort(L[:mid])
    L2 = merge_sort(L[mid:])
    return merge(L1, L2)

def merge(L1, L2):
    result = []
    L1_p,L2_p = 0, 0
    while len(L1) > L1_p and len(L2) > L2_p:
        if L1[L1_p] > L2[L2_p] :
            result.append(L2[L2_p])
            L2_p += 1
        else:
            result.append(L1[L1_p])
            L1_p += 1
    while len(L1) > L1_p and len(L2) <= L2_p:
        result.append(L1[L1_p])
        L1_p += 1
    while len(L2) > L2_p and len(L1) <= L1_p:
        result.append(L2[L2_p])
        L2_p += 1
    return result
    
nums = merge_sort(nums)

arm = round(sum(nums) / N)
mid = nums[(N-1)//2]
rng = nums[-1] - nums[0]

bin = Counter(nums).most_common()
mod = bin[0][0]

if len(bin) > 1 and bin[0][1] == bin[1][1]:
    mod = bin[1][0]

print(arm)
print(mid)
print(mod)
print(rng)
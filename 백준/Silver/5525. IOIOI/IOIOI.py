import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline()
pattern = ''

def KMP_table(pattern):
    lp = len(pattern)
    tb = [0 for _ in range(lp)]
    
    pidx = 0
    for idx in range(1, lp):
        while pidx > 0 and pattern[pidx] != pattern[idx]:
            pidx = tb[pidx-1]

        if pattern[idx] == pattern[pidx] :
            pidx += 1
            tb[idx] = pidx
    
    return tb

def KMP(word, pattern):
    table = KMP_table(pattern)
    
    results = [] 
    pidx = 0
    
    for idx in range(len(word)):
        while pidx > 0 and word[idx] != pattern[pidx] :
            pidx = table[pidx-1]

        if word[idx] == pattern[pidx]:
            if pidx == len(pattern)-1 :
                results.append(idx-len(pattern)+1)
                pidx = table[pidx]
            else:
                pidx += 1
    
    return results

for i in range(2*N+1):
    if i%2 == 1:
        pattern += 'O'
    else:
        pattern += 'I'

res = KMP(S, pattern)

print(len(res))
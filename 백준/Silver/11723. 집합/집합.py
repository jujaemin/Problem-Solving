import sys

M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    input = sys.stdin.readline().strip()

    if input == 'all':
        S = set(range(1, 22))
        pass

    elif input == 'empty':
        S =  set()
        pass

    else:
        cal, x = input.split()
        x = int(x)
    
        if cal == 'add':
            S.add(x)

        elif cal == 'remove':
            S.discard(x)

        elif cal == 'check':
            if x in S:
                print(1)
            else:
                print(0)
    
        elif cal == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)
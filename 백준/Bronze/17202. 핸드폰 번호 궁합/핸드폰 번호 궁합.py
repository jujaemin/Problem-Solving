import sys

number = []
for _ in range(2):
  number.append(sys.stdin.readline().strip())

A = number[0]
B = number[1]
first = ''

for i in range(len(A)):
    first += str(A[i])
    first += str(B[i])

def solution(num):
  result = ''
  for i in range(len(num)-1):
      result += str((int(num[i])+int(num[i+1]))%10)
  if len(result) == 2:
      return result
   
  elif len(num) == 1:
      return '0'+result
  
  else:
     return solution(result)

print(solution(first))

import sys

N = int(sys.stdin.readline())

class ABSHeap:

    def __init__(self):
        self.data = [0]

    def insert(self, item):
        self.data.append(item)
        m = len(self.data)-1
        while m > 1:
            if abs(self.data[m]) < abs(self.data[m//2]):
                self.data[m], self.data[m//2] = self.data[m//2], self.data[m]
                m = m//2

            elif abs(self.data[m]) == abs(self.data[m//2]):
                if self.data[m] < self.data[m//2]:
                    self.data[m], self.data[m//2] = self.data[m//2], self.data[m]
                    m = m//2
                else:
                    break

            else:
                break
    
    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.ABSheapify(1)
        else:
            data = 0
        return data
    
    def ABSheapify(self, i):
        left, right = 2*i, 2*i+1
        biggest = i
        if left < len(self.data) and abs(self.data[left]) < abs(self.data[biggest]):
            biggest = left
        if left < len(self.data) and abs(self.data[left]) == abs(self.data[biggest]):
            if self.data[left] < self.data[biggest]:
                biggest = left
        if right < len(self.data) and abs(self.data[right]) < abs(self.data[biggest]):
            biggest = right
        if right < len(self.data) and abs(self.data[right]) == abs(self.data[biggest]):
            if self.data[right] < self.data[biggest]:
                biggest = right
        if biggest != i:
            self.data[biggest], self.data[i] = self.data[i], self.data[biggest]
            self.ABSheapify(biggest)

nums = ABSHeap()

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        print(nums.remove())     
    else:
        nums.insert(x)
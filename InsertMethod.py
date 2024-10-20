class InsertMethod:
    A = []

    def __init__(self, A):
        self.A.extend(A)
        self.sort()

    def sort(self):
        for i in range(1, len(self.A)):
            self.insertElement(i)

    def mySwap(self, i, j):
        c = self.A[i]
        self.A[i] = self.A[j]
        self.A[j] = c

    def insertElement(self, k):
        for j in reversed(range(1, k+1)): # From k -> ... -> 1
            if (self.A[j-1] > self.A[j]):
                self.mySwap(j-1, j)
            else :
                break

    def printSortedList(self):
        print(self.A)
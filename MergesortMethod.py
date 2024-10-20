class MergesortMethod :
    A = []

    def __init__(self, A) :
        self.A.extend(A)
        self.mergesort(0, len(self.A) - 1)


    def mergesort(self, l, r):
        if l < r :
            m = (l + r) // 2

            self.mergesort(l, m)
            self.mergesort(m + 1, r)
            self.merge(l, m, r) 


    def merge(self, l, m, r):
        # Length of the new 2 lists
        n1 = m - l + 1
        n2 = r - m

        # Create the 2 temporary lists
        L = [0] * n1
        R = [0] * n2

        # Copy elements inside the new lists
        for i in range(n1):
            L[i] = self.A[l + i]

        for j in range(n2) :
            R[j] = self.A[m + 1 + j]

        # Merge the 2 temp lists into self.A
        i = 0
        j = 0
        k = l

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                self.A[k] = L[i]
                i += 1
            else:
                self.A[k] = R[j]
                j += 1
            k += 1
 
        # Copy the remaining elements of L[], if there are any
        while i < n1:
            self.A[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there are any
        while j < n2:
            self.A[k] = R[j]
            j += 1
            k += 1


    def printSortedList(self):
        print(self.A)
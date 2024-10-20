class QuicksortMethod:
    A = []
    
    def __init__(self, A) -> None:
        self.A.extend(A)
        self.quicksort(0, len(self.A)-1)


    def partition(self, low, high):
        # Take as pivot the last elent of the list
        pivot = self.A[high]

        i = low -1

        for j in range(low, high):
            if self.A[j] <= pivot :
                i += 1
                (self.A[i], self.A[j]) = (self.A[j], self.A[i])
        (self.A[i + 1], self.A[high]) = (self.A[high], self.A[i + 1])
        return i + 1

    def quicksort(self, low, high):
        if low < high :
            pi = self.partition(low, high)

            # Recursive call on the left 
            self.quicksort(low, pi - 1)

            # Recursive call on the right 
            self.quicksort(pi + 1, high)    

    def printSortedList(self):
        print(self.A)
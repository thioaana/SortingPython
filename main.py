from InsertMethod import InsertMethod
from QuicksortMethod import QuicksortMethod 
from MergesortMethod import MergesortMethod

if __name__ == "__main__":
    A = [5, 7, 4, 12, 6, 2]
    print(A)
    # method = InsertMethod(A)
    # method.printSortedList()

    # method = QuicksortMethod(A)
    # method.printSortedList()

    method = MergesortMethod(A)
    method.printSortedList()

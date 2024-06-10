#Import random to generate a random collection of numbers in an array
import random

def Obs1_SinkSort(A):
    n = len(A)
    # Use of (n-1) instead of (n-2) as python indexing accounts for (n-2)
    for i in range(n-1, 0, -1):
        swap = False
        for j in range(0, i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swap = True
                
        if not swap:
            break
        
        #Cascade scan of the array
        swap = False
        for j in range(i-1, 0, -1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swap = True

            if not swap:
                break
            
# This generates an array that is unsorted for the user to see what numbers where generated
A = [random.randint(1, 100) for a in range(20)]
print("\nUnsorted Array Of Generated Numbers: ", A)

# This sorts the array using the SinkSort algorithm
Obs1_SinkSort(A)
print("\nSorted array: ", A)

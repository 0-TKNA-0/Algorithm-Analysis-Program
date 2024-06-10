#Import random to generate a random collection of numbers in an array
import random

def SinkSort(A):
    n = len(A)
    # Use of (n-1) instead of (n-2) as python indexing accounts for (n-2)
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            
# This generates an array that is unsorted for the user to see what numbers where generated
A = [random.randint(1, 100) for a in range(20)]
print("\nUnsorted Array Of Generated Numbers: ", A)

# This sorts the array using the SinkSort algorithm
SinkSort(A)
print("\nSorted array: ", A)

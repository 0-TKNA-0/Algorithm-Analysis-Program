#Import random to generate a random collection of numbers in an array
import random

def bubbleSort(A):
    n = len(A)
    # Use of (n-1) instead of (n-2) as python indexing accounts for (n-2)
    for i in range(n-1):
        # Use of (n-i-1) instead of (n-i-2) as python indexing accounts for (n-i-2)
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

# This generates an array that is unsorted for the user to see what numbers where generated
A = [random.randint(1, 100) for a in range(20)]
print("\nUnsorted Array Of Generated Numbers: ", A)

# This sorts the array using the bubble sort algorithm
bubbleSort(A)
print("\nSorted array: ", A)

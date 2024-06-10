#Import random to generate a random collection of numbers in an array
import random

def BiDirectionalBubbleSort(A):
    n = len(A)
    # Use of (n+1) instead of (n+2) as python indexing accounts for (n+2)
    for i in range(1,(n+1)//2):
        # This is the left-to-right scanning method
        for j in range(i-1, n-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
        # This is the right-to-left scanning method
        for j in range(n-i, i-1, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]

# This generates an array that is unsorted for the user to see what numbers where generated
A = [random.randint(1, 100) for a in range(20)]
print("\nUnsorted Array Of Generated Numbers: ", A)

# This sorts the array using the Bi-Directional Bubble Sort algorithm
BiDirectionalBubbleSort(A)
print("\nSorted array: ", A)

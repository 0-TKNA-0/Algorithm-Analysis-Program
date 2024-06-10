import random
import time

def selectionSort(unsortedArray):
    comparisons = 0
    for i in range(len(unsortedArray)):
        minI = i
        for j in range(i+1, len(unsortedArray)):
            comparisons += 1
            if unsortedArray[j] < unsortedArray[minI]:
                minI = j

        unsortedArray[i], unsortedArray[minI] = unsortedArray[minI], unsortedArray[i]
        
    return unsortedArray, comparisons


def insertionSort(unsortedArray):
    comparisons = 0
    for i in range(1, len(unsortedArray)):
        minI = unsortedArray[i]
        j = i - 1
        while j >= 0 and minI < unsortedArray[j]:
            unsortedArray[j + 1] = unsortedArray[j]
            j -= 1
            comparisons += 1
        unsortedArray[j + 1] = minI
        comparisons += 1
        
    return unsortedArray, comparisons   
    
    

def mergeSort(unsortedArray):
    comparisons = 0
    if len(unsortedArray) > 1:
        
        arrayMiddle = len(unsortedArray) // 2
        arrayLeft = unsortedArray[:arrayMiddle]
        arrayRight = unsortedArray[arrayMiddle:]
        
        leftSorted, leftComparison = mergeSort(arrayLeft)
        rightSorted, rightComparison = mergeSort(arrayRight)
        comparisons = leftComparison + rightComparison
        
        i = j = k = 0
        
        while i < len(arrayLeft) and j < len(arrayRight):
            comparisons += 1
            if arrayLeft[i] < arrayRight[j]:
                unsortedArray[k] = arrayLeft[i]
                i += 1
            else:
                unsortedArray[k] = arrayRight[j]
                j += 1

            k += 1
            
        while i < len(arrayLeft):
            unsortedArray[k] = arrayLeft[i]
            i += 1
            k += 1
            
        while j < len(arrayRight):
            unsortedArray[k] = arrayRight[j]
            j += 1
            k += 1
            
    return unsortedArray, comparisons  


def quickSort(unsortedArray):
    comparisons = 0
    stack = [(0, len(unsortedArray) - 1)]
    while stack:
        arrayStart, arrayEnd = stack.pop()
        if arrayEnd - arrayStart <= 0:
            continue
        pivotElement = unsortedArray[arrayStart]
        i, j = arrayStart + 1, arrayEnd
        while i <= j:
            while i <= j and unsortedArray[i] <= pivotElement:
                comparisons += 1
                i += 1
            while i <= j and unsortedArray[j] > pivotElement:
                comparisons += 1
                j -= 1
            if i <= j:
                unsortedArray[i], unsortedArray[j] = unsortedArray[j], unsortedArray[i]
        unsortedArray[arrayStart], unsortedArray[j] = unsortedArray[j], unsortedArray[arrayStart]
        stack.append((arrayStart, j - 1))
        stack.append((j + 1, arrayEnd))
    return unsortedArray, comparisons

            
def heapSort(unsortedArray):
    comparisons = 0
    n = len(unsortedArray)
    for i in range(n // 2 - 1, -1, -1):
        j = i
        while True:
            arrayMax = j
            arrayLeft = 2 * j + 1
            arrayRight = 2 * j + 2
            
            if arrayLeft < n and unsortedArray[arrayLeft] > unsortedArray[arrayMax]:
                arrayMax = arrayLeft

            if arrayRight < n and unsortedArray[arrayRight] > unsortedArray[arrayMax]:
                arrayMax = arrayRight

            comparisons += 2

            if arrayMax != j:
                unsortedArray[j], unsortedArray[arrayMax] = unsortedArray[arrayMax], unsortedArray[j]
                j = arrayMax
            else:
                break

    for i in range(n - 1, 0, -1):
        unsortedArray[i], unsortedArray[0] = unsortedArray[0], unsortedArray[i]

        j = 0

        while True:
            arrayMax = j
            arrayLeft = 2 * j + 1
            arrayRight = 2 * j + 2
            
            if arrayLeft < i and unsortedArray[arrayLeft] > unsortedArray[arrayMax]:
                arrayMax = arrayLeft

            if arrayRight < i and unsortedArray[arrayRight] > unsortedArray[arrayMax]:
                arrayMax = arrayRight

            comparisons += 2

            if arrayMax != j:
                unsortedArray[j], unsortedArray[arrayMax] = unsortedArray[arrayMax], unsortedArray[j]
                j = arrayMax
            else:
                break

    return unsortedArray, comparisons


def bubbleSort(unsortedArray):
    comparisons = 0
    n = len(unsortedArray)
    for i in range(n-1):
        for j in range(n-i-1):
            comparisons += 1
            if unsortedArray[j] > unsortedArray[j+1]:
                unsortedArray[j], unsortedArray[j+1] = unsortedArray[j+1], unsortedArray[j]
                
    return unsortedArray, comparisons


def obs1_BubbleSort(unsortedArray):
    comparisons = 0
    n = len(unsortedArray)
    for i in range(n-1):
        swap = n-1
        for j in range(0, swap):
            comparisons += 1
            if unsortedArray[j] > unsortedArray[j+1]:
                unsortedArray[j], unsortedArray[j+1] = unsortedArray[j+1], unsortedArray[j]
                swap = j
        if swap == n-1:
            break
        
    return unsortedArray, comparisons


def obs2_BubbleSort(unsortedArray):
    comparisons = 0
    n = len(unsortedArray)
    for i in range(n-1):
        swap = False
        for j in range(n-i-1):
            comparisons += 1
            if unsortedArray[j] > unsortedArray[j+1]:
                unsortedArray[j], unsortedArray[j+1] = unsortedArray[j+1], unsortedArray[j]
                swap = True
        if swap == False:
            break
        
    return unsortedArray, comparisons
    

def obs3_BubbleSort(unsortedArray):
    comparisons = 0
    n = len(unsortedArray)
    for i in range(n-1):
        swap = False
        for j in range(n-1):
            comparisons += 1
            if unsortedArray[j] > unsortedArray[j+1]:
                unsortedArray[j], unsortedArray[j+1] = unsortedArray[j+1], unsortedArray[j]
                swap = True
                lastSwap = j
        if swap == False:
            break

        n = lastSwap + 1
    return unsortedArray, comparisons


def sinkDown(unsortedArray):
    comparisons = 0
    n = len(unsortedArray)
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            comparisons += 1
            if unsortedArray[j] > unsortedArray[j+1]:
                unsortedArray[j], unsortedArray[j+1] = unsortedArray[j+1], unsortedArray[j]
                
    return unsortedArray, comparisons


def biDirectionalBubbleSort(unsortedArray):
    comparisons = 0
    n = len(unsortedArray)
    for i in range(1,(n+1)//2):
        for j in range(i-1, n-i):
            comparisons += 1
            if unsortedArray[j] > unsortedArray[j+1]:
                unsortedArray[j], unsortedArray[j+1] = unsortedArray[j+1], unsortedArray[j]
                
        for j in range(n-i, i-1, -1):
            comparisons += 1
            if unsortedArray[j] < unsortedArray[j-1]:
                unsortedArray[j], unsortedArray[j-1] = unsortedArray[j-1], unsortedArray[j]
                
    return unsortedArray, comparisons


while True:
    print("-----------------\n    Main Menu\n-----------------")
    print("1. Test An Individual Sorting Algorithm\n2. Test Multiple Sorting Algorithms\n3. Exit Program")
    menuChoice = input("\nEnter : ")
    if menuChoice == "1":
        while True:
            print("\n----------------------------------\n    Individual Sorting Algorithms\n----------------------------------")
            print("1. Test Selection Sort Algorithm\n2. Test Insertion Sort Algorithm\n3. Test Merge Sort Algorithm\n4. Test Quick Sort Algorithm\n5. Test Heap Sort Algorithm\n6. Test Bubble Sort Algorithm")
            print("7. Test Obs1-Bubble Sort Algorithm\n8. Test Obs2-Bubble Sort Algorithm\n9. Test Obs3-Bubble Sort Algorithm\nA. Test Sink-Down Sort Algorithm\nB. Test Bi-Directional Sort Algorithm\nR. Return")
            indSortingChoice = input("\nEnter : ").lower()
            if indSortingChoice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "r"]:
                if indSortingChoice == "1":
                    while True:
                        try:
                            arraySize = int(input("Enter Array Size : "))
                            if arraySize <= 0:
                               print("Invalid Input")
                            else:
                                unsortedArray = [random.randint(0, 150) for a in range(arraySize)]
                                print("\n-----------------------------------------------------\nUnsorted :", unsortedArray)
                                selectionSort(unsortedArray)
                                sortedArray, comparisons = selectionSort(unsortedArray)
                                print("Sorted :", sortedArray, "\n-----------------------------------------------------")
                                break
                        except ValueError:
                            print("Invalid Input, Enter A Positive Number")
                            break
                        
                elif indSortingChoice == "2":
                    while True:
                        try:
                            arraySize = int(input("Enter Array Size : "))
                            if arraySize <= 0:
                               print("Invalid Input")
                            else:
                                unsortedArray = [random.randint(0, 150) for a in range(arraySize)]
                                print("\n-----------------------------------------------------\nUnsorted :", unsortedArray)
                                insertionSort(unsortedArray)
                                sortedArray, comparisons = insertionSort(unsortedArray)
                                print("Sorted :", sortedArray, "\n-----------------------------------------------------")
                                break
                        except ValueError:
                            print("Invalid Input, Enter A Positive Number")
                            break
                        
                elif indSortingChoice == "3":
                    while True:
                        try:
                            arraySize = int(input("Enter Array Size : "))
                            if arraySize <= 0:
                               print("Invalid Input")
                            else:
                                unsortedArray = [random.randint(0, 150) for a in range(arraySize)]
                                print("\n-----------------------------------------------------\nUnsorted :", unsortedArray)
                                mergeSort(unsortedArray)
                                sortedArray, comparisons = mergeSort(unsortedArray)
                                print("Sorted :", sortedArray, "\n-----------------------------------------------------")
                                break
                        except ValueError:
                            print("Invalid Input, Enter A Positive Number")
                            break
                        
                elif indSortingChoice == "4":
                    while True:
                        try:
                            arraySize = int(input("Enter Array Size : "))
                            if arraySize <= 0:
                               print("Invalid Input")
                            else:
                                unsortedArray = [random.randint(0, 150) for a in range(arraySize)]
                                print("\n-----------------------------------------------------\nUnsorted :", unsortedArray)
                                quickSort(unsortedArray)
                                sortedArray, comparisons = quickSort(unsortedArray)
                                print("Sorted :", sortedArray, "\n-----------------------------------------------------")
                                break
                        except ValueError:
                            print("Invalid Input, Enter A Positive Number")
                            break
                        
                elif indSortingChoice == "5":
                    while True:
                        try:
                            arraySize = int(input("Enter Array Size : "))
                            if arraySize <= 0:
                               print("Invalid Input")
                            else:
                                unsortedArray = [random.randint(0, 150) for a in range(arraySize)]
                                print("\n-----------------------------------------------------\nUnsorted :", unsortedArray)
                                heapSort(unsortedArray)
                                sortedArray, comparisons = heapSort(unsortedArray)
                                print("Sorted :", sortedArray, "\n-----------------------------------------------------")
                                break
                        except ValueError:
                            print("Invalid Input, Enter A Positive Number")
                            break
                        
                elif indSortingChoice == "6":
                    while True:
                        try:
                            arraySize = int(input("Enter Array Size : "))
                            if arraySize <= 0:
                               print("Invalid Input")
                            else:
                                unsortedArray = [random.randint(0, 150) for a in range(arraySize)]
                                print("\n-----------------------------------------------------\nUnsorted :", unsortedArray)
                                bubbleSort(unsortedArray)
                                sortedArray, comparisons = bubbleSort(unsortedArray)
                                print("Sorted :", sortedArray, "\n-----------------------------------------------------")
                                break
                        except ValueError:
                            print("Invalid Input, Enter A Positive Number")
                            break
                        
                elif indSortingChoice == "7":
                    while True:
                        try:
                            arraySize = int(input("Enter Array Size : "))
                            if arraySize <= 0:
                               print("Invalid Input")
                            else:
                                unsortedArray = [random.randint(0, 150) for a in range(arraySize)]
                                print("\n-----------------------------------------------------\nUnsorted :", unsortedArray)
                                obs1_BubbleSort(unsortedArray)
                                sortedArray, comparisons = obs1_BubbleSort(unsortedArray)
                                print("Sorted :", sortedArray, "\n-----------------------------------------------------")
                                break
                        except ValueError:
                            print("Invalid Input, Enter A Positive Number")
                            break
                        
                elif indSortingChoice == "8":
                    while True:
                        try:
                            arraySize = int(input("Enter Array Size : "))
                            if arraySize <= 0:
                               print("Invalid Input")
                            else:
                                unsortedArray = [random.randint(0, 150) for a in range(arraySize)]
                                print("\n-----------------------------------------------------\nUnsorted :", unsortedArray)
                                obs2_BubbleSort(unsortedArray)
                                sortedArray, comparisons = obs2_BubbleSort(unsortedArray)
                                print("Sorted :", sortedArray, "\n-----------------------------------------------------")
                                break
                        except ValueError:
                            print("Invalid Input, Enter A Positive Number")
                            break
                        
                elif indSortingChoice == "9":
                    while True:
                        try:
                            arraySize = int(input("Enter Array Size : "))
                            if arraySize <= 0:
                               print("Invalid Input")
                            else:
                                unsortedArray = [random.randint(0, 150) for a in range(arraySize)]
                                print("\n-----------------------------------------------------\nUnsorted :", unsortedArray)
                                obs3_BubbleSort(unsortedArray)
                                sortedArray, comparisons = obs3_BubbleSort(unsortedArray)
                                print("Sorted :", sortedArray, "\n-----------------------------------------------------")
                                break
                        except ValueError:
                            print("Invalid Input, Enter A Positive Number")
                            break
                        
                elif indSortingChoice == "a":
                    while True:
                        try:
                            arraySize = int(input("Enter Array Size : "))
                            if arraySize <= 0:
                               print("Invalid Input")
                            else:
                                unsortedArray = [random.randint(0, 150) for a in range(arraySize)]
                                print("\n-----------------------------------------------------\nUnsorted :", unsortedArray)
                                sinkDown(unsortedArray)
                                sortedArray, comparisons = sinkDown(unsortedArray)
                                print("Sorted :", sortedArray, "\n-----------------------------------------------------")
                                break
                        except ValueError:
                            print("Invalid Input, Enter A Positive Number")
                            break
                        
                elif indSortingChoice == "b":
                    while True:
                        try:
                            arraySize = int(input("Enter Array Size : "))
                            if arraySize <= 0:
                               print("Invalid Input")
                            else:
                                unsortedArray = [random.randint(0, 150) for a in range(arraySize)]
                                print("\n-----------------------------------------------------\nUnsorted :", unsortedArray)
                                biDirectionalBubbleSort(unsortedArray)
                                sortedArray, comparisons = biDirectionalBubbleSort(unsortedArray)
                                print("Sorted :", sortedArray, "\n-----------------------------------------------------")
                                break
                        except ValueError:
                            print("Invalid Input, Enter A Positive Number")
                            break
                        
                elif indSortingChoice == "r":
                    break
            
            else:
                print("ERROR")
                
    elif menuChoice == "2":
        while True:
            try:
                print("Please Place Compiler Into FullScreen")
                arraySize = int(input("Enter Array Size : "))
                if arraySize <= 0:
                    print("Invalid Input")
                else:
                    unsortedArray = [random.randint(0, 150) for a in range(arraySize)]
                    print("|----------------------------------------------------------------------------------|")
                    print("|   Sorting Algorithm Name  | Array Size | Num. of Comparisons | Run Time (in ms.) |")
                    print("|----------------------------------------------------------------------------------|")

                    startTime = time.perf_counter()
                    selectionSort(unsortedArray)
                    sortedArray, comparisons = selectionSort(unsortedArray)
                    endTime = time.perf_counter()
                    milliSecs = round((endTime - startTime) * 1000, 3)
                    print("|       Selection Sort      |    ", arraySize, "    |         ", comparisons, "        |    ", milliSecs, "(ms.)   |")

                    startTime = time.perf_counter()
                    insertionSort(unsortedArray)
                    sortedArray, comparisons = insertionSort(unsortedArray)
                    endTime = time.perf_counter()
                    milliSecs = round((endTime - startTime) * 1000, 3)
                    print("|       Insertion Sort      |    ", arraySize, "    |         ", comparisons, "         |    ", milliSecs, "(ms.)   |")

                    startTime = time.perf_counter()
                    mergeSort(unsortedArray)
                    sortedArray, comparisons = mergeSort(unsortedArray)
                    endTime = time.perf_counter()
                    milliSecs = round((endTime - startTime) * 1000, 3)
                    print("|         Merge Sort        |    ", arraySize, "    |         ", comparisons, "        |    ", milliSecs, "(ms.)   |")


                    startTime = time.perf_counter()
                    quickSort(unsortedArray)
                    sortedArray, comparisons = quickSort(unsortedArray)
                    endTime = time.perf_counter()
                    milliSecs = round((endTime - startTime) * 1000, 3)
                    print("|         Quick Sort        |    ", arraySize, "    |         ", comparisons, "        |    ", milliSecs, "(ms.)   |")

                    startTime = time.perf_counter()
                    heapSort(unsortedArray)
                    sortedArray, comparisons =  heapSort(unsortedArray)
                    endTime = time.perf_counter()
                    milliSecs = round((endTime - startTime) * 1000, 3)
                    print("|         Heap Sort         |    ", arraySize, "    |         ", comparisons, "        |    ", milliSecs, "(ms.)   |")

                    startTime = time.perf_counter()
                    bubbleSort(unsortedArray)
                    sortedArray, comparisons =  bubbleSort(unsortedArray)
                    endTime = time.perf_counter()
                    milliSecs = round((endTime - startTime) * 1000, 3)
                    print("|         Bubble Sort       |    ", arraySize, "    |         ", comparisons, "        |    ", milliSecs, "(ms.)   |")

                    startTime = time.perf_counter()
                    obs1_BubbleSort(unsortedArray)
                    sortedArray, comparisons =  obs1_BubbleSort(unsortedArray)
                    endTime = time.perf_counter()
                    milliSecs = round((endTime - startTime) * 1000, 3)
                    print("|      Obs1 Bubble Sort     |    ", arraySize, "    |         ", comparisons, "         |    ", milliSecs, "(ms.)   |")

                    startTime = time.perf_counter()
                    obs2_BubbleSort(unsortedArray)
                    sortedArray, comparisons =  obs2_BubbleSort(unsortedArray)
                    endTime = time.perf_counter()
                    milliSecs = round((endTime - startTime) * 1000, 3)
                    print("|      Obs2 Bubble Sort     |    ", arraySize, "    |         ", comparisons, "         |    ", milliSecs, "(ms.)   |")

                    startTime = time.perf_counter()
                    obs3_BubbleSort(unsortedArray)
                    sortedArray, comparisons =  obs3_BubbleSort(unsortedArray)
                    endTime = time.perf_counter()
                    milliSecs = round((endTime - startTime) * 1000, 3)
                    print("|      Obs3 Bubble Sort     |    ", arraySize, "    |         ", comparisons, "         |    ", milliSecs, "(ms.)   |")

                    startTime = time.perf_counter()
                    sinkDown(unsortedArray)
                    sortedArray, comparisons =  sinkDown(unsortedArray)
                    endTime = time.perf_counter()
                    milliSecs = round((endTime - startTime) * 1000, 3)
                    print("|       Sink Down Sort      |    ", arraySize, "    |         ", comparisons, "        |    ", milliSecs, "(ms.)   |")

                    startTime = time.perf_counter()
                    biDirectionalBubbleSort(unsortedArray)
                    sortedArray, comparisons =  biDirectionalBubbleSort(unsortedArray)
                    endTime = time.perf_counter()
                    milliSecs = round((endTime - startTime) * 1000, 3)
                    print("| BiDirectional Bubble Sort |    ", arraySize, "    |         ", comparisons, "        |    ", milliSecs, "(ms.)    |")

                    print("|----------------------------------------------------------------------------------|\n")
                    

                    break
            except ValueError:
                print("Invalid Input, Enter A Positive Number")
                break

    elif menuChoice == "3":
        exit()
        
    else:
        print("\nError, Invalid Input\n")

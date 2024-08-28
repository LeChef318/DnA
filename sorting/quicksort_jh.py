import random

def quicksort(A, low = 0, high = None):
    if high == None:
        high = len(A) - 1
    if low < high:
        pivotIndex = split(A, low, high)
        quicksort(A, low, pivotIndex)
        quicksort(A, pivotIndex + 1, high)
    return A


def split(A, low, high):
    pivot = random.randrange(low, high)
    A[pivot], A[high] = A[high], A[pivot]
    c = low - 1
    for i in range(low, high):
        if A[i] < A[high]:
            c = c + 1
            A[i], A[c] = A[c], A[i]
    
    A[high], A[c + 1] = A[c + 1], A[high]
    return c + 1



def sort(A, low = 0, high = None):
        if high == None:
            high = len(A) - 1
        if low < high:

            pivot = random.randrange(low, high)
            A[pivot], A[high] = A[high], A[pivot]
            c = low - 1
            for i in range(low, high):
                if A[i] < A[high]:
                    c = c + 1
                    A[i], A[c] = A[c], A[i]
        
            A[high], A[c + 1] = A[c + 1], A[high]


            pivotIndex = c + 1

            sort(A, low, pivotIndex)
            sort(A, pivotIndex + 1, high)
        return A


test = [random.randint(0,100) for i in range(10)]
print(sort(test))
import random

def bubblesort(A):
    for i in range(len(A)):
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swapped = True
        if not swapped:
            break
    return A


test = [random.randint(0,100) for i in range(10)]
print(bubblesort(test))
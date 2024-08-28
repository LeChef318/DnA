import random

def mergesort(A):
    if len(A) <= 1:
        return A
    else:
        left = []
        right = []
        for i in range(len(A) // 2):
            left.append(A[i])
        for i in range(len(A) // 2, len(A)):
            right.append(A[i])
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)

def merge(left, right):
    out = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            out.append(right[0])
            right.pop(0)
        else:
            out.append(left[0])
            left.pop(0)
    while len(left) == 0 and len(right) > 0:
        out.append(right[0])
        right.pop(0)
    while len(left) > 0 and len(right) == 0:
        out.append(left[0])
        left.pop(0)
    return out

test = [random.randint(0,100) for i in range(10)]
print(mergesort(test))
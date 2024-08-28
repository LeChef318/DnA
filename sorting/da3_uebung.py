import random

class Sorter:
    def sort(self, A):
        """
            Sort a list A in increasing order.
            Important: Always return a *copy* of the input list A, do *not* change the list A 
                       
            return: The sorted list A
        """
        raise NotImplementedError

class Bubblesort(Sorter):
    """
        Implements BUBBLESORT as discussed in the lecture
    """
    name = "BUBBLESORT"
    def sort(self, A):
        A = list(A)
        for i in range(len(A) - 1):
            swapped = False
            for j in range(len(A) - 1 - i):
                if A[j] > A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]
                    swapped = True
            if not swapped:
                break
        return A



class Quicksort(Sorter):
    """
        Implements QUICKSORT as discussed in the lecture
    """
    name = "QUICKSORT"
    def sort(self, A, low = 0, high = None):
        A = list(A)
        if high == None:
            high = len(A) - 1
        if low < high:
            pivotIndex = self.split(A, low, high)
            A = self.sort(A, low, pivotIndex)
            A = self.sort(A, pivotIndex + 1, high)
        return A


    def split(self, A, low, high):
        pivot = random.randrange(low, high)
        A[pivot], A[high] = A[high], A[pivot]
        c = low - 1
        for i in range(low, high):
            if A[i] < A[high]:
                c = c + 1
                A[i], A[c] = A[c], A[i]
    
        A[high], A[c + 1] = A[c + 1], A[high]
        return c + 1

class Mergesort(Sorter):
    """
        Implements MERGESORT as discussed in the lecture
        Tipp: Moeglicherweise eine Hilfs-methode merge(self, links, rechts) implementieren
    """
    name = "MERGESORT"
    def sort(self, A):
        A = list(A)
        if len(A) <= 1:
            return A
        else:
            left = []
            right = []
            for i in range(len(A) // 2):
                left.append(A[i])
            for i in range(len(A) // 2, len(A)):
                right.append(A[i])
        left = self.sort(left)
        right = self.sort(right)
        return self.merge(left, right)
    
    def merge(self, left, right):
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




if __name__ == "__main__":
    for s in [Bubblesort(), Quicksort(), Mergesort()]:
        a = [random.randint(0,100) for i in range(10)]
        # Test ob euer Sortierverfahren das gleiche zurueckgibt wie die Python Implementation
        assert s.sort(a) == sorted(a), \
                            "List is not propertly sorted. "+s.name+" returned: "+str(s.sort(a))+" but we expected: "+str(sorted(a))

    print("Well done! Now go and read: https://en.wikipedia.org/wiki/Timsort to see how Python does it.")

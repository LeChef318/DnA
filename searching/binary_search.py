def binary_search(L, k):
    """
        Sucht ein Element `k` in der Liste `L`.
        Bedingung: `L` ist *aufsteigend sortiert*
 
        Return: `k` falls gefunden
                None sonst
    """
    if k > L[len(L)-1]:
        return
    if k < L[0]:
        return
    mid = len(L) // 2
    if k < L[mid]:
        return binary_search(L[:mid], k)
    elif k > L[mid]:
        return binary_search(L[mid:], k)
    elif k == L[mid]:
        return k
    else:
        return


list = list(range(1, 101, 1))
x = binary_search(list, 44)

print(x)
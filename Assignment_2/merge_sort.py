def mergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2

        mergeSort(A, p, q)
        print(A)

        mergeSort(A, q + 1, r)
        print(A)

        merge(A, p, q, r)
        print(A)


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + j + 1]

    L[n1] = float("inf")
    R[n2] = float("inf")

    i = 0
    j = 0

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def run_merge_sort(array):
    n = len(array)
    mergeSort(array, 0, n - 1)
    return array


array = [2, 1, 6, 3, 4]
print("Unsorted Array: ", array)

sorted_array = run_merge_sort(array)
print("Fully Sorted Array: ", sorted_array)
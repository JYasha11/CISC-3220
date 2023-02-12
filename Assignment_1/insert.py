def reverseInsertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1

        while i >= 0 and A[i] < key:
            A[i + 1] = A[i]
            i = i - 1

            A[i + 1] = key


def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1

        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1

            A[i + 1] = key


A = [2, 8, 4, 3, 1, 6, 3]

reverseInsertionSort(A)

print('Sorted Array in Descending Order:', A)

insertionSort(A)

print('Sorted Array in Ascending Order:', A)

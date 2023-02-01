def reverseInsertionSort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        
        while i >= 0 and array[i] < key : 
            array[i + 1] = array[i]
            i = i - 1
        
            array[i + 1] = key

def insertionSort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        
        while i >= 0 and array[i] > key : 
            array[i + 1] = array[i]
            i = i - 1
        
            array[i + 1] = key


data = [2,8,4,3,1,6,3]

reverseInsertionSort(data)

print('Sorted Array in Descending Order:' , data)

insertionSort(data)

print('Sorted Array in Ascending Order:' , data)


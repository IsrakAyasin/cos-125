def MaxHeapify(arr, N, idx, verbose=False):
    # If indexed node is outside of the array, skip
    if idx >= N:
        return
    # get left and right children indices
    l = 2 * idx + 1
    r = 2 * idx + 2

    # Set current node as largest among its children by default
    Max = idx

    # Check if left child is larger than current node
    if l < N and arr[l] > arr[idx]:
        Max = l
    # Check if right child is largest
    if r < N and arr[r] > arr[Max]:
        Max = r

    if verbose == True:
      print("Array: ", arr, " | idx: ", idx, " left child: ", l," right child: ", r, " | Max: ", Max)

    # Put maximum value at root and recur for the child with the maximum value if necessary
    if Max != idx:
        arr[Max], arr[idx] = arr[idx], arr[Max]
        MaxHeapify(arr, N, Max)

def buildMaxHeap(arr, N, verbose=False):
    # building the heap from first non-leaf
    # node by calling Max heapify function
    for i in range(int(N / 2) - 1, -1, -1):
        MaxHeapify(arr, N, i, verbose)

        
if __name__ == '__main__':

    a = [10, 15, 60, 2, 20, 100, 95]
    N = len(a)

    # Sort array a into max heap. Use verbose=True to print out intermediate arrays during sort
    buildMaxHeap(a, N, verbose=True)

    for i in range(N):
        print(a[i], end=" ")
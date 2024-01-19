def MinHeapify(arr, N, idx, verbose=False):
    # If indexed node is outside of the array, skip
    if idx >= N:
        return

    # get left and right children indices
    l = 2 * idx + 1
    r = 2 * idx + 2

    # Set current node as largest among its children by default
    Min = idx

    # Check if left child is smaller than current node
    if l < N and arr[l] < arr[idx]:
        Min = l
    # Check if right child is smallest
    if r < N and arr[r] < arr[Min]:
        Min = r

    if verbose == True:
      print("Array: ", arr, " | left: ", l, " idx: ", idx," right: ", r, " | Max: ", Min)

    # Put minimum value at root and recur for the child with the minimum value
    if Min != idx:
        arr[Min], arr[idx] = arr[idx], arr[Min]
        MinHeapify(arr, N, Min)

def buildMinHeap(arr, N, verbose=False):
    # building the heap from first non-leaf node
    # by calling Min heapify function
    for i in range(int(N / 2) - 1, -1, -1):
        MinHeapify(arr, N, i, verbose)
if __name__ == '__main__':
    a = [5, 2, 3, 4, 1, 3]
    N = len(a)

    # Sort array a into max heap. Use verbose=True to print out intermediate arrays during sort
    buildMinHeap(a, N, verbose=True)

    for i in range(N):
        print(a[i], end=" ")
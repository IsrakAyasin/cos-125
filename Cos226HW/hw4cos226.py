class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def height(tree):
    if not tree:
        return 0
    left_height = height(tree.left)
    right_height = height(tree.right)
    return max(left_height, right_height) + 1

def merge_trees(tree1, tree2):
    merged_nodes = []

    def in_order_traversal(node):
        nonlocal merged_nodes
        if node:
            in_order_traversal(node.left)
            merged_nodes.append(node.key)
            in_order_traversal(node.right)

    in_order_traversal(tree1)
    in_order_traversal(tree2)

    return merged_nodes

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
      print("Array: ", arr, " | left: ", l, " idx: ", idx," right: ", r, " | Min: ", Min)

    # Put minimum value at root and recur for the child with the minimum value
    if Min != idx:
        arr[Min], arr[idx] = arr[idx], arr[Min]
        MinHeapify(arr, N, Min)

def buildMinHeap(arr, N, verbose=False):
    # building the heap from first non-leaf node
    # by calling Min heapify function
    for i in range(int(N / 2) - 1, -1, -1):
        MinHeapify(arr, N, i, verbose)

def arr2bt(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    root = TreeNode(arr[mid])

    root.left = arr2bt(arr[:mid])
    root.right = arr2bt(arr[mid+1:])
    return root

def print_tree_in_order(node):
    if node: 
        print_tree_in_order(node.left)
        print(node.key, end=' ')
        print_tree_in_order(node.right)
# Create the first binary tree
#       2
#      / \
#     5   3
tree1 = TreeNode(2)
tree1.left = TreeNode(5)
tree1.right = TreeNode(3)

# Create the second binary tree
#       1
#      / \
#     4   3
tree2 = TreeNode(1)
tree2.left = TreeNode(4)
tree2.right = TreeNode(3)

if __name__ == '__main__':
    a = merge_trees(tree1, tree2)
    N = len(a)
    # Sort array a into max heap. Use verbose=True to print out intermediate arrays during sort
    buildMinHeap(a, N, verbose=True)
    #print("\nMerged min-heap: ")
#print_tree_in_order(arr2bt(a))
print("Merged min-heap: ", a)
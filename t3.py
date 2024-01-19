class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def splay(root, key):
    if not root or root.key == key:
        return root

    if key < root.key:
        if not root.left:
            return root
        if key < root.left.key:
            root.left.left = splay(root.left.left, key)
            root = rotate_right(root)
        elif key > root.left.key:
            root.left.right = splay(root.left.right, key)
            root = rotate_left(root)
        
        if root.left:
            root = rotate_right(root)
        return root

    else:  # key > root.key
        if not root.right:
            return root
        if key > root.right.key:
            root.right.right = splay(root.right.right, key)
            root = rotate_left(root)
        elif key < root.right.key:
            root.right.left = splay(root.right.left, key)
            root = rotate_right(root)
        
        if root.right:
            root = rotate_left(root)
        return root

def combine_heaps(T1, T2):
    if not T1:
        return T2
    if not T2:
        return T1

    max_T1 = find_max(T1)
    T1 = splay(T1, max_T1.key)
    T1.right = T2
    return T1

def find_max(root):
    while root.right:
        root = root.right
    return root

def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    return x

def rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    return y

# Example usage:
T1 = TreeNode(2)
T1.left = TreeNode(5)
T1.right = TreeNode(3)

T2 = TreeNode(1)
T2.left = TreeNode(4)
T2.right = TreeNode(3)

combined_tree = combine_heaps(T1, T2)
print(combined_tree.key)  # Output: 5
print(combined_tree.left.key)  # Output: 2
print(combined_tree.right.key)  # Output: 4
#print(combined_tree.left.left.key)  # Output: 1
#print(combined_tree.left.right.key)  # Output: 3
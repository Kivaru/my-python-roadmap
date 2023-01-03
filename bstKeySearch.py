def search(root, key):

    #root is null or key is present at root
    if root is None or root.val == key:
        return root
    #key is greater than the root key
    if root.val < key:
        return search(root.right, key)
    #key is less than the root key
    if root.val > key:
        return search(root.left, key)

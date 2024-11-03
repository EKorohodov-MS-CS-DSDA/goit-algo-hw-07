import random

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def get_min_value_node(root):
    current = root
    while current.left:
        current = current.left
    return current

def get_max_value_node(root):
    current = root
    while current.right:
        current = current.right
    return current

def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = get_min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root

def get_values_sum(root):
    if root is None:
        return 0
    return root.val + get_values_sum(root.left) + get_values_sum(root.right)


def main():
    vals = random.sample(range(1, 100), 10)
    root = None
    for i in vals:
        root = insert(root, i)

    print(f"Tree: {root}")
    print(f"Tree min value: {get_min_value_node(root).val}")
    print(f"Tree max value: {get_max_value_node(root).val}")
    print(f"Tree values sum: {get_values_sum(root)}")

if __name__ == "__main__":
    main()

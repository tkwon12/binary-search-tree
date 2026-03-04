from bst import insert, search, delete

root = None

root = insert(root, 10, 100)
root = insert(root, 5, 50)
root = insert(root, 15, 150)

print(search(root, 15))
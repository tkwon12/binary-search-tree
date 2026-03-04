# Binary Search Tree Implementation

This project implements a Binary Search Tree (BST) in Python.

## Features

- Insert node
- Delete node
- Search for a key
- Find minimum and maximum nodes
- Count nodes in subtrees

## Implementation Details

The tree stores key-value pairs.  
The deletion algorithm selects replacement nodes based on subtree sizes.

## Example

```python
root = insert(root, 10, 100)
root = insert(root, 5, 50)
root = insert(root, 15, 150)

print(search(root, 15))

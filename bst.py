# BST Variation 2

from __future__ import annotations
import json

# The class for a particular node in the tree.
# DO NOT MODIFY!
class Node():
    def  __init__(self,
                  key        : int  = None,
                  value      : int  = None,
                  leftchild  : Node = None,
                  rightchild : Node = None):
        self.key        = key
        self.value      = value
        self.leftchild  = leftchild
        self.rightchild = rightchild

# For the tree rooted at root:
# Return the json.dumps of the list with indent=2.
# DO NOT MODIFY!
def dump(root: Node) -> str:
    def _to_dict(node) -> dict:
        return {
            "key"        : node.key,
            "value"      : node.value,
            "leftchild"  : (_to_dict(node.leftchild) if node.leftchild is not None else None),
            "rightchild" : (_to_dict(node.rightchild) if node.rightchild is not None else None)
        }
    if root == None:
        dict_repr = {}
    else:
        dict_repr = _to_dict(root)
    return json.dumps(dict_repr,indent = 2)

# For the tree rooted at root and the key and value given:
# Insert the key/value pair.
# The key is guaranteed to not be in the tree.
# Follow the variation rules as per the PDF.
def insert(root: Node, key: int, value: int) -> Node:
 
    if root is None:
        return Node(key,value)

    stored_key = root.key
    stored_value = root.value
    

    replace_check = True

    if root.leftchild is not None: 
        max_node = findmaxnode(root.leftchild)
        if key <= max_node.key:
            replace_check = False 
    
    if root.rightchild is not None: 
        min_node = findminnode(root.rightchild)
        if key >= min_node.key:
            replace_check = False 
        
    

    if replace_check == True: 
        root.key = key 
        root.value = value
        if stored_key < key:
           root.leftchild = insert(root.leftchild,stored_key,stored_value)
        else :
            root.rightchild = insert(root.rightchild,stored_key,stored_value)
    
    else:
        if root.key > key:
            root.leftchild = insert(root.leftchild,key,value)     
        else :
            root.rightchild = insert(root.rightchild,key,value)
    



    return root

def findmaxnode(root:Node):
    current = root
    while current.rightchild is not None:
        current = current.rightchild
    return current
    
def findminnode(root:Node):
   current = root
   while current.leftchild is not None:
        current = current.leftchild
   return current 

# For the tree rooted at root and the key given, delete the key.
# Follow the variation rules as per the PDF.
def delete(root: Node, key: int) -> Node:
    # Fill in code.
    if root is None: 
        return root

    if key == root.key:
        if root.leftchild is None:
            root = root.rightchild
        elif root.rightchild is None: 
            root = root.leftchild
        else: 
            num_left = count_node(root.leftchild)
            num_right = count_node(root.rightchild)

            if num_left > num_right:
                max_node = findmaxnode(root.leftchild)
                root.key = max_node.key
                root.value = max_node.value
                root.leftchild = delete(root.leftchild, max_node.key)
            else:
                min_node = findminnode(root.rightchild)
                root.key = min_node.key
                root.value = min_node.value
                root.rightchild = delete(root.rightchild, min_node.key)
    elif key < root.key:
        root.leftchild = delete(root.leftchild, key)
    else:
        root.rightchild = delete(root.rightchild, key)

    return root


def count_node(root:Node):
    if root is None:
        return 0
    else: 
        return 1 + count_node(root.leftchild)+count_node(root.rightchild)

# For the tree rooted at root and the key given:
# Calculate the list of values on the path from the root down to and including the search key node.
# The key is guaranteed to be in the tree.
# Return the json.dumps of the list with indent=2.
def search(root: Node, search_key: int) -> str:
    # Remove the next line and fill in code to construct value_list.
    value_list = []
    current = root
    
    while current is not None:
        value_list.append(current.value)
        if current.key == search_key:
            current = None
        
        elif search_key < current.key:
            current = current.leftchild
        
        else:
            current = current.rightchild
   
    return json.dumps(value_list,indent = 2)
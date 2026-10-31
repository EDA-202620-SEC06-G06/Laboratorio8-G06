from DataStructures.Tree import rbt_node as rn
from DataStructures.List import single_linked_list as sll

def new_map():
    bst = {"root":None}
    return bst

def put(my_rbt,key,value):
    my_rbt["root"] = insert_node(my_rbt["root"],key,value)
    rn.change_color(my_rbt["root"],rn.BLACK)
    return my_rbt

def insert_node (current_node,key,value):
  
    if current_node is None:
        return rn.new_node(key,value, rn.RED)
    cmp = default_compare(key, current_node["key"])
    if cmp < 0:
        current_node["left"] = insert_node(current_node["left"],key,value)
    elif cmp > 0:
        current_node["right"] = insert_node(current_node["right"],key,value)
    else:
        current_node["value"] = value
    
    if is_red(current_node["right"]) and not is_red(current_node["left"]):
        current_node = rotate_left(current_node)
    
    if is_red(current_node["left"]) and is_red(current_node["left"]["left"]):
        current_node = rotate_right(current_node)
        
    current_node["size"] = 1 + size_tree(current_node["left"]) + size_tree(current_node["right"])
    if is_red(current_node["right"]) and is_red(current_node["left"]):
            current_node = flip_colors(current_node)
    return current_node
def is_red(my_node):
    if my_node is None:
        return False
    return rn.is_red(my_node)

def size_tree(current_node):
    if current_node is None:
        return 0
    else:
        size = current_node["size"]
        return size
    
def default_compare(key,key_node):
    if key == key_node:
        return 0
    elif key < key_node:
        return -1
    else:
        return 1
def flip_node_color(my_node):
    if is_red(my_node):
        rn.change_color(my_node,rn.BLACK)
    else:
        rn.change_color(my_node,rn.RED)
def flip_colors(my_node):
    flip_node_color(my_node)
    flip_node_color(my_node["left"])
    flip_node_color(my_node["right"])
    return my_node
def rotate_left(my_node):
    new_node = my_node["right"]
    my_node["right"] = new_node["left"]
    new_node["left"] = my_node
    new_node["color"] = my_node["color"]
    my_node["color"] = rn.RED
    my_node["size"] = size_tree(my_node["left"])+size_tree(my_node["right"])+1
    new_node["size"] = size_tree(new_node["left"])+size_tree(new_node["right"])+1
    return new_node
def rotate_right(my_node):
    new_node = my_node["left"]
    my_node["left"] = new_node["right"]
    new_node["right"] = my_node
    new_node["color"] = my_node["color"]
    my_node["color"] = rn.RED
    my_node["size"] = size_tree(my_node["left"])+size_tree(my_node["right"])+1
    new_node["size"] = size_tree(new_node["left"])+size_tree(new_node["right"])+1
    return new_node
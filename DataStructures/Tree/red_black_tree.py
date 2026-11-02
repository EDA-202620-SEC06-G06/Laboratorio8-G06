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
def get(my_rbt,key):
    value = get_node(my_rbt["root"],key)
    return value
def get_node(root,key):
    
    if root is None:
        return None
    cmp = default_compare(key,root["key"])
    if cmp < 0:
        return get_node(root["left"],key)
    elif cmp > 0 : 
        return get_node(root["right"],key)
    elif cmp == 0:
        return root["value"]
def contains(my_rbt,key):
    if get(my_rbt,key) is None:
        return False
    else:
        return True
def size(my_rbt):
    return size_tree(my_rbt["root"])
def is_empty(my_rbt):
    return size(my_rbt)== 0
def key_set(my_rbt):
    key_list = sll.new_list()
    key_set_tree(my_rbt["root"], key_list)
    return key_list
def key_set_tree(root,key_list):
    if root is not None:
        key_set_tree(root["left"], key_list)
        sll.add_last(key_list, rn.get_key(root))
        key_set_tree(root["right"], key_list)
    return key_list
def value_set(my_rbt):
    value_list = sll.new_list()
    value_set_tree(my_rbt["root"], value_list)
    return value_list   
def value_set_tree(root, value_list):
    if root is not None:
        value_set_tree(root["left"], value_list)
        sll.add_last(value_list, rn.get_value(root))
        value_set_tree(root["right"], value_list)
    return value_list
def get_min(my_rbt):
    return get_min_node(my_rbt["root"])
def get_min_node(root):
    if root is None:
        return None
    if root["left"] is None:
        return root["key"]
    return get_min_node(root["left"])
def get_max(my_rbt):
    return get_max_node(my_rbt["root"])
def get_max_node(root):
    if root is None:
        return None
    if root["right"] is None:
        return root['key']
    return get_max_node(root["right"])
def height(my_rbt):
    return height_tree(my_rbt["root"])
def height_tree(root):
    if root is None:
        return 0
    left_h = height_tree(root["left"])
    right_h = height_tree(root["right"])
    return 1 + max(left_h,right_h)
def keys(my_rbt,key_initial,key_final):
    key_list = sll.new_list()
    keys_range(my_rbt["root"],key_initial,key_final,key_list)
    return key_list
def keys_range(root,key_initial,key_final,key_list):
    if root is not None:
        cmp_low = default_compare(key_initial, root["key"])
        cmp_high = default_compare(key_final, root["key"])
        if cmp_low < 0:
            keys_range(root["left"], key_initial, key_final, key_list)
        if cmp_low <= 0 and cmp_high >= 0:
            sll.add_last(key_list, rn.get_key(root))
        if cmp_high > 0:
            keys_range(root["right"], key_initial, key_final, key_list)
    return key_list
def values(my_rbt,value_initial,value_final):
    value_list = sll.new_list()
    values_range(my_rbt["root"],value_initial,value_final,value_list)
    return value_list
def values_range(root,value_initial,value_final,value_list):
    if root is not None:
        cmp_low = default_compare(value_initial, root["key"])
        cmp_high = default_compare(value_final, root["key"])
        if cmp_low < 0:
            values_range(root["left"], value_initial, value_final, value_list)
        if cmp_low <= 0 and cmp_high >= 0:
            sll.add_last(value_list, rn.get_value(root))
        if cmp_high > 0:
            values_range(root["right"], value_initial, value_final, value_list)
    return value_list
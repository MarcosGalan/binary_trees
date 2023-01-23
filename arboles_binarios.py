# coding: utf-8

"""
Esta practica se encarga de los arboles binarios.

Utiliza un puntero inicial que señala el comienzo del arbol,

El modelo de nodo utilizado es:

Attributes:
    Node(dict):{
        parent: posicion en la lista de elemnto inmediatamente superior.
        value: int
        left_child: posicion en lista del elemento izquierdo.
        right_child: posicion en lista del elemento derecho.
    }

    tree(list): Almacena los nodos en forma de lista
    cache(dict): Almacena los nodos que es posible que se utilicen.

"""

import math

# VARIABLES
pointer = None  # Almacena la posicion del nodo raiz en la lista tree
tree = []
base = {}
cache = {}


def search_node(value, pos, lst, pos_cache):
    if pos is None:
        return None

    node = lst[pos]

    if value in pos_cache:
        return pos_cache[value]
    elif value == node['value']:
        return pos

    if value > node['value']:
        if node['right_child'] is None:
            return None
        return search_node(value, node['right_child'], lst, pos_cache)

    if value < node['value']:
        if node['left_child'] is None:
            return None

        return search_node(value, node['left_child'], lst, pos_cache)


def insert_node(value, pos, lst, pos_cache):
    if pos is None:
        global pointer
        pointer = len(tree)
        lst.append({
            'parent': None,
            'value': value,
            'left_child': None,
            'right_child': None,
        })
        base[value] = len(lst)
        return

    node = lst[pos]

    if value in pos_cache:
        print('EL valor introducido ya esta en el arbol')
        return
    elif value == node['value']:
        print('EL valor introducido ya esta en el arbol')
        return

    if value > node['value']:
        if node['right_child'] is None:
            node['right_child'] = len(lst)
            try:
                base.pop(node['value'])
            except KeyError:
                pass
            base[value] = len(lst)
            lst.append({
                'parent': pos,
                'value': value,
                'left_child': None,
                'right_child': None,
            })

            return
        insert_node(value, node['right_child'], lst, pos_cache)

    if value < node['value']:
        if node['left_child'] is None:
            node['left_child'] = len(lst)
            try:
                base.pop(node['value'])
            except KeyError:
                pass
            base[value] = len(lst)
            base[value] = len(lst)
            lst.append({
                'parent': pos,
                'value': value,
                'left_child': None,
                'right_child': None,
            })
            return

        insert_node(value, node['left_child'], lst, pos_cache)


def is_empty(pos, lst):
    return True if pos is None or (lst[pos]['left_child'] is None and lst[pos]['right_child'] is None) else False


def is_complete(pos, lst):
    return False if pos is None or (lst[pos]['left_child'] is None and lst[pos]['right_child'] is None) else True


def pre_order(pos, lst, pos_cache={}):
    if pos is None:
        return pos_cache

    node = lst[pos]

    pos_cache[pos] = node['value']
    temp_cache = pre_order(node['left_child'], lst, pos_cache)
    return pre_order(node['right_child'], lst, temp_cache)


def post_order(pos, lst, pos_cache={}):
    if pos is None:
        return pos_cache

    node = lst[pos]

    temp_cache = post_order(node['left_child'], lst, pos_cache)
    cached = post_order(node['right_child'], lst, temp_cache)
    cached[pos] = node['value']
    return cached


def in_order(pos, lst, pos_cache={}):
    if pos is None:
        return pos_cache

    node = lst[pos]

    temp_cache = in_order(node['left_child'], lst, pos_cache)
    temp_cache[pos] = node['value']
    return in_order(node['right_child'], lst, temp_cache)


def level_order(pos, lst, pos_cache={}):
    total_height = height(pos, tree)

    for i in range(1, total_height + 1):
        pos_cache.update(return_level(i, pos, tree, {}))

    return pos_cache


def return_level(level, pos, root, lst, level_cache={}):
    if level_cache is None:
        level_cache = {}
    if pos is None:
        return level_cache

    node = lst[pos]

    if level == node_level(pos, root, lst):
        level_cache[pos] = node['value']

    temp_cache = return_level(level, node['left_child'], root, lst, level_cache)
    return return_level(level, node['right_child'], root, lst, temp_cache)


def node_level(value, pos, lst, counter=1):
    if pos is None:
        return None

    node = lst[pos]
    value_node = lst[value]

    if value_node['value'] == node['value']:
        return counter

    if value_node['value'] > node['value']:
        if node['right_child'] is None:
            return None
        return node_level(value, node['right_child'], lst, counter + 1)

    if value_node['value'] < node['value']:
        if node['left_child'] is None:
            return None

        return node_level(value, node['left_child'], lst, counter + 1)


def height(pos, lst):
    if is_empty(pos, lst):
        return 1

    node = lst[pos]

    left_height = height(node['left_child'], lst)
    right_height = height(node['right_child'], lst)

    return (left_height if left_height > right_height else right_height) + 1


def is_full(pos, lst):
    height_val = height(pos, lst)
    level = list(return_level(height_val, pos, pos, tree, cache).values())

    return True if len(level) == math.pow(2, height_val - 1) else False


def reordered_list(lst: list, final_list=[], ballast=None):
    lst.sort()

    if not lst:
        return final_list

    lst.append(ballast) if ballast is not None else None

    if len(lst) % 2 == 0:

        temp_ballast = lst.pop()
        lst.pop()
        return reordered_list(lst, final_list, temp_ballast)

    else:
        final_list.append(lst[int((len(lst) - 1) / 2)])
        lst.pop(int(((len(lst) - 1) / 2)))
        temp_lst = reordered_list(lst[0:int((len(lst)) / 2)], final_list)
        return reordered_list(lst[int((len(lst)) / 2):len(lst)], temp_lst, ballast)


def list_override_inserter(lst):
    global pointer
    pointer = None
    global tree
    tree = []
    global base
    base = {}
    global cache
    cache = {}
    for i in lst:
        insert_node(i, pointer, tree, cache)


def level_printer(level, pos, lst, base):
    nivel = return_level(level, pos, pos, lst)
    lista_lineas = ([], [], [], [], [], [], [], [], [])
    base_len = 24 * len(base)

    margin = (((base_len - (24 * len(nivel))) / len(nivel)) / 2)

    for num in nivel.values():
        lista_lineas[0].append((f'{" ":^{margin}}' + f'                        ' + f'{" ":^{margin}}'))
        lista_lineas[1].append((f'{" ":^{margin}}' + f'                        ' + f'{" ":^{margin}}'))
        lista_lineas[2].append((f'{" ":^{margin}}' + f'         ******         ' + f'{" ":^{margin}}'))
        lista_lineas[3].append((f'{" ":^{margin}}' + f'       *        *       ' + f'{" ":^{margin}}'))
        lista_lineas[4].append((f'{" ":^{margin}}' + f'     *            *     ' + f'{" ":^{margin}}'))
        lista_lineas[5].append((f'{" ":^{margin}}' + f'     *{num:^12}*     ' + f'{" ":^{margin}}'))
        lista_lineas[6].append((f'{" ":^{margin}}' + f'     *            *     ' + f'{" ":^{margin}}'))
        lista_lineas[7].append((f'{" ":^{margin}}' + f'       *        *       ' + f'{" ":^{margin}}'))
        lista_lineas[8].append((f'{" ":^{margin}}' + f'         ******         ' + f'{" ":^{margin}}'))

    for linea in lista_lineas:

        for nodo_texto in linea:
            print(nodo_texto, end='')
        print('')

    nivel.clear()


def tree_printer(pos, lst, base):

    if is_full(pointer,lst):
        tree_height = height(pos, lst)

        for i in range(tree_height):
            level_printer(i + 1, pointer, tree, base)
    else:
        print('Para imprimir el arbol debe estar lleno')


def insert_predeterminado():
    insert_node(30, pointer, tree, cache)
    insert_node(50, pointer, tree, cache)
    insert_node(80, pointer, tree, cache)
    insert_node(15, pointer, tree, cache)
    insert_node(35, pointer, tree, cache)
    insert_node(70, pointer, tree, cache)
    insert_node(85, pointer, tree, cache)
    insert_node(95, pointer, tree, cache)
    insert_node(60, pointer, tree, cache)
    insert_node(90, pointer, tree, cache)
    insert_node(5, pointer, tree, cache)
    insert_node(25, pointer, tree, cache)
    insert_node(33, pointer, tree, cache)
    insert_node(40, pointer, tree, cache)
    insert_node(55, pointer, tree, cache)


insert_predeterminado()

list_override_inserter(reordered_list(list(post_order(pointer,tree).values())))

tree_printer(pointer, tree, base)

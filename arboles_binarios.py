# coding: utf-8
import time

from rich.console import *
from rich import *
from rich.panel import Panel

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


def search_node(value, pos, lst, pos_cache={}):
    '''
    Funcion encargada de buscar nodos

    Args:
        value: valor a buscar
        pos: posicion de inicio del arbol o del punto del arbol donde desea buscar
        lst: lista donde desea buscar
        pos_cache: Cache

    Returns:
        La posicion del nodo o None

    '''


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


def insert_node(value, pos, lst, pos_cache={}):
    '''
    Funcion encargada de insertar un nodo
    Args:
        value: valor a insertar
        pos: poscion del nodo raiz
        lst: arbol a insertar
        pos_cache: cache

    Returns:
        None
    '''

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
    '''
    Funcion encargada de decir si un nodo esta o no vacio
    Args:
        pos: posicion del nodo que se desea comprobar
        lst: arbol sobre el que se va a buscar

    Returns:
        True si esta vacio False si no

    '''
    return True if pos is None or (lst[pos]['left_child'] is None and lst[pos]['right_child'] is None) else False


def is_complete(pos, lst):
    '''
        Funcion encargada de decir si un nodo esta o no lleno
        Args:
            pos: posicion del nodo que se desea comprobar
            lst: arbol sobre el que se va a buscar

        Returns:
            True si esta lleno, False si no

        '''

    return False if pos is None or (lst[pos]['left_child'] is None and lst[pos]['right_child'] is None) else True


def pre_order(pos, lst, pos_cache={}):
    '''
    Recorrido en pre order del arbol

    Args:
        pos: posicion de inicio
        lst: arbol sobre el que buscar
        pos_cache: cache que almacena los datos encontrados

    Returns:
        pos_cache: {position : value}

    '''

    if pos is None:
        return pos_cache

    node = lst[pos]

    pos_cache[pos] = node['value']
    temp_cache = pre_order(node['left_child'], lst, pos_cache)
    return pre_order(node['right_child'], lst, temp_cache)


def post_order(pos, lst, pos_cache={}):
    '''
        Recorrido en post order del arbol

        Args:
            pos: posicion de inicio
            lst: arbol sobre el que buscar
            pos_cache: cache que almacena los datos encontrados

        Returns:
            pos_cache: {position : value}

        '''
    if pos is None:
        return pos_cache

    node = lst[pos]

    temp_cache = post_order(node['left_child'], lst, pos_cache)
    cached = post_order(node['right_child'], lst, temp_cache)
    cached[pos] = node['value']
    return cached


def in_order(pos, lst, pos_cache={}):
    '''
        Recorrido en in order del arbol

        Args:
            pos: posicion de inicio
            lst: arbol sobre el que buscar
            pos_cache: cache que almacena los datos encontrados

        Returns:
            pos_cache: {position : value}

        '''
    if pos is None:
        return pos_cache

    node = lst[pos]

    temp_cache = in_order(node['left_child'], lst, pos_cache)
    temp_cache[pos] = node['value']
    return in_order(node['right_child'], lst, temp_cache)


def level_order(pos, lst, pos_cache={}):
    '''
        Recorrido en level order del arbol

        Args:
            pos: posicion de inicio
            lst: arbol sobre el que buscar
            pos_cache: cache que almacena los datos encontrados

        Returns:
            pos_cache: {position : value}

        '''
    total_height = height(pos, tree)

    for i in range(1, total_height + 1):
        pos_cache.update(return_level(i, pos, tree, {}))

    return pos_cache


def return_level(level, pos, root, lst, level_cache={}):
    '''
    Devuelve un arbol en formato lista
    Args:
        level: nivel devolver
        pos: posicion sobre la que comenzar a buscar
        root: raiz
        lst: arbol sobre el que buscar
        level_cache: cache se deja en blanco

    Returns:
        lista con los valores del nivel

    '''
    if pos is None:
        return level_cache
    print(pos)
    print(lst[pos])
    node = lst[pos]

    if level == node_level(pos, root, lst):
        level_cache[pos] = node['value']

    temp_cache = return_level(level, node['left_child'], root, lst, level_cache)
    return return_level(level, node['right_child'], root, lst, temp_cache)


def node_level(value, pos, lst, counter=1):
    '''
    Devuelve el nivel de un nodo
    Args:
        value: valor a conocer el nive
        pos: nodo raiz
        lst: lista sobre la que buscar
        counter: se establece por defecto en 1

    Returns:

        el nivel del nodo en referencia a pos

    '''

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
    '''
    Devuelve la altura de un arbol
    Args:
        pos: nodo donde comenzar la busqueda
        lst: lista sobre la que analizar el arboñ

    Returns:
        int: altura

    '''

    if is_empty(pos, lst):
        return 1

    node = lst[pos]

    left_height = height(node['left_child'], lst)
    right_height = height(node['right_child'], lst)

    return (left_height if left_height > right_height else right_height) + 1


def is_full(pos, lst):
    '''
    Devuelve si un arbol esta lleno es decir si todo un nivel esta completo
    Args:
        pos: nodo raiz de referencia
        lst: lista sobre la que buscar

    Returns:
        True si esta lleno False si no lo esta

    '''

    height_val = height(pos, lst)
    level = list(return_level(height_val, pos, pos, tree, cache).values())

    return True if len(level) == math.pow(2, height_val - 1) else False


def reordered_list(lst: list, final_list=[], ballast=None):
    '''
    Reordena la lista de la forma mas eficiente posible
    Args:
        lst: lista sobre la que buscar
        final_list: lista a devolver(no se introduce como parametro)
        ballast: carga de numero (no se introduce como parametro)

    Returns:
        final_list: Una lista ordenada

    '''
    if not lst:
        return final_list

    lst.append(ballast) if ballast is not None else None

    if len(lst) % 2 == 0:

        temp_ballast = lst.pop()
        lst.pop()
        return reordered_list(lst, final_list, temp_ballast)

    else:
        final_list.append(lst[int((len(lst) - 1) / 2)]) if lst[int((len(lst) - 1) / 2)] not in final_list else None
        lst.pop(int(((len(lst) - 1) / 2)))
        temp_lst = reordered_list(lst[0:int((len(lst)) / 2)], final_list)
        return reordered_list(lst[int((len(lst)) / 2):len(lst)], temp_lst, ballast)


def list_override_inserter(lst):

    '''
    Sobre escrible las variables globales
    Args:
        lst: lista nueva

    Returns:
        None

    '''
    global pointer, tree, base, cache
    pointer = None
    tree = []
    base = {}
    cache = {}

    for i in lst:
        insert_node(i, pointer, tree, cache)


def return_level_printer(level, pos, root, lst, level_cache=[]):
    '''
        Al igual que la funcion primitiva pero devolviendo los valores vacios en la lista

    '''

    if pos is None:
        return level_cache

    node = lst[pos]

    if pos == root and level == node_level(pos, root, tree):
        level_cache.append(node['value'])
        return level_cache

    if level - 1 == node_level(pos, root, lst):
        level_cache.append(lst[node['left_child']]['value']) if node['left_child'] is not None else level_cache.append(
            None)
        level_cache.append(lst[node['right_child']]['value']) if node[
                                                                     'right_child'] is not None else level_cache.append(
            None)
        return level_cache

    if is_empty(pos, lst) and height(pos, lst) is not height(root, lst) - 1:
        for i in range(int(math.pow(2, height(pos, tree)))):
            level_cache.append(None)

    temp_cache = return_level_printer(level, node['left_child'], root, lst, level_cache)
    return return_level_printer(level, node['right_child'], root, lst, temp_cache)


def level_printer(level, pos, lst, base):
    '''
    Funcion encargada de imprimir un nivel
    Args:
        level: Nivel a introducir
        pos: Posicion de raiz a comeienzo de busqueda
        lst: lista de busqueda
        base: diccionario con los valores de la base

    Returns:
        None

    '''

    nivel = return_level_printer(level, pos, pos, lst)
    lista_lineas = ([], [])
    base_len = 4 * len(return_level_printer(height(pos, lst), pos, pos, lst, []))
    margin = (((base_len - (4 * len(nivel))) / len(nivel)) / 2)
    bar = '\\'
    for num in nivel:

        if num is not None:
            lista_lineas[0].append((f'{" ":^{margin}}' + f'{num:^4}' + f'{" ":^{margin}}'))
            lista_lineas[1].append((f'{" ":^{margin}}' + f'{"/":<2}{bar:>2}' + f'{" ":^{margin}}'))
        else:
            lista_lineas[0].append((f'{" ":^{margin}}' + f'    ' + f'{" ":^{margin}}'))
            lista_lineas[1].append((f'{" ":^{margin}}' + f'    ' + f'{" ":^{margin}}'))

    for linea in lista_lineas:

        for nodo_texto in linea:
            print(nodo_texto, end='')
        print('')

    nivel.clear()


def tree_printer(pos, lst, base):

    '''
    Funcion encargada de llamar a la funcion de level printer una vez por cada nivel existente
    Args:
        pos: poscion de la raiz
        lst: lista que contiene el arbol
        base: valores de la base en forma de diccionario

    Returns:
        None
    '''

    tree_height = height(pos, lst)

    for i in range(tree_height):
        level_printer(i + 1, pointer, tree, base)


def menu():

    '''Funcion encargada de hacer un menu visual'''

    panel = Panel("""
[blue]1-[/blue] [bold]Insertar Nodo[/bold]              [blue]6-[/blue] [bold]Esta lleno Nodo[/bold]
[blue]2-[/blue] [bold]Borrar Nodo[/bold]                [blue]7-[/blue] [bold]Esta completo Nodo[/bold]
[blue]3-[/blue] [bold]Buscar Nodo[/bold]                [blue]8-[/blue] [bold]Recorrido Pre Order[/bold]
[blue]4-[/blue] [bold]Altura Nodo[/bold]                [blue]9-[/blue] [bold]Recorrido Post Order[/bold]
[blue]5-[/blue] [bold]Esta vacio Nodo[/bold]            [blue]10-[/blue] [bold]Recorrido In Order[/bold]
                            
        """, title="[green]Menu[/green]", subtitle='[red]Para salir pulse E', width=60, )
    while True:
        if tree:
            tree_printer(pointer, tree, base)
        else:
            pass
        print(panel)
        option = str(input('Introduzca la opcion que desea realizar: '))
        if option == "E":
            return
        elif option == '1':
            try:
                value = int(input('Introduzca el valor que desea introducir: '))

                insert_node(value, pointer, tree)


            except ValueError:
                print('Formato no valido')
        elif option == '2':
            try:
                value = int(input('Introduzca el valor que desea eliminar: '))

                lista = reordered_list(list(post_order(pointer, tree).values()))
                if value in lista:

                    for pos, val in enumerate(lista):
                        if val == value:
                            lista.pop(pos)
                else:
                    print('Valor no existente en la lista')

                list_override_inserter(lista)

            except ValueError:
                print('Formato no valido')
        elif option == '3':

            try:
                value = int(input('Introduzca el valor que desea buscar: '))

                value_pos = search_node(value, pointer, tree, cache)

                if value_pos == None:
                    print('Nodo no existente')
                else:
                    nodo = dict(tree[value_pos])

                    try:
                        print(f"padre ->{dict(tree[nodo['parent']])['value']}")
                    except TypeError or ValueError:
                        print('padre ->None')

                    print(f" valor ->{nodo['value']}")

                    try:
                        print(f"hijo_izq ->{dict(tree[nodo['parent']])['value']}")
                    except TypeError or ValueError:
                        print('padre ->None')

                    try:
                        print(f"hijo_dcha ->{dict(tree[nodo['right_child']])['value']}")
                    except TypeError or ValueError:
                        print('padre ->None')

            except ValueError:
                print('Formato no valido')
        elif option == '4':
            try:
                value = int(input('Introduzca el valor que desea conocer su altura: '))

                value_pos = search_node(value, pointer, tree, cache)

                if value_pos is None:
                    print('Nodo no existente')
                else:

                    print(f'La altura es {height(value_pos, tree)}')



            except ValueError:
                print('Formato no valido')
        elif option == '5':
            try:
                value = int(input('Introduzca el valor del nodo que desea saber si esta vacio: '))

                value_pos = search_node(value, pointer, tree, cache)

                if value_pos is None:
                    print('Nodo no existente')
                else:

                    print(f'El nodo {value} esta vacio:  {is_empty(value_pos,tree)}')

            except ValueError:
                print('Formato no valido')
        elif option == '6':
            try:
                value = int(input('Introduzca el valor del nodo que desea saber si esta vacio: '))

                value_pos = search_node(value, pointer, tree, cache)

                if value_pos is None:
                    print('Nodo no existente')
                else:

                    print(f'El nodo {value} esta lleno:  {is_full(value_pos, tree)}')

            except ValueError:
                print('Formato no valido')
        elif option == '7':
            try:
                value = int(input('Introduzca el valor del nodo que desea saber si esta vacio: '))

                value_pos = search_node(value, pointer, tree, cache)

                if value_pos is None:
                    print('Nodo no existente')
                else:

                    print(f'El nodo {value} esta completo:  {is_complete(value_pos, tree)}')

            except ValueError:
                print('Formato no valido')
        elif option == '8':
            print(list(pre_order(pointer, tree).values()))
        elif option == '9':
            print(list(post_order(pointer, tree).values()))
        elif option == '10':
            print(list(in_order(pointer, tree).values()))
        time.sleep(2)
        os.system('clear')


menu()



    
### Function `height` {#id}




>     def height(
>         pos,
>         lst
>     )


Devuelve la altura de un arbol

Args
-----=
**```pos```**
:   nodo donde comenzar la busqueda


**```lst```**
:   lista sobre la que analizar el arboñ



Returns
-----=
<code>int</code>
:   altura



    
### Function `in_order` {#id}




>     def in_order(
>         pos,
>         lst,
>         pos_cache={}
>     )


Recorrido en in order del arbol


Args
-----=
**```pos```**
:   posicion de inicio


**```lst```**
:   arbol sobre el que buscar


**```pos_cache```**
:   cache que almacena los datos encontrados



Returns
-----=
<code>pos\_cache</code>
:   {position : value}



    
### Function `insert_node` {#id}




>     def insert_node(
>         value,
>         pos,
>         lst,
>         pos_cache={}
>     )


Funcion encargada de insertar un nodo

Args
-----=
**```value```**
:   valor a insertar


**```pos```**
:   poscion del nodo raiz


**```lst```**
:   arbol a insertar


**```pos_cache```**
:   cache



Returns
-----=
None

    
### Function `is_complete` {#id}




>     def is_complete(
>         pos,
>         lst
>     )


Funcion encargada de decir si un nodo esta o no lleno

Args
-----=
**```pos```**
:   posicion del nodo que se desea comprobar


**```lst```**
:   arbol sobre el que se va a buscar



Returns
-----=
True si esta lleno, False si no

    
### Function `is_empty` {#id}




>     def is_empty(
>         pos,
>         lst
>     )


Funcion encargada de decir si un nodo esta o no vacio

Args
-----=
**```pos```**
:   posicion del nodo que se desea comprobar


**```lst```**
:   arbol sobre el que se va a buscar



Returns
-----=
True si esta vacio False si no

    
### Function `is_full` {#id}




>     def is_full(
>         pos,
>         lst
>     )


Devuelve si un arbol esta lleno es decir si todo un nivel esta completo

Args
-----=
**```pos```**
:   nodo raiz de referencia


**```lst```**
:   lista sobre la que buscar



Returns
-----=
True si esta lleno False si no lo esta

    
### Function `level_order` {#id}




>     def level_order(
>         pos,
>         lst,
>         pos_cache={}
>     )


Recorrido en level order del arbol


Args
-----=
**```pos```**
:   posicion de inicio


**```lst```**
:   arbol sobre el que buscar


**```pos_cache```**
:   cache que almacena los datos encontrados



Returns
-----=
<code>pos\_cache</code>
:   {position : value}



    
### Function `level_printer` {#id}




>     def level_printer(
>         level,
>         pos,
>         lst,
>         base
>     )


Funcion encargada de imprimir un nivel

Args
-----=
**```level```**
:   Nivel a introducir


**```pos```**
:   Posicion de raiz a comeienzo de busqueda


**```lst```**
:   lista de busqueda


**```base```**
:   diccionario con los valores de la base



Returns
-----=
None

    
### Function `list_override_inserter` {#id}




>     def list_override_inserter(
>         lst
>     )


Sobre escrible las variables globales

Args
-----=
**```lst```**
:   lista nueva



Returns
-----=
None

    
### Function `menu` {#id}




>     def menu()


Funcion encargada de hacer un menu visual

    
### Function `node_level` {#id}




>     def node_level(
>         value,
>         pos,
>         lst,
>         counter=1
>     )


Devuelve el nivel de un nodo

Args
-----=
**```value```**
:   valor a conocer el nive


**```pos```**
:   nodo raiz


**```lst```**
:   lista sobre la que buscar


**```counter```**
:   se establece por defecto en 1



Returns
-----=
el nivel del nodo en referencia a pos

    
### Function `post_order` {#id}




>     def post_order(
>         pos,
>         lst,
>         pos_cache={}
>     )


Recorrido en post order del arbol


Args
-----=
**```pos```**
:   posicion de inicio


**```lst```**
:   arbol sobre el que buscar


**```pos_cache```**
:   cache que almacena los datos encontrados



Returns
-----=
<code>pos\_cache</code>
:   {position : value}



    
### Function `pre_order` {#id}




>     def pre_order(
>         pos,
>         lst,
>         pos_cache={}
>     )


Recorrido en pre order del arbol


Args
-----=
**```pos```**
:   posicion de inicio


**```lst```**
:   arbol sobre el que buscar


**```pos_cache```**
:   cache que almacena los datos encontrados



Returns
-----=
<code>pos\_cache</code>
:   {position : value}



    
### Function `reordered_list` {#id}




>     def reordered_list(
>         lst: list,
>         final_list=[],
>         ballast=None
>     )


Reordena la lista de la forma mas eficiente posible

Args
-----=
**```lst```**
:   lista sobre la que buscar


**```final_list```**
:   lista a devolver(no se introduce como parametro)


**```ballast```**
:   carga de numero (no se introduce como parametro)



Returns
-----=
<code>final\_list</code>
:   Una lista ordenada



    
### Function `return_level` {#id}




>     def return_level(
>         level,
>         pos,
>         root,
>         lst,
>         level_cache={}
>     )


Devuelve un arbol en formato lista

Args
-----=
**```level```**
:   nivel devolver


**```pos```**
:   posicion sobre la que comenzar a buscar


**```root```**
:   raiz


**```lst```**
:   arbol sobre el que buscar


**```level_cache```**
:   cache se deja en blanco



Returns
-----=
lista con los valores del nivel

    
### Function `return_level_printer` {#id}




>     def return_level_printer(
>         level,
>         pos,
>         root,
>         lst,
>         level_cache=[]
>     )


Al igual que la funcion primitiva pero devolviendo los valores vacios en la lista

    
### Function `search_node` {#id}




>     def search_node(
>         value,
>         pos,
>         lst,
>         pos_cache={}
>     )


Funcion encargada de buscar nodos


Args
-----=
**```value```**
:   valor a buscar


**```pos```**
:   posicion de inicio del arbol o del punto del arbol donde desea buscar


**```lst```**
:   lista donde desea buscar


**```pos_cache```**
:   Cache



Returns
-----=
La posicion del nodo o None

    
### Function `tree_printer` {#id}




>     def tree_printer(
>         pos,
>         lst,
>         base
>     )


Funcion encargada de llamar a la funcion de level printer una vez por cada nivel existente

Args
-----=
**```pos```**
:   poscion de la raiz


**```lst```**
:   lista que contiene el arbol


**```base```**
:   valores de la base en forma de diccionario



Returns
-----=
None



-----

# backend/utils.py


def binary_search(lista, target):
    """
    Realiza busca binária em uma lista ordenada.
    Retorna o índice do elemento se encontrado, ou -1 caso contrário.
    """
    left = 0
    right = len(lista) - 1

    while left <= right:
        mid = (left + right) // 2
        if lista[mid] == target:
            return mid
        elif lista[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_tuples(lista, target_key):
    """
    Realiza busca binária em uma lista ordenada de tuplas.
    Compara apenas o índice [0] de cada tupla com o target_key.
    Retorna o índice na lista se encontrado, ou -1 caso contrário.

    Exemplo:
        lista = [("bala", 5), ("fps", 12), ("tiro", 2)]
        binary_search_tuples(lista, "fps") -> 1
    """
    left = 0
    right = len(lista) - 1

    while left <= right:
        mid = (left + right) // 2
        if lista[mid][0] == target_key:
            return mid
        elif lista[mid][0] < target_key:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def sorted_insert_tuple(lista, item):
    """
    Insere um item (tupla) em uma lista mantendo-a ordenada pelo índice [0].
    Usa busca binária para encontrar a posição correta — O(log N) busca, O(N) inserção.

    Exemplo:
        lista = [("bala", 0), ("tiro", 2)]
        sorted_insert_tuple(lista, ("fps", 1))
        # lista -> [("bala", 0), ("fps", 1), ("tiro", 2)]
    """
    left = 0
    right = len(lista) - 1
    pos = len(lista)  # posição padrão: final da lista

    while left <= right:
        mid = (left + right) // 2
        if lista[mid][0] < item[0]:
            left = mid + 1
        else:
            pos = mid
            right = mid - 1

    lista.insert(pos, item)
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

def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim =  len(lista) - 1
    if inicio < fim:
        pivot = partition(lista, inicio, fim)
        quicksort(lista, inicio, pivot-1)
        quicksort(lista, pivot+1, fim)

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

def arrayMedian(listaOrdenada) -> float:
    medianTerm = len(listaOrdenada) // 2
    if len(listaOrdenada) % 2 == 0:
        return float((listaOrdenada[medianTerm] + listaOrdenada[medianTerm-1]) / 2)
    else:
        return float(listaOrdenada[medianTerm])

def findMedianSortedArrays(lista1, lista2):
    fullLista = lista1 + lista2
    quicksort(fullLista)
    return arrayMedian(fullLista)

nums1 = [1,2]
nums2 = [3,4]

print(findMedianSortedArrays(nums1, nums2))


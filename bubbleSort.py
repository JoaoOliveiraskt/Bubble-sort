
def bubble_sort(lista):
    n = len(lista)
    for i in range(n -1):
        for j in range (n - i -1):
            if (lista[j] > lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista =[6, 4, 9, 7, 8, 2, 1, 3, 5, 0]

print(f"A lista não ordenada é: {lista}")
print(f"A lista ordenada é: {bubble_sort(lista)}")
def wyswietl_co_drugi(lista_liczb):
    for i in range(0, len(lista_liczb), 2):
        print(lista_liczb[i])


# przykład użycia:
liczby = list(range(10))
wyswietl_co_drugi(liczby)

def wyswietl_parzyste(lista_liczb):
    for liczba in lista_liczb:
        if liczba % 2 == 0:
            print(liczba)


# przykład użycia:
liczby = list(range(10))   # 0,1,2,3,4,5,6,7,8,9
wyswietl_parzyste(liczby)
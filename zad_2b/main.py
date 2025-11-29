#wersja 1
def pomnoz_przez_dwa_for(lista_liczb):
    wynik = []
    for liczba in lista_liczb:
        wynik.append(liczba * 2)
    return wynik


# przykład użycia
liczby = [1, 2, 3, 4, 5]
print(pomnoz_przez_dwa_for(liczby))


#wersja 2
def pomnoz_przez_dwa_comprehension(lista_liczb):
    return [liczba * 2 for liczba in lista_liczb]


# przykład użycia
liczby = [1, 2, 3, 4, 5]
print(pomnoz_przez_dwa_comprehension(liczby))
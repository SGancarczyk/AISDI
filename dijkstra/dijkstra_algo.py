import sys
import heapq
from typing import List, Tuple


def wczytaj_plansze(nazwa_pliku: str) -> List[str]:
    with open(nazwa_pliku) as f:
        plansza = [list(line.strip()) for line in f if line.strip()]
    return plansza


def znajdz_litery_X(plansza: List[str]) -> Tuple[int, int]:
    X = []
    for i, wiersz in enumerate(plansza):
        for j, znak in enumerate(wiersz):
            if znak == 'X':
                X.append((i, j))
    return X[0], X[1]       # zwraca dwa pola poczatku i celu


def koszt_wejscia(z: Tuple[int, int], na: Tuple[int, int], plansza: List[str]) -> int:
    if plansza[na[0]][na[1]] == 'X':
        return 0
    if plansza[z[0]][z[1]] == 'J':
        return 0
    if plansza[na[0]][na[1]] == 'J':
        return 0
    return int(plansza[na[0]][na[1]])  


def sasiedzi(x: int, y: int, wysokosc: int, szerokosc: int):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < wysokosc and 0 <= ny < szerokosc:
            yield nx, ny        # returnuje po kolei sasiadow pola


def dijkstra(plansza: List[str], start: Tuple[int, int], cel: Tuple[int, int]):
    wysokosc = len(plansza)
    szerokosc = len(plansza[0])
    koszty = {start: 0}     # Słownik z kosztami dla kazdego z pol
    kolejka = [(0, start)]      # kolejka z przetwarzanymi po kolei polaczeniami, incjujemy ja wartoscia 0 i polem startowym
    poprzednik = {}     # Lista poprzednikow dla każdego z pól na planszy

    while kolejka:
        koszt, (x, y) = heapq.heappop(kolejka)

        if (x, y) == cel:
            break

        for nx, ny in sasiedzi(x, y, wysokosc, szerokosc):
            nowy_koszt = koszt + koszt_wejscia((x, y), (nx, ny), plansza)
            if (nx, ny) not in koszty or nowy_koszt < koszty[(nx, ny)]:
                koszty[(nx, ny)] = nowy_koszt
                poprzednik[(nx, ny)] = (x, y)
                heapq.heappush(kolejka, (nowy_koszt, (nx, ny)))

    # Odtworzenie ścieżki
    sciezka = []
    komorka = cel
    while komorka != start:
        sciezka.append(komorka)
        komorka = poprzednik.get(komorka)
    sciezka.append(start)
    return sciezka, koszty[cel]


def wypisz_trase(plansza: List[str], sciezka: List[Tuple[int, int]]) -> None:
    for i, wiersz in enumerate(plansza):
        linia = []
        for j, znak in enumerate(wiersz):
            linia.append((znak if (i, j) in sciezka else ' '))
        linia = ''.join(linia)
        print(linia)


def main():
    if len(sys.argv) != 2:
        print("Bledna ilosc argumentow")
        return

    nazwa_pliku = sys.argv[1]
    plansza = wczytaj_plansze(nazwa_pliku)
    start, cel = znajdz_litery_X(plansza)
    sciezka, koszt = dijkstra(plansza, start, cel)
    wypisz_trase(plansza, sciezka)
    print(f"\nKoszt: {koszt}")


if __name__ == "__main__":
    main()

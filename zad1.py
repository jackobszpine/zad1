magazyn = ("łódź", 'gniezno', 'katowice', 'leszno')
sklep = ('bydgoszcz', 'czestochowa', 'krakow', 'poznan', 'radom', 'warszawa', 'wroclaw')
macierz_1 = [
    [magazyn[0], magazyn[1], magazyn[2], magazyn[3]],
    [sklep[0], sklep[1], sklep[2], sklep[3], sklep[4], sklep[5], sklep[6]]
]
macierz_2 = [
    [230,   127,    286,    214,164,    138,    200],
    [81,	320,	473,	60,	336,	293,	232],
    [411,	82	,83,	384,	236,	295,	196],
    [209,	282,	377,	79,	433,	381,	100]
]
def wypisanie():
    for x in macierz_1[0][0:]:
        for y in macierz_1[1][0:]:
            print(f'{x} {y}')


def siema():
    for i in range(len(magazyn)):
        for j in range(len(sklep)):
            print(f'{magazyn[i]} {sklep[j]} {macierz_2[i][j]}')


zmienna = [magazyn[0] for _ in range(len(macierz_2[0]))]
result = macierz_2[0]
for col in range(len(macierz_2[0])):
    for row in range(len(macierz_2)):
        if  macierz_2[row][col] < result[col]:
            result[col] = macierz_2[row][col]
            zmienna[col] = magazyn[row]



for koszt, m, s in (zip(result, zmienna, sklep)):
    print(f'{koszt} {m} {s}')
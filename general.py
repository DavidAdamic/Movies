#SPLOŠNA PYTHON DATOTEKA, KI BO VSEBOVALA SPLOŠNO FUNKCIJO
#DODATNE DATOTEKE, KI SO POTREBNE ZA IZVAJANJE PROGRAMA DOBO PRILOŽENE LOČENO
#functions VSEBUJE VSE FUNKCIJE, UPORABLJENE V TEM PROJEKTU

from functions import *

#KORAK 1 - uporabnik vnese svoje tri najljubše filme
#aplikacija uporablja spletno stran http://www.omdbapi.com/, ki pa potrebuje ključ - uporabnik naj si pridobi svoj ključ
api_key = '8429793f'

resp = input('Ali želite sproti videvati podatke o vaših izbranih filmih? (odgovorite z DA ali NE) ')

data1 = None
while data1 is None:
    try:
        movie1 = input('Vnesite točen naslov (v angleščini) vašega prvega najljubšega filma: ')
        data1 = get_data(movie1)
    except:
        print('Vašega filma ne moremo najti! Prosimo preverite črkovanje ali pa vnesite drug film')
        pass
if resp == 'DA':
    print(present_data(data1))

data2 = None
while data2 is None:
    try:
        movie2 = input('Vnesite točen naslov (v angleščini) vašega drugega najljubšega filma: ')
        data2 = get_data(movie2)
    except:
        print('Vašega filma ne moremo najti! Prosimo preverite črkovanje ali pa vnesite drug film')
        pass
if resp == 'DA':
    print(present_data(data2))

data3 = None
while data3 is None:
    try:
        movie3 = input('Vnesite točen naslov (v angleščini) vašega tretjega najljubšega filma: ')
        data3 = get_data(movie3)
    except:
        print('Vašega filma ne moremo najti! Prosimo preverite črkovanje ali pa vnesite drug film')
        pass
if resp == 'DA':
    print(present_data(data3))

combined = combine_data(data1, data2, data3)

print('Prosimo, počakajte!')

#KORAK 2
#iz strani top 200 filmov iz leta 2018 preberemo naslove in njihove podatke

url = 'https://editorial.rottentomatoes.com/guide/best-movies-of-2018/'
titles = get_titles(url)

#glede na dane kriterije pregledamo vse dobljene filme in jih ustrezno točkujemo
points = {}
for item in titles:
    if item in combined[0]:
        pass #uporabnik je vnesel film, ki je na seznamu
    else:
        try:
            info = get_data(item) #če filma slučajno ni v podatkovni bazi OMDb
            a = compare(info, combined)
            points[item] = a
        except:
            pass

#KORAK 4
#izpišemo 3 najbolj primerne filme (glede na število točk, ki jih dobi pri preverjanju kriterijev)
import operator

points_sorted = sorted(points.items(), key = operator.itemgetter(1)) #postane list tuplov
print(present_data(get_data(points_sorted[-3][0])))
print(present_data(get_data(points_sorted[-2][0])))
print(present_data(get_data(points_sorted[-1][0])))
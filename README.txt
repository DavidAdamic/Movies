NAMEN PROGRAMA:
Program predlaga 3 filme izdane leta 2018 na podlagi treh filmov, ki jih vnese uporabnik.

OMDB API KLJUC:
Uporabnik naj si priskrbi OMDb API kluc (http://www.omdbapi.com/),
saj ga program uporablja za pridobivanje podatkov iz internetne strani OMDb API.

NAVODILA ZA UPORABO:
Uporabniku je na zacetku ponudena moznost ali naj se mu pri vpisovanju fimskih naslovov izpisejo njegovi podatki. 
Uporabnik naj odgovori z DA ali NE!

Uporabnik mora nato vnesti 3 naslove svojih (najljubsih) filmov. S pomocjo pomozne funkcije get_data, bo program pridobil vse potrebne 
podatke o danem filmu iz strani OMDb API - poln naslov, datum izida, dolzina (v minutah), zanri, reziserje, pisce, 
igralsko zasedbo, producente in kratek opis zgodbe.
V primeru, ce je uporabnik v prejsnjem koraku odgovoril z DA, bo program te podatke tudi pregledno izpisal.

Ko program prejme 3 veljavne naslove bo te podatke skombiniral z uporabo funkcije combine_data.

Sledi pridobivanje naslovov s strani 202 najboljsa filma izdana v letu 2018 - 
https://editorial.rottentomatoes.com/guide/best-movies-of-2018/

Program nato s uporabo funkcije compare primerja posamezen film iz leta 2018 s kombinacijo podatkov treh danih filmov.
Kriteriji za primerjanje filmov:
- povprecna dolzina danih treh filmov +-5 min -> 5 tock
- ujemanje zanrov (upostevamo pogostost zanrov) -> (pogostost zanra)**2 tock
(ce se zanr ACTION pojavi v vseh treh filmih, bo torej dobil film, ki ima action v spisku zanrov dobil 9 tock.
ce se zanr ANIMATED pojavi samo v enem izmed treh filmov, bo torej film, ki ima animated v spisku zanrov dobil 1 tocko)
- ujemanje režiserjev -> 10 tock
- ujemanje piscev -> 6 tock
- ujemanje igralcev -> 10 tock
- ujemanje produkcije -> 5 tock

Program ustvari slovar oblike NASLOV : ST. TOCK. Slovar uredimo po velikosti vrednosti in izpisemo podatke zadnjih treh filmov.

SKUPINA:
David Adamic, Emina Susman
April 2019
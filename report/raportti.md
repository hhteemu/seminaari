# Koneoppiminen Pythonilla ja Ford-merkkisten autojen hintojen arviointi

## Linkki videoon
https://haagahelia-my.sharepoint.com/personal/bgx196_myy_haaga-helia_fi/_layouts/15/stream.aspx?id=%2Fpersonal%2Fbgx196%5Fmyy%5Fhaaga%2Dhelia%5Ffi%2FDocuments%2FRecording%2D20231203%5F214251%2Ewebm&nav=%7B%22defaultNavPanel%22%3A%7B%22pluginName%22%3A%22MediaSettingsLayer%22%7D%7D&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview

## Johdanto
Seminaarityöni tarkoituksena oli tutustua koneoppimiseen Pythonin avulla ilman erityistä ongelmaa, jota olisin pyrkinyt ratkaisemaan. Selailin internettiä ja etsin erilaista dataa, jota voisin hyödyntää projektissani. Löysin ilmaista dataa lähes kaikesta, ja se sai pääni täyteen ideoita siitä, mitä koneoppimisella voisi tehdä. Aluksi aloin opettelemaan koneoppimista osakkeiden hinnoista kertovan datan kanssa, mutta siitä alkoi tulla todella monimutkaista, joten päätin etsiä hieman erilaista dataa. Löysin pian paljon erilaista dataa autojen hintatiedoista, ja päätin hyödyntää niitä tutkiessani koneoppimista. Aluksi tutkin yleisesti autojen hintatietoja ja niiden suhdetta eri ominaisuuksiin, mikä auttoi minua hahmottamaan koneoppimisen perusteet. Lopulta päädyin keskittymään ainoastaan Ford-automerkin hintoihin, sillä isäni on suuri Ford-mies, joten pidin ajatusta hieman hauskana. Loppujen loppuksi minulle kävi selväksi, että tämä löytämäni data juuri vain Ford-automerkin hinnoista oli loistava valinta projektiini. Sen avulla pystyin kirjoittamaan simppelin skriptin ja luomaan simppelin mallin, jolla pääsin tutustumaan koneoppimiseen.

## Toimenpiteet ja Oppiminen
1. Datan hankinta ja esikäsittely: Hankin Ford-autojen hintadataa ja käytin sitä opiskeluni perustana. Käytin pandas-kirjastoa datan käsittelyyn ja hyödynsin One-Hot Encoding -menetelmää kategoristen muuttujien käsittelyssä.

1. Koneoppimismallin luominen: Valmistin datan mallin koulutusta varten ja käytin päätöspuurekonstruktoria (DecisionTreeRegressor) ennustemallin rakentamiseksi. Jaoin datan koulutus- ja testisetteihin, koulutin mallin ja ennustin testidataa.

1. Tekemäni havainnot: Yllättävää oli, että perusmallin luominen koneoppimiseen ei ollutkaan niin monimutkaista kuin olin alun perin ajatellut. Pystyin kehittämään toimivan skriptin ennustamaan Ford-auton hintoja ilman suuria ongelmia.

## Koodin Tekninen Tarkastelu
Käytin Pythonia toteuttamaan koneoppimismallin ja sen visualisoinnin. Tässä lyhyt katsaus käyttämääni koodiin:

### Datan esikäsittely
1. **Datan lukeminen:**
    Aluksi käytetään pd.read_csv()-funktiota Pandas-kirjastosta datan lukemiseen tiedostosta. Tässä tapauksessa käytettiin ford.csv-tiedostoa, joka sisältää Ford-autojen hintadataa.

1. **Kategoristen sarakkeiden käsittely One-Hot Encoding -tekniikalla:**
Datan kategoriset sarakkeet, kuten auton malli (model), vaihteisto (transmission) ja polttoainetyyppi (fuelType), käsiteltiin One-Hot Encoding -tekniikalla. Tämä tarkoittaa, että kategoriset muuttujat muutettiin numeerisiksi dummy-muuttujiksi, jotka ovat ymmärrettäviä koneoppimismalleille. pd.get_dummies()-funktiota käytettiin tässä yhteydessä.

1. **Datan jakaminen koulutus- ja testidataksi:**
Valmisteltu data jaettiin kahteen erilliseen osaan: koulutusdataan ja testidataan. Tämä tehtiin käyttäen train_test_split()-funktiota sklearn.model_selection-kirjastosta. Tyypillisesti noin 80% datasta varataan koulutukseen ja loput 20% testaukseen. Näin varmistetaan, että malli koulutetaan riittävällä datamäärällä ja testataan sen suorituskykyä ennalta näkemättömällä datalla.

### Mallin luominen
1. **Mallin valmistelu:**
Ennen mallin luomista datalle tehtiin edellä mainitut esikäsittelyvaiheet.

1. **Mallin valinta ja koulutus:**
Päätöspuurekonstruktoria käytettiin tässä skriptissä (DecisionTreeRegressor). fit()-metodia käytettiin kouluttamaan mallia X_train- ja y_train-datalla. Malli oppii koulutusdatan piirteistä ja niitä vastaavista tavoitemuuttujista löytääkseen optimaaliset säännöt ennusteiden tekemiseen.

### Mallin arvioiminen
1. **Ennusteiden tekeminen:**
predict()-metodia käytettiin ennusteiden tekemiseen testidatalla. Koulutetun mallin avulla ennustettiin testidatan piirteiden perusteella hinnat (y_test) ja näitä ennusteita vertailtiin todellisten hintojen kanssa.

1. **Mallin suorituskyvyn arviointi:**
Usein käytetään erilaisia suorituskyvyn mittareita mallin arvioimiseen, kuten tarkkuus (accuracy) luokittelumalleissa tai score()-metodia regressiomalleissa. Tässä tapauksessa score()-metodia käytettiin regressiomallin suorituskyvyn arviointiin testidatalla. Mallissani score()-metodi antaa R^2 arvon, joka kertoo, kuinka hyvin malli sopii testidatan havaintoihin. R^2 on arvo välillä 0 ja 1, ja se mittaa sitä, kuinka suuri osa vastemuuttujan vaihtelusta voidaan selittää mallin avulla. Korkea R^2-arvo (lähellä 1), viittaa siihen, että malli selittää suuren osan vastemuuttujan vaihtelusta ja antaa hyviä ennusteita testidataan. Minun mallini R^2 arvo oli 1.0. Mallin suorituskyvyn arviointi on keskeinen vaihe koneoppimisprosessissa. Sen avulla voidaan arvioida mallin kykyä tehdä oikeita ennusteita uusilla, ennalta näkemättömillä datapistemuodoilla.

1. **Visualisoinnit:**
Koodissa on myös visualisointeja, jotka ovat kommentoituina pois. Ne voi ottaa käyttöön halutessaan.

## Päätelmä
Kokonaisuudessaan tämä projekti auttoi minua ymmärtämään paremmin koneoppimisen perusteet. Koneoppimismallin luominen ja sen soveltaminen auton hintojen arviointiin oli opettavaista. Ymmärrän myös paljon paremmin sitä, mihin kaikkeen koneoppimista voi käyttää. Tämä projekti opetti minulle myös paljon datasta, ja sen käsittelemisestä. Minulla oli myös tarkoituksena luoda graafinen käyttöliittymä, jolla luomaani koneoppimismallia olisi voinut kokeilla käytännössä. En kuitenkaan saanut sitä toimimaan, joten se on toistaiseksi TODO-listalla.


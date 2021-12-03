# posti.py
Hakee viimeisimmän tapahtuman Postin seurantakoodilla. Koodeja voi olla myös useampi peräkkäin.

Testattu Python3 versiolla 3.9.1

Käyttö:
```
usage: posti.py [-h] [-l] koodi [koodi ...]

positional arguments:
  koodi        seurantakoodi

optional arguments:
  -h, --help   show this help message and exit
  -l, --lista  tulosta pitkä lista
```

```
./posti.py <seurantakoodi1> <seurantakoodi2>
<seurantakoodi1>: Lähetys on lajiteltu. 2018-06-28 07:54:39, OULU
<seurantakoodi2>: Lähetys on vastaanotettu kuljetuksesta. 2018-06-28 12:52:34, Posti kuljetus
```

```
./posti.py <seurantakoodi1> <seurantakoodi2> -l
<seurantakoodi1>: Lähetys on lajiteltu. 2018-06-30 06:22:28, OULU
<seurantakoodi1>: Lähetys on vastaanotettu kuljetuksesta. 2018-06-30 05:48:18, Posti kuljetus
<seurantakoodi1>: Lähetys on kuljetuksessa. 2018-06-29 20:32:15, TAMPERE
<seurantakoodi1>: Lähetys on rekisteröity. 2018-06-29 18:19:41, TAMPERE
<seurantakoodi1>: Lähetys on lajiteltu. 2018-06-29 18:18:25, Lajittelukeskus TAMPERE
<seurantakoodi1>: Lähetys ei ole vielä saapunut Postille, odotathan 2018-06-29 09:34:13, HELSINKI

<seurantakoodi2>: Lähetys ei ole vielä saapunut Postille, odotathan 2018-06-30 08:32:11, HELSINKI
```
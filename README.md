﻿# PolishCitiesTemperatures

Chcemy sprawdzić w danym roku dla każdego miasta jaka była najdłuższa seria dni z temperaturą maksymalną powyżej 30 stopnii.

TODO:
- [x] zebrać dane dla wybranych lat
  - [x] zebrać dane dla 2022 roku z 
  https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/dobowe/synop/
  
  - [x] wyekstrahować `.csv` z plików `.zip` i umieścić je w jednym folderze `data\src`
- [ ] Analiza i processing danych
  - [x] Przygotować nazwy kolumn w tablicy `col_names` w pliku `utils.py`
  - [x] napisać skrypt, który zliczy ilość dni upału pod rząd dla danego miasta, można to zrobić za pomocą `pandas.DataFrame`

# PolishCitiesTemperatures

Chcemy sprawdzić w danym roku dla każdego miasta jaka była najdłuższa seria dni z temperaturą maksymalną powyżej 30 stopnii.

TODO:
- [ ] zebrać dane dla wybranych lat
  - [ ] zebrać dane dla 2022 roku z 
  https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/dobowe/synop/
  - [ ] wyekstrahować `.csv` z plików `.zip` i umieścić je w jednym folderze `data\src`
  - [ ] napisać skrypt, który połączy dane ze wszystkich `.csv` do jednego pliku, docelowo `data\df.csv`
    - można to zrobić za pomocą `pandas.DataFrame` 
- [ ] analiza danych

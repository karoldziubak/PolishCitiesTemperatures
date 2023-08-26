import pandas as pd

def calc_hot_days(df:pd.DataFrame,temp:float)->int:
    # wyciagnac kolumne 'max temp'
    temps = df.temp_max.to_list()

    # zrobic liste z zerami i jedynkami, w zaleznosci czy jest powyzej temp, czy nie
    temps_above_threshold = [1 if t > temp else 0 for t in temps]

    #zliczasz ilość 1 w serii
    # [1,1,0,0,0,1,1,1,1,0]
    # [1,2,0,0,0,1,2,3,4,0]
    temps_cumsum = [temps_above_threshold[0]]
    for i in range(1,len(temps_above_threshold)):
        if temps_above_threshold[i]==0:
            temps_cumsum.append(0)
        elif temps_above_threshold[i]==1:
            temps_cumsum.append(temps_cumsum[i-1]+1)

    #zwracasz największą liczbę z drugiej listy
    return max(temps_cumsum)


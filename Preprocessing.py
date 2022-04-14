import pandas as pd
import numpy as np
import sys
import sklearn
from sklearn.preprocessing import StandardScaler


#Scale the data
scaler = StandardScaler()

# x_train = scaler.fit_transform(x_train)
# x_val = scaler.transform(x_val)
# x_test = scaler.transform(x_test)


"""
unit number: Numéro du moteur (1 à 100)
time (cycles): Temps en cycles de vie (1 à n)
op. setting <1-3>: Paramètres de l'expérience (peuvent être ignorés car stable pour cette série d'expériences)
sensor <01-21>: 21 différents capteurs sur le moteur. Les données sont anonymisées.
RUL: "Remaining Useful Life", Nombre de cycles de vie restant avant arrêt forcé.
"""

def loadTurboFanData():
    """
    Loads the TurboFan data from the csv file.
    :return: TurboFan dataframe
    """
    df = pd.read_csv('data/NASA_turbofan_RUL_data.csv')
    return df

def separateData(df, nTrain, nTest, nVal):
    '''
    return train, test, val in that order
    '''
    nEngines = max(df['unit number'])
    maxIndexTrain = nTrain * nEngines
    maxIndexTest = maxIndexTrain + nTest * nEngines
    maxIndexVal = maxIndexTest + nVal * nEngines
    
    assert maxIndexVal == nEngines, f'percent error: {maxIndexTrain}, {maxIndexTest}, {maxIndexVal}'
    
    train = df.loc[df['unit number'] <= maxIndexTrain]
    test = df.loc[df['unit number'] <= maxIndexTest].loc[df['unit number'] > maxIndexTrain]
    val = df.loc[df['unit number'] > maxIndexTest]
    return train, test, val

def splitDataWithCycles(nCycles, data):
    '''
    split data depending on nCycles
    => nCycles = 3
       it will return the tensors of 3 rows max, for each engine, depending on his life cycle
       [life_cycle = [0, 1, 2], [life_cycle = [1, 2, 3]], [...]]  
       
    return two nparrays
    one containing the data arrays
    one containing the RUL array
    
    [[data_splitted1], [data_splitted2], [data_splitted3]]
    [rul1, rul2, rul3, rul4, rul5, rul6, rul7, rul8, rul9]
    so for data_splitted1 the rul to guess is rul3
    for data_splitted2 the rul to guess is rul4
    for data_splitted3 the rul to guess is rul5
    '''
    global scaler
    
    features = data.drop(["RUL"], axis=1)
    RUL = data.drop(data.columns.difference(["RUL"]), axis=1)
    
    
    try:
        features = scaler.transform(features)
    except sklearn.exceptions.NotFittedError:
        features = scaler.fit_transform(features)
    
    RUL = np.asarray(RUL)
    
    counter = 0
    x = []
    y = []
    for i in range(0, len(features)):
        stopIndex = i+nCycles+1
        # if the unit number is the same for i to max
        if stopIndex < len(features) and features[i][0] == features[stopIndex][0]:
            x.append(features[i:stopIndex][1::]) # append the reshaped data, after dropping the unit number
            y.append(RUL[stopIndex][0])
            counter += 1
    
    print(f'{counter} new datasets created')
    
    return np.array(x),np.array(y)

def classify(y,ranges):
    '''
    create classed depending on ranges:
    if ranges = [50, 150]
    it will return an array mirroring the y array, as classes:
    0 if < 50, 1 if 50 <= y <= 150, 2 if > 150
    '''
    ranges.append(sys.maxsize)
    ret = []
    for item in y:
        for index_range, range in enumerate(ranges):
            if item <= range:
                ret.append(index_range)
                break
    return ret


def getData():
    classes = [50,150] # 0:50: Low, 50:150: Medium, 150:: High
    
    df = loadTurboFanData()
    
    
    trainPrecent, testPrecent, valPrecent = 0.7, 0.2, 0.1
    trainEngines, testEngines, valEngines = separateData(df, trainPrecent, testPrecent, valPrecent)
    
    cycles = 3
    x_train, y_train = splitDataWithCycles(cycles, trainEngines)
    x_val, y_val = splitDataWithCycles(cycles, valEngines)
    x_test, y_test = splitDataWithCycles(cycles, testEngines)

    
    y_train = classify(y_train,classes)
    y_val = classify(y_val,classes)
    y_test = classify(y_test,classes)
    
    
    x_train = np.asanyarray(x_train)
    x_val = np.asanyarray(x_val)
    x_test = np.asanyarray(x_test)
    y_train = np.asanyarray(y_train)
    y_val = np.asanyarray(y_val)
    y_test = np.asanyarray(y_test)
    
    
    
    return x_train,x_val,x_test,y_train,y_val,y_test


if __name__ == "__main__":
    getData()
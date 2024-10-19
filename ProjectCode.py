import pip
def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])

import math
import pandas as pd
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import_or_install('pingouin') # We need this library to have our normality test graph
import pingouin as pg
import statistics as st

path = 'https://raw.githubusercontent.com/prof-apartida/data-exercises/main/'
df = pd.read_csv(path+'Housing1.csv')
print(df.head())

print('\nprice is a numerical continuous variable that indicates the price of the house')
print('\narea is a numerical continuous variable that indicates the size of the property.')
print('\nbedrooms is a numerical discrete variable that indicates the number of bedrooms in the house.')
print('\nbathrooms is a numerical discrete variable that indicates the number of bathrooms in the house.')
print('\nstories is a numerical discrete variable that indicates the number of floors in the property.')
print('\nmainroad is a boolean variable that indicates if the property is connected to a mainroad.')
print('\nguestroom is a boolean variable that indicates if the property has a guestroom.')
print('\nbasement is a boolean variable that indicates if the property has a basement.')
print('\nhotwaterheating is a boolean variable that indicates if the property has a water heating system.')
print('\nairconditioning is a boolean variable that indicates if the property has an air conditioning device.')
print('\nparking is a boolean variable that indicates if the property has vehicle parking.')
print('\nprefarea is a boolean variable that indicates if the property is located in the preferred neighbourhood of the city.')
print('\nfurnishingstatus is a categorical variable that indicates the furnishing status of the house.')


#df.describe().apply(lambda s: s.apply('{0:.5f}'.format))
median_price = st.median(df['price'])
mode_price = st.mode(df['price'])
IQR_price = np.percentile(df['price'], 75) - np.percentile(df['price'], 25)
print('Statistics of price:\n',
    df['price'].describe().apply(lambda x: format(x, 'f')), '\n', 
    f'Median: {median_price}', '\n',
    f'Mode: {mode_price}', '\n',
    f'IQR: {IQR_price}','\n',
    f'Range: {max(df['price'])-min(df["price"])}')



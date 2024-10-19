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
print('\nStatistics of price:\n',
    df['price'].describe().apply(lambda x: format(x, 'f')), '\n', 
    f'Median: {median_price}', '\n',
    f'Mode: {mode_price}', '\n',
    f'IQR: {IQR_price}','\n',
    f'Range: {max(df['price'])-min(df["price"])}')

median_area = st.median(df['area'])
mode_area = st.mode(df['area'])
IQR_area = np.percentile(df['area'], 75) - np.percentile(df['area'], 25)
print('\nStatistics of area:\n',
    df['area'].describe().apply(lambda x: format(x, 'f')), '\n', 
    f'Median: {median_area}', '\n',
    f'Mode: {mode_area}', '\n',
    f'IQR: {IQR_area}','\n',
    f'Range: {max(df['area'])-min(df["area"])}')

median_bathrooms = st.median(df['bathrooms'])
mode_bathrooms = st.mode(df['bathrooms'])
IQR_bathrooms = np.percentile(df['bathrooms'], 75) - np.percentile(df['bathrooms'], 25)
print('\nStatistics of bathrooms:\n',
    df['bathrooms'].describe().apply(lambda x: format(x, 'f')), '\n', 
    f'Median: {median_bathrooms}', '\n',
    f'Mode: {mode_bathrooms}', '\n',
    f'IQR: {IQR_bathrooms}','\n',
    f'Range: {max(df['bathrooms'])-min(df["bathrooms"])}')

median_stories = st.median(df['stories'])
mode_stories = st.mode(df['stories'])
IQR_stories = np.percentile(df['stories'], 75) - np.percentile(df['stories'], 25)
print('\nStatistics of stories:\n',
    df['stories'].describe().apply(lambda x: format(x, 'f')), '\n', 
    f'Median: {median_stories}', '\n',
    f'Mode: {mode_stories}', '\n',
    f'IQR: {IQR_stories}','\n',
    f'Range: {max(df['stories'])-min(df['stories'])}')

median_parking = st.median(df['parking'])
mode_parking = st.mode(df['parking'])
IQR_parking = np.percentile(df['parking'], 75) - np.percentile(df['parking'], 25)
print('\nStatistics of parking:\n',
    df['parking'].describe().apply(lambda x: format(x, 'f')), '\n', 
    f'Median: {median_parking}', '\n',
    f'Mode: {mode_parking}', '\n',
    f'IQR: {IQR_parking}','\n',
    f'Range: {max(df['parking'])-min(df['parking'])}')

print('There are ',df['mainroad'].value_counts()['yes'], ' houses connected to the mainroad.\n')
print('There are ',df['guestroom'].value_counts()['yes'], ' houses connected that have a guestroom.\n')
print('There are ',df['basement'].value_counts()['yes'], ' houses that have a basement.\n')
print('There are ',df['hotwaterheating'].value_counts()['yes'], ' houses with a water heating system.\n')
print('There are ',df['airconditioning'].value_counts()['yes'], ' houses with an air conditioning system.\n')
print('There are ',df['prefarea'].value_counts()['yes'], ' houses in the preferred neighborhood.\n')
print('There are ',df['furnishingstatus'].value_counts()['furnished'], ' furnished houses,',
    df['furnishingstatus'].value_counts()['semi-furnished'],' partially furnished houses, and ',
    df['furnishingstatus'].value_counts()['unfurnished'], ' unfurnished houses.')


#plt.show(plt.hist(df['price']))
#plt.show(plt.hist(df['area']))
#plt.show(plt.hist(df['bathrooms']))
#plt.show(plt.hist(df['stories']))
#plt.show(plt.hist(df['parking']))

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
import statistics as sta

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

#################


### INTELIGENT WAY TO DO IT
###def print_stats(df,variable):
###  print('Min:',df[variable].min())
###  print('Max:',df[variable].max())
###  print('Mean:',df[variable].mean())
###  print('SD:',df[variable].std())


###################

median_price = sta.median(df['price'])
mode_price = sta.mode(df['price'])
IQR_price = np.percentile(df['price'], 75) - np.percentile(df['price'], 25)
print('\nStatistics of price:\n',
    df['price'].describe().apply(lambda x: format(x, 'f')), '\n', 
    f'Median: {median_price}', '\n',
    f'Mode: {mode_price}', '\n',
    f'IQR: {IQR_price}','\n',
    f'Range: {max(df['price'])-min(df["price"])}')

median_area = sta.median(df['area'])
mode_area = sta.mode(df['area'])
IQR_area = np.percentile(df['area'], 75) - np.percentile(df['area'], 25)
print('\nStatistics of area:\n',
    df['area'].describe().apply(lambda x: format(x, 'f')), '\n', 
    f'Median: {median_area}', '\n',
    f'Mode: {mode_area}', '\n',
    f'IQR: {IQR_area}','\n',
    f'Range: {max(df['area'])-min(df["area"])}')

median_bathrooms = sta.median(df['bathrooms'])
mode_bathrooms = sta.mode(df['bathrooms'])
IQR_bathrooms = np.percentile(df['bathrooms'], 75) - np.percentile(df['bathrooms'], 25)
print('\nStatistics of bathrooms:\n',
    df['bathrooms'].describe().apply(lambda x: format(x, 'f')), '\n', 
    f'Median: {median_bathrooms}', '\n',
    f'Mode: {mode_bathrooms}', '\n',
    f'IQR: {IQR_bathrooms}','\n',
    f'Range: {max(df['bathrooms'])-min(df["bathrooms"])}')

median_stories = sta.median(df['stories'])
mode_stories = sta.mode(df['stories'])
IQR_stories = np.percentile(df['stories'], 75) - np.percentile(df['stories'], 25)
print('\nStatistics of stories:\n',
    df['stories'].describe().apply(lambda x: format(x, 'f')), '\n', 
    f'Median: {median_stories}', '\n',
    f'Mode: {mode_stories}', '\n',
    f'IQR: {IQR_stories}','\n',
    f'Range: {max(df['stories'])-min(df['stories'])}')

median_parking = sta.median(df['parking'])
mode_parking = sta.mode(df['parking'])
IQR_parking = np.percentile(df['parking'], 75) - np.percentile(df['parking'], 25)
print('\nStatistics of parking:\n',
    df['parking'].describe().apply(lambda x: format(x, 'f')), '\n', 
    f'Median: {median_parking}', '\n',
    f'Mode: {mode_parking}', '\n',
    f'IQR: {IQR_parking}','\n',
    f'Range: {max(df['parking'])-min(df['parking'])}')

print('There are ',df['mainroad'].value_counts()['yes'], ' houses connected to the mainroad.\n')
print('There are ',df['guestroom'].value_counts()['yes'], ' houses that have a guestroom.\n')
print('There are ',df['basement'].value_counts()['yes'], ' houses that have a basement.\n')
print('There are ',df['hotwaterheating'].value_counts()['yes'], ' houses with a water heating system.\n')
print('There are ',df['airconditioning'].value_counts()['yes'], ' houses with an air conditioning system.\n')
print('There are ',df['prefarea'].value_counts()['yes'], ' houses in the preferred neighborhood.\n')
print('There are ',df['furnishingstatus'].value_counts()['furnished'], ' furnished houses,',
    df['furnishingstatus'].value_counts()['semi-furnished'],' partially furnished houses, and ',
    df['furnishingstatus'].value_counts()['unfurnished'], ' unfurnished houses.')

values = pd.DataFrame({ 
    'price' : df['price'], 
    'area' : df['area'], 
    'stories' : df['stories'], 
    'bathrooms' : df['bathrooms'] 
}) 

hist = values.hist(bins=8) 
plt.show()


houses_with_mainroad = len(df[(df['mainroad']== 'yes')])
houses_without_mainroad = 272 - houses_with_mainroad

fig, ax = plt.subplots()
ax.pie([houses_with_mainroad, houses_without_mainroad], labels=['With Mainroad', 'No Mainroad'], autopct='%1.1f%%')
plt.show()

houses_with_guestroom = len(df[(df['guestroom']== 'yes')])
houses_without_guestroom = 272 - houses_with_guestroom

fig, ax = plt.subplots()
ax.pie([houses_with_guestroom, houses_without_guestroom], labels=['With Guestroom', 'No Guestroom'], autopct='%1.1f%%')
plt.show()

houses_with_basement = len(df[(df['basement']== 'yes')])
houses_without_basement = 272 - houses_with_basement

fig, ax = plt.subplots()
ax.pie([houses_with_basement, houses_without_basement], labels=['With Basement', 'No Basement'], autopct='%1.1f%%')
plt.show()

houses_with_hotwaterheating = len(df[(df['hotwaterheating']== 'yes')])
houses_without_hotwaterheating = 272 - houses_with_hotwaterheating

fig, ax = plt.subplots()
ax.pie([houses_with_hotwaterheating, houses_without_hotwaterheating], labels=['With Hot Water Heating', 'No Hot Water Heating'], autopct='%1.1f%%')
plt.show()


houses_with_airconditioning = len(df[(df['airconditioning']== 'yes')])
houses_without_airconditioning = 272 - houses_with_airconditioning

fig, ax = plt.subplots()
ax.pie([houses_with_airconditioning, houses_without_airconditioning], labels=['With Air Conditioning', 'No Air Conditioning'], autopct='%1.1f%%')
plt.show()

houses_with_prefarea = len(df[(df['prefarea']== 'yes')])
houses_without_prefarea = 272 - houses_with_prefarea

fig, ax = plt.subplots()
ax.pie([houses_with_prefarea, houses_without_prefarea], labels=['In Preferred Neighbourhood', 'No Preferred Neighbourhood'], autopct='%1.1f%%')
plt.show()

houses_furnished = len(df[(df['furnishingstatus']== 'furnished')])
houses_semifurnished = len(df[(df['furnishingstatus']== 'semi-furnished')])
houses_unfurnished = len(df[(df['furnishingstatus']== 'unfurnished')])

fig, ax = plt.subplots()
ax.pie([houses_furnished, houses_semifurnished, houses_unfurnished], labels=['Furnished', 'Semi-furnished','Unfurnished'], autopct='%1.1f%%')
plt.show()

# Define the variables and their values
N = 272 # Population size
CL = 0.95 # Confidence level
p = 0.5 # Standard Deviation. If unknown, leave it as 0.5
e = 0.05 # Margin of error

alpha_half = (1-CL)/2
Z_score = st.norm.ppf(alpha_half+CL)

n = ((Z_score**2)*p*(1-p))/e**2 # Sample size for an unlimited population (remember, the small n)
sample_size = n/(1+(((Z_score**2)*p*(1-p))/((e**2)*N))) # Sample size for a limited population

print('\nSample size for a population of',N,'elements =',sample_size)

sample_houses = df.sample(n=159)

print(sample_houses.head())
n=160


##going to calculate mean for price, area and bedrooms; then for every confidence
##interval, will check if the population mean falls there.



mean_sample_price = sta.mean(sample_houses['price'])
sd_sample_price = sta.stdev(sample_houses['price'])
mean_sample_area = sta.mean(sample_houses['area'])
sd_sample_area = sta.stdev(sample_houses['area'])
mean_sample_bedrooms = sta.mean(sample_houses['bedrooms'])
sd_sample_bedrooms = sta.stdev(sample_houses['bedrooms'])

## Z-score for two tailed 95% confidence level:
z = st.norm.ppf(0.975)

ci_price_from = mean_sample_price-z*(sd_sample_price/math.sqrt(n))
ci_price_to = mean_sample_price+z*(sd_sample_price/math.sqrt(n))

ci_price_from = "{:,.2f}".format(ci_price_from)
ci_price_to = "{:,.2f}".format(ci_price_to)

mean_price = sta.mean(df['price'])
mean_price = "{:,.2f}".format(mean_price)


##Confidence interval for mean of sample price:
print(f'Confidence interval of mean price from {ci_price_from} to {ci_price_to}, compared to a population mean of {mean_price}.')

ci_area_from = mean_sample_area-z*(sd_sample_area/math.sqrt(n))
ci_area_to = mean_sample_area+z*(sd_sample_area/math.sqrt(n))

ci_area_from = "{:,.2f}".format(ci_area_from)
ci_area_to = "{:,.2f}".format(ci_area_to)

mean_area = sta.mean(df['area'])
mean_area = "{:,.2f}".format(mean_area)


##Confidence interval for mean of sample area:
print(f'Confidence interval of mean area from {ci_area_from} to {ci_area_to}, compared to a population mean of {mean_area}.')

ci_bedrooms_from = mean_sample_bedrooms-z*(sd_sample_bedrooms/math.sqrt(n))
ci_bedrooms_to = mean_sample_bedrooms+z*(sd_sample_bedrooms/math.sqrt(n))

ci_bedrooms_from = "{:,.2f}".format(ci_bedrooms_from)
ci_bedrooms_to = "{:,.2f}".format(ci_bedrooms_to)

mean_bedrooms = sta.mean(df['bedrooms'])
mean_bedrooms = "{:,.2f}".format(mean_bedrooms)


##Confidence interval for mean of sample bedrooms:
print(f'Confidence interval of mean bedrooms from {ci_bedrooms_from} to {ci_bedrooms_to}, compared to a population mean of {mean_bedrooms}.')

print('Normality tests for price')
print("{:,.5f}".format(st.kstest(df['price'],'norm').pvalue))
print("{:,.5f}".format(st.shapiro(df['price']).pvalue))
print("{:,.5f}".format(st.jarque_bera(df['price']).pvalue))
print("{:,.5f}".format(st.normaltest(df['price']).pvalue))
print('With very low p-values for KS, Shapiro-Wilk, Jarque-Bera and Anderson-Darling (st.normaltest), \nwe can reject the null hypothesis that variable follows a normal distribution.')
print('\n We can go even further and ilustrate the point:')

plt.show(pg.qqplot(df['price'], dist='norm', confidence=.95))

print('Normality tests for area')
print("{:,.5f}".format(st.kstest(df['area'],'norm').pvalue))
print("{:,.5f}".format(st.shapiro(df['area']).pvalue))
print("{:,.5f}".format(st.jarque_bera(df['area']).pvalue))
print("{:,.5f}".format(st.normaltest(df['area']).pvalue))
print('Area shows very low p-values as well, which means we can reject the null hypothesis that the variable follows a normal distribution.')
print('\n The illustration is similar to price:')

plt.show(pg.qqplot(df['area'], dist='norm', confidence=.95))
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 12:04:12 2022

@author: get gd nub
"""
#Problem Statement - Should US Colleges continue admission without SAT post-covid?

#Visualisations built in power BI

#Key Analysis:   
#Graduation rate and first year retention rate throughout the year (i.e. pre-exemption of SAT vs post-exemption of SAT)
#Minority admission rate pre-exemption of SAT vs post-exememption of SAT
#Correlation between graduation rates and sat test results
#Correlation between first year retention rate and sat test results
#Comparison between correlation of (HSGPA - College AVG GPA) and (SAT - College AVG GPA)

#Key Findings:
#More then 75% of us college dont require sat and act as of 2021
#SAT scores are moderately correlated with first year retention rate and graduation rate(4 years), with respective coefficient value of 0.51 and 0.5
#37% less people submmited sat/act scores upon the exemption in 2019
#9.7% increase in admission of minority in US colleges
#A sharp drop in grdaution rate and a sharp increase in freshman retention rate upon exemption of sat/act test

#Conclusion:
#benefit of exempting sat and act scores outweights its setbacks, therefore US colleges are encourge to continute exemption of test results post covid

#Limitations of Analysis:
#Confidence of recommendation may improve, alter, or amend upon increase avaliability of post-exemption data
#Pre-2013 college data are not included for the analysis; accuracy of analysis may improve with pre-2013 data
#Correlations of HSGPA/SAT vs College GPA are based on a sample size of 30 universities; accuracy may improve with the inclusion of a bigger sample size

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.support.select import Select
import numpy as np

delimiter = ","

#Scrapping https://www.collegetransitions.com/dataverse/retention-and-graduation-rates

with open('data_scraping_us_uni.csv', 'w') as file:
    file.write("institutions, freshman_rentention_rates, gradution_rates_4_years, graduation_rates_5_years \n")

options = webdriver.ChromeOptions()
  
driver = webdriver.Chrome(executable_path="C:/Users/get gd nub/Desktop/web scrapper/chromedriver.exe", options=options)
driver.set_window_size(1120, 1000)

url ='https://www.collegetransitions.com/dataverse/retention-and-graduation-rates#:~:text=Nationwide%2C%20the%20average%20retention%20rate,it%20takes%20to%20do%20so.'
driver.get(url)

for i in range(10):
    institutions = driver.find_elements_by_xpath('//*[@id="footable_10551"]/tbody/tr/td[1]')
    for institution in institutions:
        print(institution.text)
        
    freshman_rentention_rates = driver.find_elements_by_xpath('//*[@id="footable_10551"]/tbody/tr/td[2]')
    for freshman_rentention_rate in freshman_rentention_rates:
        print(freshman_rentention_rate.text)
        
    gradution_rates_4_years = driver.find_elements_by_xpath('//*[@id="footable_10551"]/tbody/tr/td[3]')
    for gradution_rate_4_years in  gradution_rates_4_years:
        print(gradution_rate_4_years.text)
        
    graduation_rates_5_years  = driver.find_elements_by_xpath('//*[@id="footable_10551"]/tbody/tr/td[4]')
    for graduation_rate_5_years in graduation_rates_5_years:
        print(graduation_rate_5_years.text)
        
    with open('data_scraping_us_uni.csv', 'a') as file:
        for i in range(len(institutions)):
            file.write(institutions[i].text + "," + freshman_rentention_rates[i].text + "," + gradution_rates_4_years[i].text + "," + graduation_rates_5_years[i].text + "\n")
                       
    try:
                driver.find_element_by_xpath('//*[@id="footable_10551"]/tfoot/tr/td/div/ul/li[15]/a').click()
    except NoSuchElementException:
                print("cmi la cb")
                
                open()
                               
    file.close()
    
#Scraping https://www.insidehighered.com/admissions/article/2021/03/08/common-application-data-show-most-applicants-are-not-submitting-test

with open('sat_act_submitted.csv', 'w') as file:
    file.write("Category of College, Percentage Submitted Scaores 2019, Percentage Submitted Scores 2020 \n")

options = webdriver.ChromeOptions()
  
driver = webdriver.Chrome(executable_path="C:/Users/get gd nub/Desktop/web scrapper/chromedriver.exe", options=options)
driver.set_window_size(1120, 1000)

url ='https://www.insidehighered.com/admissions/article/2021/03/08/common-application-data-show-most-applicants-are-not-submitting-test'
driver.get(url)

    col_1 = driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/div/div[2]/div[1]/div/div[15]/div/div/div/div/div/table[1]/tbody/tr/td[1]')
    for col1 in col_1:
        print(col1.text)
        
    col_2 = driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/div/div[2]/div[1]/div/div[15]/div/div/div/div/div/table[1]/tbody/tr/td[2]')
    for col2 in col_2:
        print(col2.text)
        
    col_3 = driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/div/div[2]/div[1]/div/div[15]/div/div/div/div/div/table[1]/tbody/tr/td[3]')
    for col3 in col_3:
        print(col3.text)
        
    with open('sat_act_submitted.csv', 'a') as file:
        for i in range(len(col_1)):
            file.write(col_1[i].text + "," + col_2[i].text + "," + col_3[i].text + "," + "\n")
                       
    file.close()
    
#Scraping https://www.insidehighered.com/admissions/article/2021/03/08/common-application-data-show-most-applicants-are-not-submitting-test

with open('sat_act_submitted2.csv', 'w') as file:
    file.write("Category of College, Percentage Submitted Scaores 2019, Percentage Submitted Scores 2020 \n")

options = webdriver.ChromeOptions()
  
driver = webdriver.Chrome(executable_path="C:/Users/biyin/Desktop/web scrapper/chromedriver.exe", options=options)
driver.set_window_size(1120, 1000)

url ='https://www.insidehighered.com/admissions/article/2021/03/08/common-application-data-show-most-applicants-are-not-submitting-test'
driver.get(url)

    col_4 = driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/div/div[2]/div[1]/div/div[15]/div/div/div/div/div/table[2]/tbody/tr/td[1]')
    for col4 in col_4:
        print(col4.text)
        
    col_5 = driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/div/div[2]/div[1]/div/div[15]/div/div/div/div/div/table[2]/tbody/tr/td[2]')
    for col5 in col_5:
        print(col5.text)
        
    col_6 = driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/div/div[2]/div[1]/div/div[15]/div/div/div/div/div/table[2]/tbody/tr/td[3]')
    for col6 in col_6:
        print(col6.text)
        
    with open('sat_act_submitted2.csv', 'a') as file:
        for i in range(len(col_4)):
            file.write(col_4[i].text + "," + col_5[i].text + "," + col_6[i].text + "," + "\n")
                       
    file.close()
    
#Preparing Data
#dataframe - submittion rate 2019 vs 2020

df1 = pd.read_csv('sat_act_submitted2.csv')

df1.drop(df1.index[7:16],0,inplace=True)
df1.columns = ["1", "2","3","4","5","6"]

mge = df1["1"]+ df1["2"]+ df1["3"]
df11 = df1[["5", "6"]]
df1 = pd.concat([mge , df11], axis = 1)
df1.columns = ["Category of College", "% Submitted Scores 2019","% Submitted Scores 2020"]

df2 = pd.read_csv('sat_act_submitted.csv')  
df = pd.concat([df1, df2], axis = 0)
df.reset_index(level=None, drop=True, inplace=True, col_level=0, col_fill='')

df['% Submitted Scores 2019'] = df['% Submitted Scores 2019'].str.rstrip('%').astype('float') / 100.0
df['% Submitted Scores 2020'] = df['% Submitted Scores 2020'].str.rstrip('%').astype('float') / 100.0

Submittion_rate_mean = pd.Series.mean(df)
Submittion_rate_mean.to_csv("submittion rate 2019 vs 2020.csv")

#dataframe - Collegetransition Data 2021

df2021 = pd.read_csv('data_scraping_us_uni.csv')
df2021_mean = pd.Series.mean(df2021[" freshman_rentention_rates"])
df2021[' freshman_rentention_rates'] = df2021[' freshman_rentention_rates'].str.rstrip('%').astype('float') / 100.0
df2021[' gradution_rates_4_years'] = df2021[' gradution_rates_4_years'].str.rstrip('%').astype('float') / 100.0
df2021[' graduation_rates_5_years '] = df2021[' graduation_rates_5_years '].str.rstrip('%').astype('float') / 100.0
df2021_mean = pd.Series.mean(df2021)


#dataframe - Collegescorecard Data 2012 to 2020

df_colleges = df2021["institutions"]

df2020 = pd.read_csv('MERGED2019_20_PP.csv')
df2020 = df2020[["INSTNM", "RET_FT4", "C150_4", "SAT_AVG"]]
df2020.columns = ["institutions", " freshman_rentention_rates", " gradution_rates_4_years", "SAT Average"]
df_2020_merged = pd.merge(df_colleges, df2020, how='inner', on="institutions")#drawing len(df2021) sample from all Collegescoredatas
df2020_mean = pd.Series.mean(df_2020_merged)

df2019 = pd.read_csv('MERGED2018_19_PP.csv')
df2019 = df2019[["INSTNM", "C150_4", "RET_FT4", "SAT_AVG"]]
df2019.columns = ["institutions", " freshman_rentention_rates", " gradution_rates_4_years", "SAT Average"]
df_2019_merged = pd.merge(df_colleges, df2019, how='inner', on="institutions")#drawing len(df2021) sample from all Collegescoredatas
df2019_mean = pd.Series.mean(df_2019_merged)

df2018 = pd.read_csv('MERGED2017_18_PP.csv')
df2018 = df2018[["INSTNM", "C150_4", "RET_FT4", "SAT_AVG"]]
df2018.columns = ["institutions", " freshman_rentention_rates", " gradution_rates_4_years", "SAT Average"]
df_2018_merged = pd.merge(df_colleges, df2018, how='inner', on="institutions")#drawing len(df2021) sample from all Collegescoredatas
df2018_mean = pd.Series.mean(df_2018_merged)

df2017 = pd.read_csv('MERGED2016_17_PP.csv')
df2017 = df2017[["INSTNM", "C150_4", "RET_FT4", "SAT_AVG"]]
df2017.columns = ["institutions", " freshman_rentention_rates", " gradution_rates_4_years", "SAT Average"]
df_2017_merged = pd.merge(df_colleges, df2017, how='inner', on="institutions")#drawing len(df2021) sample from all Collegescoredatas
df2017_mean = pd.Series.mean(df_2017_merged)

df2016 = pd.read_csv('MERGED2015_16_PP.csv')
df2016 = df2016[["INSTNM", "C150_4", "RET_FT4", "SAT_AVG"]]
df2016.columns = ["institutions", " freshman_rentention_rates", " gradution_rates_4_years", "SAT Average"]
df_2016_merged = pd.merge(df_colleges, df2016, how='inner', on="institutions")#drawing len(df2021) sample from all Collegescoredatas
df2016_mean = pd.Series.mean(df_2016_merged)

df2015 = pd.read_csv('MERGED2014_15_PP.csv')
df2015 = df2015[["INSTNM", "C150_4", "RET_FT4", "SAT_AVG"]]
df2015.columns = ["institutions", " freshman_rentention_rates", " gradution_rates_4_years", "SAT Average"]
df_2015_merged = pd.merge(df_colleges, df2015, how='inner', on="institutions")#drawing len(df2021) sample from all Collegescoredatas
df2015_mean = pd.Series.mean(df_2015_merged)

df2014 = pd.read_csv('MERGED2013_14_PP.csv')
df2014 = df2014[["INSTNM", "C150_4", "RET_FT4", "SAT_AVG"]]
df2014.columns = ["institutions", " freshman_rentention_rates", " gradution_rates_4_years", "SAT Average"]
df_2014_merged = pd.merge(df_colleges, df2014, how='inner', on="institutions")#drawing len(df2021) sample from all Collegescoredatas
df2014_mean = pd.Series.mean(df_2014_merged)

df2013 = pd.read_csv('MERGED2012_13_PP.csv')
df2013 = df2013[["INSTNM", "C150_4", "RET_FT4", "SAT_AVG"]]
df2013.columns = ["institutions", " freshman_rentention_rates", " gradution_rates_4_years", "SAT Average"] 
df_2013_merged = pd.merge(df_colleges, df2013, how='inner', on="institutions")#drawing len(df2021) sample from all Collegescoredatas
df2013_mean = pd.Series.mean(df_2013_merged)


#TOTAL mean through the years

df_mean_total = pd.concat([df2013_mean, df2014_mean, df2015_mean, df2016_mean, df2017_mean, df2018_mean, df2019_mean, df2020_mean, df2021_mean], axis = 1)
df_mean_total.columns = ["2013", "2014","2015","2016","2017","2018", "2019", "2020", "2021" ]
df_mean_total = df_mean_total.transpose()

df_mean_total.to_csv("df mean total.csv")
writer = pd.ExcelWriter('df mean total.xlsx')
df_mean_total.to_excel(writer)


#correlation coefficient test - SAT/GRADUATION RATE

df2020_nonan = df2020.fillna(df2020.median())
data1 = df2020_nonan[[' gradution_rates_4_years','SAT Average']]
correlation = data1.corr(method='pearson')

#correlation coefficient test - SAT/FRESHMAN RETENTION RATE
df2018_nonan = df2018.fillna(df2018.median())
data = df2018_nonan[[' freshman_rentention_rates','SAT Average']]
correlation_sat_retention = data.corr(method='pearson')


#correlation between College GPA with HSGPA and SAT

gpa_sat = pd.read_csv('gpa_sat.csv')
gpa_sat_merged = pd.merge(gpa_sat, df2018, how='inner', on="institutions")#drawing len(gpa_sat) sample from all Collegescoredatas
gpa_sat_merged_nonan = gpa_sat_merged.fillna(gpa_sat_merged.median())

data3 = gpa_sat_merged_nonan[['SAT Average', 'Average GPA']]
correlation_gpa_sat = data3.corr(method='pearson')
correlation_gpa_sat.to_csv("correlation_gpa_sat.csv")
gpa_sat_merged_nonan.to_csv("gpa_sat_merged_nonan.csv")

data4 = gpa_sat_merged_nonan[['Average GPA  of accepted students', 'Average GPA']]
correlation_gpa_hsgpa = data4.corr(method='pearson')

#comparing minority intake 2018 and 2019

minority = pd.read_csv("minority.csv")
minority_sum = minority.sum(axis=1)
minority_percentage = minority_sum.iloc.set_index('W').apply(pd.to_datetime).diff(-1, axis=1)
minority_sum.to_csv("minority sum.csv")


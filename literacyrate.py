import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from IPython.core.display import display, HTML
import seaborn as sns
import math
import plotly.plotly as py
import plotly
import nvd3
from nvd3 import multiBarChart
from IPython.core.display import display, HTML


#cleaning the dataset of adult literacy rate
def sheet3():
    df = pd.ExcelFile(r"/home/mohit/Desktop/Mini_project/Youth_Adult_Literacy_Rate.xlsx")
    df = df.parse('Adult literacy rate',skiprows = 10 ,na_values = ['NA'])
    df.columns=['ISO Code','Countries','Year','Total','S5','Male','S7','Female','S9','S10']
    df = df.iloc[:-18,:]
    df = df.drop('S10', axis = 1)
    df = df.dropna(axis='columns',how='all')
    df = df.dropna(axis='rows',how='any')

    df.to_excel('ALRcleaned.xlsx',index = False)



#importing the cleaned dataset
df = pd.ExcelFile(r"/home/mohit/Desktop/Mini_project/ALRcleaned.xlsx")
df= pd.read_excel("/home/mohit/Desktop/Mini_project/ALRcleaned.xlsx",index_col = 1)

# Dividing of countries into region
Arabic = ['ARM','ARE','GEO','IRQ','BHR','JOR','KAZ','KGZ','IRN','SAU','OMN','PSE','SYR','TJK','TUR','TKM','UZB','YEM','UKR','QAT']

Asia_Pacific = ['AFG','AZE','BGD','BTN','CHN','KHM','IND','IDN','JPN','MDV','MNG','MMR','NPL','PAK','LKA',
'PHL','THA','SGP','VNM']
  
American_Region = ['ATG','BHS','BRB','BRA','CHL','BLZ','CAN','COL','CYM','CRI','CUB','CUW','DMA','ECU','DOM','SLV','GRL','GRD',
'GLP','GTM','HTI','HND','JAM','MTQ','MEX','SPM','MSR','ANT','KNA','NIC','PAN','PER','PRI','BES','BES','SXM',
'KNA','LCA','SPM','VCT','TTO','TCA','USA','VIR','VGB','URY']
  
  
African_Region = ['DZA','AGO','SHN','BEN','BWA','BFA','BDI','CMR','CPV','CAF','TCD','COM','COG',
'COD','DJI','EGY','GNQ','ERI','ETH','GAB','GMB','GHA','GIN','GNB','CIV','KEN','LSO','LBR','LBY',
'MDG','MWI','MLI','MRT','MUS','MYT','MAR','MOZ','NAM','NER','NGA','STP','REU','RWA','STP','SEN','SYC',
'SLE','SOM','ZAF','SSD','SHN','SDN','SWZ','TZA','TGO','TUN','UGA','COD','ZMB','TZA','ZWE']

Rest = Asia_Pacific+Arabic+American_Region+African_Region

# For representing the countries
Arabic_countries = df.loc[df['ISO Code'].isin(Arabic)]
Asian_countries = df.loc[df['ISO Code'].isin(Asia_Pacific)]
African_countries = df.loc[df['ISO Code'].isin(African_Region)]
American_countries = df.loc[df['ISO Code'].isin(American_Region)]
Rest_countries = df.loc[~df['ISO Code'].isin(Rest)]

#plotting graphs according to literacy rate vs countries
def country():
    var = sns.barplot(x='ISO Code', y='Total',data =Arabic_countries,color='darkblue')
    var.set(xlabel='Arab Countries', ylabel='Literacy rate %')
    plt.show()

    var = sns.barplot(x='ISO Code', y='Total',data =Asian_countries,color='darkred')
    var.set(xlabel='Asian Countries', ylabel='Literacy rate %')
    plt.show()

    var = sns.barplot(x='ISO Code', y='Total',data =African_countries,color='darkgreen')
    var.set(xlabel='African Countries', ylabel='Literacy rate % ')
    plt.show()
    var = sns.barplot(x='ISO Code', y='Total',data =American_countries,color='yellow')
    var.set(xlabel='American Countries', ylabel='Literacy rate %')
    plt.show()

    var = sns.barplot(x='ISO Code', y='Total',data =Rest_countries,color='magenta')
    var.set(xlabel='Rest of Countries', ylabel='Literacy rate %')
    plt.show()

#Calculating literacy rate wrt male and female
def Asia_MF():
    men_asian = math.floor(Asian_countries['Male'].mean())
    female_asian = math.floor(Asian_countries['Female'].mean())

    asian = {'Male': men_asian,
            'Female': female_asian
            }


    y = pd.Series(asian)
    y = pd.DataFrame(y)
    y.columns = ['asian']
    print(y)

def Arab_MF():
    men_arab = math.floor(Arabic_countries['Male'].mean())
    female_arab = math.floor(Arabic_countries['Female'].mean())
    arab = {'Male': men_arab,
            'Female': female_arab
            }


    y = pd.Series(arab)
    y = pd.DataFrame(y)
    y.columns = ['arab region']
    print(y)    

def Africa_MF():
    men_african = math.floor(African_countries['Male'].mean())
    female_african = math.floor(African_countries['Female'].mean())

    african = {'Male':men_african,
               'Female': female_african
               }


    y = pd.Series(african)
    y = pd.DataFrame(y)
    y.columns = ['African']
    print(y)

def America_MF():
    male_america = math.floor(American_countries['Male'].mean())
    female_america = math.floor(American_countries['Female'].mean())
    America = {'Male': male_america,
                     'Female':female_america
                     }
    y = pd.Series(America)
    y = pd.DataFrame(y)
    y.columns = ['American region']
    print(y)

def Rest_MF():
    male_rest = math.floor(Rest_countries['Male'].mean())
    female_rest = math.floor(Rest_countries['Female'].mean())
    Rest = {'Male': male_rest,
            'Female':female_rest
           }
    y = pd.Series(Rest)
    y = pd.DataFrame(y)
    y.columns = ['Rest of countries']
    print(y)

 #Plotting world map of countries with literacy rate
def worldmap():
    plotly.tools.set_credentials_file(username='mohit_awana', api_key='etlxovt5BLTXK5xRRn13')
    df = pd.read_excel('/home/mohit/Desktop/Mini_project/ALRcleaned.xlsx')
    data =  dict(
        type = 'choropleth',
        locations = df['ISO Code'],
        z = df['Total'],
        text = df['Countries'],
        colorscale = [[0,'rgb(5, 10, 172)'],[0.35,"rgb(106, 137, 247)"],[0.5,"rgb(190,190,190)"],
                     [0.6,"rgb(220, 170, 132)"],[0.7,"rgb(230, 145, 90)"],[1,"rgb(178, 10, 28)"]],
        autocolorscale = False,
        reversescale = True,
        name = 'Total',
        marker = dict(
            line = dict (
                color = 'rgb(220,220,0)',
                width = 1.0
                ) ),
        )
    fig = dict( data=[data] )
    py.iplot( fig, validate=False, filename='literacyRate_map' )


#Plotting graph wrt male and female literacy rate
def stackedMF():
    output_file = open('literacy_rate_nvd3.html', 'w')
    chart = multiBarChart(width=1000, height=400, x_axis_format=None,color = 'green')
    data = ['Male','Female']
    Arabic_countries =[95,90]
    Asian_countries = [85,75]
    African_countries = [56,71]
    American_countries = [90,88]
    rest_countries = [95,93]
    chart.add_serie(name="Arab region", y=Arabic_countries, x=data)
    chart.add_serie(name="Asian region", y=Asian_countries, x=data)
    chart.add_serie(name="African region", y=African_countries, x=data)
    chart.add_serie(name="American region", y=American_countries, x=data)
    chart.add_serie(name=" Rest of world", y=rest_countries, x=data)
    chart.buildhtml()
    display(HTML(chart.htmlcontent))
    output_file.write(chart.htmlcontent)
    output_file.close()    

if __name__ == '__main__':
    #country()
    sheet3()
    Asia_MF()
    Arab_MF()
    America_MF()
    Africa_MF()
    Rest_MF()
    worldmap()
    stackedMF()     
import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from IPython.core.display import display, HTML
import seaborn as sns 

#Cleaning the dataset containing net enrolment rate
def sheet1():
	df = pd.ExcelFile(r"/home/mohit/Desktop/Mini_project/primary_enrolment.xlsx")
	df = df.parse('Pre-primary GER',skiprows = 10 ,na_values = ['NA'])
	df.columns=['ISO Code','Countries','Year','Total','S5','Male','S7','Female','S9','S10']
	df = df.iloc[:-18,:]
	df = df.drop('S10', axis = 1)
	df = df.dropna(axis='columns',how='all')
	df = df.dropna(axis='rows',how='any')

	df.to_excel('primaryNER.xlsx',index = False)



# Importing Data Sets 
df = pd.ExcelFile(r"/home/mohit/Desktop/Mini_project/primaryNER.xlsx")
df = pd.read_excel("/home/mohit/Desktop/Mini_project/primaryNER.xlsx",index_col = 1)


# Dividing of countries into region
Arabic = ['ARM','GEO','IRQ','JOR','KAZ','KGZ','OMN','PSE','SYR','TJK','TUR','TKM','UZB','YEM','UKR']

Asia_Pacific = ['AFG','AZE','BGD','BTN','CHN','KHM','IND','IDN','JPN','MDV','MNG','MMR','NPL','PAK',
'PHL','THA','VNM']
	
American_Region = ['ATG','BHS','BRB','BLZ','CAN','COL','CYM','CRI','CUB','CUW','DMA','DOM','SLV','GRL','GRD',
'GLP','GTM','HTI','HND','JAM','MTQ','MEX','SPM','MSR','ANT','KNA','NIC','PAN','PER','PRI','BES','BES','SXM',
'KNA','LCA','SPM','VCT','TTO','TCA','USA','VIR','VGB']
	
	
African_Region = ['DZA','AGO','SHN','BEN','BWA','BFA','BDI','CMR','CPV','CAF','TCD','COM','COG',
'COD','DJI','EGY','GNQ','ERI','ETH','GAB','GMB','GHA','GIN','GNB','CIV','KEN','LSO','LBR','LBY',
'MDG','MWI','MLI','MRT','MUS','MYT','MAR','MOZ','NAM','NER','NGA','STP','REU','RWA','STP','SEN','SYC',
'SLE','SOM','ZAF','SSD','SHN','SDN','SWZ','TZA','TGO','TUN','UGA','COD','ZMB','TZA','ZWE']

Rest = (Asia_Pacific+Arabic+American_Region+African_Region)

# For representing the countries
Arabic_countries = df.loc[df['ISO Code'].isin(Arabic)]
Asian_countries = df.loc[df['ISO Code'].isin(Asia_Pacific)]
African_countries = df.loc[df['ISO Code'].isin(African_Region)]
American_countries = df.loc[df['ISO Code'].isin(American_Region)]
Rest_countries = df.loc[df['ISO Code'].isin(Rest)]

# Taking Total Average
avg_Arabic = Arabic_countries['Total'].mean()
avg_Asian = Asian_countries['Total'].mean()
avg_African = African_countries['Total'].mean()
avg_American = American_countries['Total'].mean()
avg_rest = Rest_countries['Total'].mean()

Arabic_AVG = {'avg_Arabic':avg_Arabic}
a1 = pd.Series(Arabic_AVG)
a1 = pd.DataFrame(a1)
a1.columns = ['Total Average']

Asian_AVG = {'AV_Total_Asian':avg_Asian}
a2 = pd.Series(Asian_AVG)
a2 = pd.DataFrame(a2)
a2.columns = ['Total Average']

African_AVG = {'avg_African':avg_African}
a3 = pd.Series(African_AVG)
a3 = pd.DataFrame(a3)
a3.columns = ['Total Average']

American_AVG = {'avg_American':avg_American}
a4 = pd.Series(American_AVG)
a4 = pd.DataFrame(a4)
a4.columns = ['Total Average']

rest_AVG = {'avg_Other':avg_rest}
a5 = pd.Series(rest_AVG)
a5 = pd.DataFrame(a5)
a5.columns = ['Total Average']

Total_avg = [a1,a2,a3,a4,a5]
Total = pd.concat(Total_avg)
Total = pd.DataFrame(Total)
print(Total)

#plotting graph of gross enrolment ratio vs countries 
def graph():
	dataset =['Arabic countries','Asian countries','African countries','American countries','Rest of countries']
	var = sns.barplot(x=dataset, y='Total Average',data =Total,color = 'darkred')
	var.axes.set_title('Gross enrollment ratio(Country Wise)')
	var.set(xlabel='Countries', ylabel='Average Gross enrollment ratio')
	plt.show()




if __name__ == '__main__':
	sheet1()
	graph()
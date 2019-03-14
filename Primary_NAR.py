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


#Cleaning the dataset of primary net attendance ratio
def sheet2():
    df = pd.ExcelFile(r"/home/mohit/Desktop/Mini_project/primary_net_ratio.xlsx")
    df = df.parse('Primary NAR',skiprows = 9 )
    df = df.drop(df.index[197:219]) 
    df = df.drop('Source',axis =1)
    df = df.drop('Secondary Source',axis=1) 
    df = df.dropna(axis=1,how='all')
    df = df.dropna(axis=0,how='any')
    df.to_excel('PrimaryNAR.xlsx',index = False)

# Importing Data Sets 

df = pd.ExcelFile(r"/home/mohit/Desktop/Mini_project/PrimaryNAR.xlsx")
df = pd.read_excel("/home/mohit/Desktop/Mini_project/PrimaryNAR.xlsx")


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

Rest = Asia_Pacific+Arabic+American_Region+African_Region

# For representing the countries
Arabic_countries = df.loc[df['ISO Code'].isin(Arabic)]
Asian_countries = df.loc[df['ISO Code'].isin(Asia_Pacific)]
African_countries = df.loc[df['ISO Code'].isin(African_Region)]
American_countries = df.loc[df['ISO Code'].isin(American_Region)]
Rest_countries = df.loc[~df['ISO Code'].isin(Rest)]
#print(Arabic_countries)
#print(African_countries)
#print(American_countries)
#print(Rest_countries)

# Taking Total Average
def NAR():
    avg_Arabic = Arabic_countries['Total'].mean()
    avg_Asian = Asian_countries['Total'].mean()
    avg_African = African_countries['Total'].mean()
    avg_American = American_countries['Total'].mean()
    avg_rest = Rest_countries['Total'].mean()

    Arabic_AVG = {'Arabic':avg_Arabic}
    a1 = pd.Series(Arabic_AVG)
    a1 = pd.DataFrame(a1)
    a1.columns = ['Total Average']

    Asian_AVG = {'Asian':avg_Asian}
    a2 = pd.Series(Asian_AVG)
    a2 = pd.DataFrame(a2)
    a2.columns = ['Total Average']

    African_AVG = {'African':avg_African}
    a3 = pd.Series(African_AVG)
    a3 = pd.DataFrame(a3)
    a3.columns = ['Total Average']

    American_AVG = {'American':avg_American}
    a4 = pd.Series(American_AVG)
    a4 = pd.DataFrame(a4)
    a4.columns = ['Total Average']

    Rest_AVG = {'rest':avg_rest}
    a5 = pd.Series(Rest_AVG)
    a5 = pd.DataFrame(a5)
    a5.columns = ['Total Average']

    Total_avg = [a1,a2,a3,a4,a5]
    Total = pd.concat(Total_avg)
    Total = pd.DataFrame(Total)
    print(Total)

    dataset =['Arabic ','Asian ','African ','American ','Rest']
    var = sns.barplot(x=dataset, y='Total Average',data =Total,color = 'darkred')
    var.axes.set_title('Net attendance ratio(Country Wise)')
    var.set(xlabel='Countries', ylabel='Average Net attendance ratio')
    plt.show()

#calculating mean wealth quintile for all the countries
def asia():
    wq_poor_asia = math.floor(Asian_countries['WQ-Poor'].mean())
    wq_second_asia = math.floor(Asian_countries['WQ-Second'].mean())
    wq_middle_asia = math.floor(Asian_countries['WQ-Middle'].mean())
    wq_fourth_asia = math.floor(Asian_countries['WQ-Fourth'].mean())
    wq_richest_asia = math.floor(Asian_countries['WQ-Richest'].mean())
    asia = {'WQ-Poor': wq_poor_asia,
            'WQ-Second': wq_second_asia,
            'WQ-Middle': wq_middle_asia,
            'WQ-Fourth': wq_fourth_asia,
            'WQ-Richest': wq_richest_asia}
    
    d = pd.Series(asia)
    d = pd.DataFrame(d)
    d.columns=['asia']
    #print(d)
    
    #plot asian countries wrt wealth quintile
    objects = ('WQ(Poor)', 'WQ(Second)', 'WQ(Middle)', 'WQ(Fourth)', 'WQ(Richest)')
    y_pos = np.arange(len(objects))
    netrate  = [wq_poor_asia,wq_second_asia,wq_middle_asia,wq_fourth_asia,wq_richest_asia]
 
    plt.barh(y_pos, netrate, align='center', alpha=0.5, color=['darkblue','darkred','darkgreen','yellow','black'])
    plt.yticks(y_pos, objects)
    plt.title('Asian Countries')
    plt.xlabel('Net attendance %')
    for i, v in enumerate(netrate):
        plt.text(v + 3, i + .25, str(v)+"%", color='blue', fontweight='bold')
    plt.show()

def africa():
    wq_poor_africa = math.floor(African_countries['WQ-Poor'].mean())
    wq_second_africa = math.floor(African_countries['WQ-Second'].mean())
    wq_middle_africa = math.floor(African_countries['WQ-Middle'].mean())
    wq_fourth_africa = math.floor(African_countries['WQ-Fourth'].mean())
    wq_richest_africa = math.floor(African_countries['WQ-Richest'].mean())

    africa = {'WQ-Poor': wq_poor_africa,
            'WQ-Second': wq_second_africa,
            'WQ-Middle': wq_middle_africa,
            'WQ-Fourth': wq_fourth_africa,
            'WQ-Richest': wq_richest_africa}
    d = pd.Series(africa)
    d = pd.DataFrame(d)
    d.columns=['africa']
    #print(d)

    #plotting african countries wrt wealth quintile    
    objects = ('WQ(Poor)', 'WQ(Second)', 'WQ(Middle)', 'WQ(Fourth)', 'WQ(Richest)')
    y_pos = np.arange(len(objects))
    netrat1  = [wq_poor_africa,wq_second_africa,wq_middle_africa,wq_fourth_africa,wq_richest_africa] 
    plt.barh(y_pos, netrat1, align='center', alpha=0.5, color=['darkblue','darkred','darkgreen','yellow','black'])
    plt.yticks(y_pos, objects)
    plt.title('African Countries')
    plt.xlabel(' Net Attendance %')
    for i, v in enumerate(netrat1):
        plt.text(v + 3, i + .25, str(v)+"%", color='blue', fontweight='bold')
    plt.show()

def america():
	wq_poor_America = math.floor(American_countries['WQ-Poor'].mean())
	wq_second_America = math.floor(American_countries['WQ-Second'].mean())
	wq_middle_America = math.floor(American_countries['WQ-Middle'].mean())
	wq_fourth_America = math.floor(American_countries['WQ-Fourth'].mean())
	wq_richest_America = math.floor(American_countries['WQ-Richest'].mean())

	America = {'WQ-Poor': wq_poor_America,
				'WQ-Second': wq_second_America,
				'WQ-Middle': wq_middle_America,
				'WQ-Fourth': wq_fourth_America,
				'WQ-Richest': wq_richest_America}
	d = pd.Series(America)
	d = pd.DataFrame(d)
	d.columns=['American_countries']
	#print(d)

	#plotting south american countries wrt wealth quintile
	objects = ('WQ(Poor)', 'WQ(Second)', 'WQ(Middle)', 'WQ(Fourth)', 'WQ(Richest)')
	y_pos = np.arange(len(objects))
	netrat3  = [wq_poor_America,wq_second_America,wq_middle_America,wq_fourth_America,wq_richest_America]
	plt.barh(y_pos, netrat3, align='center', alpha=0.5, color=['blue','red','green','yellow','black'])
	plt.yticks(y_pos, objects)
	plt.title('American Countries')
	plt.xlabel(' Net Attendance %')
	for i, v in enumerate(netrat3):
		plt.text(v + 3, i + .25, str(v)+"%", color='blue', fontweight='bold')

	plt.show()

def arab():
    wq_poor_arab = math.floor(Arabic_countries['WQ-Poor'].mean())
    wq_second_arab = math.floor(Arabic_countries['WQ-Second'].mean())
    wq_middle_arab = math.floor(Arabic_countries['WQ-Middle'].mean())
    wq_fourth_arab = math.floor(Arabic_countries['WQ-Fourth'].mean())
    wq_richest_arab = math.floor(Arabic_countries['WQ-Richest'].mean())
    arab = {'WQ-Poor': wq_poor_arab,
            'WQ-Second': wq_second_arab,
            'WQ-Middle': wq_middle_arab,
            'WQ-Fourth': wq_fourth_arab,
            'WQ-Richest': wq_richest_arab}
    
    d = pd.Series(arab)
    d = pd.DataFrame(d)
    d.columns=['Arabic Countries']
    #print(d)

    #plot asian countries wrt wealth quintile
    objects = ('WQ(Poor)', 'WQ(Second)', 'WQ(Middle)', 'WQ(Fourth)', 'WQ(Richest)')
    y_pos = np.arange(len(objects))
    netrate  = [wq_poor_arab,wq_second_arab,wq_middle_arab,wq_fourth_arab,wq_richest_arab]
    plt.barh(y_pos, netrate, align='center', alpha=0.5, color=['darkblue','darkred','darkgreen','yellow','black'])
    plt.yticks(y_pos, objects)
    plt.title('Arabic Countries')
    plt.xlabel('Net attendance %')
    for i, v in enumerate(netrate):
        plt.text(v + 3, i + .25, str(v)+"%", color='blue', fontweight='bold')
    plt.show()

def rest():
    wq_poor_rest = math.floor(Rest_countries['WQ-Poor'].mean())
    wq_second_rest = math.floor(Rest_countries['WQ-Second'].mean())
    wq_middle_rest = math.floor(Rest_countries['WQ-Middle'].mean())
    wq_fourth_rest = math.floor(Rest_countries['WQ-Fourth'].mean())
    wq_richest_rest = math.floor(Rest_countries['WQ-Richest'].mean())
    rest = {'WQ-Poor': wq_poor_rest,
            'WQ-Second': wq_second_rest,
            'WQ-Middle': wq_middle_rest,
            'WQ-Fourth': wq_fourth_rest,
            'WQ-Richest': wq_richest_rest}
    
    d = pd.Series(rest)
    d = pd.DataFrame(d)
    d.columns=['Rest of countries']
    #print(d)
    
    #plot asian countries wrt wealth quintile
    objects = ('WQ(Poor)', 'WQ(Second)', 'WQ(Middle)', 'WQ(Fourth)', 'WQ(Richest)')
    y_pos = np.arange(len(objects))
    netrate  = [wq_poor_rest,wq_second_rest,wq_middle_rest,wq_fourth_rest,wq_richest_rest]
 
    plt.barh(y_pos, netrate, align='center', alpha=0.5, color=['darkblue','darkred','darkgreen','yellow','black'])
    plt.yticks(y_pos, objects)
    plt.title('Rest of Countries')
    plt.xlabel('Net attendance %')
    for i, v in enumerate(netrate):
        plt.text(v + 3, i + .25, str(v)+"%", color='blue', fontweight='bold')
    plt.show()

#Creating world map consisting of primary attendance ratio
def worldmapNAR():
    plotly.tools.set_credentials_file(username='mohit_awana', api_key='etlxovt5BLTXK5xRRn13')
    df = pd.read_excel('/home/mohit/Desktop/Mini_project//PrimaryNAR.xlsx')
    data = dict(
           type = 'choropleth',
           locations = df['ISO Code'],
           z = df['Total'],
           text = df['Countries'],
           colorscale = [[0,'rgb(5, 10, 172)'],[0.35,"rgb(106, 137, 247)"],[0.5,"rgb(190,190,190)"],\
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
    py.iplot( fig, validate=False, filename='PrimaryNetAttendanceRate_map')    


#Plotting a bargraphs using nvd3 of countries vs wealth quintile
def wealthquintileNAR():
    output_file = open('net_attendance_rate_nvd3.html', 'w')
    chart = multiBarChart(width=1000, height=400, x_axis_format=None,color = 'green')
    data = ['Poorest','Second','Middle','Fourth','Richest']
    Arabic_countries =[92,95,96,97,97.]
    Asian_countries = [81,86,89,90,92]
    African_countries = [62,69,75,82,88]
    American_countries = [91,94,95,96,97]
    rest_countries = [89,91,92,92,94]

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
    sheet2()
    NAR()
    asia()
    africa()
    america()
    arab()
    rest()
    worldmapNAR()
    wealthquintileNAR()
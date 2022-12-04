# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 16:11:24 2022

@author: Usuario
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd


## We read the data and convert it to a pandas data frame

pm_df = pd.read_csv(r"C:/Users\Usuario/Desktop\Apuntes/Master/Anal_y_Visa/Proyecto-Contaminacion-Aire-main/datosPM.csv",
                          index_col=0, header=0)

## We add a column to our data frame with the maximum value of the concentration
#  of pm10 of each day

pm_df["hmax"]=pm_df[['h05', 'h06','h07', 'h08','h09', 
                         'h11','h12', 'h13','h14','h15', 'h16', 'h17','h18', 
                         'h19','h20','h21', 'h22','h23','h24']].max(axis=1)



## We drop rows which correspond to days in which all the measurements taken
#  are nan

pm_df = pm_df.dropna(subset=["hmax"])



## We flip the data set, so we have it chronologically from the begining

pm_df = pm_df.iloc[::-1]



## We define the column "data" as a datetime column, so we can extract
#  information about the time of the measurements.

pm_df['data'] = pd.to_datetime(pm_df.data, format = '%Y-%m-%dT%H:%M:%S')



## We define subdata frames, one for each metering station

hebron_df = pm_df.loc[pm_df['altitud'] == 136]

gracia_df = pm_df.loc[pm_df['altitud'] == 57]

#llobregat_df = pm_df.loc[pm_df['altitud'] == 29]

eixample_df = pm_df.loc[pm_df['altitud'] == 26]

fabra_df = pm_df.loc[pm_df['altitud'] == 415]

palau_df = pm_df.loc[(pm_df['altitud'] == 81) & (pm_df['magnitud'] == 10)]

#palau_pm25_df = pm_df.loc[pm_df['magnitud'] == 9]

poblenou_df = pm_df.loc[pm_df['altitud'] == 3]

#besos_df = pm_df.loc[pm_df['altitud'] == 7]


## Now we separate the data frames again per year.

hebron2019_df = hebron_df[hebron_df.data.dt.year.eq(2019)]
hebron2020_df = hebron_df[hebron_df.data.dt.year.eq(2020)]
hebron2021_df = hebron_df[hebron_df.data.dt.year.eq(2021)]
hebron2022_df = hebron_df[hebron_df.data.dt.year.eq(2022)]
hebroncovid_df = hebron_df.loc[(hebron_df['data'] > '2020-03-15'
            ) & (hebron_df['data'] < '2020-05-01')]   ## To see how covid affected



gracia2019_df = gracia_df[gracia_df.data.dt.year.eq(2019)]
gracia2020_df = gracia_df[gracia_df.data.dt.year.eq(2020)]
gracia2021_df = gracia_df[gracia_df.data.dt.year.eq(2021)]
gracia2022_df = gracia_df[gracia_df.data.dt.year.eq(2022)]
graciacovid_df = gracia_df.loc[(gracia_df['data'] > '2020-03-15'
            ) & (gracia_df['data'] < '2020-05-01')]



eixample2019_df = eixample_df[eixample_df.data.dt.year.eq(2019)]
eixample2020_df = eixample_df[eixample_df.data.dt.year.eq(2020)]
eixample2021_df = eixample_df[eixample_df.data.dt.year.eq(2021)]
eixample2022_df = eixample_df[eixample_df.data.dt.year.eq(2022)]
eixamplecovid_df = eixample_df.loc[(eixample_df['data'] > '2020-03-15'
            ) & (eixample_df['data'] < '2020-05-01')]


fabra2019_df = fabra_df[fabra_df.data.dt.year.eq(2019)]
fabra2020_df = fabra_df[fabra_df.data.dt.year.eq(2020)]
fabra2021_df = fabra_df[fabra_df.data.dt.year.eq(2021)]
fabra2022_df = fabra_df[fabra_df.data.dt.year.eq(2022)]
fabracovid_df = fabra_df.loc[(fabra_df['data'] > '2020-03-15'
            ) & (fabra_df['data'] < '2020-05-01')]


palau2019_df = palau_df[palau_df.data.dt.year.eq(2019)]
palau2020_df = palau_df[palau_df.data.dt.year.eq(2020)]
palau2021_df = palau_df[palau_df.data.dt.year.eq(2021)]
palau2022_df = palau_df[palau_df.data.dt.year.eq(2022)]
palaucovid_df = palau_df.loc[(palau_df['data'] > '2020-03-15'
            ) & (palau_df['data'] < '2020-05-01')]


poblenou2019_df = poblenou_df[poblenou_df.data.dt.year.eq(2019)]
poblenou2020_df = poblenou_df[poblenou_df.data.dt.year.eq(2020)]
poblenou2021_df = poblenou_df[poblenou_df.data.dt.year.eq(2021)]
poblenou2022_df = poblenou_df[poblenou_df.data.dt.year.eq(2022)]
poblenoucovid_df = poblenou_df.loc[(poblenou_df['data'] > '2020-03-15'
            ) & (poblenou_df['data'] < '2020-05-01')]



## Now we get the mean values of the concentrations of each year for each
#  station using numpy

hebron2019 = np.mean(hebron2019_df["hmax"])
hebron2020 = np.mean(hebron2020_df["hmax"])
hebron2021 = np.mean(hebron2021_df["hmax"])
hebron2022 = np.mean(hebron2022_df["hmax"])
hebroncovid = np.mean(hebroncovid_df["hmax"])

gracia2019 = np.mean(gracia2019_df["hmax"])
gracia2020 = np.mean(gracia2020_df["hmax"])
gracia2021 = np.mean(gracia2021_df["hmax"])
gracia2022 = np.mean(gracia2022_df["hmax"])
graciacovid = np.mean(graciacovid_df["hmax"])

eixample2019 = np.mean(eixample2019_df["hmax"])
eixample2020 = np.mean(eixample2020_df["hmax"])
eixample2021 = np.mean(eixample2021_df["hmax"])
eixample2022 = np.mean(eixample2022_df["hmax"])
eixamplecovid = np.mean(eixamplecovid_df["hmax"])

fabra2019 = np.mean(fabra2019_df["hmax"])
fabra2020 = np.mean(fabra2020_df["hmax"])
fabra2021 = np.mean(fabra2021_df["hmax"])
fabra2022 = np.mean(fabra2022_df["hmax"])
fabracovid = np.mean(fabracovid_df["hmax"])

palau2019 = np.mean(palau2019_df["hmax"])
palau2020 = np.mean(palau2020_df["hmax"])
palau2021 = np.mean(palau2021_df["hmax"])
palau2022 = np.mean(palau2022_df["hmax"])
palaucovid = np.mean(palaucovid_df["hmax"])

poblenou2019 = np.mean(poblenou2019_df["hmax"])
poblenou2020 = np.mean(poblenou2020_df["hmax"])
poblenou2021 = np.mean(poblenou2021_df["hmax"])
poblenou2022 = np.mean(poblenou2022_df["hmax"])
poblenoucovid = np.mean(poblenoucovid_df["hmax"])




## Now we plot these mean values in a bar diagram with matplotlib



## We set the lists to be plotted

regiones = ["Hebron", "Gràcia", "Eixample",       ## X axis
            "Fabra", "Palau Reial", "Poblenou"]  

valores2019 = [hebron2019, gracia2019, eixample2019, fabra2019, palau2019,
               poblenou2019]  ## 2019 mean values

valores2020 = [hebron2020, gracia2020, eixample2020, fabra2020, palau2020,
               poblenou2020]  ## 2020 mean values

valores2021 = [hebron2021, gracia2021, eixample2021, fabra2021, palau2021,
               poblenou2021]  ## 2021 mean values

valores2022 = [hebron2022, gracia2022, eixample2022, fabra2022, palau2022,
               poblenou2022]  ## 2022 mean values

valorescovid = [hebroncovid, graciacovid, eixamplecovid, fabracovid,
                palaucovid, poblenoucovid]  ## Covid period mean values


barWidth = 0.25         ## Width of the plot bars
X = np.arange(0, 12, 2)  ## List to display the names of the stations on the x axis
plt.figure(figsize=(8,6))
plt.bar(X, valores2019, color="greenyellow", width=barWidth, label=2019)
plt.bar(X+0.25, valores2020, color="yellowgreen", width=barWidth, label=2020)
plt.bar(X+0.5, valores2021, color="limegreen", width=barWidth, label=2021)
plt.bar(X+0.75, valores2022, color="olive", width=barWidth, label=2022)
plt.bar(X+1, valorescovid, color="darkolivegreen", width=barWidth, label="Lockdown")
plt.xticks([x+1.5*barWidth for x in X], regiones)
plt.grid('on', linestyle='--', linewidth=1, alpha=0.7)
plt.xlabel("Metering station", fontsize = 13)
plt.ylabel("PM10 Concentration/(µg/$m^{3}$)", fontsize = 13)
plt.legend(loc='best')
plt.title("Mean value of PM10 concentration", fontsize = 15)



#%%


import folium
import webbrowser
import os




## Folium Map

mymap = folium.Map(
    location=[41.399916, 2.166029],
    zoom_start=12,
    tiles='OpenStreetMap')

## We open the geojson with the shape of the districts of Barcelona

HOME = 'C:/Users/Usuario/Desktop/Apuntes/Master/Anal_y_Visa/Proyecto-Contaminacion-Aire-main'
DATA = os.path.join(HOME, 'districtes.geojson')

## We read the geojson file

comunidades = gpd.read_file(DATA)

## We translate the file to json

geoPath = comunidades.geometry.to_json()

## We assign the poligons in the file to a variable

poligonos=folium.features.GeoJson(geoPath)


## We add the shapes of the districts of Barcelona to my map

mymap.add_child(poligonos)

## We add markers for each station on the map

## We define a new data frame with the stations just once, to have the locations
#  of each one, to be able to add them to the map but just one time each

map_df = pm_df.head(7)      
map_df = map_df.drop(8194008) 

## Now we iterate to add the markers

for i, row in map_df.iterrows():
    
    iframe = folium.IFrame(row["nom_estacio"])
    
    popup = folium.Popup(iframe, min_width=300, max_width=300)

    folium.Marker(location=[row['latitud'],row['longitud']],
                  icon=folium.Icon(color='red' ,
                icon='fa-thin fa-location-dot')).add_to(mymap)

## We save the map and we open it

mymap.save("map.html")
webbrowser.open("map.html")







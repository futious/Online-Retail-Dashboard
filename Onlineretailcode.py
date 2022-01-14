#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 08:11:46 2021

@author: koreynishimoto
"""


import pandas as pd

import numpy as n
import pandas as pd

import numpy as np
from numpy import mean
from numpy import std

import matplotlib.pyplot as plt


from sklearn.model_selection import GridSearchCV
from sklearn_evaluation import plot


from sklearn.linear_model import LogisticRegression 
lr = LogisticRegression(max_iter=1000,C=1)


from sklearn.naive_bayes import GaussianNB
g=GaussianNB()

from sklearn.svm import SVC 
clf = SVC(max_iter=100000, C=1000)


from sklearn.model_selection import KFold

from sklearn.model_selection import cross_val_score


from sklearn import tree
dt = tree.DecisionTreeClassifier(max_depth=10)


import dash
from dash import dcc

from dash import html
from dash.dependencies import Input, Output

from pandas.io.formats import style


import plotly.express as px

app = dash.Dash(__name__)

import pycountry
import geopandas as gpd
import datetime
import dash_bootstrap_components as dbc






#################################################################################################
########################################################################
########################################################################


df = pd.read_csv('/Users/koreynishimoto/Desktop/Retail/'
                   +'OnlineRetail.csv', index_col=False)


colors = {"background": "#011833", "text": "#7FDBFF"}


#Remove Time of sale and keep date
df['InvoiceDate']=df['InvoiceDate'].str.split(expand=True)[0]
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

#Remove European Community Rows.Group of six European countries. 61 rows
#Remove Unspecified Countries. 466 rows
df = df.loc[df['Country']!='European Community']
df = df.loc[df['Country']!='Unspecified']

#Clean Countries to Have ISO Code

df['Country'] = df['Country'].str.replace('EIRE', 'Ireland')
df['Country'] = df['Country'].str.replace('Channel Islands','United Kingdom')
df['Country'] = df['Country'].str.replace('Czech Republic', 'Czechia')
df['Country'] = df['Country'].str.replace('USA', 'United States')
df['Country'] = df['Country'].str.replace('RSA', 'South Africa')



countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha_3

df['Country Code'] = [countries.get(country, 'Unknown code') for country in df['Country'] ]

df['Total Sales'] = df['Quantity'].multiply(df['UnitPrice'],fill_value=0)


#Make new data frame for mapping dollar amount and number of sales
 
mapdf = pd.DataFrame()
mapdf['Country'] = df['Country'].unique()
mapdf['Country Code'] = [countries.get(country, 'Unknown code') for country in mapdf['Country'] ]
mapdf = mapdf.join(df['Country'].value_counts(), on='Country', lsuffix='', rsuffix =' Count')




# Quantity of sales per day

#quantity = df.groupby(by='InvoiceDate')['Quantity'].sum().fillna(0).reset_index(drop=False)
#quantity['Month'] = quantity['InvoiceDate'].dt.month
#quantity['Year'] = quantity['InvoiceDate'].dt.year

quantity = df.groupby(by=['InvoiceDate', 'Country'])['Quantity'].sum().reset_index(drop=False)

totalsales = df.groupby(by=['InvoiceDate', 'Country'])['Total Sales'].sum().reset_index(drop=False)



###Finding best customer based on sales and customer id###

customer = df.groupby(by=['CustomerID'])['Total Sales'].sum().reset_index(drop=False)




################ ################ ################ ################ ################ ################ ################ ################ 
################ ################ ################ ################ ################ 
################ ################ ################ ################ ################ 


###type of graphs###

mapfig = px.choropleth(data_frame = mapdf, 
                    locations = 'Country Code',
                    locationmode = 'ISO-3',
                    color = "Country Count",
                    #color_continuous_scale=px.colors.sequential.Plotly3,
                    hover_name = "Country",  
                    height = 800,
                    range_color = (0,1000),
                    )

total = px.line(data_frame = quantity,
             x = 'InvoiceDate',
             y = 'Quantity',            
             )


top_customers = px.bar(data_frame = customer,
             x = 'CustomerID',
             y = 'Total Sales',
             orientation = 'h'            
             )

items = px.scatter(data_frame = df,
             x = 'InvoiceDate',
             y = 'Quantity',            
             )

#############################################################################



###Layout of graphs###


app.layout = html.Div([
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    
    dcc.Graph(
        id='Map',
        figure=mapfig
    ),
    

 
  
html.Div([   
    
    html.Div([
        html.Label("Information Type"),
    dcc.Dropdown(
        id='category',
        options=[{'label': y, 'value': y }
                 for y in ['Total Sales','Quantity']
                 ],
        value = 'Total Sales',
        className="dropdown",
        ),
    
    ], style={ 'padding' :10,'flex':1} 
        ),
    
    html.Div([
        html.Label("Country"),
    dcc.Dropdown(
        id = 'fig_dropdown',
        options = [{'label': y, 'value': y }
                 for y in quantity['Country']
                 ],
        value ='United Kingdom',
        className = "dropdown",
        ),
    ], style={ 'padding' :10,'flex':1}  
        ),
    
     
     
    ], style={'display': 'flex','flex-direction':'row'}
    ),
    
    
   html.Div([
      dcc.Graph(
        id = 'example-graph0',
        figure = total,
        
        ),

]),     
   
  
### Horizontal bar chart for top customers ###
html.Div([ 
        
    html.Div([
        html.Label("Top x Customers"),
    dcc.Dropdown(
        id = 'top',
        options = [{'label': y, 'value': y }
                 for y in [1,2,3,4,5,6,7,8,9,10]
                 ],
        value = 5,
        className = "dropdown",
        ),
    ]   
        ),
   
    html.Div([
      dcc.Graph(
        id = 'horizontal-bar',
        figure = top_customers,
        
        ),

]), 

]),
   



###scatter plot for items puchased###

html.Div([ 
        
    html.Div([
        html.Label("Item"),
    dcc.Dropdown(
        id = 'item_name',
        options =  [{'label': y, 'value': y }
                 for y in  df['Description'].drop_duplicates().dropna()
                 ],
        
        value = 'WHITE HANGING HEART T-LIGHT HOLDER',
        className = "dropdown",
        ),
    ]   
        ),
   
    html.Div([
      dcc.Graph(
        id = 'item_scatter',
        figure = items,
        
        ),

]), 

]),



    
    
  ])
             
###What gets returned based on interactive materials###
             
@app.callback(
    Output(component_id='example-graph0', component_property='figure'),
    Input(component_id='fig_dropdown', component_property='value'),
    Input(component_id='category', component_property='value')
      
)


def update_graph(fig_dropdown,category):
   
    dff1 = df.groupby(by=['InvoiceDate', 'Country'])[category].sum().reset_index(drop=False)
    dff1 = dff1[dff1['Country'] == fig_dropdown]

       
    linechart1 = px.line(
        data_frame=dff1,
        x = 'InvoiceDate',
        y = category,
       # range_x=dff1['InvoiceDate'].min(), == dff1['InvoiceDate'].max()],
        #range_y=dff1[category].min(),quantity[quantity['Country'] == dff1[category].max()],

        )
       
    linechart1.update_layout(
        plot_bgcolor=colors["background"],
        paper_bgcolor=colors["background"],
        font_color=colors["text"],
    )
    


    return linechart1 


@app.callback(
Output(component_id='horizontal-bar', component_property='figure'),
Input(component_id='top', component_property='value'), 
)

def update_hgraph(top): 
  
    dff3 = customer.sort_values('Total Sales',ascending=False)[:top].sort_values('Total Sales',ascending=True)
    dff3['CustomerID'] = dff3['CustomerID'].astype(int).astype(str)     
    hlinechart = px.bar(
        data_frame=dff3,
        x = 'Total Sales',
        y = 'CustomerID',
        orientation = 'h'
        )

            

    hlinechart.update_layout(
        plot_bgcolor=colors["background"],
        paper_bgcolor=colors["background"],
        font_color=colors["text"],
     )
    


    return hlinechart



@app.callback(
Output(component_id='item_scatter', component_property='figure'),
Input(component_id='item_name', component_property='value'), 
)
 
def update_sgraph(item_name): 
  
    dff4 = df.groupby(by=['Description','InvoiceDate'])['Quantity'].sum().reset_index(drop=False) 
    dff4=dff4[dff4['Description']==item_name]
    
    scatterchart = px.scatter(
        data_frame=dff4,
        x = 'InvoiceDate',
        y = 'Quantity',
        )

            

    scatterchart.update_layout(
        plot_bgcolor=colors["background"],
        paper_bgcolor=colors["background"],
        font_color=colors["text"],
     )
    


    return scatterchart

         
                   
                   
 
if __name__ == '__main__':
        app.run_server(host = '127.0.0.1', debug=True, port = 8060)                  
                   
                  
itemname.to_csv('/Users/koreynishimoto/Desktop/itemname.csv', index = False)
                   
                   
                   
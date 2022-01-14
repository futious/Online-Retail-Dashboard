#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 09:04:47 2021

@author: koreynishimoto
"""

import pandas as pd

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_table

import plotly.express as px
import pycountry
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)




app = dash.Dash(
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                suppress_callback_exceptions=True,
      )

app.title = 'Online Retail and Distibution'


#################################################################################################
########################################################################
########################################################################


df = pd.read_csv('OnlineRetail.csv', index_col=False, encoding = "ISO-8859-1")


colors = {"background": "#011833", "text": "#7FDBFF"}

template = 'plotly_dark'


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
                    
mapfig.update_layout(
            plot_bgcolor="#011833",
            paper_bgcolor="#022248",
            geo_bgcolor="#011833",
            font=dict(color="white"),
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




# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#022248",
    "text": "#7FDBFF",
    
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "1rem 1rem",
    "background-color": "#022248",
    "text": "#7FDBFF",
    'borderWidth':0,
   
}




sidebar = html.Div(
    [
        html.H2("Online Sales", className="display-4"),
        html.Hr(),
        html.P(
            "Pick a category you would like displayed", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Item Information", href="/Item-Information", active="exact"),
                dbc.NavLink("Customer Information", href="/Customer-Information", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
        
        
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)


app.layout = html.Div([dcc.Location(id="url"), sidebar, content],
                      style={'backgroundColor': colors['background'],
                             'color': colors['text'],
                             
                             },)




@app.callback(Output("page-content", "children"),
              [Input("url", "pathname")])


def render_page_content(pathname):
    if pathname == "/":
        return [ 
            html.H1('Online Sales and Distribution'),
            
         
            html.P('This dashboard will be used to show visual representations of data. Below is the pertinent information.'
                   +' For a more detailed visual representation use the side bar to navigate.',
                   style={'display': 'inline-block'}),
            
            html.Div('This dashboard will be used to show visual representations of data. Below is the pertinent information.'
                     +' For a more detailed visual representation use the side bar to navigate.',
                   ),
                
            
            
            
            dbc.Row([
            
                dbc.Col(
                    
                    dbc.CardImg(src=app.get_asset_url('img1.jpg'),
                    style={'height':'6cm'}),
                    
                    ),
                
                dbc.Col(
                    dbc.Card(
                            dbc.CardBody(
                                [  
                                    html.H5("Card title", className="card-title"),
                                    html.P(
                                        "This card also has some text content and not much else, but "
                                        "it is twice as wide as the first card."
                                        ),
                                    dbc.Button("Go somewhere", id= 'Button-1', color="primary"),
                                    ]
                                ),
                            style={'backgroundColor': "#011833",'height':'6cm'},
                          ),
                  width=8
                  )
                
                    ],
                    
                ),
        
            
#tables on page one

            dash_table.DataTable(
                    id='table',
                    columns=[
                        {'name': 'Category',
                         'id': 'column1'
                         },
                        {'name': 'Info',
                         'id': 'column2'
                         },
                        
                        ],
                    data=[
                        {'column1': 'Best Customer','column2': list(customer.sort_values('Total Sales',ascending=False).iloc[0].index)[0] + ' ' + str(customer.sort_values('Total Sales',ascending=False).iloc[0].iloc[0]) + ' with ' + list(customer.sort_values('Total Sales',ascending=False).iloc[1].index)[1] + ' by dollars ' + str(customer.sort_values('Total Sales',ascending=False).iloc[1].iloc[1]) },
                        {'column1': 'Highest Gross by Country' ,'column2': list(mapdf.iloc[0])[0] + ' Total sales by units sold ' + str(list(mapdf.iloc[0])[2])},
                        {'column1': 'Most Sold Item' ,'column2': df.groupby(by='Description').sum()['Quantity'].sort_values()[-1:].index[0] + ' Total sales by units sold ' + str(df.groupby(by='Description').sum()['Quantity'].sort_values()[-1])},
                        {'column1': 'Highest Grossing Item' ,'column2': 'Item Name: ' + df.groupby(by=['Description']).sum()['Total Sales'].sort_values().reset_index(drop=False)[-1:]['Description'].iloc[0] + ' total sales by dollars ' + str(int(df.groupby(by=['Description']).sum()['Total Sales'].sort_values().iloc[-1:]))},
                       
                      
                    ],
                    
                    page_action='none',
                    fixed_rows={'headers': True},
                    style_table={'height': '200px', 'overflowY': 'auto'},
                    style_header={'backgroundColor': 'rgb(30, 30, 30)','color': 'white'},
                    style_data={'backgroundColor': 'rgb(50, 50, 50)','color': 'white'},
            ),
            
      
            
            
        ]
            
    
    
    
    elif pathname == "/Item-Information":
        
        return [
            html.P("This is the content of page 1. Yay!"),
            
           
            html.H1(children='Hello Dash'),

            html.Div(children='Dash: A web application framework for your data.'
            ),
    
    
    
    #map#
            html.Div(
                dcc.Graph(
                    id='Map',
                    figure=mapfig,
                  
                ),
            ),
            
             
            
                     
    #sales vs quantity line graph#
                 
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
                
            
  #scatterplot#          
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
            
            ]),
   
            html.Div([
                dcc.Graph(
                    id = 'item_scatter',
                    figure = items,
        
                    ),

            ]), 

        ]),
                
                  
                             
        ]
         
                    
                     
    


    elif pathname == "/Customer-Information":


        return [
            html.P("Oh cool, this is page 2!"),
            
                 
            
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
    
            ]
    
            
                
            
    
    
##############################################################################
##############################################################################
    # If the user tries to reach a different page, return a 404 message
    
    
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


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
                #range_x=dff1['InvoiceDate'].min(), == dff1['InvoiceDate'].max()],
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
        app.run_server(host = '127.0.0.1', debug=True, port = 8070) 
    
from dash.dependencies import Input, Output

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table, read_csv, legend_font
# from misc.mekko import value
import plotly.express as px

from app import app
import time
import pandas as pd
import numpy as np
import pathlib

from misc.mekko import summarize_data_2, draw_mekko_2, get_same_percentile_total_bins

from misc.languages import pages, find_language_in_url




# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df = read_csv(DATA_PATH.joinpath("2 - risco_cred_e_cadastro_short.csv"), encoding='utf=8')
class_names = ['Select all'] + df.DSC_CLASSE.unique().tolist()
localities = ['Select all'] + df.groupby('NOME_LOCALIDADE').NOME_LOCALIDADE.count().sort_values(ascending=False).index.tolist()
cidades = ['Select all'] + ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
equipes = ['Select all'] + ['Equipe 1', 'Equipe 2', 'Equipe 3']

def create_layout(app, language):
  

    page_texts = pages['routing'][language]  
  
    return html.Div(
        [
            Header(app, language),
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Module Summary"),
                                    html.Br([]),
                                    html.P(
                                        '\
                                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor \
                                        incididunt ut labore et dolore magna aliqua.',
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="red-box",
                            )
                        ],
                        className="row"
                    ),

                    html.Div([
                            html.H6([page_texts['graph_titles'][0]], className="subtitle padded"),
                            dcc.Dropdown(
                                id='cidades-dropdown',
                                options=[{'label':name, 'value':name} for name in cidades],
                                value = cidades[0],
                                multi=False,
                                style={'padding-left': '20px', 'padding-bottom': '20px'}, 
                                className='center'
                                #className="six columns"
                            ),
                            html.H6([page_texts['graph_titles'][1]], className="subtitle padded"),
                                dcc.Dropdown(
                                id='equipe-dropdown',
                                options=[{'label':name, 'value':name} for name in equipes],
                                value = equipes[0],
                                multi=False,
                                style={'padding-left': '20px', 'padding-bottom': '20px'}, 
                            className='center'
                                #className="six columns"
                                )
                            ],
                        #className= 'row',   
                        ),
                    html.Div([
                            html.H6(page_texts['texts'][0],
                            id='mapas',
                            #options=[{'label':name, 'value':name} for name in risk_levels],
                            #value = risk_levels[0],
                            #multi=False,
                            style={'padding-left': '20px', 'padding-bottom': '20px'}, 
                            className='center'
                            )
                        ],
                    ),
                ],    
                    className="sub_page"
            )
        ],
                className="page",
    )
@app.callback(
    Output('mapas', component_property='children'),
    
    [Input('url', 'pathname')]
)
def overview_mekkos(url):
     language = find_language_in_url(url)
     page_texts = pages['routing'][language]

     filtered_df = df.copy()

     x_bins = np.linspace(0, 1, 6)

     mekko_1_pivot = summarize_data_2(filtered_df, y_bins=None, y_col='DSC_CLASSE', x_bins=x_bins, x_col='PD_Default30', value_col='debito_total')
     mekko_2_pivot = summarize_data_2(filtered_df, y_bins=None, y_col='DSC_CLASSE', x_bins=x_bins, x_col='PD_Default30', value_col=None)

     mekko_1 = draw_mekko_2(mekko_1_pivot)
     mekko_2 = draw_mekko_2(mekko_2_pivot)
    
     graphs = [
         html.Div([
             html.H6([page_texts['graph_titles'][2]], className="subtitle padded"),
             dcc.Graph(figure=mekko_1)
             ],
             className="six columns",
         ),
         html.Div([
             html.H6([page_texts['graph_titles'][3]], className="subtitle padded"),
             dcc.Graph(figure=mekko_2)
             ],
             className="six columns",
         ),
     ]

     return graphs


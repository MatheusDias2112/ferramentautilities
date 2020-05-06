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
risk_levels = ['Select all'] + ['0-20%', '20-40%', '40-60%', '60-80%', '80-100%']
valores_saldo = ['Select all'] + ['R$0-R$100', 'R$100-R$200', 'R$200-R$300', 'R$300-R$400', '>R$400' ]
tipo_acao = ['Select all'] + ['Telecobrança', 'SMS', 'E-mail']
interval = ['Digite um Valor']
def create_layout(app, language):

    page_texts = pages['action_optimization'][language]

    # Page layouts
    return html.Div(
        
        [
            Header(app, language),
            # page 1
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5(page_texts['titles'][0]),
                                    html.Br([]),
                                    html.P(
                                        page_texts['titles'][1],
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="red-box",
                            )
                        ],
                        className="row",
                    ),
                    html.Div([
                                html.H6(page_texts['texts'][1]),
                                dcc.Dropdown(
                                    id='tipo-ação-dropdown',
                                    options=[{'label':name, 'value':name} for name in tipo_acao],
                                    value = tipo_acao[0],
                                    multi=False
                                )
                            ]
                        ),

                     html.Div([
                                html.H6(page_texts['texts'][2]),
                                dcc.Input(
                                    id='intervalo-valores-input1',
                                    type = "number",
                                    #options=[{'label':name, 'value':name} for name in tipo_acao],
                                    placeholder = "Início",
                                    #multi=False
                                )
                            ]
                        ),

                           html.Div([
                                #html.H6(page_texts['texts'][3]),
                                dcc.Input(
                                    id='intervalo-valores-input2',
                                    type = "number",
                                    #options=[{'label':name, 'value':name} for name in tipo_acao],
                                    placeholder = "Fim",
                                   # multi=False
                                )
                            ]
                        ),

                    # Row 2
                    html.Div([
                        html.Div(
                            children=[],
                            id='Ganho e Custo por Ação',
                            className="row",
                            style={"margin-bottom": "35px"}
                            )
                        ]
                    ),
                    html.Div([
                        html.Div(
                            children=[],
                            id='Efetividade por Ação',
                            className="row",
                            style={"margin-bottom": "35px"},
                            )
                        ], 
                    id='results-container'
                    )
                ],
                className="sub_page",
            )
        ],
        className="page"
    )
@app.callback(
    Output('Efetividade por Ação', component_property='children'),
    
    
    [Input('url', 'pathname')]
)
def overview_mekkos_9(url):
     language = find_language_in_url(url)
     page_texts = pages['action_optimization'][language]

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

@app.callback(
    Output('Ganho e Custo por Ação', component_property='children'),
    
    
    [Input('url', 'pathname')]
)

def overview_mekkos_9_2(url):
     language = find_language_in_url(url)
     page_texts = pages['action_optimization'][language]

     filtered_df = df.copy()

     x_bins = np.linspace(0, 1, 6)

     mekko_1_pivot = summarize_data_2(filtered_df, y_bins=None, y_col='DSC_CLASSE', x_bins=x_bins, x_col='PD_Default30', value_col='debito_total')
     mekko_2_pivot = summarize_data_2(filtered_df, y_bins=None, y_col='DSC_CLASSE', x_bins=x_bins, x_col='PD_Default30', value_col=None)

     mekko_1 = draw_mekko_2(mekko_1_pivot)
     mekko_2 = draw_mekko_2(mekko_2_pivot)
    
     graphs = [
         html.Div([
             html.H6([page_texts['graph_titles'][0]], className="subtitle padded"),
             dcc.Graph(figure=mekko_1)
             ],
             className="six columns",
         ),
         html.Div([
             html.H6([page_texts['graph_titles'][1]], className="subtitle padded"),
             dcc.Graph(figure=mekko_2)
             ],
             className="six columns",
         ),
     ]

     return graphs


# # @app.callback(
# #     Output('efetividade_prevista', component_property='children'),
# #     [
# #      Input('url', 'pathname')
# #     ]
# # )
# # def update_mekkos(url):
# #     language = find_language_in_url(url)
# #     page_texts = pages['effectiveness'][language]

# #     filtered_df = df.copy()

# #     x_bins = np.linspace(0, 1, 6)

# #     mekko_1_pivot = summarize_data_2(filtered_df, y_bins=None, y_col='DSC_CLASSE', x_bins=x_bins, x_col='PD_Default30', value_col='debito_total')
# #     mekko_2_pivot = summarize_data_2(filtered_df, y_bins=None, y_col='DSC_CLASSE', x_bins=x_bins, x_col='PD_Default30', value_col=None)

# #     mekko_1 = draw_mekko_2(mekko_1_pivot)
# #     mekko_2 = draw_mekko_2(mekko_2_pivot)

# #     graphs = [
# #         html.Div([
# #             html.H6([page_texts['graph_titles'][2]], className="subtitle padded"),
# #             dcc.Graph(figure=mekko_1)
# #             ],
# #             className= 'center',   #"six columns",
# #         ),
# #         # html.Div([
# #         #     html.H6([page_texts['graph_titles'][5]], className="subtitle padded"),
# #         #     dcc.Graph(figure=mekko_2)
# #         #     ],
# #         #     className="six columns",
# #         # ),
# #     ]

# #     return graphs


# # # @app.callback(
# # #     Output('credit_risk_result_graphs', component_property='children'),
# # #     [Input('class-dropdown', 'value'),
# # #      Input('locality-dropdown', 'value'), 
# # #      Input('url', 'pathname')]
# # # )
# # # def update_graphs(selected_class, selected_locality, url):
# # #     language = find_language_in_url(url)
# # #     page_texts = pages['credit_risk'][language]

# # #     if selected_class == 'Select all':
# # #         filtered_df = df
# # #     else:
# # #         filtered_df = df[df.DSC_CLASSE == selected_class]
    
# # #     if selected_locality == 'Select all':
# # #         filtered_df = filtered_df
# # #     else:
# # #         filtered_df = filtered_df[filtered_df.NOME_LOCALIDADE == selected_locality]

# # #     data = [0] + filtered_df.PD_Default30.values.tolist() + [1]
# # #     fig_hist = {
# # #         'data': [
# # #             {
# # #                 'x': data,
# # #                 'name': 'Open Date',
# # #                 'type': 'histogram',
# # #                 'marker': {"color": "#cc0000"},
# # #                 'nbinsx': 25, 
# # #                 'xbins': {'start': 0,  'end': 1}
# # #             }
# # #         ],
# # #         'layout': {
# # #             'xaxis': {'title':'Credit risk estimate', "titlefont": legend_font}, 
# # #             'yaxis': {'title':'Number of customers', "titlefont": legend_font},
# # #             'legend': {'title': {'text': '111', "font": legend_font}}
# # #         }
# # #     }

# # #     x_data = [0] + filtered_df.PD_Default30.values.tolist() + [1]
# # #     y_data = [0] + filtered_df.debito_total.clip(0, filtered_df.debito_total.quantile(0.95)).values.tolist() + [0]
# # #     fig_hist_2d = {
# # #         'data': [{
# # #             'x': x_data,
# # #             'y': y_data, 
# # #             'nbinsx': 25, 
# # #             'nbinsy': 25,
# # #             'name': 'Open Date',
# # #             'type': 'histogram2dcontour', 
# # #             'colorscale': [[0, '#FFFFFF'], [1, '#cc0000']]
# # #         }], 
# # #         'layout': {
# # #             'xaxis': {'title':'Credit risk estimate', "titlefont": legend_font}, 
# # #             'yaxis': {'title':'Total amount owed', "titlefont": legend_font},
# # #             'legend': {'bgcolor': 'black','title': {'text': '111', "font": legend_font}},
# # #             'annotations': [{'text':'# of<br>customers', 'align':'left', 'showarrow':False,'xref':'paper', 'yref':'paper', 'x':1.15, 'y':1.13, "font":legend_font}]
# # #         }
# # #     }

# # #     graphs = [
# # #         html.Div([
# # #             html.H6([page_texts['graph_titles'][2]], className="subtitle padded"),
# # #             dcc.Graph(figure=fig_hist)
# # #             ],
# # #             className="six columns",
# # #         ),
# # #         html.Div([
# # #             html.H6([page_texts['graph_titles'][3]], className="subtitle padded"),
# # #             dcc.Graph(figure=fig_hist_2d)
# # #             ],
# # #             className="six columns",
# # #         ),
# # #     ]

# # #     return graphs

# # # get relative data folder
# # PATH = pathlib.Path(__file__).parent
# # DATA_PATH = PATH.joinpath("../data").resolve()

# # df = read_csv(DATA_PATH.joinpath("2 - risco_cred_e_cadastro_short.csv"), encoding='utf=8')
# # class_names = ['Select all'] + df.DSC_CLASSE.unique().tolist()
# # localities = ['Select all'] + df.groupby('NOME_LOCALIDADE').NOME_LOCALIDADE.count().sort_values(ascending=False).index.tolist()


# # def create_layout(app, language):
# #     return html.Div(
# #         [
# #             Header(app, language),
# #             html.Div(
# #                 [
# #                     html.Div(
# #                         [
# #                             html.Div(
# #                                 [
# #                                     html.H5("Module Summary"),
# #                                     html.Br([]),
# #                                     html.P(
# #                                         '\
# #                                         This module uses machine learning algorithms to determine the \
# #                                         probability that he will remain delinquent, assuming that he receives\
# #                                         no collection actions. ',
# #                                         style={"color": "#ffffff"},
# #                                         className="row",
# #                                     ),
# #                                 ],
# #                                 className="red-box",
# #                             )
# #                         ],
# #                         className="row",
# #                     ),
# #                 ],
# #                 className="sub_page",
# #             ),
# #         ],
# #         className="page",
# #     )
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


# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df = read_csv(DATA_PATH.joinpath("2 - risco_cred_e_cadastro_short.csv"), encoding='utf=8')
class_names = ['Select all'] + df.DSC_CLASSE.unique().tolist()
localities = ['Select all'] + df.groupby('NOME_LOCALIDADE').NOME_LOCALIDADE.count().sort_values(ascending=False).index.tolist()


def create_layout(app, language):
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
                                        This module receives the data required \
                                        for the credit risk, effectiveness and optimization analysis.',
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="red-box",
                            )
                        ],
                        className="row",
                    ),

                    	     html.Div(
                                [
                                    html.Div(
                                        '\
                                       Please insert the Register and Invoice Database ',
                                       style = {'textAlign': 'center'}
                                        #className="row",
                                    ),

                                    dcc.Upload(
                                        children = html.Div(['Drag and Drop or ',
                                        html.A('Select Files')
                                        ]),
                                        style={
                                            'width': '100%',
                                            'height': '60px',
                                            'lineHeight': '60px',
                                            'borderWidth': '1px',
                                            'borderStyle': 'dashed',
                                            'borderRadius': '5px',
                                            'textAlign': 'center',
                                            'margin': '10px'
                                        },

                                    )
                                ],
                               # className="red-box",


                            )


                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
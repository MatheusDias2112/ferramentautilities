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
                                        This module uses machine learning algorithms to determine the \
                                        probability that he will remain delinquent, assuming that he receives\
                                        no collection actions. ',
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="red-box",
                            )
                        ],
                        className="row",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
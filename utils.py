import dash_html_components as html
import dash_core_components as dcc

import pandas as pd
from misc.languages import url_names, tab_names, allowed_languages


def Header(app, language):
    return html.Div([get_header(app), html.Br([]), get_menu(language)])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url('bain_logo.png'),
                        className='logo',
                    ),
                    html.A(
                        html.Button('Contact', id='learn-more-button'),
                        href='https://www.bain.com/pt-br/our-team/antonio-farinha/',
                    )
                ],
                className='row',
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5('Advanced Collections Solution for Utilities')],
                        className='seven columns main-title',
                    )
                ],
                className='twelve columns',
                style={'padding-left': '0'},
            ),
        ],
        className='row',
    )
    return header


def match_paths(url): 
    for tab in url_names.keys():
        for language in allowed_languages:
            if f'{url_names["root"][language]}/{url_names[tab][language]}' in url: 
                return tab
    
    for language in allowed_languages:
        if f'{url_names["root"][language]}' in url: 
            return 'introduction'


def get_menu(language):
    menu = html.Div(
        [
            dcc.Link(
                tab_names['introduction'][language],
                href=f'/{language}/{url_names["root"][language]}/{url_names["introduction"][language]}',
                className='tab first',
            ),
            dcc.Link(
                tab_names['data_input'][language],
                href=f'/{language}/{url_names["root"][language]}/{url_names["data_input"][language]}',
                className='tab',
            ),
            dcc.Link(
                tab_names['delinquecy_analysis'][language],
                href=f'/{language}/{url_names["root"][language]}/{url_names["delinquecy_analysis"][language]}',
                className='tab',
            ),
            dcc.Link(
                tab_names['covid_impacts'][language],
                href=f'/{language}/{url_names["root"][language]}/{url_names["covid_impacts"][language]}',
                className='tab',
            ),
            dcc.Link(
                tab_names['expected_results'][language],
                href=f'/{language}/{url_names["root"][language]}/{url_names["expected_results"][language]}',
                className='tab',
            ),

            html.Br(),

            dcc.Link(
                tab_names['credit_risk'][language],
                href=f'/{language}/{url_names["root"][language]}/{url_names["credit_risk"][language]}',
                className='tab first',
            ),
            dcc.Link(
                tab_names['effectiveness'][language],
                href=f'/{language}/{url_names["root"][language]}/{url_names["effectiveness"][language]}',
                className='tab',
            ),
            dcc.Link(
                tab_names['filtering_module'][language],
                href=f'/{language}/{url_names["root"][language]}/{url_names["filtering_module"][language]}',
                className='tab',
            ),
            dcc.Link(
                tab_names['action_optimization'][language], 
                href=f'/{language}/{url_names["root"][language]}/{url_names["action_optimization"][language]}',
                className='tab'
            ),
            dcc.Link(
                tab_names['routing'][language],
                href=f'/{language}/{url_names["root"][language]}/{url_names["routing"][language]}',
                className='tab',
            )
        ],
        className='row all-tabs',
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for _, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table


def read_csv(file_path, **kwargs):
    with open(file_path, 'r') as f:
        return pd.read_csv(f, **kwargs)


legend_font = {'family': 'Raleway, HelveticaNeue, Helvetica Neue, Helvetica, Arial', 'size': 17}
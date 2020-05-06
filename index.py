# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from utils import match_paths

from app import app
from misc.languages import find_language_in_url

from pages import (
    p_01_introduction,
    p_02_data_input,
    p_03_delinquecy_analysis,
    p_04_covid_impacts,
    p_05_expected_results,
    
    p_06_credit_risk,
    p_07_effectiveness,
    p_08_filtering_module,
    p_09_action_optimization,
    p_10_routing,
)

# Describe the layout/ UI of the app
app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False), 
        html.Div(id='page-content'), 
    ], style={'width': '90%'}
)

# Update page
@app.callback(
    Output('page-content', 'children'), 
    [Input('url', 'pathname')]
    )
def display_page(pathname):

    if pathname is None:
        pathname = ''

    language = find_language_in_url(pathname)

    if match_paths(pathname) == 'introduction':
        return p_01_introduction.create_layout(app, language)
    if match_paths(pathname) == 'data_input':
        return p_02_data_input.create_layout(app, language)
    if match_paths(pathname) == 'delinquecy_analysis':
        return p_03_delinquecy_analysis.create_layout(app, language)
    if match_paths(pathname) == 'covid_impacts':
        return p_04_covid_impacts.create_layout(app, language)
    if match_paths(pathname) == 'expected_results':
        return p_05_expected_results.create_layout(app, language)
    if match_paths(pathname) == 'credit_risk':
        return p_06_credit_risk.create_layout(app, language)
    if match_paths(pathname) == 'effectiveness':
        return p_07_effectiveness.create_layout(app, language)
    if match_paths(pathname) == 'filtering_module':
        return p_08_filtering_module.create_layout(app, language)
    if match_paths(pathname) == 'action_optimization':
        return p_09_action_optimization.create_layout(app, language)
    if match_paths(pathname) == 'routing':
        return p_10_routing.create_layout(app, language)


if __name__ == '__main__':
    app.run_server(debug=True)

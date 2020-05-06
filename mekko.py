# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from misc.misc import interpolate_colors
import plotly.graph_objs as go


def get_same_percentile_total_bins(data, value_column, n_bins=6, max_value=20000):
    total = data[value_column].sum()
    # Creates a list going [0, 100, 200, ..., 900, 1000, 1500, 2000, ..., 9500, 10000, 11000, 12000, 13000, ...]
    limits_to_try = (
        np.arange(0, min(max_value, 2000), 100).tolist() + 
        np.arange(2000, min(max_value, 10000), 500).tolist() +
        np.arange(10000, max_value+1, 1000).tolist()
    )
    
    bins, limits = pd.cut(data[value_column], limits_to_try, retbins=True)
    df = pd.DataFrame({'bins': bins, 'total_value': data[value_column]})
    grouped_sums = df.groupby('bins')['total_value'].sum().reset_index()
    percentages = np.cumsum(grouped_sums['total_value'])/total
    bins = limits[np.searchsorted(percentages, np.linspace(0,1,n_bins)[1:-1])]
    bins = [0] + bins.tolist() + [np.inf]
    bins = np.unique(bins)
    return bins


def get_scale(total):
    if total > 3*10**9:
        return 9, 'B'
    if total > 3*10**6:
        return 6, 'M'
    if total > 3*10**3:
        return 3, 'k'
    else: 
        return 0, ''



def draw_mekko_2(pivot_table, colors=['#DDDDDD', '#CC0000'], **subplot):
    colors = interpolate_colors(*colors, len(pivot_table.columns))

    scale, abbreviation = get_scale(pivot_table.sum().sum())

    value_cols = pivot_table.columns

    plot_data = pd.DataFrame({'x_column': pivot_table.sum(axis='columns')})
    plot_data[value_cols] = pivot_table.div(plot_data['x_column'], axis='index')

    categories = plot_data.index.tolist()
    width = plot_data['x_column']
    htmpl = '%{y}'
    bar_limits = np.cumsum([0] + list(width))
    total_positions = [np.mean([a,b]) for a, b in zip(bar_limits[:-1], bar_limits[1:])]
    x = bar_limits[:-1]
    
    figure = subplot.pop('figure', go.Figure())
    for colname, color in zip(value_cols, colors):
        figure.add_trace(go.Bar(name=colname, x=x, y=plot_data[colname], width=width, 
                                hovertemplate=htmpl, offset=0, marker_color=color), **subplot)

    total_labels = [
        {"x": x_value, "y": 1.03, "text": f'{total_value:.1f}{abbreviation}', "showarrow": False}
        for x_value, total_value in zip(total_positions, width/10**scale)
    ]
    figure = figure.update_layout(annotations=total_labels)
    figure = figure.update_xaxes(
        tickvals=x + np.array(width) / 2,
        ticktext=categories,
        range=[0, np.sum(width)]
    )
    figure = (figure
        .update_yaxes(tickformat=',.0%', range=[0, 1.03]) \
        .update_layout(barmode='stack', bargap=0, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
        margin={'t': 50}, height=400)
    )

    return figure


def rename_categories_2(limits, precision=-1):
    n_decimals = max(0, precision)
    
    categories_names = []
    categories_names.append(f'<{limits[1]:.{n_decimals}f}')
    categories_names.extend([f'{v1:.{n_decimals}f}-{v2:.{n_decimals}f}' for v1, v2 in zip (limits[1:-2], limits[2:-1])])
    categories_names.append(f'>{limits[-2]:.{n_decimals}f}')
                                
    return categories_names


def summarize_data_2(data, y_bins, y_col, x_bins, x_col, value_col): 

    if x_bins is not None: 
        x_categories = pd.cut(data[x_col], x_bins)
        data['x_categories'] = x_categories
    else: 
        data['x_categories'] = data[x_col]

    if y_bins is not None:
        y_categories = pd.cut(data[y_col], y_bins)
        data['y_categories'] = y_categories
    else: 
        data['y_categories'] = data[y_col]

    if value_col is None or value_col == 'count':
        value_col = 'count'
        data[value_col] = 1
    
    pivot_table = (
        data
        .groupby(['x_categories', 'y_categories'])
        [value_col]
        .sum()
        .reset_index()
        .pivot(index='x_categories', columns='y_categories', values=value_col)
    )

    if x_bins is not None: 
        pivot_table.index = rename_categories_2(x_bins, precision=1)
    if y_bins is not None: 
        pivot_table.columns = rename_categories_2(y_bins, precision=-1)

    return pivot_table

# -*- coding: utf-8 -*-

import numpy as np
import plotly.express as px

def interpolate_colors(color_1, color_2, n_colors):
    invalid_input = 0
    error_msg = f'Please input colors in either hex or rgb format: "#FFFFFF" or "rgb(255,255,255)". Input values: {color_1}, {color_2}'
    try:
        if '#' in color_1 and '#' in color_2:
            color_1 = px.colors.hex_to_rgb(color_1)
            color_2 = px.colors.hex_to_rgb(color_2)
        elif 'rgb' in color_1 and 'rgb' in color_2:
            color_1 = px.colors.unlabel_rgb(color_1)
            color_2 = px.colors.unlabel_rgb(color_2)
        else:
            invalid_input = 1
    except: 
        invalid_input = 1
        
    if invalid_input == 1:
        raise ValueError(error_msg)
    
    interpolated_colors = zip(
        np.linspace(color_1[0], color_2[0], n_colors), 
        np.linspace(color_1[1], color_2[1], n_colors), 
        np.linspace(color_1[2], color_2[2], n_colors)
    )
    
    interpolated_colors_strings = [px.colors.label_rgb(color) for color in interpolated_colors]
    
    return interpolated_colors_strings



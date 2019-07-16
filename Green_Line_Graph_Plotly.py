# This file was created on July 15, 2019 by Zakir Chaudry
import plotly
import csv
from typing import Dict, List


def add_stop_to_dict(x: str, y: str, name: str, stop_line: str,
                     stop_dict: Dict) -> None:
    """Adds a stop to the given dictionary, given the coordinates, name, and
    line"""
    if stop_line not in stop_dict:
        stop_dict[stop_line] = {}
        stop_dict[stop_line]['x'] = [x]
        stop_dict[stop_line]['y'] = [y]
        stop_dict[stop_line]['name'] = [name]
    else:
        stop_dict[stop_line]['x'].append(x)
        stop_dict[stop_line]['y'].append(y)
        stop_dict[stop_line]['name'].append(name)


if __name__ == '__main__':
    green_line_csv = open('GreenLineStops.csv', 'r')
    all_stops = list(csv.reader(green_line_csv))

    stops_data = {}
    for stop in all_stops:  # Converts CSV to Dictionary
        stops_data[stop[2]] = {'x': float(stop[0]), 'y': 9000 - float(stop[1]),
                               'next': stop[3], 'line': stop[4]}

    stops = {}

    for stop in stops_data:
        stop_data = stops_data[stop]
        if len(stop_data['line']) > 1:
            lines = stop_data['line'].split(';')
            for line in lines:
                add_stop_to_dict(stop_data['x'], stop_data['y'],
                                 stop, line, stops)
        else:
            add_stop_to_dict(stop_data['x'], stop_data['y'], stop,
                             stop_data['line'], stops)

    b_line = plotly.graph_objs.Scatter(
        x=stops['B']['x'],
        y=stops['B']['y'],
        # To avoid duplicate labels
        text=stops['B']['name'][:len(stops['B']['name']) - 4],
        showlegend=False,
        hoverinfo='text',
        mode="markers+lines",
        line=dict(
            color='green',
            width=15,
            shape='spline',
            smoothing=1.3
        ),
        marker=dict(
            color='white',
            size=15,
            line=dict(
                color='green',
                width=5
            )
        )
    )

    c_line = plotly.graph_objs.Scatter(
        x=stops['C']['x'],
        y=stops['C']['y'],
        text=stops['C']['name'][:len(stops['C']['name']) - 4],
        showlegend=False,
        hoverinfo='text',
        mode="markers+lines",
        line=dict(
            color='green',
            width=15,
            shape='spline',
            smoothing=1.3
        ),
        marker=dict(
            color='white',
            size=15,
            line=dict(
                color='green',
                width=5
            )
        )
    )

    d_line = plotly.graph_objs.Scatter(
        x=stops['D']['x'],
        y=stops['D']['y'],
        text=stops['D']['name'][1:len(stops['D']['name']) - 2],
        showlegend=False,
        hoverinfo='text',
        mode="markers+lines",
        line=dict(
            color='green',
            width=15,
            shape='spline',
            smoothing=1.3
        ),
        marker=dict(
            color='white',
            size=15,
            line=dict(
                color='green',
                width=5
            )
        )
    )

    e_line = plotly.graph_objs.Scatter(
        x=stops['E']['x'],
        y=stops['E']['y'],
        text=stops['E']['name'][1:],
        showlegend=False,
        hoverinfo='text',
        mode="markers+lines",
        line=dict(
            color='green',
            width=15,
            shape='spline',
            smoothing=1.3
        ),
        marker=dict(
            color='white',
            size=15,
            line=dict(
                color='green',
                width=5
            )
        )
    )

    end_lines = plotly.graph_objs.Scatter(
        x=[stops['B']['x'][0], stops['C']['x'][0], stops['D']['x'][0],
           stops['E']['x'][0]],
        y=[stops['B']['y'][0], stops['C']['y'][0], stops['D']['y'][0],
           stops['E']['y'][0]],
        # text=['Boston College', 'Cleveland Circle', 'Riverside',
        #       'Heath Street'],
        showlegend=False,
        hoverinfo='text',
        textposition='bottom center',
        mode='markers',
        marker=dict(
            color='white',
            size=20,
            line=dict(
                color='green',
                width=5
            )
        )

    )

    layout = plotly.graph_objs.Layout(
        xaxis=dict(
            autorange=True,
            showgrid=False,
            zeroline=False,
            showline=False,
            ticks='',
            showticklabels=False
        ),
        yaxis=dict(
            autorange=True,
            showgrid=False,
            zeroline=False,
            showline=False,
            ticks='',
            showticklabels=False
        )
    )

    data = [c_line, b_line, d_line, e_line, end_lines]
    fig = plotly.graph_objs.Figure(data=data, layout=layout)
    plotly.plotly.iplot(fig, filename='basic-scatter')

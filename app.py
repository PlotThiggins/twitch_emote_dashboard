import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from numpy.random import choice

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

emote_list = open('emote_list.txt').read().split('\n')
emote_counts = {}
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='Dash: A web application framework for Python.'),
    dcc.Graph(
        id='live-update-graph',
        figure={
            'data': [{'x': [key], 'y': [emote_counts[key]], 'type': 'bar', 'name':key}
                     for key in emote_counts.keys()],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    dcc.Interval(
        id='interval-component',
        interval=2 * 1000,  # in milliseconds
        n_intervals=0
        )
])

@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):

    # Update emote counts
    for key in emote_counts.keys():
        emote_counts[key] += choice(11)

    # Create updated plot
    fig = {
        'data': [{'x': [key], 'y': [emote_counts[key]], 'type': 'bar', 'name': key}
                 for key in emote_counts.keys()],
        'layout': {
            'title': 'Dash Data Visualization'
        }
    }
    return fig


if __name__ == '__main__':
    app.run_server(debug=False)
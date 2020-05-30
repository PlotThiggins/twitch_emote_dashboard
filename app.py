import dash
import dash_core_components as dcc
import dash_html_components as html
from numpy.random import choice
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

emote_count = {
    'LUL': 23,
    'Kappa': 12
}
app.layout = html.Div(children=[
    html.H1(children='Title goes here mf'),
    html.Div(id='updatable-graph',children='And then this, my dude, is the subtitle'),
    dcc.Graph(
        id='emote_count',
        figure={
            'data': [{'x': [key], 'y': [emote_count[key]], 'type':'bar', 'name':key}
                     for key in emote_count.keys()],
            'layout': {
                'title': 'Emote count'
            }
        }
    ),
    dcc.Interval(
                id='interval-component',
                interval=1*1000, # in milliseconds
                n_intervals=0
            )
    ]
)


@app.callback(Output('updatable-graph', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_counts(n):
    # Jitter the values to simulate continuous data scraping (but with minus values)
    for key in emote_count.keys():
        change_value = choice(10)
        if choice(2):
            emote_count[key] += change_value
        else:
            emote_count[key] -= change_value

    figure = {
        'data': [{'x': [key], 'y': [emote_count[key]], 'type': 'bar', 'name': key}
                 for key in emote_count.keys()],
        'layout': {
            'title': 'Emote count'
        }
    }
    return figure


if __name__ == '__main__':

    # Run server
    app.run_server(debug=False)
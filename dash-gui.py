# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import csv
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

def import_csv(file):
    with open(file, newline='') as f:
        return list(csv.reader(f))[0]


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Market-Agent-Sim'),

    html.Div(children='''
        Data visualization tool for market-agent-sim.
    '''),

    dcc.Input(id='my-id', value='initial value', type='text'),
    html.Div(id='my-div'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [i for i in range(1000)], 'y': import_csv('data/saved/{}.csv'.format('latest')), 'type': 'line', 'name': 'Price'},
            ],
            'layout': {
                'title': 'Data Visualization'
            }
        }
    )
])

@app.callback(
    dash.dependencies.Output(component_id='my-div', component_property='children'),
    [dash.dependencies.Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return input_value





if __name__ == '__main__':
    app.run_server(debug=True)
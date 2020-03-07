# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.tools as tools
import random
import csv
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


def import_csv(file):
    with open(file, newline='') as f:
        return list(csv.reader(f))


def get_marker(n, length):
    if n == length - 1:
        return dict(size=30, color='black')
    else:
        color = "#%06x" % random.randint(0, 0xFFFFFF)
        return dict(size=10, color=color)

source_list = ['data/saved/latest.csv', 'data/monte-carlo/latest.csv']
source_list_test = ['data/monte-carlo/latest.csv']



app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.H3('Market-Agent-Sim', className='main-header'),
    dcc.Dropdown(id='source-list-input',
                 options=[{'label': s, 'value': s}
                          for s in source_list],
                 value=['data/test.csv'],
                 multi=True,
                 className='data-input',
                 ),
    html.Div(children=html.Div(id='graphs', className='row'), className='container-fluid', style={'height': 100}),
    dcc.Interval(
        id='graph-update',
        interval=500),
    ], className="container", style={'width': '100%', 'height': '100%', 'max-width': 50000})

# @app.callback(dash.dependencies.Output('graphs', 'children'), [dash.dependencies.Input('source-list-input', 'value')])
@app.callback(dash.dependencies.Output('graphs', 'children'), [dash.dependencies.Input('graph-update', 'n_intervals')])
def update_graph(source_list):
    print('UPDATE GRAPHS RAN')
    graphs = []
    blocks = []

    for source in source_list_test:

        data_list = []

        source_data = import_csv(source)
        for idx, row in enumerate(source_data):
            data = go.Scatter(
                x=[i for i in range(1000)],
                y=row,
                marker=get_marker(idx, len(source_data))
            )
            data_list.append(data)


        graph_title = html.H3(str(source))

        main_graph = dcc.Graph(
            id=source,
            animate=False,
            style={'height': 720},
            config={'scrollZoom': True, 'displayModeBar': False},
            figure={'data': data_list, 'layout': go.Layout(
                                                        xaxis={'rangeslider': {'visible': False}, 'title': 'Steps', 'autorange': True},
                                                        yaxis={'title': 'Price', 'autorange': True},
                                                        # plot_bgcolor='rgba(0,0,0,10)',
                                                        # paper_bgcolor='rgba(0,0,0,10)',
                                                        font={'family': 'VT323'},
                                                        dragmode='pan'
                                                        )}

        )


        block = html.Div([graph_title, main_graph], className='block')
        # block = html.Div([graph_title, main_graph, score_graph], className='block')
        graphs.append(block)

    return graphs





if __name__ == '__main__':
    app.run_server(debug=True)
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_excel('data.xls', names=['x', 'y'], header=0)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Quantidade de Vínculos por número de funcionários'),

    html.Div(children='''
        Dados obtidos a partir de uma planilha Excel
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df['x'], 'y': df['y'], 'type': 'bar', 'name': 'Quantidade de vínculos por nº de'},
            ],
            'layout': {
                'title': 'Gráfico em barras'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
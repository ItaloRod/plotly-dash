# -*- coding: utf-8 -*-

'''
    Objetivo: O número de Médicos pela a quantidade de vínculos.
    Pergunta: Quantos Médicos tem 8 vínculos? Ou 5 vínculos?
    Observação: 
    * CNS é a identificação dos profissionais da saúde. Todo profissional se repete.
    * Cada vínculo é em qual local aquele usuário está alocado. Quanto mais ele se repetir, mais alocado ele está.
'''
import dash
import dash_core_components as dcc
import dash_html_components as html
from .data import getNumberProfessionalsByBond

df = getNumberProfessionalsByBond()

def render():
    return html.Div(children=[
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
    

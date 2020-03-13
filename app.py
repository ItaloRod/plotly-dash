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
import pandas as pd
import connection as conn

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = conn.getProfessionalsCsv()
df = df[df['cns'] != ''] # remove valores vazios
df = df[df['cbodescricao'].str.match('MEDICO')] # Pega quem é médico 

df = df.groupby(['cns']).count() # Agrupa por CNS e conta
# df.to_csv(r'output.csv')
df['vinculos'] = df.cnes 
df = df.groupby(['vinculos']).count() # Agrupa pelo Vínculo e conta
# df['cnes'].to_csv(r'output2.csv')

print(df)
                          
# num_prof = number_vim.groupby(['cnes']).count()
# print(number_vim['cns'])

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div(children=[
#     html.H1(children='Quantidade de Vínculos por número de funcionários'),

#     html.Div(children='''
#         Dados obtidos a partir de uma planilha Excel
#     '''),

#     dcc.Graph(
#         id='example-graph',
#         figure={
#             'data': [
#                 {'x': df['x'], 'y': df['y'], 'type': 'bar', 'name': 'Quantidade de vínculos por nº de'},
#             ],
#             'layout': {
#                 'title': 'Gráfico em barras'
#             }
#         }
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)
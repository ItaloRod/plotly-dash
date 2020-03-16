from flask import Flask
from dashboard.app import render
import dash


server = Flask(__name__)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] #Provisório

app = dash.Dash(
    __name__,
    server=server,
    external_stylesheets=external_stylesheets,  
    routes_pathname_prefix='/dash/' 
)

app.layout = render()


if __name__ == '__main__':
    server.run(debug=True)

# Modules
import pymongo
from pymongo import MongoClient
import pandas as pd
import dash
from dash import html
from dash import dcc 
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# Connection
# Connection string
myClient = pymongo.MongoClient("mongodb+srv://celi4832:Jcq23xpf@cluster-tue.whk5b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") 
myDB = myClient["myDB"]
mycol = myDB["omsætninger"]

mylist = [
    {"firma": "xxx", "omsætning": 120000, "år": 2021},
    {"firma": "yyy", "omsætning": 130000, "år": 2021},
    {"firma": "zzz", "omsætning": 140000, "år": 2021}
]
x = mycol.insert_many(mylist)

data = pd.DataFrame(list(mycol.find()))

fig_omsætning = px.histogram(data, 
    x='firma', y='omsætning', title='Omsætning pr. Firma',
    hover_data=[],
    labels={'omsætning':'Omsætning', 'Firma':'firma'})
fig_omsætning.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', xaxis_tickangle=45)

dash_app = dash.Dash(__name__)
app = dash_app.server

dash_app.layout = html.Div(children=[

    html.Div(children=[
            dcc.Graph(id="Firmaomsætninger", figure=fig_omsætning)
        ]),
])


if __name__ == '__main__':
    dash_app.run_server(debug=True)


#from itertools import count
#from re import X
#from turtle import width
#from typing import Collection
#from webbrowser import BackgroundBrowser
import dash
import plotly.express as px
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import warnings
warnings.simplefilter("ignore")

df = pd.read_excel("data/amazing.xlsx", engine="openpyxl")


app = dash.Dash(__name__)
# ,external_stylesheets=[dbc.themes.QUARTS]) ---- I downloaded it into assets

app.layout=html.Div([
    html.H1("Companies Flows Success"),

    dbc.Row (
        [dbc.Col(dcc.Dropdown(id='company-choice',
                              options=[{'label': html.Div(x, style={'color': 'Black'}), 'value':x }
                                for x in sorted(df.Company.unique())],
                              value='Company',
                              placeholder="Select a company",
                            ),
                width= 3
                ),
        ]
        ),

    dbc.Row ( 
        [dbc.Col(dcc.Graph(id='my-graph',), width= 5)],
    )
])

@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='company-choice', component_property='value')
)
def interactive_graphing(value_company):
    print (value_company)
    dff = df[df.Company==value_company]
    fig = px.pie(data_frame= dff, names= 'Status')
    return fig

if __name__ == '__main__':
    app.run_server()
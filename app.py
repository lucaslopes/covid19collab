import dash
import pandas as pd
import plotly.express as px
from dash import html, dcc

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets)

server = app.server

df = pd.read_csv('db.gz', compression='gzip')
fig = px.scatter_geo(df,
    locations="Code",  # Alpha-3 ISO code
    color="Income", # Income group (HIC or LMIC)
    projection="orthographic")

app.layout = html.Div(children=[
    html.H1(children='Covid19Collab'),

    html.Div(children='''
        Dashboard to visualize the scientific collaboration network between countries during the Covid-19 pandemic.
    '''),

    dcc.Graph(
        id='global-map',
        figure=fig
    )
])


__name__ == '__main__' and app.run_server(debug=True)
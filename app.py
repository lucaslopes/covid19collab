import dash
from dash import html, dcc
from figs import gen_fig

app = dash.Dash('Covid-19Collab')

server = app.server

app.layout = html.Div([
    dcc.Graph(
        id='global-map',
        figure=gen_fig(),
        style={'margin': 0,
            'border': 'thin lightgrey solid',
            'height' : '100vh'}
    )
], style={'margin':0})


__name__ == '__main__' and app.run_server(debug=True)
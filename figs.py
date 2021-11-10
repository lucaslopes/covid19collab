import pandas as pd
import plotly.express as px

def gen_fig():
    df = pd.read_csv('db.gz', compression='gzip')
    codes = pd.read_csv('db.gz', compression='gzip')['Code'].values
    incomes = {code:income for code, income in zip(df['Code'], df['Income'])}
    df_edges = pd.read_csv('edges.gz', compression='gzip')
    counts = {code:0 for code in codes}
    for (c1, c2, d, _) in df_edges.values:
        counts[c1] += d
        counts[c2] += d
    df['Collab'] = [counts[c] for c in codes]
    fig = px.scatter_geo(df,
        locations="Code",  # Alpha-3 ISO code
        color="Income", # Income group (HIC or LMIC)
        size='Collab',
        projection="orthographic")
    for (c1, c2, d, b) in df_edges.values:
        income_collab = '/'.join(
            sorted([
                incomes[c1],
                incomes[c2]]))
        fig.add_scattergeo(
            locations=[c1, c2],
            mode='lines',
            showlegend=False,
            line = dict(
                width = d/df_edges['Docs'].max()*5,
                color = {
                    'LMIC/LMIC': 'blue',
                    'HIC/HIC': 'red',
                    'HIC/LMIC': 'purple'
                }[income_collab],
                dash = {
                    'LMIC/LMIC': 'dash',
                    'HIC/HIC': 'dot',
                    'HIC/LMIC': 'dashdot'
                }[income_collab]
            ),
            opacity = b)
    return fig

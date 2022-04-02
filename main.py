import plotly.express as px
from dash import Dash, html, dcc

from builders import make_table
from corona_data import CoronaData

countries_df = CoronaData().make_daily_df_by_country()
totals_df = CoronaData().make_daily_df_global()

stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap",
]

app = Dash(__name__, external_stylesheets=stylesheets)

bubble_map = px.scatter_geo(
    countries_df,
    title='Coronavirus Cases by Country',
    locations='Country_Region',
    locationmode='country names',
    hover_name='Country_Region',
    hover_data={
        'Country_Region': False,
        'Confirmed': ":,2f",
        'Deaths': ":,2f",
        'Recovered': ":,2f",
    },
    size='Confirmed',
    size_max=50,
    color='Confirmed',
    template='plotly_dark',
    color_continuous_scale=px.colors.sequential.Oryel,
    projection="natural earth"
)

bubble_map.update_layout(margin=dict(l=0, r=0, t=50, b=0))

bars_graph = px.bar(
    totals_df,
    title='Total Global Cases',
    x='condition',
    y='count',
    labels={'condition': 'Condition', 'count': 'Count', 'color': 'Condition'},
    hover_data={'count': ":,", },
    template="plotly_dark"
)

bars_graph.update_traces(marker_color=["#e74c3c", "#8e44ad", "#27ae60"])

app.layout = html.Div(
    children=[
        html.Header(
            children=[html.H1(children='Corona Dashboard', style={'font-size': '50px'})],
            style={'textAlign': 'center', 'paddingTop': '50px', 'marginBottom': 100},
        ),
        html.Div(
            children=[
                html.Div(
                    children=[dcc.Graph(figure=bubble_map)],
                    style={"grid-column": "span 3"},
                ),
                html.Div(children=[make_table(countries_df)]),
            ],
            style={
                "display": "grid",
                "gap": 50,
                "gridTemplateColumns": "repeat(4, 1fr)",
            }
        ),
        html.Div(
            children=[dcc.Graph(figure=bars_graph)],
            style={
                "display": "grid",
                "gap": 50,
                "gridTemplateColumns": "repeat(4, 1fr)",
            },
        ),
    ],
    style={
        'fontFamily': 'Open Sans, sans-serif',
        'minHeight': '100vh',
        'backgroundColor': '#111111',
        'color': 'white'
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)

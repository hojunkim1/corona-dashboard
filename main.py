import plotly.express as px
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

from corona_data import CoronaData
from graphs import make_bubble_map, make_bars_graph
from tables import make_dropdown_options
from tables import make_table

stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap",
]

app = Dash(__name__, external_stylesheets=stylesheets)

app.title = 'Corona Dashboard'

server = app.server


def make_line_graph():
    dropdown_options = make_dropdown_options()
    return [
        dcc.Dropdown(
            placeholder="Select a Country",
            id='country_dropdown',
            options=[
                {'label': country, 'value': country} for country in dropdown_options
            ],
            style={
                "width": 320,
                "margin": "0 auto",
                "color": "#111111",
            },
        ),
        dcc.Graph(id='country_graph'),
    ]


def main_layout():
    return html.Div(
        children=[
            html.Header(
                children=[html.H1(children='Corona Dashboard', style={'font-size': '50px'})],
                style={'textAlign': 'center', 'paddingTop': '50px', 'marginBottom': 100},
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[make_bubble_map()],
                        style={'grid-column': 'span 3'},
                    ),
                    html.Div(children=[make_table()]),
                ],
                style={
                    'display': 'grid',
                    'gap': 50,
                    'gridTemplateColumns': 'repeat(4, 1fr)',
                }
            ),
            html.Div(
                children=[
                    html.Div(children=[make_bars_graph()]),
                    html.Div(
                        children=make_line_graph(),
                        style={'grid-column': 'span 3'},
                    )
                ],
                style={
                    'display': 'grid',
                    'gap': 50,
                    'gridTemplateColumns': 'repeat(4, 1fr)',
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


@app.callback(
    Output('country_graph', 'figure'),
    [Input('country_dropdown', 'value')]
)
def update_line_graph(value):
    if value:
        df = CoronaData().make_timeline_df_by_country(value)
    else:
        df = CoronaData().make_timeline_df_global()
    fig = px.line(
        df,
        x='Date',
        y=['confirmed', 'deaths', 'recovered'],
        labels={
            'value': 'Cases',
            'variable': 'Condition',
            'date': 'Date'
        },
        hover_data={
            'value': ':,',
            'variable': False,
        },
        template='plotly_dark',
    )
    fig.update_xaxes(rangeslider_visible=True)
    return fig


app.layout = main_layout()

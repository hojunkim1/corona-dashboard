from dash import Dash, html

from builders import make_table
from corona_data import CoronaData

countries_df = CoronaData().make_daily_df_by_country()

stylesheets = [
    'https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css',
    'https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap',
]

app = Dash(__name__, external_stylesheets=stylesheets)

app.layout = html.Div(
    children=[
        html.Header(
            children=[html.H1(children='Corona Dashboard', style={'font-size': '50px'})],
            style={"textAlign": "center", "paddingTop": "50px", "marginBottom": 100},
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        make_table(countries_df)
                    ]
                ),
            ]
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

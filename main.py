from dash import Dash, html

stylesheets = [
    'https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css',
    'https://fonts.googleapis.com/css2?family=Open+Sans&display=swap',
]

app = Dash(__name__, external_stylesheets=stylesheets)

app.layout = html.Div(
    children=[
        html.Header(
            children=[html.H1(children='Corona Dashboard', style={'font-size': '50px'})],
            style={'textAlign': 'center', 'paddingTop': '50px', }
        )
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

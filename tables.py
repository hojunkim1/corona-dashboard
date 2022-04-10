from dash import html

from corona_data import CoronaData


def make_dropdown_options():
    countries_df = CoronaData().make_daily_df_by_country()
    dropdown_options = countries_df.sort_values('Country_Region').reset_index()
    dropdown_options = dropdown_options['Country_Region']
    return dropdown_options


def make_table():
    country_df = CoronaData().make_daily_df_by_country()
    return html.Table(
        children=[
            html.Thead(
                children=[
                    html.Tr(
                        children=[
                            html.Th(column_name.replace('_', ' '))
                            for column_name in country_df.columns
                        ],
                        style={
                            'display': 'grid',
                            'gridTemplateColumns': 'repeat(4, 1fr)',
                            'fontWeight': '600',
                            'fontSize': 16,
                        },
                    )
                ],
                style={'display': 'block', 'marginBottom': 25},
            ),
            html.Tbody(
                children=[
                    html.Tr(
                        children=[
                            html.Td(
                                children=[value_column],
                                style={"textAlign": "center"},
                            )
                            for value_column in value
                        ],
                        style={
                            'display': 'grid',
                            'gridTemplateColumns': 'repeat(4, 1fr)',
                            'border-top': '1px solid white',
                            'padding': '30px 0px',
                        },
                    )
                    for value in country_df.values
                ],
                style={'maxHeight': '50vh', 'display': 'block', 'overflow': 'scroll', },
            )
        ]
    )

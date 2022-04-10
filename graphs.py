import plotly.express as px
from dash import dcc

from corona_data import CoronaData


def make_bubble_map():
    countries_df = CoronaData().make_daily_df_by_country()
    bubble_map = px.scatter_geo(
        countries_df,
        title='Coronavirus Cases by Country',
        locations='Country_Region',
        locationmode='country names',
        hover_name='Country_Region',
        hover_data={
            'Country_Region': False,
            'Confirmed': ':,2f',
            'Deaths': ':,2f',
            'Recovered': ':,2f',
        },
        size='Confirmed',
        size_max=50,
        color='Confirmed',
        template='plotly_dark',
        color_continuous_scale=px.colors.sequential.Oryel,
        projection='natural earth'
    )
    bubble_map.update_layout(margin=dict(l=0, r=0, t=50, b=0))
    return dcc.Graph(figure=bubble_map)


def make_bars_graph():
    totals_df = CoronaData().make_daily_df_global()
    bars_graph = px.bar(
        totals_df,
        title='Total Global Cases',
        x='condition',
        y='count',
        labels={'condition': 'Condition', 'count': 'Count', 'color': 'Condition'},
        hover_data={'count': ':,'},
        template="plotly_dark"
    )
    bars_graph.update_traces(marker_color=['#e74c3c', '#8e44ad', '#27ae60'])
    return dcc.Graph(figure=bars_graph)

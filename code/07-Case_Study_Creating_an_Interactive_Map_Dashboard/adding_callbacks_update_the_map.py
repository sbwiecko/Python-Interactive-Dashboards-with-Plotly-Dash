# import all from Dash since v2.0 https://dash.plotly.com/dash-2-0-migration
from dash import Dash, html, dcc, dash_table, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc


electricity = pd.read_csv('../../data/electricity.csv')

year_min = electricity['Year'].min()
year_max = electricity['Year'].max()


app = Dash(external_stylesheets=[dbc.themes.SOLAR])

app.layout = html.Div(
    [
        html.H1('Electricity Prices by US State'),
        dcc.RangeSlider(
            id='year-slider',
            min=year_min,
            max=year_max,
            value=[year_min, year_max],
            marks={
                i: str(i) for i in range(year_min, year_max+1)
            },
        ),
        dcc.Graph(
            id='map-graph',
            figure={},
        ),
        # see https://dash.plotly.com/datatable
        dash_table.DataTable(
            id='price-info',
            # see https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.to_dict.html
            data=electricity.to_dict('records'), # `records` list [{column -> value}, ... , {column -> value}]
            # when no columns argument is provided, columns are auto-generated based on the first row in data
            #columns=[{'name': col, 'id': col} for col in electricity.columns],
            # see interactivity offered by dash DT https://dash.plotly.com/datatable/interactivity
            sort_action='native',
        ),
    ]
)


@app.callback(
    Output('map-graph', 'figure'),
    Input('year-slider', 'value')
)
def update_map_graph(selected_years):
    filtered_electricity = electricity[
        (electricity['Year'] >= selected_years[0]) & (electricity['Year'] <= selected_years[1])
    ]
    
    avg_price_electricity = (
        filtered_electricity
        .groupby('US_State')['Residential Price']
        .mean()
        .reset_index() # to be access the `USA-State` column in the choropleth
    )

    map_fig = px.choropleth(
        data_frame=avg_price_electricity,
        locations='US_State', # name of a column in data_frame
        locationmode='USA-states', # `ISO-3`, `USA-states`, or `country names`
        color='Residential Price',
        scope='usa', # `world`, `usa`, `europe`, `asia`, `africa`, `north america`, or `south america`
        color_continuous_scale='reds',
    )

    return map_fig


if __name__ == '__main__':
    app.run_server(debug=True)

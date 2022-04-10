from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px


electricity = pd.read_csv('../../data/electricity.csv')

year_min = electricity['Year'].min()
year_max = electricity['Year'].max()

avg_price_electricity = (
    electricity
    .groupby('US_State')['Residential Price']
    .mean()
    .reset_index() # to be access the `USA-State` column in the choropleth
)

# see https://plotly.github.io/plotly.py-docs/generated/plotly.express.choropleth.html
map_fig = px.choropleth(
    data_frame=avg_price_electricity,
    locations='US_State', # name of a column in data_frame
    locationmode='USA-states', # `ISO-3`, `USA-states`, or `country names`
    color='Residential Price',
    scope='usa', # `world`, `usa`, `europe`, `asia`, `africa`, `north america`, or `south america`
    color_continuous_scale='reds',
)


app = Dash()

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
            }
        ),
        dcc.Graph(
            id='map-graph',
            figure=map_fig,
        ),
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
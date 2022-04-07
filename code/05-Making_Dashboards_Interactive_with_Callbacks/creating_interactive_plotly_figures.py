import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# app built on the previous script
app = dash.Dash()


# load the dataset
happiness = pd.read_csv('../../data/world_happiness.csv')

region_options = happiness.region.unique()
country_options = happiness['country'].unique()

app.layout = html.Div(
    [
        html.H1('World Happiness Dashboard'),
        html.P(
            [
                'This dashboard shows the happiness score.',
                html.Br(),
                html.A(
                    'World Happiness Report Data Source',
                    href='https://worldhappiness.report/',
                    target="_blank"
                )
            ]
        ),
        dcc.RadioItems(options=region_options, value=region_options[0]), # 1st option selected
        dcc.Checklist(options=region_options, value=['North America']),
        dcc.Dropdown(
            id='country-dropdown',
            options=country_options,
            value='United States',
        ),
        dcc.Graph(
            id='happiness-graph',
            figure={}, # we can leave it empty until the 1st automatic callback
        )
    ]
)

@app.callback(
    Output('happiness-graph', 'figure'),
    Input('country-dropdown', 'value'))
def update_graph(selected_country): # from the Input
    filtered_happiness = happiness[happiness['country'] == selected_country]
    line_fig = px.line(
        filtered_happiness,
        x='year',
        y='happiness_score',
        title=f'Happiness Score in {selected_country}',
    )
    return line_fig


if __name__ == '__main__':
    app.run_server(debug=True)
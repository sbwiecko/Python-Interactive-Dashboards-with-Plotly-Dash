import pandas as pd

import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# app built on the previous script
app = dash.Dash()


# load the dataset
happiness = pd.read_csv('../../data/world_happiness.csv')

region_options = happiness['region'].unique()

data_options = {
    'happiness_score': "Happiness Score",
    'happiness_rank' : "Happiness Rank",
}


app = dash.Dash()

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
        dcc.RadioItems(
            id='region-radio',
            options=region_options,
            value='North America', # value or the Radio when app starts
        ),
        dcc.Dropdown(
            id='country-dropdown',
            # options=[], # output of the 1st callback at app initiation
            # value='',   # also updated as callback output at app initiation
        ),
        dcc.RadioItems(
            id='data-radio',
            options=data_options,
            value='happiness_score',
        ),
        dcc.Graph(
            id='happiness-graph',
            figure={}, # we can leave it empty until the 1st automatic callback
        ),
        html.Div(
            id='average-div',
        ),
    ]
)

# chaining the change in the top RadioItems will be chained to the DropDown menu

@app.callback(
    Output('country-dropdown', 'options'),
    Output('country-dropdown', 'value'),
    Input('region-radio', 'value'),
)
def update_dropdown(selected_region):
    filtered_happiness = happiness[happiness['region'] == selected_region]
    country_options = filtered_happiness['country'].unique()

    return country_options, country_options[0]


@app.callback(
    Output('happiness-graph', 'figure'),
    Output('average-div', 'children'),
    Input('country-dropdown', 'value'),
    Input('data-radio', 'value'),
)
def update_graph(selected_country, selected_data):
    filtered_happiness = happiness[happiness['country'] == selected_country]
    line_fig = px.line(
        filtered_happiness,
        x="year",
        y=selected_data,
        title=f'{selected_data} in {selected_country}',
    )
    selected_avg = filtered_happiness[selected_data].mean()
    return line_fig, f'The average {selected_data} for {selected_country} is {selected_avg}'


if __name__ == '__main__':
    app.run_server(debug=True)

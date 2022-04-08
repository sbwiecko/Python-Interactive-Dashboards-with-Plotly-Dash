import pandas as pd

# new import statements in newer versions of Dash!
from dash import Dash, callback, html, dcc, Input, Output, State
import plotly.express as px

# app built on the previous script
app = Dash()


# load the dataset
happiness = pd.read_csv('../../data/world_happiness.csv')

region_options = happiness['region'].unique()

data_options = {
    'happiness_score': "Happiness Score",
    'happiness_rank' : "Happiness Rank",
}


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
        ),
        dcc.RadioItems(
            id='data-radio',
            options=data_options,
            value='happiness_score',
        ),
        html.Br(),
        html.Button(
            id='submit-button-state',
            n_clicks=0, # available to all Dash components
            children='Update the graph',
        ),
        dcc.Graph(
            id='happiness-graph',
        ),
        html.Div(
            id='average-div',
        ),
    ]
)

# chaining the change in the top RadioItems will be chained to the DropDown menu

# @app.callback( # in newer versions of Dash can import callback directly from dash
@callback(
    Output('country-dropdown', 'options'),
    Output('country-dropdown', 'value'),
    Input('region-radio', 'value'),
)
def update_dropdown(selected_region):
    filtered_happiness = happiness[happiness['region'] == selected_region]
    country_options = filtered_happiness['country'].unique()

    return country_options, country_options[0]

# State ∼ Input but doesn't trigger the callback function
# State is the `Input` of callback that:
# -gets added in @app.callback and def
# -gets passed into the callback function
# -but compared to Input, doesn't trigger the callback function

# @app.callback(
@callback(
    Output('happiness-graph', 'figure'),
    Output('average-div', 'children'),
    Input('submit-button-state', 'n_clicks'), # each click update n_clicks which triggers callback
    State('country-dropdown', 'value'), # State ∼ Input but doesn't trigger the callback function
    State('data-radio', 'value'))
# even if not used in function, Input from button and any change of it will trigger the function
def update_graph(button_click, selected_country, selected_data):
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

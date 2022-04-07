import pandas as pd

import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# app built on the previous script
app = dash.Dash()


# load the dataset
happiness = pd.read_csv('../../data/world_happiness.csv')

country_options = happiness['country'].unique()

# values are actual columns in the dataset
# data_options = [{'label': 'Happiness Score', 'value': 'happiness_score'},
#                 {'label': 'Happiness Rank', 'value': 'happiness_rank'}]
# now other formats available for RaioItem options, e.g. {"value": "label"}:
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
        dcc.Dropdown(
            id='country-dropdown',
            options=country_options,
            value='United States',
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


"""
# if at least one of the properties change it triggers the callback
@app.callback(
    Output1(component_id1, component_property1),
    Output2(component_id2, component_property2),
    Output3(component_id3, component_property3),
    Input1(component_id1, component_property1),
    Input2(component_id2, component_property2),
    Input3(component_id3, component_property3),
)
def function_name(input1, input2, input3):
    # body of the function
    return output2, output2, output3
# the order of the inputs AND the outputs is same as in the decorator !
"""


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

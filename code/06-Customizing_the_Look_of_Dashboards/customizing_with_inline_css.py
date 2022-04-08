import dash
from dash import html, dcc
import pandas as pd

soccer = pd.read_csv('../../data/fifa_soccer_players.csv')

player_name_options = soccer['long_name'].unique()

app = dash.Dash()

# the CSS property keys are camelCase in Dash

app.layout = html.Div(
    [
        html.H1(
            'Soccer Players Dashboard',
            style={
                'textAlign' : 'center',
                'fontFamily': 'fantasy',
                'fontSize'  : 50,# same as '50px'
                'color'     : 'blue'
            }
        ),
        html.P(
            [ # multiple components as children of the P component in a list
                'Source: ',
                html.A(
                    'Sofifa',
                    href='https://sofifa.com/',
                    target="_blank"
                )
            ],
           style={'border': 'solid'}
        ),
        html.Label('Player name: '),
        dcc.Dropdown(
            options=player_name_options,
            value=player_name_options[0],
            style={'backgroundColor': 'lightgreen'}
        )
    ],
    # Div is a container with specific properties
    style={'padding': 100, 'border': 'solid'}
)

if __name__ == '__main__':
    app.run_server(debug=True)

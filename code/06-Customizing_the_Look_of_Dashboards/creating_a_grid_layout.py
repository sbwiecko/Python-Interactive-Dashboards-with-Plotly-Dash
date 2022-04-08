import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

soccer = pd.read_csv('../../data/fifa_soccer_players.csv')

player_name_options = soccer['long_name'].unique()

# must have link to stylesheet to use the Bootstrap grid system
# see also https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/
# the GRID themes is an empty stylesheet with a functioning grid system
app = Dash(external_stylesheets=[dbc.themes.GRID])

app.layout = html.Div(
    [
        html.H1('Soccer Players Dashboard'),
        # Rows are lists of Cols, not the reverse !
        dbc.Row(
            [
                dbc.Col(
                    html.P(
                        [
                            'Source: ',
                            html.A('Sofifa', href='https://sofifa.com/', target="_blank"),
                        ]
                    )
                ),

                dbc.Col(
                    [
                        html.Label('Player name: '),
                        dcc.Dropdown(options=player_name_options, value=player_name_options[0]),
                    ]
                )
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)

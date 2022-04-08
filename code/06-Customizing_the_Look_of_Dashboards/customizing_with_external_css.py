from dash import Dash, html, dcc

# pip install dash-bootstrap-components
# see also https://dash-bootstrap-components.opensource.faculty.ai/
import dash_bootstrap_components as dbc
import pandas as pd

soccer = pd.read_csv('../../data/fifa_soccer_players.csv')

player_name_options = soccer['long_name'].unique()

# external_stylesheets as a list of string (URLs) or dicts
# app = Dash(external_stylesheets=["https://raw.githubusercontent.com/sbwiecko/worg_theme/main/default.scss"])

# could also be a local CSS file (see https://dash.plotly.com/external-resources)
app = Dash(external_stylesheets=[dbc.themes.SKETCHY])
# many styles available from dashèbootstrap, e.g., DARKLY, LUMEN, LUX, MINTY, PULSE, SANDSTONE, SIMPLEX etc.
# see more on https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/#available-themes

# styles cascade acc. priority:
# 1- inline CSS style
# 2- external CSS style sheets
# remove all custom inline styling in the script

app.layout = html.Div(
    [
        html.H1(
            'Soccer Players Dashboard',
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
        ),
        html.Label('Player name: '),
        dcc.Dropdown(
            options=player_name_options,
            value=player_name_options[0],
        )
    ],
)

if __name__ == '__main__':
    app.run_server(debug=True)

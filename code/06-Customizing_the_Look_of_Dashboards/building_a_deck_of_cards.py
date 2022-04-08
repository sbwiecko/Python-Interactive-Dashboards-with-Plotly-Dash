import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

sofifa_logo = "https://uptime.com/media/website_profiles/sofifa.com.png"

soccer = pd.read_csv('../../data/fifa_soccer_players.csv')
# some statistics
avg_age = soccer['age'].mean()
avg_height = soccer['height_cm'].mean()
avg_weight = soccer['weight_kg'].mean()


navbar = dbc.NavbarSimple(
    brand='Soccer Players Dashboard',
    children=[
        html.Img(src=sofifa_logo, height=20),
        html.A(
            'Data Source',
            href='https://sofifa.com/',
            target='_blank',
            style={'color': 'black'},
        )
    ],
    color='primary',
    fluid=True, # fill the horizontal bar
)

# see https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/
cards = dbc.Row(# dbc.CardDeck depreciated since v1.0, use grid system instead
    [
        dbc.Col(
            dbc.Card(
                dbc.CardBody( # CardBody helps with the padding
                    [
                        html.H4('Avg. Age'),
                        html.H5(f'{round(avg_age, 1)} years'),
                    ]
                ),
                style={'textAlign': 'center', 'color': 'white'},
                color='lightblue',
            ),
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H4('Avg. Height'),
                        html.H5(f'{round(avg_height, 1)} cm'),
                    ]
                ),
                style={'textAlign': 'center', 'color': 'white'},
                color='blue',
            ),
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H4('Avg. Weight'),
                        html.H5(f'{round(avg_weight, 1)} kg'),
                    ]
                ),
                style={'textAlign': 'center', 'color': 'white'},
                color='darkblue',
            ),
        ),
    ]
)


app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([navbar, html.Br(), cards])


if __name__ == '__main__':
    app.run_server(debug=True)
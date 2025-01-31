from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

sofifa_logo = "https://uptime.com/media/website_profiles/sofifa.com.png"

# https://dash-bootstrap-components.opensource.faculty.ai/docs/components/navbar/
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


app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(navbar)

if __name__ == '__main__':
    app.run_server(debug=True)
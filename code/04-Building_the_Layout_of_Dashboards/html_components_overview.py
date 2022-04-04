import dash
import dash_html_components as html

app = dash.Dash()

# app.layout = html.Div(
#     children=[
#         html.H1(children='World Happiness Dashboard'),
#         html.P(children=[
#             'This dashboard shows the happiness score.',
#             html.Br(),
#             html.A(
#                 'World Happiness Report Data Source',
#                 href='https://worldhappiness.report/',
#                 target="_blank" # open in a new tab
#             )
#         ])
#     ]
# )

## In the preceeding code, the layout was as follow:
# <div>
#   <h1>World Happiness Dashboard</h1>
#   <p>
#     This dashboard shows the happiness score.
#     <br>
#     <a href="https://worldhappiness.report/"
#     target="_blank">World Happiness Report Data Source</a>
#   </p>
# </div>


## Different layout, not completely equivalent
## because the text and the link will be in different paragraphs
app.layout = html.Div(children=[
    html.H1(children='World Happiness Dashboard'),
    html.P('This dashboard shows the happiness score.'),
    html.A(
        'World Happiness Report Data Source',
        href='https://worldhappiness.report/',
        target="_blank" # open in a new tab
    )
])

# <div>
#   <h1>World Happiness Dashboard</h1>
#   <p>This dashboard shows the happiness score.
#   </p>
#   <a href="https://worldhappiness.report/"
#   target="_blank">World Happiness Report Data Source</a>
# </div>

if __name__ == '__main__':
    app.run_server(debug=True)

import dash
from dash import html, dcc
from dash.dependencies import Input, Output

app = dash.Dash()

# give unique id to components of the dashboard for input and ouotput
app.layout = html.Div(
    [
        dcc.Input(id='input-text', value='Change this text', type='text'),
        html.Div(children='', id='output-text'), # children empty string optional
    ]
)


"""
@app.callback(
    Output(component_id, component_property),
    Input(component_id, component_property), #e.g., 'children' or 'value'
)
def function_name(input_argument_name): # corresponds to the Input object
    # body of the function
    return output_object                # corresponds to the Output object
"""


@app.callback(
    Output(component_id='output-text', component_property='children'),
    Input(component_id='input-text', component_property='value'),
    # no need to list input in newer versions of Dash
)
def update_output_div(input_text):
    return f"Text: {input_text}"


if __name__ == '__main__':
    app.run_server(debug=True)
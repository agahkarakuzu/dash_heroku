import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Setup the app
# Make sure not to change this file name or the variable names below,
# the template is configured to execute 'server' on 'app.py'

app = dash.Dash(__name__)


app.layout = html.Div([
    dcc.Input(id='my-id', value='initial value', type='text'),
    html.Div(id='my-div')
])

# Dash uses data driven callbacks via decorators 
# Inputs and outputs are defined by this decorator 

# The following decorator simply states that children property of the my-div component (which is just a Div)
# will have the value inputed by my-id component, which is a textbox. 

# The relationship between input and the output is determined by update_output_div function.


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

server = app.server
app.config.suppress_callback_exceptions = True

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

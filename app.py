# Import required libraries
import os
from random import randint

import plotly.plotly as py
from plotly.graph_objs import *

import flask
import dash
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html


# Setup the app
# Make sure not to change this file name or the variable names below,
# the template is configured to execute 'server' on 'app.py'

app = dash.Dash(__name__, server=server)
port = int(os.environ.get("PORT", 5000))

# Put your Dash code here


# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=False,
                   host="0.0.0.0",
                   port=port)

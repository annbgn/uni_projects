import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

import FIS001 as fis

import pandas as pd
import numpy as np
import plotly.express as px
from MFFunctions001 import *


app = dash.Dash(__name__)
app.title = "FIS"

app.config["suppress_callback_exceptions"] = True

app.layout = html.Div(
    children=[
        html.H1(children="FIS"),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Span(children="Budget: ", className="FISText"),
                        dcc.Input(
                            id="Budget",
                            type="number",
                            placeholder="Budget...",
                            value="",
                            className="FISInput",
                            min=0,
                            max=100,
                            step=5,
                        ),
                        html.Span(children="Star: ", className="FISText"),
                        dcc.Input(
                            id="Star",
                            type="number",
                            placeholder="Star...",
                            value="",
                            className="FISInput",
                            min=0,
                            max=100,
                            step=5,
                        ),
                        html.Button(
                            "Result", id="enter", n_clicks=0, className="ControlButton"
                        ),
                    ]
                ),
                html.Div(
                    id="result",
                    children=" ",
                    className="FISText",
                    style={"font-size": "2em"},
                ),
            ],
            style={
                "display": "flex",
                "flex-direction": "column",
                "justify-content": "center",
                "align-items": "center",
            },
        ),
        html.Div(
            id="fugures",
            style={
                "display": "flex",
                "flex-direction": "column",
                "justify-content": "center",
                "align-items": "center",
            },
        ),
    ]
)


@app.callback(
    Output("result", "children"),
    [Input("enter", "n_clicks")],
    [State("Budget", "value"), State("Star", "value")],
)
def FormResult(n, s, p):
    if n is not None and n > 0:
        try:
            fis.Budget = float(s)
            fis.Star = float(p)
            fis.Run()
        except:
            return "Oscar = "
        return "Oscar = " + str(fis.Oscar)
    else:
        return "Oscar = "


@app.callback(
    [Output("fig1", "style"), Output("fig2", "style"), Output("fig3", "style")],
    [State("fig1", "style")],
)
def TogleDisplay(n, s):
    if n is not None and n > 0:
        if s == {"display": "none"}:
            return 3 * [{"display": "block"}]
        else:
            return 3 * [{"display": "none"}]
    else:
        return 3 * [s]


if __name__ == "__main__":
    app.run_server(debug=True)

import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

import FIS001 as fis

import pandas as pd
import numpy as np
import plotly.express as px
from MFFunctions001 import *


def PlotTemperature():
    x = list(np.linspace(0, 100, 400))
    y1 = [mfTemperatureLow(z) for z in x]
    y2 = [mfTemperatureAverage(z) for z in x]
    y3 = [mfTemperatureHigh(z) for z in x]
    y4 = [mfTemperatureGreat(z) for z in x]
    dd = {
        "Temperature": 4 * x,
        "MF": y1 + y2 + y3 + y4,
        "LT": 400 * ["Low"] + 400 * ["Average"] + 400 * ["High"] + 400 * ["Great"],
    }
    df = pd.DataFrame(dd)
    return px.line(df, x="Temperature", y="MF", color="LT", hover_name="LT")


def PlotHumidity():
    x = list(np.linspace(0, 100, 400))
    y1 = [mfHumidityLow(z) for z in x]
    y2 = [mfHumidityAverage(z) for z in x]
    y3 = [mfHumidityHigh(z) for z in x]
    dd = {
        "Humidity": 3 * x,
        "MF": y1 + y2 + y3,
        "LT": 400 * ["Low"] + 400 * ["Middle"] + 400 * ["High"],
    }
    df = pd.DataFrame(dd)
    return px.line(df, x="Humidity", y="MF", color="LT", hover_name="LT")


def PlotComfort():
    x = list(np.linspace(2, 5, 400))
    y1 = [mfComfortBad(z) for z in x]
    y2 = [mfComfortSatisfactory(z) for z in x]
    y3 = [mfComfortGood(z) for z in x]
    y4 = [mfComfortExcellent(z) for z in x]
    dd = {
        "Comfort": 4 * x,
        "MF": y1 + y2 + y3 + y4,
        "LT": 400 * ["Bad"]
        + 400 * ["Satisfactory"]
        + 400 * ["Good"]
        + 400 * ["Excelent"],
    }
    df = pd.DataFrame(dd)
    return px.line(df, x="Comfort", y="MF", color="LT", hover_name="LT")


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
                        html.Span(children="Temperature: ", className="FISText"),
                        dcc.Input(
                            id="Temperature",
                            type="number",
                            placeholder="Temperature...",
                            value="",
                            className="FISInput",
                            min=0,
                            max=100,
                            step=5,
                        ),
                        html.Span(children="Humidity: ", className="FISText"),
                        dcc.Input(
                            id="Humidity",
                            type="number",
                            placeholder="Humidity...",
                            value="",
                            className="FISInput",
                            min=0,
                            max=100,
                            step=5,
                        ),
                        html.Button(
                            "Result", id="enter", n_clicks=0, className="ControlButton"
                        ),
                        html.Button(
                            "MFs", id="mfs", n_clicks=0, className="ControlButton"
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
            children=[
                dcc.Graph(id="fig1", figure=PlotTemperature(), style={"display": "none"}),
                dcc.Graph(id="fig2", figure=PlotHumidity(), style={"display": "none"}),
                dcc.Graph(id="fig3", figure=PlotComfort(), style={"display": "none"}),
            ],
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
    [State("Temperature", "value"), State("Humidity", "value")],
)
def FormResult(n, s, p):
    if n is not None and n > 0:
        try:
            fis.Temperature = float(s)
            fis.Humidity = float(p)
            fis.Run()
        except:
            return "Comfort = "
        return "Comfort = " + str(fis.Comfort)
    else:
        return "Comfort = "


@app.callback(
    [Output("fig1", "style"), Output("fig2", "style"), Output("fig3", "style")],
    [Input("mfs", "n_clicks")],
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

import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

import json as j
import numpy as np
import pandas as pd
import plotly.express as px

import uploadfile as uf
import FIS as f

FIS_Scheme = {}
FIS = None

TAB1 = [
    html.Div(
        children=[
            dcc.Upload(
                html.Button("🗁 Open", className="ControlButton"),
                id="myfile",
                accept="application/json",
            ),
            html.Button(
                "▶ Create FIS", id="createfis", className="ControlButton", n_clicks=0
            ),
        ],
        style={"display": "flex", "justify-content": "center", "margin-top": "0.5em"},
    ),
    html.Div(
        children=[
            dcc.Textarea(
                id="mytext",
                value="",
                placeholder="JSON...",
                wrap="hard",
                style={
                    "width": "90%",
                    "height": "15em",
                    "margin-top": "1em",
                    "font-size": "1.2em",
                },
            )
        ],
        style={"display": "flex", "justify-content": "center"},
    ),
]

TAB2 = [html.H3("FIS не сформирован", style={"text-align": "center", "color": "navy"})]

TAB3 = [
    html.H3(
        "Графики невозможно построить", style={"text-align": "center", "color": "navy"}
    )
]

tabs_style = {"height": "2em"}
tab_style = {
    "border-top": "2px solid #a0a0a0",
    "border-left": "1px solid #a0a0a0",
    "border-right": "1px solid #a0a0a0",
    "padding": "6px",
    "background-color": "#dfdfdf",
}

tab_selected_style = {
    "border-top": "2px solid #a0a0a0",
    "border-left": "1px solid #a0a0a0",
    "border-right": "1px solid #a0a0a0",
    "background-color": "white",
    "color": "black",
    "font-weight": "bold",
    "padding": "6px",
}


def JoinListsFromDict(d):
    L = []
    for k in d.keys():
        L += d[k]
    return L


def PlotInputVar(F, VarName):
    a = F.Inputs[VarName].LeftB
    b = F.Inputs[VarName].RightB
    x = list(np.linspace(a, b, 400))
    LTNames = F.Inputs[VarName].LTerms.keys()
    N = len(LTNames)
    LT = {t: F.Inputs[VarName].LTerms[t] for t in LTNames}
    Y = {t: [LT[t].MFunc.Calc(z) for z in x] for t in LTNames}
    Labels = {t: 400 * [t] for t in LTNames}
    dd = {VarName: N * x, "MF": JoinListsFromDict(Y), "LT": JoinListsFromDict(Labels)}
    df = pd.DataFrame(dd)
    return px.line(df, x=VarName, y="MF", color="LT", hover_name="LT")


def PlotOutputVar(F, VarName):
    a = F.Outputs[VarName].LeftB
    b = F.Outputs[VarName].RightB
    x = list(np.linspace(a, b, 400))
    LTNames = F.Outputs[VarName].LTerms.keys()
    N = len(LTNames)
    LT = {t: F.Outputs[VarName].LTerms[t] for t in LTNames}
    Y = {t: [LT[t].MFunc.Calc(z) for z in x] for t in LTNames}
    Labels = {t: 400 * [t] for t in LTNames}
    dd = {VarName: N * x, "MF": JoinListsFromDict(Y), "LT": JoinListsFromDict(Labels)}
    df = pd.DataFrame(dd)
    return px.line(df, x=VarName, y="MF", color="LT", hover_name="LT")


app = dash.Dash(__name__)
app.title = "FIS"

app.config["suppress_callback_exceptions"] = True

app.layout = html.Div(
    children=[
        dcc.Tabs(
            id="fistabs",
            value="fiscreation",
            children=[
                dcc.Tab(
                    id="tab1",
                    label="Create FIS",
                    value="fiscreation",
                    children=TAB1,
                    style=tab_style,
                    selected_style=tab_selected_style,
                ),
                dcc.Tab(
                    id="tab2",
                    label="Input Data",
                    value="inputdata",
                    children=TAB2,
                    style=tab_style,
                    selected_style=tab_selected_style,
                ),
                dcc.Tab(
                    id="tab3",
                    label="Membership Function",
                    value="mfunctions",
                    children=TAB3,
                    style=tab_style,
                    selected_style=tab_selected_style,
                ),
            ],
            style=tabs_style,
        )
    ]
)


@app.callback(Output("mytext", "value"), [Input("myfile", "contents")])
def load_JSON(c):
    global FIS_Scheme
    if c is not None and c != "":
        FIS_Scheme, cont = uf.loadJSON(c)
        return cont
    else:
        return ""


@app.callback(
    [Output("tab2", "children"), Output("tab3", "children")],
    [Input("createfis", "n_clicks")],
    [State("mytext", "value")],
)
def Create_FIS(n, s):
    global FIS_Scheme
    global FIS
    global TAB2
    if n is not None and n > 0:
        FIS_Scheme = j.loads(s)
        FIS = f.FIS(FIS_Scheme)
        ch2 = [
            html.Div(
                children=[
                    html.Div(
                        id="input_cont",
                        children=[
                            dcc.Input(
                                id="input_" + x,
                                type="number",
                                placeholder=x,
                                value="",
                                className="FISInput",
                            )
                            for x in FIS.Inputs
                        ],
                    ),
                    html.Button(
                        "⏎ Enter",
                        id="runfis",
                        className="ControlButton",
                        n_clicks=0,
                        style={"margin-left": "1em"},
                    ),
                    html.Div(
                        id="output_cont",
                        children=[
                            html.Div(id="output_" + y, children=y, className="FISText")
                            for y in FIS.Outputs
                        ],
                    ),
                ],
                style={"margin-top": "1em", "margin-left": "30%"},
            )
        ]
        ch3 = [
            html.Div(
                id="fugures",
                children=[
                    dcc.Graph(id="fig_" + name, figure=PlotInputVar(FIS, name))
                    for name in FIS.Inputs.keys()
                ]
                + [
                    dcc.Graph(id="fig_" + name, figure=PlotOutputVar(FIS, name))
                    for name in FIS.Outputs.keys()
                ],
            )
        ]
        return [ch2, ch3]
    else:
        return [TAB2, TAB3]


@app.callback(
    Output("output_cont", "children"),
    [Input("runfis", "n_clicks")],
    [State("input_cont", "children")],
)
def Run_FIS(n, S):
    global FIS
    if n is not None and n > 0:
        for k, x in zip(FIS.Inputs.keys(), S):
            FIS.Inputs[k].Value = float(x["props"]["value"])
        FIS.Run()
        ch = [
            html.Div(
                children=[
                    html.Div(
                        children=y + " = " + "{:.2f}".format(FIS.Outputs[y].Value),
                        className="FISText",
                    )
                ]
            )
            for y in FIS.Outputs.keys()
        ]
        return ch
    else:
        return [
            html.Div(id="output_" + y, children=y, className="FISText")
            for y in FIS.Outputs
        ]


if __name__ == "__main__":
    app.run_server(debug=True)

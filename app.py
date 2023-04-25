import dash
from dash import html, dcc
from dash.dependencies import Input, Output



import flask
import pandas as pd
import os


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/hello-world-stock.csv"
)

dash_app = dash.Dash("app")
app = dash_app.server

dash_app.scripts.config.serve_locally = False

dash_app.layout = html.Div(
    [   
        html.Script(src="https://cdn.plot.ly/plotly-basic-latest.min.js"),
        html.H1("Stock Tickers"),
        dcc.Dropdown(
            id="my-dropdown",
            options=[
                {"label": "Tesla", "value": "TSLA"},
                {"label": "Apple", "value": "AAPL"},
                {"label": "Coke", "value": "COKE"},
            ],
            value="TSLA",
        ),
        dcc.Graph(id="my-graph"),
    ],
    className="container",
)


@dash_app.callback(Output("my-graph", "figure"), [Input("my-dropdown", "value")])
def update_graph(selected_dropdown_value):
    dff = df[df["Stock"] == selected_dropdown_value]
    return {
        "data": [
            {"x": dff.Date, "y": dff.Close, "line": {"width": 3, "shape": "spline"}}
        ],
        "layout": {"margin": {"l": 30, "r": 20, "b": 30, "t": 20}},
    }


if __name__ == "__main__":
    dash_app.run_server(debug=True)

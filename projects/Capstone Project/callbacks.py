from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from services import get_filtered_animals
from typing import Any
import plotly.express as px


def register_callbacks(app, db):
    @app.callback(
        Output("datatable-id", "data"),
        Input("filter-type", "value")
    )
    def update_table(filter_type: str):
        data = get_filtered_animals(db, filter_type)

        # Convert MongoDB ObjectId to string and list traits to comma-separated string
        for record in data:
            if "_id" in record:
                record["_id"] = str(record["_id"])
            if "traits" in record and isinstance(record["traits"], list):
                record["traits"] = ", ".join(record["traits"])

        return data or []

    @app.callback(
        Output("graph-id", "children"),
        Input("datatable-id", "data")
    )
    def update_graph(viewData: Any):
        if not viewData:
            return html.P("No data available to display.")

        df = pd.DataFrame(viewData)

        # Verify required columns are present
        required_cols = ["breed", "score", "name", "location_lat", "location_long"]
        for col in required_cols:
            if col not in df.columns:
                return html.P(f"Data missing required field: {col}")

        # Pie chart: breed distribution by total score
        breed_counts = df.groupby("breed")["score"].sum().reset_index()
        pie_chart = dcc.Graph(
            figure=px.pie(breed_counts, names="breed", values="score", title="Breed Distribution")
        )

        # Map of animal locations
        map_fig = px.scatter_mapbox(
            df,
            lat="location_lat",
            lon="location_long",
            hover_name="name",
            hover_data={"breed": True, "score": True, "location_lat": False, "location_long": False},
            color="breed",
            zoom=3,
            height=400
        )
        map_fig.update_layout(
            mapbox_style="open-street-map",
            margin={"r": 0, "t": 0, "l": 0, "b": 0},
            legend_title_text=""
        )
        map_graph = dcc.Graph(figure=map_fig)

        # Return both graphs centered side by side
        return html.Div(
            children=[
                html.Div(pie_chart, style={'width': '55%', 'display': 'inline-block', 'margin-right': '2%'}),
                html.Div(map_graph, style={'width': '55%', 'display': 'inline-block'})
            ],
            style={'text-align': 'center'}
        )

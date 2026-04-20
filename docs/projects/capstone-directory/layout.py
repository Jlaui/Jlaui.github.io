# layout.py
from dash import html, dcc, dash_table


def create_layout():
    return html.Div([
        # Logo at the top of the dashboard
        html.Img(
            src='/assets/Grazioso Salvare Logo.png',
            style={'height': '100px'}
        ),

        # Main heading, centered and bolded
        html.Center(html.B(html.H1('Grazioso Salvare Rescue Animal Data Dashboard'))),
        html.Hr(),

        # Filter section for the rescue type
        html.Div([
            html.Label("Select Rescue Type:"),

            dcc.RadioItems(
                id='filter-type',
                options=[
                    {'label': 'Water Rescue', 'value': 'water'},
                    {'label': 'Mountain/Wilderness Rescue', 'value': 'mountain'},
                    {'label': 'Disaster/Tracking', 'value': 'disaster'},
                    {'label': 'Reset', 'value': 'reset'}
                ],
                value='reset',
                labelStyle={'display': 'block'}
            )
        ], style={'width': '25%', 'margin': 'auto'}),
        html.Hr(),

        # DataTable with custom column headers and styles
        dash_table.DataTable(
            id='datatable-id',
            columns=[
                {'name': 'ID', 'id': '_id'},
                {'name': 'Animal Name', 'id': 'name'},
                {'name': 'Breed', 'id': 'breed'},
                {'name': 'Age (weeks)', 'id': 'age_upon_outcome_in_weeks'},
                {'name': 'Traits', 'id': 'traits'},
                {'name': 'Latitude', 'id': 'location_lat'},
                {'name': 'Longitude', 'id': 'location_long'},
                {'name': 'Score', 'id': 'score'},
            ],
            style_table={'width': '90%', 'margin': 'auto', 'overflowX': 'auto'},
            style_header={
                'backgroundColor': '#2C3E50',
                'color': 'white',
                'fontWeight': 'bold',
                'textAlign': 'center',
            },
            style_cell={
                'textAlign': 'center',
                'padding': '8px',
                'whiteSpace': 'normal',
                'height': 'auto',
            },
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': '#ECF0F1'
                }
            ],
            page_size=10,
        ),

        html.Br(),
        html.Hr(),

        html.Div(className='row', style={'display': 'flex'}, children=[
            html.Div(id='graph-id', className='col s12 m6'),
            html.Div(id='map-id', className='col s12 m6')
        ])
    ])

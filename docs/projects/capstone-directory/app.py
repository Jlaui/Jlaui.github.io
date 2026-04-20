from dash import Dash
from crud import AnimalShelter
from layout import create_layout
from callbacks import register_callbacks

# Dash is the main web application framework used to build interactive dashboards.
# __name__ ensures that assets and routes are correctly resolved.
# Initialize app and Database
app = Dash(__name__)
db = AnimalShelter()

# Set layout; used to define the UI (data tables, charts, filters, and logo.
app.layout = create_layout()

# The callbacks are used to handle the interactive elements in Dash
# Updating data tables based on the filters
# Register callbacks is used to modularize the functions
register_callbacks(app, db)

# Runs the server in debug mode, this enables hot reload as well as additional error messages.
# In the future, for production, debug = false should be used for security reasons.
if __name__ == '__main__':
    app.run(debug=True)

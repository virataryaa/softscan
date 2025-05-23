import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

# Sample data
days_to_expiration = list(range(45, -1, -1))
open_interest = [800000 * (i / 45)**2 for i in range(45, -1, -1)]

app = Dash(__name__)

app.layout = html.Div([
    html.H2("Demo: Roll Tool Visualization (Click-enabled)"),
    dcc.Graph(
        id='roll-graph',
        figure={
            'data': [
                go.Scatter(
                    x=days_to_expiration,
                    y=open_interest,
                    mode='lines+markers',
                    name='Open Interest',
                    marker=dict(size=6)
                )
            ],
            'layout': go.Layout(
                title='Open Interest vs Trading Days to Expiration',
                xaxis={'title': 'Trading Days to Expiration'},
                yaxis={'title': 'Front Month Open Interest'},
                clickmode='event+select'
            )
        }
    ),
    html.Div(id='click-output', style={'marginTop': 20, 'fontSize': 16})
])

@app.callback(
    Output('click-output', 'children'),
    Input('roll-graph', 'clickData')
)
def display_click_data(clickData):
    if clickData:
        point = clickData['points'][0]
        return f"You clicked on: {point['x']} days, OI = {point['y']:.2f}"
    return "Click on a point to see its details."

if __name__ == '__main__':
    app.run(debug=True)  # Use app.run() instead of app.run_server()

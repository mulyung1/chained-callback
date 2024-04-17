from dash import Dash, dcc, html, callback, Output, Input

#import css
stail=['https://codepen.io/chriddyp/pen/bWLwgP.css']c
#initialize app
app=Dash(__name__, external_stylesheets=stail)
server=app.server

all_options={
    'Male':['Alek', 'Joel', 'Zack'],
    'Female':['Christine','Doreen','Jane']
}

#define app layout
app.layout=html.Div([
    html.H1('CHAINED CALLBACKS', style={'color':'red', 'fontSize':'50px','textAlign':'center'}),
    dcc.RadioItems(
        list(all_options.keys()),
        'Male',
        id='jenda'
    ),
    html.Hr(),
    dcc.RadioItems(id='name'),
    html.Hr(),
    html.Div(id='display')
])

#the chained callbacks
#callback decorators to connect between inputs and output
#1 set the name options based on selected value at jenda
@callback(
    Output('name', 'options'),
    Input('jenda','value')
)
def set_name_options(selected):
    return [{'label':i,'value':i} for i in all_options[selected]]

#2 set an initial value 
@callback(
    Output('name','value'),
    Input('name', 'options')
)
def set_name_value(available_options):
    return available_options[1]['value']

#3 display
@callback(
    Output('display','children'),
    Input('jenda','value'),
    Input('name','value')
)
def displei(slctd_jenda, slctd_name):
    return f'{slctd_name} is a {slctd_jenda} name.'
 
#run the app
if __name__ == '__main__':
    app.run(debug=True)


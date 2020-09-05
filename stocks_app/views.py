from django.shortcuts import render
import finnhub
from plotly.offline import plot
import plotly.graph_objects as go
from plotly.graph_objs import Scatter
import pandas as pd

# Create your views here.
def home(request):
    x_data = [0,1,2,3]
    y_data = [x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                mode='lines', name='test',
                opacity=0.8, marker_color='green')],
                output_type='div')
    finnhub_client = finnhub.Client(api_key="bt1fg7f48v6qjjkjlvvg")
    df = pd.read_csv('https://finnhub.io/api/v1/stock/candle?symbol=AAPL&resolution=D&count=500&format=csv&token=bt1fg7f48v6qjjkjlvvg')
    # print(df)
    fig = go.Figure(data=[go.Candlestick(x=df['t'],
                                         open=df['o'],
                                         high=df['h'],
                                         low=df['l'],
                                         close=df['c'])])

    #fig.show()
    res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)
    res1 = finnhub_client.company_profile2(symbol='AAPL')
    new = finnhub_client.company_news('AAPL', _from="2020-06-01", to="2020-06-10")
    financial = finnhub_client.company_basic_financials('AAPL', 'margin')
    return render(request, 'home.html', {'response': res, 'response1': res1, 'response_new': new, 'financial': financial, 'plot_div': plot_div,'fig':fig.to_html()})

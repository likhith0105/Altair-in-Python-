import altair as alt
from vega_datasets import data

stocks = data.stocks()

chart = alt.Chart(stocks).mark_line(point=True).encode(
    x='date:T',
    y='price:Q',
    color='symbol:N',
    tooltip=['date:T', 'price:Q', 'symbol:N']
).properties(
    title='Stock Prices Over Time'
)

chart   
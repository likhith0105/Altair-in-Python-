import altair as alt
from vega_datasets import data

cars = data.cars()

chart = alt.Chart(cars).mark_bar().encode(
    x='Cylinders:O',
    y='mean(Miles_per_Gallon):Q',
    color='Cylinders:O'
).facet(
    column='Origin:N'
).properties(
    title='Average MPG by Cylinders'
)

chart

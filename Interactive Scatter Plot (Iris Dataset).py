import altair as alt
from vega_datasets import data
iris = data.iris()

chart = alt.Chart(iris).mark_point().encode(
    x='sepalLength',
    y='petalLength',
    shape='species',
    color='species',
    tooltip=['sepalLength', 'petalLength', 'species']
)

chart
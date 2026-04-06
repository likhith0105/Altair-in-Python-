import altair as alt
import pandas as pd

d = pd.DataFrame({
    'Website': ['StackOverflow', 'FreeCodeCamp', 'GeeksForGeeks', 'MDN', 'CodeAcademy'],
    'Score': [65, 50, 99, 75, 33]
})

chart = alt.Chart(d).mark_bar().encode(
    x='Website',
    y='Score'
)

chart
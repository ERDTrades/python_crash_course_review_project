import plotly.express as px
from trade_statistics import Statistics
from journal import Journal

journal = Journal()

stats = Statistics(journal.trades)


x = []
y = stats.cumulative_winrate(journal.trades)

for trade in journal.trades:
    if trade.result == "BE":
        continue

    x.append(trade.id)

labels = {
        "x": "Trade ID ",
        "y": "Win rate % "
    }

fig = px.line(
    x=x,
    y=y,
    title="Cumulative winrate chart",
    labels=labels,
    markers=True
)

fig.update_layout(
    font_color="#1C1FAA",
    paper_bgcolor='black',
    plot_bgcolor='black'
)

fig.update_yaxes(
    gridcolor="#111257"
)

fig.update_xaxes(
    gridcolor='#111257'
)


fig.show()



# W/L/BE trade count graph

x = ["W", "L", "BE"]
y = []

w = 0
l = 0
be = 0

for trade in journal.trades:
    if trade.result == "W":
        w += 1
    elif trade.result == "L":
        l += 1
    elif trade.result == "BE":
        be += 1

y.append(w)
y.append(l)
y.append(be)


fig = px.bar(
    x=x,
    y=y,
    title="Cumulative winrate chart",
    labels=labels,
)

fig.update_traces(
    marker_color='#1C1FAA',
    marker_opacity=0.6
)

fig.update_layout(
    font_color="#1C1FAA",
    paper_bgcolor='black',
    plot_bgcolor='black'
)

fig.update_yaxes(
    gridcolor="#111257"
)

fig.update_xaxes(
    gridcolor='#111257'
)

fig.show()





## UPDATED TODO
# Make hover data
# on line graph each marker after hovering - > basically each dot
# will represent every id value from json
# basically an outcome from statistics




# Plotly structure

# basically 1:1 matplotlib -> plotly 
# only make it more appealing with colors, hovers etc.
# rest is history
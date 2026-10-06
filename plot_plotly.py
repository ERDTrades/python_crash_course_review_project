import plotly.express as px
from trade_statistics import Statistics
from journal import Journal
import pandas as pd


journal = Journal()

stats = Statistics(journal.trades)

def cumulative_winrate_plotly(journal):
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
        font_color="#4447FF",
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





def wlbe_graph_plotly(journal):

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


    labels = {
            "x": "Outcome ",
            "y": "Amount "
        }

    fig = px.bar(
        x=x,
        y=y,
        labels=labels,
        title="Cumulative winrate chart"
    )

    fig.update_traces(
        marker_color='#4447FF',
        marker_opacity=0.6
    )

    fig.update_layout(
        font_color="#4447FF",
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


# p&l curve how trades are going with amount of trades
def pnl_amount_of_trades(journal):
    x = []
    y = stats.cumulative_pnl()

    for trade in journal.trades:
        x.append(trade.id)

    labels = {
        "x": "Trade id",
        "y": "Cumulative pnl"
    }

    fig = px.line(
        x=x,
        y=y,
        title="Cumulative p&l chart",
        labels=labels
    )

    fig.update_layout(
        font_color="#4447FF",
        paper_bgcolor='black',
        plot_bgcolor='black'
    )

    fig.update_yaxes(
        gridcolor="#111257"
    )

    fig.update_xaxes(
        gridcolor="#111257"
    )

    fig.show()

def session_pnl(journal):

    d = {"trade_id": [],
     "session": [],
     "cumulative_pnl": [],
     }

    london_current = 0
    nyc_current = 0
    asia_current = 0

    for trade in journal.trades:
        d["trade_id"].append(trade.id)
        d["session"].append(trade.session)

        if trade.session == "LONDON":
            london_current += trade.pnl
            d["cumulative_pnl"].append(london_current)

        elif trade.session == "NYC":
            nyc_current += trade.pnl
            d["cumulative_pnl"].append(nyc_current)

        elif trade.session == "ASIA":
            asia_current += trade.pnl
            d["cumulative_pnl"].append(asia_current)


    df = pd.DataFrame(data=d)


    fig = px.line(
        df,
        x="trade_id",
        y="cumulative_pnl",
        color="session"
    )


    fig.update_layout(
    font_color="#4447FF",
    paper_bgcolor='black',
    plot_bgcolor='black'
    )

    fig.update_yaxes(
        gridcolor="#111257"
    )

    fig.update_xaxes(
        gridcolor="#111257"
    )

    fig.show()

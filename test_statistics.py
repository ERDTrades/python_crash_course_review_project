from trade_statistics import Statistics
from trade import Trade
def test_win_rate_func():

    trades = [
        Trade(
            was_valid="N",
            date="2026-07-26",
            session="NYC",
            pair="NAS100",
            direction="SHORT",
            market_condition="ranging",
            rr=2.43,
            result="W",
            entry=13433.12,
            exit=13500.0,
            notes="OK"
        ),
        Trade(
            was_valid="Y",
            date="2026-07-27",
            session="LONDON",
            pair="XAUUSD",
            direction="LONG",
            market_condition="trending",
            rr=1.8,
            result="W",
            entry=3412.5,
            exit=3428.9,
            notes="Clean breakout."
        ),
        Trade(
            was_valid="Y",
            date="2026-07-27",
            session="NYC",
            pair="NAS100",
            direction="SHORT",
            market_condition="high-volume",
            rr=0.9,
            result="L",
            entry=13520.3,
            exit=13545.8,
            notes="Stopped out."
        ),
        Trade(
            was_valid="Y",
            date="2026-05-05",
            session="ASIA",
            pair="EURUSD",
            direction="LONG",
            market_condition="ranging",
            rr=1.6,
            result="W",
            entry=1.1,
            exit=1.1,
            notes="Moved to BE."
        ),
        Trade(
            was_valid="N",
            date="2026-07-28",
            session="LONDON",
            pair="UK100",
            direction="SHORT",
            market_condition="counter-trending",
            rr=2.1,
            result="W",
            entry=8920.1,
            exit=8878.4,
            notes="Countertrend worked."
        )
    ]

    statistics = Statistics(trades)



    assert statistics.win_rate(trades) == 80





def test_invalid_win_rate_func():

    trades = [
        Trade(
            was_valid="N",
            date="2026-07-26",
            session="NYC",
            pair="NAS100",
            direction="SHORT",
            market_condition="ranging",
            rr=2.43,
            result="W",
            entry=13433.12,
            exit=13500.0,
            notes="OK"
        ),
        Trade(
            was_valid="Y",
            date="2026-07-27",
            session="LONDON",
            pair="XAUUSD",
            direction="LONG",
            market_condition="trending",
            rr=1.8,
            result="W",
            entry=3412.5,
            exit=3428.9,
            notes="Clean breakout."
        ),
        Trade(
            was_valid="Y",
            date="2026-07-27",
            session="NYC",
            pair="NAS100",
            direction="SHORT",
            market_condition="high-volume",
            rr=0.9,
            result="L",
            entry=13520.3,
            exit=13545.8,
            notes="Stopped out."
        ),
        Trade(
            was_valid="Y",
            date="2026-05-05",
            session="ASIA",
            pair="EURUSD",
            direction="LONG",
            market_condition="ranging",
            rr=1.6,
            result="W",
            entry=1.1,
            exit=1.1,
            notes="Moved to BE."
        ),
        Trade(
            was_valid="N",
            date="2026-07-28",
            session="LONDON",
            pair="UK100",
            direction="SHORT",
            market_condition="counter-trending",
            rr=2.1,
            result="W",
            entry=8920.1,
            exit=8878.4,
            notes="Countertrend worked."
        )
    ]

    statistics = Statistics(trades)

    assert statistics.win_rate(trades) == 99999999






def test_cumulative_winrate():

    trades = [
        Trade(
            was_valid="N",
            date="2026-07-26",
            session="NYC",
            pair="NAS100",
            direction="SHORT",
            market_condition="ranging",
            rr=2.43,
            result="W",
            entry=13433.12,
            exit=13500.0,
            notes="OK"
        ),
        Trade(
            was_valid="Y",
            date="2026-07-27",
            session="LONDON",
            pair="XAUUSD",
            direction="LONG",
            market_condition="trending",
            rr=1.8,
            result="W",
            entry=3412.5,
            exit=3428.9,
            notes="Clean breakout."
        ),
        Trade(
            was_valid="Y",
            date="2026-07-27",
            session="NYC",
            pair="NAS100",
            direction="SHORT",
            market_condition="high-volume",
            rr=0.9,
            result="L",
            entry=13520.3,
            exit=13545.8,
            notes="Stopped out."
        ),
        Trade(
            was_valid="Y",
            date="2026-05-05",
            session="ASIA",
            pair="EURUSD",
            direction="LONG",
            market_condition="ranging",
            rr=1.6,
            result="W",
            entry=1.1,
            exit=1.1,
            notes="Moved to BE."
        ),
        Trade(
            was_valid="N",
            date="2026-07-28",
            session="LONDON",
            pair="UK100",
            direction="SHORT",
            market_condition="counter-trending",
            rr=2.1,
            result="W",
            entry=8920.1,
            exit=8878.4,
            notes="Countertrend worked."
        )
    ]

    statistics = Statistics(trades)

    result = statistics.cumulative_winrate(trades)

    assert result == [100.0, 100.0, 66.67, 75.0, 80.0]



def test_invalid_cumulative_winrate():

    trades = [
        Trade(
            was_valid="N",
            date="2026-07-26",
            session="NYC",
            pair="NAS100",
            direction="SHORT",
            market_condition="ranging",
            rr=2.43,
            result="W",
            entry=13433.12,
            exit=13500.0,
            notes="OK"
        ),
        Trade(
            was_valid="Y",
            date="2026-07-27",
            session="LONDON",
            pair="XAUUSD",
            direction="LONG",
            market_condition="trending",
            rr=1.8,
            result="W",
            entry=3412.5,
            exit=3428.9,
            notes="Clean breakout."
        ),
        Trade(
            was_valid="Y",
            date="2026-07-27",
            session="NYC",
            pair="NAS100",
            direction="SHORT",
            market_condition="high-volume",
            rr=0.9,
            result="L",
            entry=13520.3,
            exit=13545.8,
            notes="Stopped out."
        ),
        Trade(
            was_valid="Y",
            date="2026-05-05",
            session="ASIA",
            pair="EURUSD",
            direction="LONG",
            market_condition="ranging",
            rr=1.6,
            result="W",
            entry=1.1,
            exit=1.1,
            notes="Moved to BE."
        ),
        Trade(
            was_valid="N",
            date="2026-07-28",
            session="LONDON",
            pair="UK100",
            direction="SHORT",
            market_condition="counter-trending",
            rr=2.1,
            result="W",
            entry=8920.1,
            exit=8878.4,
            notes="Countertrend worked."
        )
    ]

    statistics = Statistics(trades)

    result = statistics.cumulative_winrate(trades)

    assert result == []


def test_empty_win_rate():
    statistics = Statistics()

    assert statistics.win_rate([]) is None

def test_average_rr():

    trades = [
        Trade(
            was_valid="N",
            date="2026-07-26",
            session="NYC",
            pair="NAS100",
            direction="SHORT",
            market_condition="ranging",
            rr=2.43,
            result="W",
            entry=13433.12,
            exit=13500.0,
            notes="OK"
        ),
        Trade(
            was_valid="Y",
            date="2026-07-27",
            session="LONDON",
            pair="XAUUSD",
            direction="LONG",
            market_condition="trending",
            rr=1.8,
            result="W",
            entry=3412.5,
            exit=3428.9,
            notes="Clean breakout."
        ),
        Trade(
            was_valid="Y",
            date="2026-07-27",
            session="NYC",
            pair="NAS100",
            direction="SHORT",
            market_condition="high-volume",
            rr=0.9,
            result="L",
            entry=13520.3,
            exit=13545.8,
            notes="Stopped out."
        ),
        Trade(
            was_valid="Y",
            date="2026-05-05",
            session="ASIA",
            pair="EURUSD",
            direction="LONG",
            market_condition="ranging",
            rr=1.6,
            result="W",
            entry=1.1,
            exit=1.1,
            notes="Moved to BE."
        ),
        Trade(
            was_valid="N",
            date="2026-07-28",
            session="LONDON",
            pair="UK100",
            direction="SHORT",
            market_condition="counter-trending",
            rr=2.1,
            result="W",
            entry=8920.1,
            exit=8878.4,
            notes="Countertrend worked."
        )
    ]

    statistics = Statistics(trades)

    result = statistics.average_rr()

    assert result == '1.77'




def test_most_common_session():

    trades = [
        Trade(
            was_valid="N",
            date="2026-07-26",
            session="NYC",
            pair="NAS100",
            direction="SHORT",
            market_condition="ranging",
            rr=2.43,
            result="W",
            entry=13433.12,
            exit=13500.0,
            notes="OK"
        ),
        Trade(
            was_valid="Y",
            date="2026-07-27",
            session="LONDON",
            pair="XAUUSD",
            direction="LONG",
            market_condition="trending",
            rr=1.8,
            result="W",
            entry=3412.5,
            exit=3428.9,
            notes="Clean breakout."
        ),
        Trade(
            was_valid="Y",
            date="2026-07-27",
            session="NYC",
            pair="NAS100",
            direction="SHORT",
            market_condition="high-volume",
            rr=0.9,
            result="L",
            entry=13520.3,
            exit=13545.8,
            notes="Stopped out."
        ),
        Trade(
            was_valid="Y",
            date="2026-05-05",
            session="ASIA",
            pair="EURUSD",
            direction="LONG",
            market_condition="ranging",
            rr=1.6,
            result="W",
            entry=1.1,
            exit=1.1,
            notes="Moved to BE."
        ),
        Trade(
            was_valid="N",
            date="2026-07-28",
            session="LONDON",
            pair="UK100",
            direction="SHORT",
            market_condition="counter-trending",
            rr=2.1,
            result="W",
            entry=8920.1,
            exit=8878.4,
            notes="Countertrend worked."
        )
    ]

    statistics = Statistics(trades)


    assert statistics.most_common_session() == "London and Nyc"
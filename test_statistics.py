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

    assert statistics.win_rate(trades) == 80.0






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



def test_market_condition_wrs(capsys):

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

    
    statistics.market_condition_wrs()

    captured = capsys.readouterr()

    assert "Win rate on trending: 100.00%" in captured.out
    assert "Win rate on ranging: 100.00%" in captured.out
    assert "Win rate on high volume: 0.00%" in captured.out
    assert "Win rate on counter trending: 100.00%" in captured.out



def test_long_vs_short_wr(capsys):

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

    statistics.long_vs_short_wr()

    captured = capsys.readouterr()


    assert "Win rate on long positions: 100.00%" in captured.out
    assert "Win rate on short positions: 66.67%" in captured.out


def test_win_rate_by_session(capsys):

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

    statistics.win_rate_by_session()

    captured = capsys.readouterr()

    assert "Win rate on London session is: 100.00%" in captured.out
    assert "Win rate on NYC session is: 50.00%" in captured.out
    assert "Win rate on Asia session is: 100.00%" in captured.out

def test_most_traded_pair():

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

    result = statistics.most_traded_pair()

    assert result == "NAS100"


def test_max_losing_streak():

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

    result = statistics.max_losing_streak()

    assert result == 1


def test_max_winning_streak():

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

    result = statistics.max_winning_streak()

    assert result == 2


# =========================
#       Edge Cases
# =========================

def test_empty_cumulative_win_rate():

    statistics = Statistics([])

    assert statistics.cumulative_winrate([]) == []



def test_empty_win_rate():
    statistics = Statistics([])

    assert statistics.win_rate([]) == None


def test_empty_average_rr():

    statistics = Statistics([])

    assert statistics.average_rr() is None


def test_empty_average_w_rr():

    statistics = Statistics([])

    assert statistics.average_win_rr() is None

def test_empty_average_l_rr():

    statistics = Statistics([])

    assert statistics.average_loss_rr() is None

def test_empty_most_common_session():

    statistics = Statistics([])

    assert statistics.most_common_session() == None

def test_empty_market_condition_wrs():

    statistics = Statistics([])

    assert statistics.market_condition_wrs() == None


def test_empty_long_vs_short_wr():

    statistics = Statistics([])

    assert statistics.long_vs_short_wr() == None

def test_empty_win_rate_by_session():
    statistics = Statistics([])

    assert statistics.win_rate_by_session() == None


def test_empty_most_traded_pair():

    statistics = Statistics([])

    assert statistics.most_traded_pair() == None


def test_empty_max_losing_streak():

    statistics = Statistics([])

    assert statistics.max_losing_streak() == None

def test_empty_max_winning_streak():

    statistics = Statistics([])

    assert statistics.max_winning_streak() == None
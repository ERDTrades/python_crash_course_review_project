import pytest
from trade import Trade
from trade_statistics import Statistics
from journal import Journal

@pytest.fixture
def trades(): 
    # I only have 5 trade examples
    # Didn't imported whole trade json 
    return [
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

@pytest.fixture
def statistics(trades):
    return Statistics(trades)


@pytest.fixture
def empty_statistics():
    return Statistics([])


@pytest.fixture
def journal():
    return Journal()

@pytest.fixture
def empty_journal():
    return Journal([])



#test any positive cases
def test_function(statistics):
    assert statistics.average_rr() == "1.77"

#test any empty cases
def test_empty_function(empty_statistics):
    assert empty_statistics.average_win_rr() == None
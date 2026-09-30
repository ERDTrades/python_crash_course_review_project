from journal import Journal
def test_id_func():
    journal = Journal()

    trade = journal.id_find(2)

    assert trade.id == 2

def test_id_find_invalid():
    journal = Journal()

    assert journal.id_find(999) is None

def test_trade_count():
    journal = Journal()

    trade = journal.trade_count()

    assert trade == f'There are 27 trades in your journal'



def test_id_func(journal):
    assert journal.id_find(2).id == 2

def test_trade_count(journal):
    assert journal.trade_count() == f'There are 27 trades in your journal'


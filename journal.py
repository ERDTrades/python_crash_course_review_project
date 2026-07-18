from trade import Trade

class Journal:

    def __init__(self):
        self.trades = []

    def add_trade(self, trade):
        """"Adds trade to the journal"""
        self.trades.append(trade)
        return self.trades

    def display_trades(self):
        """Displays trades"""
        for trade in self.trades:
            pass

    def trade_count(self):
        """"Count trades"""
        return f"There is {len(self.trades)} trades in your journal"

    def id_find(self):
        """Find trades by id"""
        pass

    def del_trade(self):
        """deletes trades"""
        pass

    



journal = Journal()

journal.add_trade(trade) # trade doesn't exists yet
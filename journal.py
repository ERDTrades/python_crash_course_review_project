from trade import Trade

class Journal:

    def __init__(self):
        self.trades = []

    def add_trade(self, trade):
        """"Adds trade to the journal"""
        self.trades.append(trade)
        
    def display_trades(self):
        """Displays trades"""
        for trade in self.trades:
            print(trade)

    def trade_count(self):
        """"Count trades"""
        return f"There is {len(self.trades)} trades in your journal"

    def id_find(self):
        """Find trades by id"""
        pass

    def del_trade(self):
        """deletes trades"""
        pass

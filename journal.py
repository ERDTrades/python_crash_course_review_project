from pathlib import Path
import json

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
        return f"There are {len(self.trades)} trades in your journal"

    def id_find(self):
        """Find trades by id"""
        pass

    def del_trade(self):
        """deletes trades"""
        pass
    
    def save_to_json(self):
        path = Path("trades.json")
        for trade in self.trades:
            pass ## turn trade to dict so later json dump will actually work
        contents = json.dumps(self.trades)
        path.write_text(contents)

    def load_from_json(self):
        path = Path("trades.json")
        contents = path.read_text()
        contents = json.loads(contents)
        self.trades = contents

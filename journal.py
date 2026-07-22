from pathlib import Path
from trade import Trade
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
        temporary = []
        for trade in self.trades:
            temporary.append(trade.to_dict())
        contents = json.dumps(temporary, indent=4)
        path.write_text(contents)

    def load_from_json(self):
        path = Path("trades.json")
        temp_list = []
        contents = path.read_text()
        contents = json.loads(contents)
        for trade in contents:
            temp_list.append(Trade(
                trade["was_valid"],
                trade["date"],
                trade["session"],
                trade["pair"],
                trade["direction"],
                trade["market_condition"],
                trade["entry"],
                trade["exit"],
                trade["rr"],
                trade["result"],
                trade["notes"]
                )
            )
        self.trades = temp_list
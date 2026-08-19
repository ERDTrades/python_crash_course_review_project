from pathlib import Path
from trade import Trade
import json
from datetime import datetime
import pandas as pd

class Journal:

    def __init__(self):
        self.trades = []
        self.load_from_json()

    def add_trade(self, trade):
        """"Adds trade to the journal"""
        trade.id = len(self.trades) + 1
        self.trades.append(trade)
        
    def display_trades(self): #later add :.2f formatting
        """Displays trades"""
        print(f"\n\n\nLiczba transakcji: {len(self.trades)}\n")
        df = pd.DataFrame([trade.to_dict() for trade in self.trades])
        return  df

    def trade_count(self):
        """"Count trades"""
        return f"There are {len(self.trades)} trades in your journal"

    def id_find(self, trade_id):
        """Find trades by id"""
        for trade in self.trades:
            if trade.id == trade_id:
                return trade

        return None
  
    def del_trade(self, trade_id):
        """deletes trades"""
        if self.id_find(trade_id):
            self.trades.remove(self.id_find(trade_id))
            return True
        else:
            return False
    
    def save_to_json(self):
        path = Path("trades.json")

        trade_data = []

        for trade in self.trades:
            trade_data.append(trade.to_dict())
        contents = json.dumps(trade_data, indent=4)

        path.write_text(contents)

    def load_from_json(self,):
        path = Path("trades.json")
        if not path.exists():
            return
        
        load_trade = []

        contents = path.read_text()
        contents = json.loads(contents)

        for trade in contents:
            trade_obj = Trade(
                trade["was_valid"],
                datetime.strptime(trade["date"], "%Y-%m-%d").date(),
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

            trade_obj.id = trade["id"]

            load_trade.append(trade_obj)

        self.trades = load_trade
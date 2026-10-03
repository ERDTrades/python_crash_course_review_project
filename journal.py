from pathlib import Path
from trade import Trade
import json
from datetime import datetime
import pandas as pd

from rich.text import Text
from rich.table import Table
from rich.console import Console
from rich import box

console = Console()

class Journal:

    def __init__(self):
        self.trades = []
        self.load_from_json()

    def add_trade(self, trade):
        """"Adds trade to the journal"""
        trade.id = len(self.trades) + 1
        self.trades.append(trade)
        
    def display_trades(self): #finish polishing with rich
        """Displays trades"""
        console.print(f"\n\n\nAmount of trades: {len(self.trades)}\n",
                        style="dark_blue"
                      )
        df = pd.DataFrame([trade.to_dict() for trade in self.trades])

        table = Table(box=box.DOUBLE_EDGE, title="Trading Journal",
                      title_style="bold blue",
                      style="dark_blue")
        table.add_column("ID", justify="center", style="dark_blue")
        table.add_column("Was Valid?", justify="center", style="dark_blue")
        table.add_column("Date", justify="center", style="dark_blue")
        table.add_column("Session", justify="center", style="dark_blue")
        table.add_column("Pair", justify="center", style="dark_blue")
        table.add_column("Direction", justify="center", style="dark_blue")
        table.add_column("market_condition", justify="center",
                          style="dark_blue")
        table.add_column("rr", justify="center", style="dark_blue")
        table.add_column("result", justify="center")
        table.add_column("P&L", justify="center", style="dark_blue")
        table.add_column("entry", justify="center", style="dark_blue")
        table.add_column("exit", justify="center", style="dark_blue")
        table.add_column("notes", justify="center", style="dark_blue")

        for row in df.itertuples(index=False):
            if row.result == "W":
                result = Text("W", style="green")
            elif row.result == "L":
                result = Text("L", style="red")
            else: 
                result = Text("BE", style="blue")

            table.add_row(
                str(row.id),
                row.was_valid,
                row.date,
                row.session,
                row.pair,
                row.direction,
                row.market_condition,
                f"{row.rr:.2f}",
                result,
                f"{row.pnl:.2f}",
                f"{row.entry:.2f}",
                f"{row.exit:.2f}",
                row.notes
            )

        console.print(table)


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

    def edit_trade(self, trade_id):

        trade = self.id_find(trade_id)

        if not trade:
            print("Trade not found")
            return False
        
        parameter = input("What do you want to change?: ").strip().lower()

        if parameter not in [
            "id",
            "was_valid",
            "date",
            "session",
            "pair",
            "direction",
            "market_condition",
            "rr",
            "result",
            "entry",
            "exit",
            "notes"
        ]:
            print("Please enter correct parameter")
            return False




        try:
            if parameter == "id":
                print("You can not change ID")
                return False
            elif parameter == "was_valid":
                while True:
                    new_value = input("\nEnter new value: ").strip()

                    if new_value == "N" or new_value == "Y":
                        break

                    choice = (input("\nPlease follow the guidelines"
                            "\nIf you want to see the guidelines"
                            " please choose 1 in main menu."
                            "Do you want to continue? (Y/N): ")
                            .strip().upper())
                    
                    if choice == "Y":
                        continue
                    else:
                        return False
                trade.was_valid = new_value


            elif parameter == "date":
                print("\nPlease enter date in YYYY-MM-DD format")
                new_value = input("\nEnter new value: ").strip()
                trade.date = datetime.strptime(new_value, "%Y-%m-%d").date()


            elif parameter == "session":
                while True:
                    new_value = input("\nEnter new value: ").strip()

                    if (new_value == "NYC"
                        or new_value == "LONDON"
                        or new_value == "ASIA"
                    ):
                        break

                    choice = (input("\nPlease follow the guidelines"
                            "\nIf you want to see the guidelines"
                            " please choose 1 in main menu."
                            "Do you want to continue? (Y/N): ")
                            .strip().upper())
                    
                    if choice == "Y":
                        continue
                    else:
                        return False
                    
                trade.session = new_value

            elif parameter == "pair":
                new_value = input("\nEnter new value: ").strip()
                trade.pair = new_value

            elif parameter == "direction":
                while True:
                    new_value = input("\nEnter new value: ").strip()

                    if(new_value == "LONG"
                       or new_value == "SHORT"
                    ):
                        break
                    choice = (input("\nPlease follow the guidelines"
                        "\nIf you want to see the guidelines"
                        " please choose 1 in main menu."
                        "Do you want to continue? (Y/N): ")
                        .strip().upper())
                
                    if choice == "Y":
                        continue
                    else:
                        return False
                trade.direction = new_value

            elif parameter == "market_condition":
                while True:
                    new_value = input("\nEnter new value: ").strip()

                    if (
                        new_value == "trending"
                        or new_value == "counter-trending"
                        or new_value == "trending(lower-tf)"
                        or new_value == "counter-trending(lower-tf)"
                        or new_value == "ranging"
                        or new_value == "high-volume"
                        or new_value == "low-volume"
                    ):
                            break

                    choice = (input("\nPlease follow the guidelines"
                        "\nIf you want to see the guidelines"
                        " please choose 1 in main menu."
                        "Do you want to continue? (Y/N): ")
                        .strip().upper())
                
                    if choice == "Y":
                        continue
                    else:
                        return False
                
                trade.market_condition = new_value
            
            elif parameter == "rr":
                new_value = input("\nEnter new value: ").strip()
                trade.rr = float(new_value)

            elif parameter == "result":
                while True:
                    new_value = input("\nEnter new value: ").strip()

                    if (new_value == "W"
                        or new_value == "L"
                        or new_value == "BE"
                    ):
                        break

                    choice = (input("\nPlease follow the guidelines"
                        "\nIf you want to see the guidelines"
                        " please choose 1 in main menu."
                        "Do you want to continue? (Y/N): ")
                        .strip().upper())
                
                    if choice == "Y":
                        continue
                    else:
                        return False

                trade.result = new_value

            elif parameter == "entry":
                new_value = input("\nEnter new value: ").strip()
                trade.entry = float(new_value)

            elif parameter == "exit":
                new_value = input("\nEnter new value: ").strip()
                trade.exit = float(new_value)

            elif parameter == "notes":
                new_value = input("\nEnter new value: ").strip()
                if len(new_value) > 350:
                    print("Notes can contain maximum 350 letters")
                    return False
                
                trade.notes = new_value

            else: 
                print("Please enter correct parameter")
                return  False
        except ValueError:
            print("Please enter correct value")
            return False
            
        return True

    
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
                trade["pnl"],
                trade["notes"]
            )

            trade_obj.id = trade["id"]

            load_trade.append(trade_obj)

        self.trades = load_trade
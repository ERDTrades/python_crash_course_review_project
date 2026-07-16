
#Guide -Later add as a print so the user will be more familiar with terminology
#pair -> XAUUSD, EURUSD, - indicies like NAS100 too
# -- for journal indicies we will use:
# use full names [FTSE NO, UK100 YES] 
# direction -> Bullish / Bearish
# market condition -> Trending / Ranging / Volume / Countertrending(lower tf)
# entry, exit, rr obvious
# session -> London, New_York, Asia
# result -> W, L, BE, W closed early, small W, small L
# date -> date
# notes -> overall note -> I will set the limit for maximum 350 characters

from datetime import datetime

class Trade:
    
    def __init__(self, was_valid, date,
                session, pair, direction, market_condition,
                entry, exit, rr, 
                result,
                notes
                ):
        self.was_valid = was_valid # boolean
        self.date = date # I will need data module
        self.session = session # session
        self.pair = pair # string
        self.direction = direction # string
        self.market_condition = market_condition # string
        self.entry = entry #float
        self.exit = exit # float
        self.rr = rr # float
        self.result = result #string
        self.notes = notes # big string

    def __str__(self):
        return (f"Trade:\n"
                f"Trade was valid?: {bool(self.was_valid)}"
                f"\nDate: {self.date.strftime('%Y-%m-%d')}"
                f"\nSession: {self.session}"
                f"\nPair: {self.pair}"
                f"\n---------------------------------------------------------"
                f"\nDirection: {self.direction}"
                f"\nMarket Condition: {self.market_condition}"
                f"\n---------------------------------------------------------"
                f"\nRR: {self.rr}"
                f"\nResult: {self.result}"
                f"\n---------------------------------------------------------"
                f"\nEntry/exit info:"
                f"\n\tEntry: {self.entry}"
                f"\n\tExit: {self.exit}"
                f"\n---------------------------------------------------------"
                f"\n\t\tNotes: {self.notes}"
            )

    def to_dict(self,):
        
        documentation = { # Didn't added entry/exit cus its useless here tbh
            "was_valid": self.was_valid,
            "date": self.date,
            "session": self.session,
            "pair": self.pair,
            "direction": self.direction,
            "market_condition": self.market_condition,
            "rr": self.rr,
            "result": self.result,
            "entry": self.entry,
            "exit": self.exit,
            "notes": self.notes 
        }
        return documentation
# date - # "%Y, %m, %d"
trade = Trade(True, datetime.strptime("2026-07-16", "%Y-%m-%d"), "London", "XAUUSD", "Long", "Trending Bullish",
              7572.43, 7500.40, 1.99, "W",
              "Example notes") 
print(trade)
print(trade.to_dict())
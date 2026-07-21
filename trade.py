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
            "date": self.date.strftime("%Y-%m-%d"),
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
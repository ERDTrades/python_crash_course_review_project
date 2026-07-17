
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

# Guide Section 
print("\t----------------------------Users Guide:-----------------------------"
      "\npairs Example: ->  XAUUSD, EURUSD, NAS100, UK100"
      "\n---------------------------------------------------------------------"
      "\nfor journal indicies we will use:"
      " original names [FTSE NO, UK100 YES]"
      "\n---------------------------------------------------------------------"
      "\ndirection -> Bullish / Bearish"
      "\n---------------------------------------------------------------------"
      "\nmarket condition:"
      "\n\t- Trending"
      "\n\t- Ranging"
      "\n\t- High Volume"
      "\n\t- Counter-Trending (Lower Timeframe)"
      "\n---------------------------------------------------------------------"
      "\nentry, exit, rr -> use dots between digits"
      "\n---------------------------------------------------------------------"
      "\nsession -> London, New York, Asia"
      "\n---------------------------------------------------------------------"
      "\nresult -> W, L, BE, W closed early, small W, small L"
      "\n---------------------------------------------------------------------"
      "\ndate -> input date like this: 'YEAR-MONTH-DAY' for example 2026-07-17"
      "\n---------------------------------------------------------------------"
      "\nnotes -> overall note -> I will set the limit for maximum "
      "350 characters")

# i will change later Y to True and N to False for boolean
while True:
    try:
        was_valid_input = input("Trade was valid? Y \ N: ")
        date_input = datetime.strptime(input("Date: (YYYY-MM-DD): "),
                                            "%Y-%m-%d"
                                            )
        session_input = input("Session: ")
        pair_input = input("Pair: ")
        direction_input = input("Direction: ")
        market_condition_input = input("Market condition: ")
        rr_input = float(input("Risk/Reward: "))
        result_input = input("Result: ")
        entry_input = float(input("Entry: "))
        exit_input = float(input("Exit: "))
        notes_input = input("Notes: ")
        continuation = input("Do you want to continue? Y \ N: ").strip().upper()
        if continuation == "N":
            break
        elif continuation != "Y":
            print("You can only type Y or N")
            break
    except ValueError:
        print("Invalid input - Please, follow the guidelines")

# TO DO
# Allow user to type "exit" at any input pormpt to safely close application.
# Y / N bool validation
# check the digits limit in notes

trade = Trade(
    was_valid=was_valid_input,
    date=date_input,
    session=session_input,
    pair=pair_input,
    market_condition=market_condition_input,
    rr=rr_input,
    result=result_input,
    entry=entry_input,
    exit=exit_input,
    notes=notes_input
)
print(trade)
print(trade.to_dict())

#Trade
#    ↓
#Journal (lista Trade)
#    ↓
#Storage.save(journal)
#    ↓
#journal.json

# Trade -> 1 trade
# Journal -> trade collection
# Storage -> loads and dumps to json
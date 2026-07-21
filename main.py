from datetime import datetime
from trade import Trade

def create_trade():
    """function creating 1 trade"""
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

                # Trade object
                trade = Trade(
                was_valid=was_valid_input,
                date=date_input,
                session=session_input,
                pair=pair_input,
                direction=direction_input,
                market_condition=market_condition_input,
                rr=rr_input,
                result=result_input,
                entry=entry_input,
                exit=exit_input,
                notes=notes_input
                )
                return trade
        except ValueError:
                print("Invalid input - Please, follow the guidelines")

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



from journal import Journal

journal = Journal()

date = datetime.now()

while True:
        trade = create_trade()
        journal.add_trade(trade)
        if input("Do you want to add another trade? Y / N: ").upper() != "Y":
              break

#journal.save_to_json()



# TODO

# Make json loads and dumps work (to_dict) (for loop)

# Create CLI flow (firstly in main.py)
# 1. Program start
# 2. Load Json
# 3. Show journal? Y/N
# 4. Add trade? Y/N
# 5. Add another trade? Y/N
# 6. show updated journal? Y/N
# 7. Save Json
# 8. exit

# after creating working script transfer it to menu.py


# Main menu:
# 1. Add new trade
# 2. View journal
# 3. Exit


# Later
# Statistics
# - Trade count
# - Win rate
# - Average RR
# - Average win RR
# - Average loss RR

# Find trade by ID

# Delete trade

# Edit trade

# Charts
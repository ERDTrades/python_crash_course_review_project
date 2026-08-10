from journal import Journal
from trade_statistics import Statistics
from trade_input import guide

journal= Journal()

stats = Statistics(journal.trades)

def edit_trade(journal, trades, stats):
    if (input("Do you want to see the journal? Y/N: ")
    .upper().strip()== "Y"
    ):
        journal.display_trades()

    trade_id = input("Enter trade ID: ")
    trade = stats.id_find(trade_id)
    print(trade)

    if (
        input("BEFORE YOU CHANGE ANYTHING:"
        "1. You can't change trades ID" \
        "\n2. You have to follow the guidelines" \
        "\n3. If you want to see the guidelines Y/N: ")
        .upper().strip() == "Y"
    ):
        guide()
        print("\n\n\t\tList of parameters:" \
        "was_valid, date, session, pair, direction" \
        "market_condition, entry, exit, rr, result, notes")


    parameter = input("What parameter do you want to change?:").strip()
    if parameter == "was_valid":
        new_value = input("New value: ").upper().strip()
        trade.was_valid = new_value

    elif parameter == "date":
        new_value = input("New value: ")
        trade.date = new_value

    elif parameter == "session":
        new_value = input("New value: ").upper().strip()
        trade.session = new_value

    elif parameter == "pair":
        new_value = input("New Value: ").upper().strip()
        trade.pair = new_value

    elif parameter == "direction":
        new_value = input("New value: ").upper().strip()
        trade.direction = new_value

    elif parameter == "market_condition":
        new_value = input("New value: ").upper().strip()
        trade.market_condition = new_value

    elif parameter == "entry":
        new_value = float(input("New value: ").strip())
        trade.entry = new_value

    elif parameter == "exit":
        new_value = float(input("New value: ").strip())
        trade.exit = new_value

    elif parameter == "rr":
        new_value = float(input("New value: ").strip())
        trade.rr = new_value

    elif parameter == "result":
        new_value = input("New value: ").upper().strip()
        trade.result = new_value

    elif parameter == "notes":
        new_value = input("New value:")
        trade.notes = new_value

    else:
        print("Please enter correct parameter name")


# show the change
# confirm
# if Y
# change and save



#edit trade skeleton

#   show change & ask for confirmation

# if confirmed
#   change trade object

#convert trade object to dict/json

# save changes

# do that to every editable paremeter without id


# Pipeline
# menu
# edit trade
# choose certain trade by ID
# find object trade with ID
# display that trade
# ask what do you want to change
# decide what attribute of trade object to change
# input change
# validation 
# ask Change Confirmation -> input Y/N
# change trade object
# to JSON
# save
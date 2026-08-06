from datetime import datetime
from trade import Trade

def create_trade():
    """function creating 1 trade"""
    while True:
        try:
                while True:
                        was_valid_input = (input("\nTrade was valid? Y / N: ")
                        ).strip().upper()
                        if was_valid_input == "N" or was_valid_input == "Y":
                               break
                        else:
                               print("Please follow the guidelines")

                date_input = datetime.strptime(input("Date: (YYYY-MM-DD): "),
                                                    "%Y-%m-%d"
                                                    )
                
                while True:
                        session_input = input("Session: ").strip().upper()
                        if (
                            session_input == "NYC"
                            or session_input == "LONDON"
                            or session_input == "ASIA"
                        ):
                               break
                        else:
                               print("Please Follow the Guidelines")

                pair_input = input("Pair: ").upper().strip()

                while True:
                        direction_input = input("Direction: ").upper().strip()
                        if (
                            direction_input == "LONG"
                            or direction_input == "SHORT"):
                               break
                        else:
                               print("Please Follow the Guidelines")

                while True:              
                        market_condition_input = (input("Market condition: ")
                        .lower().strip()
                        )
                        if (
                            market_condition_input == "trending"
                            or market_condition_input == "counter-trending"
                            or market_condition_input == "trending(lower-tf)"
                            or market_condition_input
                            == "counter-trending(lower-tf)"
                            or market_condition_input == "ranging"
                            or market_condition_input == "high-volume"
                            or market_condition_input == "low-volume"
                        ):
                                break
                        else:
                               print("Please Follow the Guidelines")


                rr_input = float(input("Risk/Reward: "))

                while True:
                       result_input = input("Result: ").strip().upper()
                       if (result_input == "W"
                            or result_input == "L"
                            or result_input == "BE"
                       ):
                              break
                       else:
                              print("Please Follow the Guidelines")
                entry_input = float(input("Entry: "))
                exit_input = float(input("Exit: "))

                while True:
                     notes_input = input("Notes: ")
                     if len(notes_input) <= 350:
                            break
                     else:
                            print("Please Follow the Guidelines"
                            " - max 350characters.")

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

def guide():
        # Guide Section 
        print("\t----------------------------Users Guide:-------------"
        "----------------"
        "\npairs Example: ->  XAUUSD, EURUSD, NAS100, UK100"
        "\n-----------------------------------------------------------"
        "----------"
        
        "\nfor journal indicies we will use:"
        " original names [FTSE NO, UK100 YES]"

        "\n-----------------------------------------------------------"
        "----------"
        
        "\ndirection -> LONG / SHORT "
        
        "\n-----------------------------------------------------------"
        "----------"
        
        "\nmarket condition:"
        "\n\t- trending"
        "\n\t- trending(lower-tf)"
        "\n\t- ranging"
        "\n\t- high-volume"
        "\n\t- low-volume"
        "\n\t- counter-trending(lower-tf)"
        "\n\t- counter-trending"
        
        "\n-----------------------------------------------------------"
        "----------"
        
        "\nentry, exit, rr -> use dots between digits"
        "\n-----------------------------------------------------------"
        "----------"
        
        "\nsession -> LONDON, NYC, ASIA"
        "\n-----------------------------------------------------------"
        "----------"
        
        "\nresult -> W, L, BE"
        "\n-----------------------------------------------------------"
        "----------"
        
        "\ndate -> input date like this: 'YEAR-MONTH-DAY' for example "
        "2026-07-17"
        
        "\n-----------------------------------------------------------"
        "----------"
        
        "\nnotes -> overall note -> I will set the limit for maximum "
        "350 characters")
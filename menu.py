from journal import Journal
from trade_input import create_trade
from trade_input import guide


journal = Journal()

journal.load_from_json()


def show_menu():
    print(
        "========================"
        "\nTrading Journal"
        "\n========================"
        "\n1. Add Trade"
        "\n2. View Journal"
        "\n3. Search trade by ID"
        "\n4. Exit"
    )

def handle_option(option, journal):
    """Handle user's menu option."""#for future
    # later - transfer opinion making from menu loop here
    pass
def menu_loop():
    """Main menu loop"""
    while True:
        if input("Show menu? (Y/N): ").strip().upper() == "Y":
            show_menu()
        option = input("Choose an option (1-4): ").strip()

        if option == "1":
            if input("\nDo you want to see Users Guide"
                " before entering new trade? (Y/N): "
                ).strip().upper() == "Y":
               # Guide Section 
                guide()
            while True:
                    trade = create_trade()
                    journal.add_trade(trade)
                    journal.save_to_json()
                    if input("Do you want to add another trade?"
                    " Y / N: ").strip().upper() != "Y":
                            break
                        
        elif option == "2":
            if (input("Do you want to see updated journal? (Y/N): ")
            .strip().upper() == "Y"):
                journal.display_trades()

        elif option == "3":
             if (input("Do you want to search trade by id? (Y/N): ")
                 .strip().upper() == "Y"):
                  
                  trade_id = int(input("Enter trade ID: "))
                  trade = journal.id_find(trade_id)

                  if trade:
                       print(trade)
                  else:
                       print("Trade not found.")

        elif option == "4":
                break

        else: 
             print("Invalid option")

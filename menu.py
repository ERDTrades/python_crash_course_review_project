from journal import Journal
from trade_input import create_trade
from trade_input import guide
from trade_statistics import Statistics

journal = Journal()


journal.load_from_json()

stats = Statistics(journal.trades)

def show_menu():
    print(
        "========================"
        "\nTrading Journal"
        "\n========================"
        "\n0. Exit"
        "\n1. Add Trade"
        "\n2. View Journal"
        "\n3. Search trade by ID"
        "\n4. Delete Trade by ID"
        "\n5. Show Statistics"
    )

def menu_loop():
    """Main menu loop"""
    while True:
        if input("Show menu (Y/N): ").strip().upper() == "Y":
            show_menu()
        option = input("Choose an option (1-5): ").strip()

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
             if (input("Do you want to delete trade? (Y/N): ")
             .strip().upper() == "Y"
             ):
                  
                  trade_id = int(input("Enter trade ID that you want to delete: "))
                  trade = journal.del_trade(trade_id)

                  if trade:
                       journal.save_to_json()
                       print("Trade deleted")
                  else:
                       print("Trade not found")

        elif option == "5":
             stats.show_statistics()
                       
        elif option == "0":
                break

        else: 
             print("Invalid option")

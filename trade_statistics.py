

class Statistics(): #later do this class using NumPy
    def __init__(self, trades):
        self.trades = trades
        
    def trade_count(self):
        """"Count trades"""
        return f"There are {len(self.trades)} trades in your journal"
    def win_rate(self,):
        """win rate mean"""
        pass

    def average_rr(self,): 
        rr_mean = [trade.rr for trade in self.trades]
        count_sum = sum(rr_mean)
        final = count_sum / len(rr_mean)
        print(final)

    def average_win_rr(self):
        awr = []
        for trade in self.trades:
            if trade.result == "W":
                awr.append(trade.rr)


        if awr:
            awr_count_sum = sum(awr)
            awr_final = awr_count_sum / len(awr)
            print(awr_final)
        else:
            print("Empty")

    def average_loss_rr(self):
        awl = []
        for trade in self.trades:
            if trade.result == "L":
                awl.append(trade.rr)

        if awl:
            awl_count_sum = sum(awl)
            awl_final = awl_count_sum / len(awl)
            print(awl_final)
        else:
            print("Empty")

    def most_common_session(self):
        london = []
        nyc = []
        for trade in self.trades:
            if trade.session == "LONDON":
                london.append(trade.session)
            elif trade.session == "NYC":
                nyc.append(trade.session)
        if len(london) > len(nyc):
            print("Most common session is London.")
        elif len(london) < len(nyc):
            print("Most common session is NYC.")
        elif len(london) == len(nyc):
            print("Both sessions have the same amount of trades.")

    def show_statistics(self):
        pass

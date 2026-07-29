

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
        pass

    def average_loss_rr(self):
        pass

    def most_common_session(self):
        pass

    def show_statistics(self):
        pass

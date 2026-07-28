

class Statistics():
    def __init__(self, trades):
        self.trades = trades
        
    def trade_count(self):
        """"Count trades"""
        return f"There are {len(self.trades)} trades in your journal"
        pass
    def win_rate(self, rr):
        """win rate mean"""
        rr_mean = []
        for trade in self.trades:
            trade.rr = rr
            rr_mean.append(trade)
            # del rr
        pass

    def average_rr(self):
        pass

    def average_win_rr(self):
        pass

    def average_loss_rr(self):
        pass

    def most_common_session(self):
        pass

    def show_statistics(self):
        pass

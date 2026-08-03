

class Statistics(): #later do this class using NumPy
    def __init__(self, trades):
        self.trades = trades
        
    def trade_count(self):
        """"Count trades"""
        return f"There are {len(self.trades)} trades in your journal"
    def win_rate(self, trades):
        """win rate mean"""
        losses = []
        for trade in trades:
            if trade.result == "L":
                losses.append(trade)
        if not trades:
            return "No Trades"

        wins = len(trades) - len(losses)
        win_rate = wins / len(trades) * 100

        return win_rate
    
    def average_rr(self): 
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
        asia = []
        for trade in self.trades:
            if trade.session == "LONDON":
                london.append(trade.session)

            elif trade.session == "NYC":
                nyc.append(trade.session)

            elif trade.session == "ASIA":
                asia.append(trade.session)

        if len(london) > len(nyc) and len(london) > len(asia):
            print("Most common session is London.")

        elif len(nyc) > len(london) and len(nyc) > len(asia):
            print("Most common session is NYC.")

        elif len(asia) > len(london) and len(asia) > len(nyc):
            print("Most common session is Asia")

        elif len(london) == len(nyc) > len(asia):
            print("Most common sessions are London and NYC.")

        elif len(london) == len(asia) > len(nyc):
            print("Most common sessions are London and Asia.")

        elif len(nyc) == len(asia) > len(london):
            print("Most common sessions are NYC and Asia.")

        elif len(london) == len(nyc) == len(asia):
            print("All sessions have the same amount of trades.")
        


    def market_condition_wrs(self):
        """Basically defines on which market condition
        U have the biggest winratio"""
        trending = []
        trending_lower_tf = []
        ranging = []
        high_volume = []
        low_volume = []
        counter_trending_ltf = []
        counter_trending = []

        for trade in self.trades:
            if trade.market_condition == "trending":
                trending.append(trade)

            elif trade.market_condition == "trending(lower-tf)":
                trending_lower_tf.append(trade)

            elif trade.market_condition == "ranging":
                ranging.append(trade)

            elif trade.market_condition == "high-volume":
                high_volume.append(trade)

            elif trade.market_condition == "low-volume":
                low_volume.append(trade)

            elif trade.market_condition == "counter-trending(lower-tf)":
                counter_trending_ltf.append(trade)

            elif trade.market_condition == "counter-trending":
                counter_trending.append(trade)


        trending_w = self.win_rate(trending)
        print(f"Win rate on Trending: {trending_w:.2f}%")

        trending_ltf_w = self.win_rate(trending_lower_tf)
        print(f"Win rate on trending lower timeframe: {trending_ltf_w:.2f}%")

        ranging_w = self.win_rate(ranging)
        print(f"Win rate on ranging: {ranging_w:.2f}%")

        high_vol_w = self.win_rate(high_volume)
        print(f"Win rate on high_vol: {high_vol_w:.2f}%")

        low_vol_w = self.win_rate(low_volume)
        print(f"Win rate on low volume: {low_vol_w:.2f}%")

        counter_t_ltf = self.win_rate(counter_trending_ltf)
        print(f"Win rate on counter trending lower timeframe is:"
              f" {counter_t_ltf:.2f}%")

        counter_t_w = self.win_rate(counter_trending)
        print(f"Win rate on counter trending is: {counter_t_w:.2f}%")

        # Later do combined because som of them could be like:
        # trending + counter_trending_ltf + high vol
        # You can also return a dictionary "Trending": ...,
        # with final prints u aswell might wanna add:
        # Trending:
        # Trades: ..
        # Win Rate: ...%
        #but I will have to think whether i want it here or in menu.py
    def show_statistics(self):
        pass

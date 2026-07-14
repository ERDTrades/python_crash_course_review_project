
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


class Trade:
    
    def __init__(self, pair, direction, market_condition,
                  entry, exit, rr, 
                  session, result,
                  date, notes,
                  was_valid):
        self.pair = pair # string
        self.direction = direction # string
        self.market_condition = market_condition # string
        self.entry = entry #float
        self.exit = exit # float
        self.rr = rr # float
        self.session = session # session
        self.result = result #string
        self.date = date # I will need data module
        self.notes = notes # big string
        self.was_valid = was_valid # boolean

    def __str__(self):
        pass

    def to_dict(self):
        pass
import matplotlib.pyplot as plt
from trade_statistics import Statistics
from journal import Journal


journal = Journal()

stats = Statistics(journal.trades)

x = []
y = stats.cumulative_winrate(journal.trades)

for trade in journal.trades:
    if trade.result == "BE":
        continue

    x.append(trade.id)

print(len(x))
print(len(y))

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set_title("Cumulative Win rate")
ax.set_xlabel("Trade ID")
ax.set_ylabel("Win rate %")

plt.show()










# Is edge getting better? -> line graph, X - trade ID ,
# Y - winrate (use winrate function prolly)

# W, BE, L ->  bar graph simple x,y,z   x -> W BE L y -> trade_count

# RR graph -> straight line chart. showing X -> ID Y-> Trade count
# basically calculation if rr got better or worse after taking X amount 
# of trades


#most common session
# bar graph -> above the bar -> wr%

# most common direction
# 2 bars -. long/short
# also show wr% above 

#skeleton
#plt.figure()
#plt.plot(x, y)
#plt.title(...)
#plt.xlabel(...)
#plt.ylabel(...)
#plt.grid(True)
#plt.show()
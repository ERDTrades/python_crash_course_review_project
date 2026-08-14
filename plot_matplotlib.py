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





x = ["W", "L", "BE"]
y = []

w = 0
l = 0
be = 0

for trade in journal.trades:
    if trade.result == "W":
        w += 1
    elif trade.result == "L":
        l += 1
    elif trade.result == "BE":
        be += 1

y.append(w)
y.append(l)
y.append(be)


fig, ax = plt.subplots()

bars= ax.bar(x, y,
       color="darkblue",
       edgecolor="black",
       alpha=0.8,
       )

ax.bar_label(
    bars,
    padding=3,
    fontweight="bold"
)


ax.set_xlabel("outcome")
ax.set_ylabel("trade count")

plt.show()



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

# And lastly ofc make a option in menu py to show matplot
import matplotlib.pyplot as plt

x=[2,4,6,8,10]
y=[6,7,8,2,4,]

x2=[1,3,5,7,9]
y2=[7,8,2,4,2]

#for line chart
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#plt.plot(x,y,label="Line One")
#plt.plot(x2,y2,label="Line Two")
#plt.xlabel("Plot Number")
#plt.ylabel("Important var")

#for bar chart
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
plt.bar(x,y, label="Bar 1", color="r")
plt.bar(x2,y2, label="Bar 2", color="c")

plt.legend()
plt.title("Important Graph")
plt.show()


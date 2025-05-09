from matplotlib import pyplot as plt
from matplotlib import style
# In a graph data can be dataframes from pandas also

# Simple graph with only data
plt.plot(['Radhika', 'Nidhi', 'Vidhi'],[3,2,1],)
plt.show()

# Graph with title and lables 
x = [1,2,3]  
y = [4,5,1]

plt.plot(x,y)
plt.title("Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

#  Add Styles 
x = [1,2,3]
y = [4,5,1]
x2 = [2,3,4]
y2 = [1,2,3]

plt.plot(x,y,'g',label='Line One',linewidth=2 ) # g = green color
plt.plot(x2,y2,'b',label='Line Two',linewidth=2 ) # b = blue color

plt.title("Info")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid()
plt.show()
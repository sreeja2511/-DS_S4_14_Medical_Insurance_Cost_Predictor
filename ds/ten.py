import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10]
y=[2,4,5,7,6,8,9,11,12,12]
plt.scatter(x,y,label="stars",color="k",marker="*",s=30)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter Plot")
plt.legend()
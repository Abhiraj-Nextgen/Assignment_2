import matplotlib.pyplot as plt
import numpy as np

x = list(range(100))
y = [i**2 for i in x]
z = [i**3 for i in x]

plt.figure() #Basic Plot
plt.plot(x, y)
plt.savefig("basic_plot.jpg")

plt.figure() #Adding Titles and Labels
plt.plot(x, y, label="y = x^2")
plt.title("Quadratic Function")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.savefig("plot_with_labels.jpg")

plt.figure() #Scatter Plot
plt.scatter(x, y, color='red', label="Scatter: y = x^2")
plt.title("Scatter Plot of y = x^2")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.savefig("scatter_plot.jpg")

plt.figure() #Customize Line Style and Markers
plt.plot(x, y, linestyle="--", marker="o", color="g", label="Dashed Line with Markers")
plt.title("Custom Line Style and Markers")
plt.legend()
plt.savefig("custom_line_plot.jpg")

plt.figure() #Plot another dataset on the same plot
plt.plot(x, y, linestyle="-", color="b", label="y = x^2")
plt.plot(x, z, linestyle="--", color="r", label="z = x^3")
plt.title("Comparing Quadratic and Cubic Functions")
plt.legend()
plt.savefig("multiple_plot.jpg")

fig, axs = plt.subplots(3, 1, figsize=(6, 12)) #Subplots for different plots
axs[0].plot(x, y, label="y = x^2", color="blue")
axs[0].set_title("Plot of x vs y")
axs[0].legend()
axs[1].plot(x, z, label="z = x^3", color="red")
axs[1].set_title("Plot of x vs z")
axs[1].legend()
axs[2].plot(y, z, label="y vs z", color="green")
axs[2].set_title("Plot of y vs z")
axs[2].legend()

plt.tight_layout()
plt.savefig("subplots.jpg")

hist_data = np.random.randint(1, 100, 100) #Histogram with custom data
plt.figure()
plt.hist(hist_data, bins=10, color="purple", edgecolor="black", label="Random Data Distribution")
plt.title("Histogram of Random Data")
plt.legend()
plt.savefig("histogram.jpg")

plt.figure() #Customize all ticks
plt.plot(x, y, label="y = x^2")
plt.xticks(np.arange(0, 101, step=10))
plt.yticks(np.arange(0, max(y) + 5000, step=5000))
plt.title("Customized Ticks on the Plot")
plt.legend()
plt.savefig("custom_ticks.jpg")

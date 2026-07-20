try:
	from matplotlib import pyplot as plt
except Exception:
	raise ImportError('matplotlib.pyplot could not be imported. Ensure matplotlib is installed.')

X = [1, 2, 3, 4]
Y = [5, 6, 7, 8]

# plot the data, then show the figure
plt.plot(X, Y)
plt.show()
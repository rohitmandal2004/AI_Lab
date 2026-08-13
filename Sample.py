try:
	from matplotlib import pyplot as plt
except Exception:
	raise ImportError('matplotlib.pyplot could not be imported. Ensure matplotlib is installed.')

X = [1, 2, 3, 4]
Y = [5, 6, 7, 8]

# plot the data, then show the figure
plt.plot(X, Y)
plt.show()


# 1. Copy the example environment file
cp .env.example .env

# 2. Open the .env file in your editor and add your GEMINI_API_KEY
# (And modify USER_NAME if you like)

# 3. Activate the virtual environment
.\venv\Scripts\Activate.ps1

# 4. Launch ROX!
python run.py

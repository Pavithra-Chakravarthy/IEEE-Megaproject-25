import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 10 * t)

plt.plot(t, signal)
plt.title("Test Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()
import numpy as np
import matplotlib.pyplot as plt
fs = 1000          # Sampling frequency
t = np.linspace(0, 1, fs)
# Licensed signals
band1 = np.sin(2 * np.pi * 50 * t)     # Band 1 (licensed)
band2 = np.sin(2 * np.pi * 120 * t)    # Band 2 (licensed)
band3 = np.sin(2 * np.pi * 250 * t)    # Band 3 (licensed)
unauthorized = 0.8 * np.sin(2 * np.pi * 120 * t)
noise = np.random.normal(0, 0.5, fs)
signal_normal = band1 + band2 + band3 + noise
signal_illegal = band1 + band2 + band3 + unauthorized + noise
plt.figure(figsize=(10,4))
plt.plot(t, signal_illegal)
plt.title("Time Domain Signal (With Unauthorized Transmission)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()
fft_signal = np.abs(np.fft.fft(signal_illegal))
freq = np.fft.fftfreq(len(fft_signal), 1/fs)

plt.plot(freq[:fs//2], fft_signal[:fs//2])
plt.title("Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()





import numpy as np
import matplotlib.pyplot as plt
fs = 1000
t = np.linspace(0, 1, fs)

band1 = np.sin(2 * np.pi * 50 * t)
band2 = np.sin(2 * np.pi * 120 * t)
band3 = np.sin(2 * np.pi * 250 * t)

unauthorized = 0.8 * np.sin(2 * np.pi * 120 * t)
noise = np.random.normal(0, 0.5, fs)

signal = band1 + band2 + band3 + unauthorized + noise
fft_signal = np.abs(np.fft.fft(signal))
freq = np.fft.fftfreq(len(fft_signal), 1/fs)
fft_signal = fft_signal[:fs//2]
freq = freq[:fs//2]
bands = {
    "Band 1 (40–60 Hz)": (40, 60),
    "Band 2 (100–140 Hz)": (100, 140),
    "Band 3 (230–270 Hz)": (230, 270)
}
threshold = 100   # We will tune this later
results = {}

for band, (low, high) in bands.items():
    indices = np.where((freq >= low) & (freq <= high))
    energy = np.sum(fft_signal[indices] ** 2)
    results[band] = energy
for band, energy in results.items():
    if energy > threshold:
        print(f"{band}: OCCUPIED (Energy = {energy:.2f})")
    else:
        print(f"{band}: FREE (Energy = {energy:.2f})")
plt.figure(figsize=(10,4))
plt.plot(freq, fft_signal)
plt.axhline(y=threshold, color='r', linestyle='--', label="Threshold")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Spectrum with Energy Detection")
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# ======================
# 1. Signal Parameters
# ======================
fs = 1000  # Sampling frequency (Hz)
t = np.linspace(0, 1, fs, endpoint=False)

# ======================
# 2. Licensed Signals
# ======================
band1 = np.sin(2 * np.pi * 50 * t)     # Band 1 (Authorized)
band2 = np.sin(2 * np.pi * 120 * t)    # Band 2 (Authorized base)
band3 = np.sin(2 * np.pi * 250 * t)    # Band 3 (Authorized)

# ======================
# 3. Unauthorized Signal (Injected)
# ======================
unauthorized = 2.5 * np.sin(2 * np.pi * 120 * t)  # Extra power in Band 2

# ======================
# 4. Noise
# ======================
noise = np.random.normal(0, 0.3, fs)

# ======================
# 5. Total Signal
# ======================
signal = band1 + band2 + band3 + unauthorized + noise

# ======================
# 6. FFT Analysis
# ======================
fft_signal = np.abs(np.fft.fft(signal))
freq = np.fft.fftfreq(len(fft_signal), 1/fs)

# Keep only positive frequencies
fft_signal = fft_signal[:fs // 2]
freq = freq[:fs // 2]

# ======================
# 7. Licensed Band Definitions
# ======================
licensed_bands = {
    "Band 1 (50 Hz)": {"range": (40, 60), "expected_energy": 900},
    "Band 2 (120 Hz)": {"range": (100, 140), "expected_energy": 900},
    "Band 3 (250 Hz)": {"range": (230, 270), "expected_energy": 900}
}

# ======================
# 8. Unauthorized Detection Logic
# ======================
print("\n--- BAND STATUS REPORT ---")
results = {}

for band, info in licensed_bands.items():
    low, high = info["range"]
    expected = info["expected_energy"]

    indices = np.where((freq >= low) & (freq <= high))
    energy = np.sum(fft_signal[indices])

    if energy > expected * 1.5:
        status = "UNAUTHORIZED ⚠️"
    else:
        status = "AUTHORIZED ✅"

    results[band] = (energy, status)
    print(f"{band}: {status} (Energy = {energy:.2f})")

# ======================
# 9. Visualization
# ======================
plt.figure(figsize=(10, 4))
plt.plot(freq, fft_signal)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Spectrum Sensing with Unauthorized Band Detection")
plt.grid(True)
plt.show()

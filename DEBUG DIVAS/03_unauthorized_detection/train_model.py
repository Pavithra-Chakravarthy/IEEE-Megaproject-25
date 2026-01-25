import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ======================
# Signal Generator
# ======================
def generate_sample(unauthorized=False, noise_level=0.4):
    fs = 1000
    t = np.linspace(0, 1, fs, endpoint=False)

    band1 = np.sin(2 * np.pi * 50 * t)
    band2 = np.sin(2 * np.pi * 120 * t)
    band3 = np.sin(2 * np.pi * 250 * t)

    signal = band1 + band2 + band3

    if unauthorized:
        signal += 3.0 * np.sin(2 * np.pi * 120 * t)

    signal += np.random.normal(0, noise_level, fs)

    fft_signal = np.abs(np.fft.fft(signal))[:fs//2]

    energy = np.sum(fft_signal ** 2)
    variance = np.var(fft_signal)

    return [energy, variance]

# ======================
# Dataset Creation
# ======================
X = []
y = []

for _ in range(500):
    X.append(generate_sample(False))
    y.append(0)   # Authorized

    X.append(generate_sample(True))
    y.append(1)   # Unauthorized

X = np.array(X)
y = np.array(y)

# ======================
# Train/Test Split
# ======================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ======================
# Train Model
# ======================
model = LogisticRegression()
model.fit(X_train, y_train)

# ======================
# Evaluate
# ======================
accuracy = accuracy_score(y_test, model.predict(X_test))
print("Training Accuracy:", accuracy)

# ======================
# Save Model
# ======================
joblib.dump(model, "model.pkl")
print("✅ model.pkl saved successfully")

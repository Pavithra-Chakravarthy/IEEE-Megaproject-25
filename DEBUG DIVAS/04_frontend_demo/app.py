import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import joblib
import os
import time


@st.cache_resource
def load_model():
    base_dir = os.path.dirname(__file__)
    model_path = os.path.join(base_dir, "model.pkl")
    return joblib.load(model_path)

model = load_model()


# =====================================================
# TITLE & INTRO
# =====================================================
st.title("Cognitive Radio Spectrum Security System")

st.markdown("""
This system continuously monitors radio spectrum activity.  
Unauthorized transmissions are **detected, classified, and blocked**
before message delivery.
""")

st.divider()

# =====================================================
# USER INPUT PANEL
# =====================================================
st.subheader("Transmission Request")

message = st.text_input("Message Payload")

tx_mode = st.radio(
    "Select Transmission Channel",
    ["Authorized Channel", "Unauthorized Channel"]
)

noise_level = st.slider(
    "Environmental Noise Level",
    0.0, 1.0, 0.3
)

start_scan = st.button("Initiate Spectrum Scan")

# =====================================================
# SIGNAL SETUP
# =====================================================
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)

band1 = np.sin(2 * np.pi * 50 * t)
band2 = np.sin(2 * np.pi * 120 * t)
band3 = np.sin(2 * np.pi * 250 * t)

freq = np.fft.fftfreq(fs, 1/fs)[:fs//2]

# =====================================================
# MAIN PROCESS
# =====================================================
if start_scan:

    st.divider()
    st.subheader("Live Spectrum Monitoring")

    plot_area = st.empty()

    # -------- LIVE SPECTRUM ANIMATION --------
    for _ in range(12):
        signal = band1 + band2 + band3

        if tx_mode == "Unauthorized Channel":
            signal += 3.0 * np.sin(2 * np.pi * 120 * t)

        signal += np.random.normal(0, noise_level, fs)

        fft_signal = np.abs(np.fft.fft(signal))[:fs//2]

        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(freq, fft_signal)
        ax.set_xlabel("Frequency (Hz)")
        ax.set_ylabel("Magnitude")
        ax.set_title("Real-Time Spectrum Scan")
        ax.grid(True)

        plot_area.pyplot(fig)
        time.sleep(0.12)

    # =================================================
    # ENERGY-BASED DETECTION
    # =================================================
    st.subheader("Energy-Based Band Analysis")

    bands = {
        "Band 1 (50 Hz)": (40, 60),
        "Band 2 (120 Hz)": (100, 140),
        "Band 3 (250 Hz)": (230, 270),
    }

    EXPECTED_POWER = 2e5
    THRESHOLD_FACTOR = 1.6

    energy_alert = False

    for band, (low, high) in bands.items():
        idx = np.where((freq >= low) & (freq <= high))
        power = np.sum(fft_signal[idx] ** 2)

        if power > EXPECTED_POWER * THRESHOLD_FACTOR:
            st.error(f"{band}: Unauthorized activity detected")
            energy_alert = True
        else:
            st.success(f"{band}: Within licensed limits")

    # =================================================
    # ML DETECTION
    # =================================================
    st.subheader("Machine Learning Classification")

    with st.spinner("Extracting features and classifying signal..."):
        time.sleep(1.2)

    features = [
        np.sum(fft_signal ** 2),
        np.var(fft_signal)
    ]

    prediction = model.predict([features])[0]

    if prediction == 1:
        st.error("ML Decision: Unauthorized Transmission")
    else:
        st.success("ML Decision: Authorized Transmission")

    # =================================================
    # MESSAGE CONTROL
    # =================================================
    st.subheader("Transmission Control")

    if message.strip() == "":
        st.info("No message payload provided.")
    else:
        with st.spinner("Applying security policy..."):
            time.sleep(1)

        if prediction == 1 or energy_alert:
            st.error("Transmission Blocked: Policy Violation Detected")
        else:
            st.success("Transmission Approved")
            st.code(message, language="text")

    st.divider()
    st.caption("Cognitive Radio Security Demonstration")

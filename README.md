Cognitive Radio Spectrum Monitoring System


---

👥 Team Details

Team Name: Cognitive Radio Innovators

Team Members:

Aakanksha A

Pavithra C



---

🌐 Domain of the Project

Wireless Communication / Cognitive Radio / Spectrum Monitoring


---

💡 Idea

Efficient utilization of the radio frequency spectrum is a major challenge in modern wireless communication systems. Unauthorized or inefficient spectrum usage can lead to interference, reduced network performance, and wastage of valuable spectrum resources.

The Cognitive Radio Spectrum Monitoring System addresses this issue by simulating radio signals, analyzing spectrum usage, and detecting unauthorized transmissions. The system uses FFT-based energy detection along with a machine learning model (Logistic Regression) to classify spectrum activity. An interactive Streamlit-based web application visualizes signals and detection results in real time, making the system intuitive and easy to understand.


---

🛠 Tech Stack Used

Python

NumPy & SciPy – signal generation and FFT-based spectrum analysis

Scikit-learn – Logistic Regression model for unauthorized signal detection

Matplotlib – signal and frequency-domain visualization

Streamlit – interactive frontend and cloud deployment

Joblib – machine learning model serialization



---

▶️ How to Execute the Code (Local Setup)

Prerequisites

Python 3.9 or above

Git


Steps

1. Clone the repository

git clone https://github.com/Pavithra-Chakravarthy/Cognitive-radio-streamlit.git
cd Cognitive-radio-streamlit


2. Install required dependencies

python -m pip install -r requirements.txt


3. Run the Streamlit application

python -m streamlit run 04_frontend_demo/app.py


4. Access the application

Open a browser and navigate to:

http://localhost:8501





---

🔗 Code Sample / Hosted Website

GitHub Repository:
👉 https://github.com/Pavithra-Chakravarthy/Cognitive-radio-streamlit.git

Live Hosted Application:
👉 https://cognitive-radio-app-ek3gpxaiwcidd7spnax7nn.streamlit.app/



---

💻 Code Sample (Run Command)

python -m streamlit run 04_frontend_demo/app.py


---

📝 Notes for Evaluators

The project demonstrates spectrum sensing using FFT, energy detection, and machine learning-based classification.

The modular project structure separates signal generation, spectrum sensing, unauthorized detection, and frontend visualization.

The system is scalable and can be extended to work with real-time inputs from Software Defined Radios (SDRs) in future implementations.

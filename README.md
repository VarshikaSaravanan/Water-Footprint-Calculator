# 🌊Water Footprint Calculator
📖 Overview
Water scarcity is a growing global concern, particularly in agriculture, which accounts for a significant portion of the world's freshwater withdrawals. The Water Footprint Predictor is an AI-powered web application designed to address this challenge by providing estimated water consumption data for various agricultural crops. By bridging the gap between complex data science and everyday farming, this tool empowers farmers, researchers, and policymakers to make informed, data-driven decisions that promote sustainable resource management and water conservation.

✨ Key Features
AI-Powered Estimation: Utilizes a pre-trained machine learning model to predict the total water footprint (in cubic meters) based on critical inputs: Crop Type, State, District, and Cultivation Area.
Locality-Specific Analysis: Takes into account regional differences by pinpointing predictions to specific States and Districts, ensuring higher accuracy relevant to the local climate and conditions.
Session History: Includes a "Prediction History" feature that logs recent queries during the session, allowing users to easily compare potential water usage across different crops or land sizes.
Educational Impact: Every prediction result is accompanied by a randomized water conservation quote, reinforcing the importance of saving water.
Modern UI/UX: Built with a responsive, pleasing interface using Tailwind CSS, ensuring a smooth experience across desktop and mobile devices.
🛠️ Technologies Used
Backend Framework: Python (Flask)
Machine Learning & Data: Scikit-learn, Pandas, NumPy, Pickle
Frontend: HTML5, Tailwind CSS
Deployment: Capable of running on local servers or cloud platforms like Render/Heroku.
🚀 Getting Started
Clone the repository.
Install dependencies: pip install -r requirements.txt
Ensure the model files (modelo.pkl, encoder.pkl) are in the models/ directory.
Run the application: python app.py
Open your browser and navigate to http://localhost:5000.
<img width="1600" height="793" alt="image" src="https://github.com/user-attachments/assets/a29bc4eb-c02f-4e3e-8a08-9a47172a657d" />
<img width="1600" height="797" alt="image" src="https://github.com/user-attachments/assets/41f459b5-fac7-4778-9f12-6476509433e0" />
<img width="1600" height="801" alt="image" src="https://github.com/user-attachments/assets/05409f7b-05c1-4a3a-8ce4-2bacd6ef21de" />



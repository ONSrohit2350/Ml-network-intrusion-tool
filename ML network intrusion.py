import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

print("==================================================")
print("   Topic 6: ML Network Intrusion Detector         ")
print("==================================================")

# Step 1: Generate/Simulate Network Traffic Dataset (Mocking NSL-KDD style features)
# Features: [duration, src_bytes, dst_bytes, connection_count]
# Label: 0 = Normal Traffic, 1 = Network Intrusion / Anomaly
np.random.seed(42)
n_samples = 1000

data = {
    'duration': np.random.randint(0, 100, n_samples),
    'src_bytes': np.random.randint(100, 5000, n_samples),
    'dst_bytes': np.random.randint(100, 10000, n_samples),
    'count': np.random.randint(1, 50, n_samples)
}

df = pd.DataFrame(data)

# Rules for synthetic anomalies (e.g., high duration and high source bytes)
y = np.where((df['duration'] > 70) & (df['src_bytes'] > 3000), 1, 0)
noise = np.random.choice([0, 1], size=n_samples, p=[0.9, 0.1])
y = np.logical_or(y, noise).astype(int)

X = df[['duration', 'src_bytes', 'dst_bytes', 'count']]

# Step 2: Split data into Training and Testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train Random Forest Machine Learning Model
print("\n[*] Training Random Forest Classifier model...")
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X_train, y_train)
print("[+] Model training completed successfully!")

# Step 4: Evaluate Model Performance
y_pred = model.predict(X_test)
print("\n--- Model Evaluation Report ---")
print(f"Accuracy Score: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# Step 5: Test with New Network Flows (Real-time Simulation)
print("\n[*] Testing model with new live network packet flows:")

# Sample 1: Typical normal traffic packet
sample_normal = [[12, 250, 600, 3]]
# Sample 2: Suspicious/Anomalous traffic packet (High duration & bytes)
sample_attack = [[85, 4800, 9200, 42]]

pred_1 = model.predict(sample_normal)[0]
pred_2 = model.predict(sample_attack)[0]

print(f"  - Packet 1 (Normal Flow) Prediction : {'Anomaly/Attack 🚨' if pred_1 == 1 else 'Normal Traffic ✅'}")
print(f"  - Packet 2 (Suspicious Flow) Prediction: {'Anomaly/Attack 🚨' if pred_2 == 1 else 'Normal Traffic ✅'}")

import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# =========================
# 1. Load Dataset
# =========================
data = pd.read_csv("student_performance.csv")

print("Columns:", data.columns)

# =========================
# 2. Select Features
# =========================
features = [
    "StudyHours",
    "Attendance",
    "Motivation",
    "StressLevel"
]

target = "LearningStyle"

data = data[features + [target]].dropna()

# =========================
# 3. Train Model
# =========================
X = data[features]
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=120)
model.fit(X_train, y_train)

# =========================
# 4. Accuracy
# =========================
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# =========================
# 5. Save Model
# =========================
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained successfully!")
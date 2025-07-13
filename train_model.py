import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

# 1. Load dataset
df = pd.read_csv("dataset_topik_judul_100_expanded.csv")

# 2. Pisahkan fitur dan label
X = df["Judul Tugas"]
y = df["Topik"]

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. TF-IDF + SVM pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LinearSVC())
])

# 5. Train model
model.fit(X_train, y_train)

# 6. Evaluasi
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# 7. Simpan model
joblib.dump(model, "model_klasifikasi.pkl")
print("Model disimpan sebagai model_klasifikasi.pkl")

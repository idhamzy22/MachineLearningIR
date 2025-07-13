import pandas as pd
import string
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.exceptions import UndefinedMetricWarning

# === STEP 0: Bersihin warning bawel ===
warnings.filterwarnings("ignore", category=UndefinedMetricWarning)

# === STEP 1: Load Dataset ===
df = pd.read_csv('dataset_topik_judul_1000.csv')  # ganti path kalau perlu

# === STEP 2: Preprocessing Judul ===
df["Judul Bersih"] = df["Judul Tugas"].str.lower().str.translate(str.maketrans('', '', string.punctuation))

# === STEP 3: TF-IDF Vectorization ===
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["Judul Bersih"])
y = df["Topik"]

# === STEP 4: Split Data ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# === STEP 5: Training Model ===
model = MultinomialNB()
model.fit(X_train, y_train)

# === STEP 6: Evaluasi ===
y_pred = model.predict(X_test)
print("=== Classification Report ===")
print(classification_report(y_test, y_pred))

# === VISUAL 1: Bar Chart Topik ===
plt.figure(figsize=(10, 5))
sns.countplot(y=df["Topik"], order=df["Topik"].value_counts().index, palette="viridis")
plt.title("Distribusi Jumlah Judul per Topik")
plt.xlabel("Jumlah Judul")
plt.ylabel("Topik")
plt.tight_layout()
plt.show()

# === VISUAL 2: Confusion Matrix ===
cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)

plt.figure(figsize=(10, 7))
disp.plot(cmap=plt.cm.Blues, xticks_rotation=45)
plt.title("Confusion Matrix - Hasil Klasifikasi Judul")
plt.tight_layout()
plt.show()

# === VISUAL 3: Kata Paling Sering (Manual Stopwords) ===
manual_stopwords = {
    'pt', 'xyz', 'kasus', 'tahun', 'bandung', 'studi', 'di', 'dengan', 'untuk',
    'menggunakan', 'berbasis', 'baru', 'pada', 'dan', 'dalam', 'online',
    'yang', 'dari', 'oleh', 'akan', 'sebagai'
}

tokens = []
for text in df["Judul Bersih"]:
    for word in text.split():
        if word not in manual_stopwords:
            tokens.append(word)

freq = Counter(tokens)
top_words = freq.most_common(20)

# Tampilkan grafik
words, counts = zip(*top_words)
plt.figure(figsize=(12, 6))
sns.barplot(x=list(counts), y=list(words), palette="magma")
plt.title("20 Kata Paling Sering Muncul (Stopwords Manual)")
plt.xlabel("Jumlah")
plt.ylabel("Kata")
plt.tight_layout()
plt.show()

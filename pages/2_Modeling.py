import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

st.title("2. Pelatihan Model")

df = pd.read_csv("data/lulus.csv")
X = df[['IPK','Pelatihan Pengetahuan','Prestasi','Kegiatan Organisasi']]
y = df['Lulus Cepat'].map({'Yes':1,'No':0})

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Naive Bayes
nb = GaussianNB()
:contentReference[oaicite:13]{index=13}
:contentReference[oaicite:14]{index=14}
:contentReference[oaicite:15]{index=15}

# Model KNN (k=5)
:contentReference[oaicite:16]{index=16}
:contentReference[oaicite:17]{index=17}
:contentReference[oaicite:18]{index=18}
:contentReference[oaicite:19]{index=19}

:contentReference[oaicite:20]{index=20}
:contentReference[oaicite:21]{index=21}
:contentReference[oaicite:22]{index=22}

:contentReference[oaicite:23]{index=23}
:contentReference[oaicite:24]{index=24}

:contentReference[oaicite:25]{index=25}
:contentReference[oaicite:26]{index=26}

# Simpan model
import pickle
:contentReference[oaicite:27]{index=27}
    :contentReference[oaicite:28]{index=28}
:contentReference[oaicite:29]{index=29}
    :contentReference[oaicite:30]{index=30}

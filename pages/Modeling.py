def run():
    import streamlit as st
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import GaussianNB
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import classification_report

    st.subheader("🛠️ Modeling (Train Naive Bayes & KNN)")

    df = pd.read_csv("data/lulus.csv")
    X = df[['IPK', 'Pelatihan Pengetahuan', 'Prestasi', 'Kegiatan Organisasi']]
    y = df['Lulus Cepat'].map({'Yes': 1, 'No': 0})

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model_nb = GaussianNB()
    model_nb.fit(X_train, y_train)
    y_pred_nb = model_nb.predict(X_test)

    model_knn = KNeighborsClassifier(n_neighbors=3)
    model_knn.fit(X_train, y_train)
    y_pred_knn = model_knn.predict(X_test)

    st.markdown("### 📘 Naive Bayes")
    st.text(classification_report(y_test, y_pred_nb))

    st.markdown("### 📗 KNN (k=3)")
    st.text(classification_report(y_test, y_pred_knn))

def run():
    import streamlit as st
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import GaussianNB
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import accuracy_score

    st.title("🔧 Modeling - Pelatihan Model")

    # Load data
    df = pd.read_csv("lulus.csv")
    df.columns = df.columns.str.strip()  # 🔧 Hapus spasi di nama kolom

    # Debug tampilkan nama kolom
    st.write("Kolom DataFrame:", df.columns.tolist())

    # Fitur dan target
    X = df[['IPK', 'Pelatihan Pengetahuan', 'Prestasi', 'Kegiatan Organisasi']]
    y = df['Lulus Cepat']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Naive Bayes
    nb = GaussianNB()
    nb.fit(X_train, y_train)
    y_pred_nb = nb.predict(X_test)
    acc_nb = accuracy_score(y_test, y_pred_nb)

    # Train KNN
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    y_pred_knn = knn.predict(X_test)
    acc_knn = accuracy_score(y_test, y_pred_knn)

    # Output akurasi
    st.subheader("🎯 Akurasi Model:")
    st.write(f"✅ Naive Bayes: {acc_nb:.2f}")
    st.write(f"✅ KNN: {acc_knn:.2f}")

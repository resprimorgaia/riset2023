import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.densenet import preprocess_input
import os

# Fungsi untuk melakukan prediksi
def predict(image_path, model):
    # Membaca gambar dan melakukan preprocessing
    img = image.load_img(image_path, target_size=(256, 256))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)

    # Melakukan prediksi
    predictions = model.predict(img)
    return predictions

# Mendefinisikan kelas rimpang
classes = ['Jahe', 'Kunyit', 'Lengkuas']

# Judul dan deskripsi aplikasi
st.title("Aplikasi Klasifikasi Rimpang")
st.write("Upload gambar rimpang (Jahe, Kunyit, Lengkuas) yang diidentifikasi.")

# Memungkinkan pengguna untuk mengunggah file gambar
uploaded_file = st.file_uploader("Pilih sebuah gambar...", type=["jpg", "jpeg", "png"])

# Load model DenseNet121
model_path = 'model/resnanda-rempah-densenet-98-08.h5'  # Gantilah dengan path model Anda
loaded_model = load_model(model_path)

if uploaded_file is not None:
    # Menampilkan gambar yang diunggah
    st.image(uploaded_file, caption="Gambar yang diunggah.", use_column_width=True)
    st.write("")

    # Melakukan prediksi ketika gambar diunggah
    st.write("Melakukan prediksi...")
    # Simpan file gambar untuk prediksi di folder 'upload'
    image_path = os.path.join("upload", uploaded_file.name)
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Melakukan prediksi
    predictions = predict(image_path, loaded_model)
    predicted_class = classes[np.argmax(predictions)]
    accuracy = np.max(predictions) * 100  # Menghitung akurasi dalam persen

    # Menampilkan hasil prediksi dan akurasi
    st.write(f"Hasil Klasifikasi: {predicted_class}")
    st.write(f"Akurasi: {accuracy:.2f}%")

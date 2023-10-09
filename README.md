# Aplikasi Deteksi Rimpang Berbasis Website dengan Streamlit
Rimpang yang diklasifikasi terbatas pada jenis Jahe, Kunyit, dan Lengkuas. Aplikasi ini saya buat dengan menggunakan pemodelan Convolutional Neural Network dengan akurasi 97%, dari model yang sudah disimpan pada format h5 dimuat pada kerangka streamlit yang sebelumnya sudah saya bangun. Projek ini dapat berjalan di local dengan python versi 3.8.18, ataupun secara online.
Beberapa dependensi yang digunakan pada projek ini adalah :

* streamlit
* Pillow
* numpy
* tensorflow

---
### Model
Model dibangun dengan memanfaatkan arsitektur DenseNet121 yang sudah disediakan oleh keras. DenseNet121 adalah arsitektur dengan ukuran terkecil di antara 2 arsitektur Densenet lainnya namum masih memiliki akurasi yang tinggi.

![download](https://github.com/resprimorgaia/riset2023/assets/113764627/49875668-ab46-45c3-b21f-f534e7cb11be)

---

### Website
Kerangka website menggunakan framework python Streamlit yang sangat mendukung dalam pengaplikasian projek data mining. Tatutan website yang telah dihosting https://deteksirimpang.streamlit.app/
![image](https://github.com/resprimorgaia/riset2023/assets/113764627/0d7577d7-7255-4bf5-8105-9ab8842cf41c)

![image](https://github.com/resprimorgaia/riset2023/assets/113764627/0d872544-37c9-4ac4-b6b4-6a4683ad76a1)


---
### Instalasi pada Local
Untuk menjalankan aplikasi ini di perangkat komputer local diperlukan beberapa cara. Pada sistem operasi windows dan anaconda bisa mengikuti cara berikut:
1. Buat Environment Python baru dengan Python versi 3.8.18 supaya tidak menimpa base environment yang ada di anaconda. Untuk yang sudah memiliki environment ini atau tidak mau mebuat environment baru silahkan lewati langkah ini.
Pada anaconda prompt:
```
# conda create -n coba python=3.8.18
```
Anda bisa mengganti kata "coba" dengan nama lain yang anda kehendaki. Kemudian aktifkan environment yang sudah dibuat.
```
# activate coba
```
Ganti kata "coba" dengan nama lain yang anda buat sebelumnya

2.   Install beberapa dependensi yang digunakan, jika anda sudah mengunduh projeknya bisa melakukan dengan cara pada anaconda prompt arahkan pada folder tempat anda menyimpan.
```
# pip install -r requirements.txt
```
Jika anda belum mengunduh silahkan mengikuti perintah berikut.
```
# pip install streamlit==1.27.2 Pillow=10.0.1 numpy==1.24.3 tensorflow==2.13.0
```
3.   Unduh projek ini dan simpan pada direktori yang dikendaki keudian pada anaconda prompt arahkan pada direktori tempat anda menyimpan dengan perintah cd lokasi_direktori. Sebagai contoh saya menyimpannya pada direktori C:/Users/NamaSaya/AI Mastery/Coba/riset2023-main maka perintahnya adalah
```
# cd AI Masteri/Coba/riset2023-main
```
Anda bisa menyesuaikannya dengan direktori tempat anda kehendaki. Jika sudah anda bisa menjalakan pada local dengan cara
```
# streamlit run app.py
```
dan secara default akan berjalan pada http://localhost:8501/ atau anda bisa melihat alamat yang muncul di anaconda prompt.

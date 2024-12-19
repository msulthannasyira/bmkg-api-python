# bmkg-api-python
disini saya akan memberikan kode yang dapat mengambil data dari API bmkg yang selanjutnya dapat di save menjadi json file dan antarmuka dalam bentuk grafik. Berikut adalah penjelasan rinci:

## Langkah-langkah Program

### 1. Mengimpor Library

• `pandas` untuk manipulasi data.

• `matplotlib.pyplot` untuk membuat grafik.

• `json` untuk membaca/menyimpan data dalam format JSON.

• `datetime` untuk menangani data waktu.

### 2. Input Tanggal Prakiraan

```python
forecast_date = input("Enter the forecast date (YYYY-MM-DD): ")
```

• Pengguna diminta memasukkan tanggal prakiraan dalam format YYYY-MM-DD.

### 3. Data Cuaca Sampel

• Data cuaca disimpan dalam format JSON. Data ini mencakup informasi lokasi (provinsi, kota, kecamatan, desa, longitude, latitude, dll.) dan data prakiraan cuaca per jam.

• Setiap data prakiraan memiliki atribut seperti:

• `datetime`: Waktu prakiraan.

• `t`: Suhu (°C).

• `weather_desc`: Deskripsi cuaca (Cerah, Berawan, Hujan, dll.).

• `ws`: Kecepatan angin (m/s).

• `hu`: Kelembapan (%).

• `vs`: Jarak pandang (m).

### 4. Ekstraksi Data

• Program mengambil data cuaca dari struktur JSON, mengolahnya menjadi beberapa list (time_series, temperature_series, dll.).

• Data waktu diubah menjadi objek `datetime` agar dapat diolah lebih lanjut.

### 5. Membuat DataFrame

• Jika terdapat data cuaca, program membuat DataFrame menggunakan `pandas` dengan kolom:

• `Time`: Waktu prakiraan.

• `Temperature`: Suhu.

• `Weather Description`: Deskripsi cuaca.

• `Wind Speed (m/s)`: Kecepatan angin.

• `Humidity (%)`: Kelembapan.

• `Visibility (m)`: Jarak pandang.

• Kolom `Time` diubah ke format string agar bisa diserialisasi ke JSON.

### 6. Membuat Grafik

• Grafik suhu dan kelembapan dibuat menggunakan `matplotlib`. Data waktu diplot pada sumbu x, sementara suhu dan kelembapan diplot pada sumbu y.

• Grafik diberi label, legenda, dan disimpan dalam file gambar dengan nama `weather_forecast.png`.

### 7. Menyimpan Data ke File JSON

• Data DataFrame dikonversi menjadi format JSON menggunakan `to_dict(orient='records')` dan disimpan dalam file bernama `weather_forecast_data.json`.

### 8. Output

• Program memberi tahu lokasi file hasil dalam pesan terminal:

```
Files saved as 'D:\scrapping\weather_forecast.png' and 'D:\scrapping\weather_forecast_data.json'
```

## Komponen Program

### Data JSON

Struktur JSON digunakan untuk menyimpan data lokasi dan prakiraan cuaca per jam.

### Manipulasi Data

• List: Data cuaca diekstraksi ke dalam beberapa list (contoh: `temperature_series`, `humidity_series`).

• DataFrame: Data list dikonversi menjadi DataFrame untuk kemudahan pengolahan dan ekspor data.

### Visualisasi

• Grafik: Grafik suhu dan kelembapan dibuat untuk memberikan gambaran tren cuaca sepanjang hari.

### Ekspor

File Gambar: Grafik disimpan sebagai file `.png`.

File JSON: Data prakiraan disimpan dalam format `.json`.

### Tambahan Program

### Lokasi Penyimpanan File

• Ubah direktori output D:\scrapping\ jika ingin menyimpan file di lokasi lain.

### Data Input

• Tambahkan lebih banyak data cuaca untuk lokasi atau waktu berbeda.

### Visualisasi Lain

•  Tambahkan grafik untuk atribut lain seperti kecepatan angin (ws) atau jarak pandang (vs).

### Penggunaan di Dunia Nyata

• Sambungkan program dengan API cuaca untuk mengambil data nyata (contohnya API OpenWeatherMap).



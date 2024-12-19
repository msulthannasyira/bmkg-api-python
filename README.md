# bmkg-api-python
Kode Python ini dirancang untuk mengambil data cuaca dari API BMKG, mengolahnya, dan menyimpan hasilnya dalam bentuk file JSON. Selain itu, kode ini juga menyediakan user interface berupa grafik untuk mempermudah analisis data cuaca. kalian dapat mengambil data dari waktu kapanpun selama data tersebut masih tersedia di API BMKG-nya sendiri. Berikut adalah penjelasan rinci mengenai cara kerjanya:

kode dapat diakses melalui: https://github.com/msulthannasyira/bmkg-api-python

API BMKG dapat diakses melalui: https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4=33.24.12.2006&fbclid=IwZXh0bgNhZW0CMTAAAR35ShvcFv-oBidD3IvMzV7ffDcUmkUfgcO5ytLXwRW762RECImdXoFoHbM_aem_BnmytKhbVDWA3T0G0QPooQ

## Screenshot Tampilan

![image](https://github.com/user-attachments/assets/81ef7518-298c-4770-95f8-e1348eb2b216)

![image](https://github.com/user-attachments/assets/8e42cd4d-d157-4e79-a6e0-4eb9ad6f654b)

![image](https://github.com/user-attachments/assets/42c793cf-29f9-4be7-af5c-6f3362f4673d)

## Langkah-langkah Program

### 1. Mengimpor Library

• `pandas` untuk manipulasi data.

• `matplotlib.pyplot` untuk membuat grafik.

• `json` untuk membaca/menyimpan data dalam format JSON.

• `datetime` untuk menangani data waktu.

### 2. Edit Lokasi

• Untuk mengedit lokasi dalam kode, cukup ganti informasi yang terdapat pada kunci lokasi dan dalam elemen lokasi pada data cuaca. Berikut adalah lokasi yang sudah diperbarui ke tempat baru:

```python
weather_data = {
    'lokasi': {
        'provinsi': 'Jawa Timur',  # Ganti provinsi
        'kotkab': 'Surabaya',      # Ganti kota/kabupaten
        'kecamatan': 'Wonokromo',  # Ganti kecamatan
        'desa': 'Darmo',           # Ganti desa
        'lon': 112.7398983,        # Ganti longitude
        'lat': -7.2891668,         # Ganti latitude
        'timezone': 'Asia/Jakarta' # Zona waktu
    },
    'data': [
        {
            'lokasi': {
                'provinsi': 'Jawa Timur',  # Ganti provinsi
                'kotkab': 'Surabaya',      # Ganti kota/kabupaten
                'kecamatan': 'Wonokromo',  # Ganti kecamatan
                'desa': 'Darmo',           # Ganti desa
                'lon': 112.7398983,        # Ganti longitude
                'lat': -7.2891668,         # Ganti latitude
                'timezone': '+0700',       # Ganti zona waktu jika perlu
                'type': 'adm4'
            },
            'cuaca': [
                # Data cuaca tetap sama seperti sebelumnya
            ]
        }
    ]
}
```
• Setelah mengganti lokasi sesuai kebutuhan, Anda dapat menjalankan kembali kode untuk mendapatkan data yang diperbarui dengan informasi lokasi tersebut. Jika ada elemen lain yang perlu diperbarui, tambahkan dalam struktur data sesuai format yang ada.

### 3. Input Tanggal Ramalan Cuaca

```python
forecast_date = input("Enter the forecast date (YYYY-MM-DD): ")
```

• Pengguna diminta memasukkan tanggal prakiraan dalam format YYYY-MM-DD.

### 4. Sampel Data Cuaca

• Data cuaca disimpan dalam format JSON. Data ini mencakup informasi lokasi (provinsi, kota, kecamatan, desa, longitude, latitude, dll.) dan data prakiraan cuaca per jam.

• Setiap data prakiraan memiliki atribut seperti:

• `datetime`: Waktu prakiraan.

• `t`: Suhu (°C).

• `weather_desc`: Deskripsi cuaca (Cerah, Berawan, Hujan, dll.).

• `ws`: Kecepatan angin (m/s).

• `hu`: Kelembapan (%).

• `vs`: Jarak pandang (m).

### 5. Ekstraksi Data

• Program mengambil data cuaca dari struktur JSON, mengolahnya menjadi beberapa list (time_series, temperature_series, dll.).

• Data waktu diubah menjadi objek `datetime` agar dapat diolah lebih lanjut.

### 6. Membuat DataFrame

• Jika terdapat data cuaca, program membuat DataFrame menggunakan `pandas` dengan kolom:

• `Time`: Waktu prakiraan.

• `Temperature`: Suhu.

• `Weather Description`: Deskripsi cuaca.

• `Wind Speed (m/s)`: Kecepatan angin.

• `Humidity (%)`: Kelembapan.

• `Visibility (m)`: Jarak pandang.

• Kolom `Time` diubah ke format string agar bisa diserialisasi ke JSON.

### 7. Membuat Grafik

• Grafik suhu dan kelembapan dibuat menggunakan `matplotlib`. Data waktu diplot pada sumbu x, sementara suhu dan kelembapan diplot pada sumbu y.

• Grafik diberi label, legenda, dan disimpan dalam file gambar dengan nama `weather_forecast.png`.

### 8. Menyimpan Data ke File JSON

• Data DataFrame dikonversi menjadi format JSON menggunakan `to_dict(orient='records')` dan disimpan dalam file bernama `weather_forecast_data.json`.

### 9. Output

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



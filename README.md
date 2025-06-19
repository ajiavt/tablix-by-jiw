This README is available in two languages.
- [English Version](#tablix---java-code-search-application)
- [Versi Bahasa Indonesia](#tablix---aplikasi-pencarian-kode-java)

---

# Tablix - Java Code Search Application

Tablix is a web-based application that allows users to search for Java code within `.DAT` files based on database table names and specific keywords. This application is ideal for analyzing and finding SQL queries within a large Java codebase.

## Features

- Search by table name.
- Search with a combination of table name and keywords (e.g., `jt`, `jdbc`, `jdbcTemplate`).
- Upload a folder containing source code.
- Easy-to-read display of search results.
- Export search results to an Excel file.

## Requirements

- Python `3.9.6`
- Flask
- Pandas
- OpenPyxl

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/ajiavt/tablix-by-jiw.git
   cd tablix-by-jiw
   ```

2. Manually install the required dependencies. It is recommended to use a virtual environment.
   ```sh
   # Note: Use 'python' or 'python3' depending on your system configuration.
   # The following commands are based on using 'python3'.
   python3 -m pip install Flask
   python3 -m pip install pandas
   python3 -m pip install openpyxl
   ```

3. Run the application:
   - For **Windows**, run the `run.bat` script:
     ```sh
     run.bat
     ```
   - For **macOS and Linux**, make the script executable and then run it:
     ```sh
     chmod +x run.sh
     ./run.sh
     ```

4. Open your web browser and navigate to `http://localhost:5000`.

## How to Use

1. Open the application in your browser.
2. Upload the folder containing your source files (as `.DAT` files).
3. Select a table name from the dropdown list.
4. (Optional) Select or add keywords to refine the search.
5. Click the "Search" button.
6. View the search results.
7. (Optional) Download the results as an Excel file.

## Project Structure

```
Tablix/
│
├── app.py                   # Main Flask application file
├── run.bat                  # Run script for Windows
├── run.sh                   # Run script for macOS/Linux
├── requirements.txt         # List of Python dependencies
├── setting-tbl-name.txt     # List of database table names
├── roadmap.txt              # Development plan
│
├── source/                  # Folder containing Java source code files (.DAT)
│
├── uploads/                 # Folder to store exported files
│
└── templates/               # HTML templates for the web interface
    └── index.html           # Main page of the application
```

## Workflow

1. **Collection**: The application reads all files in the `source/` directory and loads the list of table names from `setting-tbl-name.txt`.
2. **Get Properties (User Input)**: The user selects a table name and optional keywords from the web interface.
3. **Searching**: The application searches through the source files for lines containing both the selected table name and keywords.
4. **Reporting**: The search results are displayed on the web page and can be downloaded as an Excel file.

## Additional Information

Tablix is designed to analyze Java 1.7 source code stored in `.DAT` files. The application finds queries and the full context where the table name and keywords appear together, making it easier for developers to find and analyze relevant code.

## Contributing

Contributions to the development of this application are welcome. Please create a pull request for any improvements or new features.

---

# Tablix - Aplikasi Pencarian Kode Java

Tablix adalah aplikasi web yang memungkinkan pengguna untuk mencari kode Java dalam file-file `.DAT` berdasarkan nama tabel database dan keyword tertentu. Aplikasi ini ideal untuk menganalisis dan menemukan query SQL (perintah untuk mengakses database) dalam codebase (kumpulan kode) Java yang besar.

## Fitur

- Pencarian berdasarkan nama tabel.
- Pencarian dengan kombinasi tabel dan keyword (misalnya: `jt`, `jdbc`, `jdbcTemplate`).
- Fitur unggah folder yang berisi source code.
- Tampilan hasil pencarian yang mudah dibaca.
- Ekspor (menyimpan) hasil pencarian ke file Excel.

## Persyaratan

- Python `3.9.6`
- Flask (kerangka kerja web untuk Python)
- Pandas (pustaka untuk manipulasi data)
- OpenPyxl (pustaka untuk membaca/menulis file Excel)

## Instalasi

1. Clone (salin) repositori ini:
   ```sh
   git clone https://github.com/ajiavt/tablix-by-jiw.git
   cd tablix-by-jiw
   ```

2. Instal dependensi yang diperlukan secara manual. Disarankan untuk menggunakan *virtual environment* (lingkungan virtual untuk proyek Python).
   ```sh
   # Catatan: Gunakan 'python' atau 'python3' tergantung pada konfigurasi sistem Anda.
   # Perintah berikut menggunakan 'python3'.
   python3 -m pip install Flask
   python3 -m pip install pandas
   python3 -m pip install openpyxl
   ```

3. Jalankan aplikasi:
   - Untuk **Windows**, jalankan skrip `run.bat`:
     ```sh
     run.bat
     ```
   - Untuk **macOS dan Linux**, buat skrip menjadi *executable* lalu jalankan:
     ```sh
     chmod +x run.sh
     ./run.sh
     ```

4. Buka browser Anda dan akses `http://localhost:5000`.

## Cara Penggunaan

1. Buka aplikasi di browser.
2. Unggah folder yang berisi file-file source code Anda (dalam format `.DAT`).
3. Pilih nama tabel dari daftar dropdown.
4. (Opsional) Pilih atau tambahkan keyword untuk mempersempit pencarian.
5. Klik tombol "Cari".
6. Lihat hasil pencarian.
7. (Opsional) Unduh hasil dalam format Excel.

## Struktur Proyek

```
Tablix/
│
├── app.py                   # File utama aplikasi Flask
├── run.bat                  # Skrip untuk menjalankan di Windows
├── run.sh                   # Skrip untuk menjalankan di macOS/Linux
├── requirements.txt         # Daftar dependensi Python
├── setting-tbl-name.txt     # Daftar nama-nama tabel database
├── roadmap.txt              # Rencana pengembangan
│
├── source/                  # Folder berisi file source code Java (.DAT)
│
├── uploads/                 # Folder untuk menyimpan file hasil ekspor
│
└── templates/               # Template HTML untuk antarmuka web
    └── index.html           # Halaman utama aplikasi
```

## Alur Kerja

1. **Collection (Pengumpulan)**: Aplikasi akan membaca semua file di dalam folder `source/` dan memuat daftar nama tabel dari file `setting-tbl-name.txt`.
2. **Get Properties (Input Pengguna)**: Pengguna memilih nama tabel dan keyword (opsional) melalui antarmuka web.
3. **Searching (Pencarian)**: Aplikasi akan mencari baris kode di dalam file source code yang mengandung nama tabel dan keyword yang telah dipilih.
4. **Reporting (Pelaporan)**: Hasil pencarian ditampilkan di halaman web dan dapat diunduh dalam format Excel.

## Informasi Tambahan

Tablix dirancang untuk menganalisis source code Java versi 1.7 yang disimpan dalam file berekstensi `.DAT`. Aplikasi akan mencari query dan konteks lengkap di mana nama tabel dan keyword muncul bersamaan, memudahkan pengembang untuk menemukan dan menganalisis kode yang relevan.

## Kontribusi

Kontribusi untuk pengembangan aplikasi ini sangat diterima. Silakan buat *pull request* (permintaan untuk menggabungkan kode) untuk perbaikan atau penambahan fitur.

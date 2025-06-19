#!/bin/bash

# Instal dependencies
echo "Menginstal dependensi..."
python3 -m pip install -r requirements.txt

# Jalankan aplikasi
echo "Menjalankan aplikasi pada http://localhost:5000"
python3 app.py 
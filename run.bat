@echo off
echo Menginstal dependensi...
python -m pip install -r requirements.txt

echo Menjalankan aplikasi pada http://localhost:5000
python app.py

pause

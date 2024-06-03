import requests


url = "http://localhost:8000/upload/"


file_path = "/Users/putuwistika/Documents/5. Data Engginer/PostgreSQL/mpcn2_nilai/mahasiswa.csv"


with open(file_path, 'rb') as file:
    files = {'file': file}
    response = requests.post(url, files=files)

# Cek status respon
if response.status_code == 200:
    print("File berhasil diunggah")
else:
    print("Gagal mengunggah file:", response.text)

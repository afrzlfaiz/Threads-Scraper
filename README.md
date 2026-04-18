# Threads Scraper

Tool Python untuk mencari postingan di Threads berdasarkan keyword, lalu menyimpan hasilnya ke `JSON`, `CSV`, atau `Excel`.

Project ini memakai request ke endpoint internal Threads, sehingga proses scraping membutuhkan cookie `sessionid` dari akun yang sedang login.

## Fitur

- Pencarian post Threads berdasarkan keyword
- Target jumlah post bisa ditentukan sendiri
- Menghindari duplikasi post berdasarkan ID
- Menyimpan hasil ke format `JSON`, `CSV`, `XLSX`, atau semuanya sekaligus
- Mendukung pencarian beberapa keyword dalam satu sesi
- Tersedia script setup dan start untuk Windows dan Linux/macOS

## Struktur Project

```text
scrape-threads/
|-- threads_scraper.py
|-- requirements.txt
|-- setup.bat
|-- setup.sh
|-- start.bat
|-- start.sh
`-- results/
```

## Requirements

- Python 3.9+
- `pip`
- Koneksi internet
- Cookie `sessionid` dari akun Threads yang aktif login

## Instalasi

### Opsi 1: langsung dengan pip

```bash
pip install -r requirements.txt
```

### Opsi 2: pakai script bawaan

Windows:

```bat
setup.bat
```

Linux/macOS:

```bash
chmod +x setup.sh start.sh
./setup.sh
```

## Cara Menjalankan

Windows:

```bat
start.bat
```

Linux/macOS:

```bash
./start.sh
```

Atau langsung lewat Python:

```bash
python threads_scraper.py
```

## Cara Mengambil `sessionid`

1. Login ke `https://www.threads.com`
2. Buka Developer Tools di browser (`F12`)
3. Masuk ke tab `Application` atau `Storage`
4. Buka bagian `Cookies`
5. Pilih domain `https://www.threads.com`
6. Cari cookie bernama `sessionid`
7. Copy nilainya lalu paste ke program saat diminta

## Alur Penggunaan

Saat program dijalankan, Anda akan diminta:

1. Memasukkan `sessionid`
2. Memasukkan keyword pencarian
3. Menentukan jumlah post yang ingin diambil
4. Memilih format penyimpanan hasil

Contoh:

```text
Masukkan session ID: <sessionid_anda>
Keyword pencarian: saham
Jumlah post yang ingin diambil: 50
Pilihan simpan: 4
```

## Output

File hasil akan disimpan di folder `results/` dengan pola nama:

```text
threads_<keyword>_<jumlah>posts.json
threads_<keyword>_<jumlah>posts.csv
threads_<keyword>_<jumlah>posts.xlsx
```

Contoh:

```text
results/threads_saham_50posts.json
results/threads_saham_50posts.csv
results/threads_saham_50posts.xlsx
```

## Data yang Disimpan

Setiap post umumnya berisi field berikut:

- `id`
- `code`
- `timestamp`
- `date`
- `user.username`
- `user.full_name`
- `user.is_verified`
- `user.profile_pic_url`
- `caption`
- `like_count`
- `reply_count`
- `repost_count`
- `quote_count`
- `url`
- `hashtags`
- `mentions`
- `tag`

## Contoh Format JSON

```json
{
  "id": "3874761242607351150",
  "code": "DXF6tIfD_Vu",
  "date": "2026-04-14 07:45:56",
  "caption": "Contoh isi post",
  "like_count": 271,
  "reply_count": 332,
  "repost_count": 20,
  "quote_count": 0,
  "url": "https://threads.net/@username/post/DXF6tIfD_Vu"
}
```

## Dependencies

Isi `requirements.txt`:

- `requests`
- `pandas`
- `openpyxl`

## Catatan Penting

- Scraper ini bergantung pada endpoint internal Threads yang bisa berubah kapan saja.
- Jika `sessionid` tidak valid atau sudah expired, request bisa gagal atau hasil kosong.
- Tidak semua keyword selalu mengembalikan jumlah post sesuai target.
- Program akan berhenti lebih awal jika tidak menemukan post baru dalam beberapa halaman berturut-turut.
- Gunakan tool ini secara bertanggung jawab dan sesuai ketentuan platform yang berlaku.

## Troubleshooting

### `Python tidak ditemukan`

Pastikan Python sudah terpasang dan bisa diakses dari terminal:

```bash
python --version
```

### Gagal install dependency

Coba upgrade `pip`, lalu install ulang:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Tidak ada hasil pencarian

Periksa hal berikut:

- `sessionid` masih valid
- keyword memang punya hasil di Threads
- koneksi internet stabil
- Threads tidak mengubah endpoint atau format respons

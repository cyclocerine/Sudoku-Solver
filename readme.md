# 🧩 Penyelesai Sudoku

Alat sederhana untuk menyelesaikan teka-teki Sudoku, program ini menggunakan algoritma MRV dan Backtracking yang apabila digabungkan menjadi perpaduan yang powerfull.

## 📝 Apa itu?

Program ini membantu kamu menyelesaikan teka-teki Sudoku dengan cepat. Kamu bisa pakai melalui terminal, aplikasi, atau lewat browser web.

## ✨ Kemampuan

- Nyelesain Sudoku 9x9 dalam sekejap
- Pakai cara pintar buat cari jawaban paling efisien
- Bisa dipakai di terminal, aplikasi desktop, atau browser
- Otomatis mengecek apakah angka-angkanya masuk akal

## 🚀 Cara Pakai

### Lewat Terminal (Command Line)

```bash
# Jalankan programnya
python main.py

# Tinggal ikuti petunjuknya
```

### Lewat Aplikasi Desktop (GUI)

```bash
# Jalankan aplikasi dengan tampilan
python main-gui.py
```

Setelah terbuka:
- Klik kotak mana yang mau diisi, terus ketik angkanya
- Klik tombol "Solve" kalau mau dicarikan jawabannya
- Ada tombol "Clear" buat hapus semua isian
- Tombol "Load" buat ambil soal dari file

### Lewat Browser Web
-Jalankan file main.html

## 📋 Cara Ngisi

### Di Terminal

Tinggal masukkan 9 baris angka, pisahkan pakai spasi. Kalau kosong, isi angka 0:

```
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

### Di Aplikasi Desktop atau Web

- Klik kotak yang mau diisi
- Ketik angkanya dari 1-9 (kotak kosong bisa dibiarin atau diisi 0)

## 💻 Cara Install

### Yang Harus Ada Dulu

- Python 3.X atau lebih baru
- pip (buat install paket lainnya)

### Langkah-Langkahnya

1. Download atau clone repository ini
   ```bash
   git clone https://github.com/username/sudoku-solver.git
   cd sudoku-solver
   ```

2. Install semua yang dibutuhkan
   ```bash
   pip install tkinter
   ```

### Buat Aplikasi Desktop (Tkinter)

Biasanya Tkinter sudah terpasang bareng Python. Kalau belum:

**Windows:**
Harusnya sudah ada waktu install Python.

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install python3-tk
```

**macOS:**
```bash
brew install python-tk
```

### Buat Web (Flask)

```bash
pip install flask
```

## 🔍 Gimana Cara Kerjanya?

### Cara Mencari Jawaban

Program ini kerja dengan cara:
1. Cari kotak yang masih kosong
2. Coba-coba isi pakai angka 1 sampai 9
3. Kalau valid, lanjut ke kotak berikutnya
4. Kalau mentok, balik lagi ke kotak sebelumnya dan coba angka lain

### Teknik Pintar yang Dipakai

Program ini pakai trik khusus:
- Pilih kotak yang pilihannya paling sedikit dulu
- Jadi lebih cepat selesai karena nggak perlu coba-coba terlalu banyak
- Berguna banget buat soal-soal yang susah

## 📂 Isi Foldernya

```
sudoku-solver/
├── main.py             # Program terminal
├── main-gui.py         # Aplikasi desktop
├── main.html           # Aplikasi web
├── static/             # File CSS dan JavaScript
└── README.md           # Petunjuk yang sedang kamu baca
```

## 🤝 Mau Bantu?

Kalau mau bantu pengembangan, boleh banget:
- Lapor kalau ada yang error
- Kasih ide fitur baru
- Kirim perbaikan kode

## 📜 Lisensi

Program ini bebas dipakai sesuai [Lisensi MIT](LICENSE).

---

Dibuat dengan ❤️ oleh cyclocerine

# Bridgestone Employer Branding Insights

Dashboard Next.js App Router, React, TypeScript, Tailwind CSS v4, dan Lucide. Menggunakan 46 respons asli pada sheet `Form Responses 1` dari Employee Branding Survey, 17–21 September 2026.

## Menjalankan lokal

Memerlukan Node.js 20.9 atau lebih baru.

```sh
npm install
npm run dev
```

Buka URL yang ditampilkan terminal. Build produksi: `npm run build`. Hasil static export berada di `out/` dan dapat di-host di server statis. `npm start` tidak digunakan untuk static export.

## Interaksi

- Klik batang, segmen donat, atau legenda untuk memfilter semua chart dan KPI.
- Klik pilihan yang sama lagi untuk menghapus filter tersebut.
- Filter lintas pertanyaan menggunakan kondisi DAN, satu pilihan aktif per pertanyaan.
- Filter status dan tanggal, reset, tab eksplorasi, serta pencarian jawaban terbuka tersedia.
- Kontrol chart berbentuk tombol dan dapat digunakan melalui keyboard. Legenda menyediakan alternatif tombol untuk segmen donat.

## Data dan pembaruan

Data adalah snapshot, tidak tersambung langsung ke Excel. Workbook sumber tidak diubah. Sheet pivot tidak digabung karena merupakan ringkasan dari respons yang sama. Q3/Q4/Q6 dipecah berdasarkan koma menjadi pilihan unik per responden. Persentase = jumlah responden yang memilih / jumlah responden setelah filter. Q5 adalah skor pentingnya gambaran budaya kerja, bukan kepuasan karyawan. Timestamp dipertahankan tanpa mengasumsikan zona waktu tambahan.

Untuk mengganti snapshot dengan workbook berskema sama, pasang Python dan `openpyxl`, lalu:

```sh
python scripts/import-data.py "path/Employee Branding Survey.xlsx"
npm run build
```

Periode tampilan/filter saat ini disesuaikan dengan survei September 2026; perbarui label periode dan batas tanggal di `app/page.tsx` jika workbook baru memakai periode lain. Pertahankan akses privat saat memuat data survei internal. Data dalam static export dapat diakses oleh orang yang memiliki akses ke website.

## Validasi

Build produksi dan pengecekan TypeScript. Verifikasi browser: jumlah 46, filter peserta magang 23, kombinasi status/Instagram, reset, rentang tanggal, kondisi tanpa hasil, filter skor kosong, pencarian teks, dan tidak ada overflow horizontal pada layar 390px.

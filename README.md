# 🇮🇩 Brevet Pajak AB — Virtual Lab

Simulasi perpajakan Indonesia untuk pembelajaran Brevet Pajak A & B. Berisi **105 file PDF** dokumen simulasi, studi kasus, soal, dan kunci jawaban untuk 14 bab.

## Struktur

| Bab | Topik | Dokumen Simulasi |
|-----|-------|------------------|
| 1 | KUP | NPWP, SKPKB, STP, SPT Masa/Tahunan |
| 2 | PPh Orang Pribadi | Slip gaji, bukti potong 1721-A1, SPT 1770S, tabel PTKP |
| 3 | PPh Badan | Laporan laba rugi, rekonsiliasi fiskal, SPT 1771, tarif |
| 4 | PPh 21 | Slip gaji (3 varian), payroll summary, invoice honorarium |
| 5 | PPh 23 | Invoice jasa/royalti/sewa, e-Bupot, tabel tarif |
| 6 | PPh 22 | PIB impor, kuitansi pemerintah, tabel tarif |
| 7 | PPh 26 | Invoice LN, form DGT/SKD, tabel treaty |
| 8 | PPh Final 4(2) | Bukti potong UMKM/sewa/deposito/hadiah/jasa konstruksi |
| 9 | PPN & PPnBM | Faktur pajak (keluaran/masukan), nota retur, SPT 1111 |
| 10 | PBB | SPPT PBB, bukti bayar, tabel NJOP |
| 11 | Bea Meterai | Kuitansi (kena/tidak kena), surat perjanjian, tabel objek |
| 12 | BPHTB | SSPD BPHTB, AJB, tabel NPOPTKP |
| 13 | Coretax | ID Billing, e-Bupot rekap, e-Faktur rekap, bukti SPT elektronik |
| 14 | Studi Kasus Terpadu | Neraca, laba rugi, rekap PPh 21, rekap transaksi pajak |

## Cara Penggunaan

1. Pilih bab yang dipelajari
2. Buka **studi-kasus.pdf** — ada skenario + pertanyaan
3. Buka **soal.pdf** — soal konseptual & aplikasi
4. Gunakan dokumen PDF simulasi sebagai referensi (slip gaji, faktur, invoice, dll)
5. Cek jawaban di **kunci-jawaban.pdf**
6. Script **generate.py** bisa dipakai untuk regenerasi dokumen (custom nama/angka)

## Persyaratan (untuk generate ulang)

```bash
pip install fpdf2
```

```bash
python md2pdf.py <file.md> <output.pdf>
```

## Lisensi

Hak Cipta © 2026. Materi pembelajaran terbuka untuk umum.

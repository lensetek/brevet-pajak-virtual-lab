from fpdf import FPDF
import os

OUT = r'C:\Users\ACER\Documents\GitHub\BrevetAB-VirtualLab\bab-8-pph-final'

class Doc(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 7)
        self.cell(0, 8, f'Simulasi Brevet Pajak AB - Halaman {self.page_no()}/{{nb}}', 0, 0, 'C')

# ========== 8A. BUKTI POTONG UMKM (0,5%) ==========
def bukti_umkm():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 7, 'BUKTI PEMOTONGAN PPh FINAL', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, 'Pasal 4 Ayat (2) - UMKM PP 55/2022', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'IDENTITAS PEMOTONG & PENERIMA', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Pemotong', 'PT Maju Sejahtera Tbk'), ('NPWP', '01.234.567.8-012.000'),
                  ('Penerima', 'CV Karya Mandiri'), ('NPWP', '03.789.012.3-456.000')]:
        pdf.cell(30, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'RINCIAN', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    items = [
        ('Jenis Penghasilan', 'Pembelian Barang/Jasa dari UMKM'),
        ('Omzet Penerima (per tahun)', 'Rp4.800.000.000'),
        ('Dasar Pengenaan Pajak', 'Rp50.000.000'),
        ('Tarif', '0,5%'),
        ('PPh Final 4(2) Dipotong', 'Rp250.000'),
    ]
    for l, v in items:
        pdf.cell(60, 5, f'  {l}', 1)
        pdf.set_font('Helvetica', 'B', 9) if 'PPh Final' in l else pdf.set_font('Helvetica', '', 9)
        pdf.cell(0, 5, f'  {v}', 1, 1, 'R' if 'Rp' in v else 'L')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'I', 8)
    pdf.multi_cell(0, 4, 'Catatan: PPh Final ini tidak dapat dikreditkan. Penerima tidak perlu menggabungkan penghasilan ini di SPT Tahunan (cukup dilaporkan).')
    pdf.output(os.path.join(OUT, 'bukti-potong-final-umkm.pdf'))

# ========== 8B. KUITANSI SEWA BANGUNAN ==========
def kuitansi_sewa():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 7, 'KUITANSI PEMBAYARAN SEWA', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(0, 4, 'PPh Final Pasal 4 Ayat (2) - Sewa Tanah dan/atau Bangunan', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('No. Kuitansi', 'KWT-2026-0088'), ('Tanggal', '15 Januari 2026'),
                  ('Penyewa', 'PT Maju Sejahtera Tbk'), ('NPWP', '01.234.567.8-012.000'),
                  ('Pemilik', 'PT Graha Properti Prima'), ('NPWP', '06.789.012.3-456.000'),
                  ('Objek Sewa', 'Gedung Kantor Lt. 5 - Jl. Merdeka No. 88, Jakarta'),
                  ('Periode Sewa', 'Januari - Desember 2026')]:
        pdf.cell(35, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(140, 6, '  Uraian', 1, 0, 'L', fill=True)
    pdf.cell(0, 6, 'Jumlah (Rp)', 1, 1, 'C', fill=True)
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(140, 5, '    Sewa Gedung - 1 tahun', 1); pdf.cell(0, 5, '120.000.000', 1, 1, 'R')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(140, 5, '    TOTAL SEWA', 1, 0, 'R'); pdf.cell(0, 5, '120.000.000', 1, 1, 'R')
    pdf.ln(1)
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'PPh Final 4(2) dipotong: 10% x Rp120.000.000 = Rp12.000.000', 0, 1)
    pdf.cell(0, 4, 'Diterima pemilik setelah pajak: Rp120.000.000 - Rp12.000.000 = Rp108.000.000', 0, 1)
    pdf.ln(3)
    pdf.cell(80, 4, 'Jakarta, 15 Januari 2026', 0, 1)
    pdf.cell(0, 4, 'PT Graha Properti Prima', 0, 1)
    pdf.ln(8)
    pdf.cell(0, 4, '(_______________________)', 0, 1)
    pdf.output(os.path.join(OUT, 'kuitansi-sewa-bangunan.pdf'))

# ========== 8C. SLIP BUNGA DEPOSITO ==========
def bunga_deposito():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 7, 'BANK NUSANTARA', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(0, 4, 'Jl. Thamrin No. 1, Jakarta 10310', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 6, 'BUKTI PEMBAYARAN BUNGA DEPOSITO', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('No. Referensi', 'DP-2026-001234'), ('Tanggal', '31 Januari 2026'),
                  ('Nasabah', 'PT Maju Sejahtera Tbk'), ('NPWP', '01.234.567.8-012.000'),
                  ('No. Rekening Deposito', '003-01-12345-6'),
                  ('Jenis Deposito', '1 Bulan'), ('Nilai Deposito', 'Rp100.000.000')]:
        pdf.cell(40, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(140, 6, '  Rincian', 1, 0, 'L', fill=True)
    pdf.cell(0, 6, 'Jumlah (Rp)', 1, 1, 'C', fill=True)
    pdf.set_font('Helvetica', '', 9)
    bunga = int(100_000_000 * 0.05 / 12)
    pph = int(bunga * 0.2)
    pdf.cell(140, 5, '    Bunga Deposito (5% p.a. / 12 bulan)', 1); pdf.cell(0, 5, f'{bunga:,}'.replace(',','.'), 1, 1, 'R')
    pdf.cell(140, 5, '    PPh Final 4(2) Dipotong (20%)', 1); pdf.cell(0, 5, f'{pph:,}'.replace(',','.'), 1, 1, 'R')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(140, 5, '    Bunga Diterima Setelah Pajak', 1, 0, 'R')
    pdf.cell(0, 5, f'{bunga-pph:,}'.replace(',','.'), 1, 1, 'R')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.multi_cell(0, 3, 'PPh Final 4(2) atas bunga deposito: 20% x Rp416.667 = Rp83.333. Pajak bersifat final, tidak dapat dikreditkan.')
    pdf.output(os.path.join(OUT, 'bunga-deposito-final.pdf'))

# ========== 8D. KUITANSI HADIAH UNDIAN ==========
def hadiah_undian():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 7, 'PT GAME NUSANTARA', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(0, 4, 'Jl. Gatot Subroto Kav. 20, Jakarta 12950', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 6, 'KUITANSI HADIAH UNDIAN', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'PPh Final Pasal 4(2) - Hadiah Undian', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('No. Referensi', 'UND-2026-0045'), ('Tanggal', '20 Januari 2026'),
                  ('Pemenang', 'Budi Santoso'), ('NPWP', '12.345.678.9-012.000'),
                  ('Jenis Undian', 'Undian Tabungan Berhadiah - Periode 1')]:
        pdf.cell(40, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(140, 6, '  Rincian', 1, 0, 'L', fill=True)
    pdf.cell(0, 6, 'Jumlah (Rp)', 1, 1, 'C', fill=True)
    pdf.set_font('Helvetica', '', 9)
    hadiah = 50_000_000
    pph = int(hadiah * 0.25)
    pdf.cell(140, 5, '    Hadiah Undian Tabungan', 1); pdf.cell(0, 5, f'{hadiah:,}'.replace(',','.'), 1, 1, 'R')
    pdf.cell(140, 5, '    PPh Final 4(2) (25%)', 1); pdf.cell(0, 5, f'{pph:,}'.replace(',','.'), 1, 1, 'R')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(140, 5, '    Diterima Setelah Pajak', 1, 0, 'R')
    pdf.cell(0, 5, f'{hadiah-pph:,}'.replace(',','.'), 1, 1, 'R')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.cell(0, 3, 'PPh Final 25% atas hadiah undian bersifat final.', 0, 1)
    pdf.output(os.path.join(OUT, 'hadiah-undian-final.pdf'))

# ========== 8E. BUKTI POTONG JASA KONSTRUKSI ==========
def jasa_konstruksi():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 7, 'BUKTI PEMOTONGAN PPh FINAL', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, 'Pasal 4 Ayat (2) - Jasa Konstruksi', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'IDENTITAS', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Pemotong', 'PT Maju Sejahtera Tbk'), ('Penerima', 'PT Bangun Karya Konstruksi'),
                  ('NPWP', '01.234.567.8-012.000'), ('NPWP', '07.890.123.4-567.000'),
                  ('Proyek', 'Renovasi Gedung Kantor Lt. 3-4'),
                  ('Nilai Kontrak', 'Rp500.000.000')]:
        pdf.cell(35, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'PERHITUNGAN PPh FINAL', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    items = [
        ('Kualifikasi', 'Sedang (memiliki SBU)'),
        ('Tarif', '3%'),
        ('Dasar Pengenaan', 'Rp500.000.000'),
        ('PPh Final 4(2) Dipotong', 'Rp15.000.000'),
    ]
    for l, v in items:
        pdf.cell(50, 5, f'  {l}', 1)
        pdf.set_font('Helvetica', 'B', 9) if 'PPh' in l else pdf.set_font('Helvetica', '', 9)
        pdf.cell(0, 5, v, 1, 1, 'R' if 'Rp' in v else 'L')
    pdf.output(os.path.join(OUT, 'bukti-potong-jasa-konstruksi.pdf'))

# ========== 8F. TABEL TARIF PPh FINAL ==========
def tabel_final():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 7, 'TABEL TARIF PPh FINAL PASAL 4 AYAT (2)', 0, 1, 'C')
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(0, 51, 102)
    pdf.set_text_color(255)
    pdf.cell(60, 7, 'Objek Pajak', 1, 0, 'C', fill=True)
    pdf.cell(20, 7, 'Tarif', 1, 0, 'C', fill=True)
    pdf.cell(0, 7, 'Dasar Hukum', 1, 1, 'C', fill=True)
    pdf.set_text_color(0)
    data = [
        ('Bunga deposito/tabungan/SBI', '20%', 'PMK 212/2018'),
        ('Bunga obligasi/surat utang negara', '15%', 'PP 16/2009'),
        ('Bunga simpanan koperasi ke anggota', '10%', 'PP 15/2009'),
        ('Hadiah undian', '25%', 'PP 132/2000'),
        ('Transaksi saham di bursa (non-pendiri)', '0,1%', 'PP 14/1997'),
        ('Penjualan saham pendiri', '0,5%', 'PP 14/1997'),
        ('Dividen untuk WP OP', '10%', 'UU PPh'),
        ('Sewa tanah dan/atau bangunan', '10%', 'PP 71/2008'),
        ('Pengalihan tanah/bangunan', '2,5%', 'PP 34/2016'),
        ('Pengalihan RSS/sederhana', '1%', 'PP 34/2016'),
        ('Jasa konstruksi - kecil', '2%', 'PP 9/2022'),
        ('Jasa konstruksi - sedang', '3%', 'PP 9/2022'),
        ('Jasa konstruksi - besar', '4%', 'PP 9/2022'),
        ('UMKM (omzet <= Rp4,8M)', '0,5%', 'PP 55/2022'),
    ]
    pdf.set_font('Helvetica', '', 8)
    for row in data:
        pdf.cell(60, 5, f'  {row[0]}', 1)
        pdf.cell(20, 5, row[1], 1, 0, 'C')
        pdf.cell(0, 5, f'  {row[2]}', 1, 1)
    pdf.output(os.path.join(OUT, 'tabel-tarif-final.pdf'))

if __name__ == '__main__':
    bukti_umkm(); print('OK: bukti-potong-final-umkm.pdf')
    kuitansi_sewa(); print('OK: kuitansi-sewa-bangunan.pdf')
    bunga_deposito(); print('OK: bunga-deposito-final.pdf')
    hadiah_undian(); print('OK: hadiah-undian-final.pdf')
    jasa_konstruksi(); print('OK: bukti-potong-jasa-konstruksi.pdf')
    tabel_final(); print('OK: tabel-tarif-final.pdf')

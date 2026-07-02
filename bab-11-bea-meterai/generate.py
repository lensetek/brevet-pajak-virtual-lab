from fpdf import FPDF
import os

OUT = r'C:\Users\ACER\Documents\GitHub\BrevetAB-VirtualLab\bab-11-bea-meterai'

class Doc(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 7)
        self.cell(0, 8, f'Simulasi Brevet Pajak AB - Halaman {self.page_no()}/{{nb}}', 0, 0, 'C')

# ========== 11A. KUITANSI > Rp5JT (KENA METERAI) ==========
def kuitansi_meterai():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(0, 7, 'PT MAJU SEJAHTERA TBK', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(0, 4, 'Jl. Merdeka No. 88, Jakarta Pusat 10110', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 7, 'KUITANSI', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('No. Kuitansi', 'KWT-2026-0099'), ('Tanggal', '25 Januari 2026'),
                  ('Telah Terima Dari', 'PT Distributor Utama'),
                  ('NPWP', '08.901.234.5-678.000'),
                  ('Sejumlah Uang', 'Rp10.000.000'),
                  ('Terbilang', 'Sepuluh Juta Rupiah'),
                  ('Untuk Pembayaran', 'Pembelian Barang Konsumsi - 100 unit')]:
        pdf.cell(35, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(2)
    # Meterai box
    pdf.set_draw_color(0)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(255, 250, 220)
    pdf.rect(150, pdf.get_y(), 40, 25)
    x = pdf.get_x() + 150
    y = pdf.get_y() + 3
    pdf.set_xy(x, y)
    pdf.cell(40, 4, 'METERAI', 0, 1, 'C')
    pdf.set_xy(x, y+4)
    pdf.cell(40, 4, 'TEMPEL', 0, 1, 'C')
    pdf.set_xy(x, y+8)
    pdf.set_font('Courier', 'B', 10)
    pdf.cell(40, 5, 'Rp10.000', 0, 1, 'C')
    pdf.set_xy(x, y+13)
    pdf.set_font('Helvetica', 'I', 6)
    pdf.cell(40, 3, 'e-Meterai', 0, 1, 'C')
    pdf.set_xy(10, y+25)
    pdf.ln(8)
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(80, 4, 'Jakarta, 25 Januari 2026', 0, 1)
    pdf.ln(8)
    pdf.cell(80, 4, 'PT Maju Sejahtera Tbk', 0, 0)
    pdf.cell(80, 4, 'Penerima,', 0, 1)
    pdf.ln(8)
    pdf.cell(80, 4, '(_______________________)', 0, 0)
    pdf.cell(80, 4, '(_______________________)', 0, 1)
    pdf.output(os.path.join(OUT, 'kuitansi-meterai-10jt.pdf'))

# ========== 11B. KUITANSI < Rp5JT (TIDAK KENA METERAI) ==========
def kuitansi_non_meterai():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(0, 7, 'PT MAJU SEJAHTERA TBK', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(0, 4, 'Jl. Merdeka No. 88, Jakarta Pusat', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 7, 'KUITANSI', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('No. Kuitansi', 'KWT-2026-0033'), ('Tanggal', '10 Januari 2026'),
                  ('Telah Terima Dari', 'PT Maju Sejahtera Tbk'),
                  ('Sejumlah Uang', 'Rp3.000.000'),
                  ('Terbilang', 'Tiga Juta Rupiah'),
                  ('Untuk Pembayaran', 'Biaya Langganan Majalah Bulanan')]:
        pdf.cell(35, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Kuitansi ini tidak terutang Bea Meterai (nilai < Rp5.000.000).', 0, 1)
    pdf.ln(8)
    pdf.cell(0, 4, 'Jakarta, 10 Januari 2026', 0, 1)
    pdf.ln(8)
    pdf.cell(0, 4, '(_______________________)', 0, 1)
    pdf.output(os.path.join(OUT, 'kuitansi-non-meterai-3jt.pdf'))

# ========== 11C. SURAT PERJANJIAN (2 HALAMAN) ==========
def surat_perjanjian():
    pdf = Doc()
    pdf.alias_nb_pages()
    # Halaman 1
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 7, 'SURAT PERJANJIAN SEWA MENYEWA', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, 'No: 001/SP/PTMS/2026', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', '', 9)
    pdf.multi_cell(0, 5, 'Pada hari ini, Senin tanggal 5 Januari 2026, bertempat di Jakarta, yang bertanda tangan di bawah ini:')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 5, 'PIHAK PERTAMA (PENYEWA):', 0, 1)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Nama', 'PT Maju Sejahtera Tbk'), ('NPWP', '01.234.567.8-012.000'),
                  ('Alamat', 'Jl. Merdeka No. 88, Jakarta Pusat')]:
        pdf.cell(25, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 5, 'PIHAK KEDUA (PEMILIK):', 0, 1)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Nama', 'PT Graha Properti Prima'), ('NPWP', '06.789.012.3-456.000'),
                  ('Alamat', 'Jl. Sudirman Kav. 10, Jakarta Selatan')]:
        pdf.cell(25, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 5, 'PASAL 1 - OBJEK SEWA', 0, 1)
    pdf.set_font('Helvetica', '', 9)
    pdf.multi_cell(0, 5, 'Pihak Kedua menyewakan kepada Pihak Pertama gedung perkantoran lt. 5 seluas 200m2 yang berlokasi di Jl. Merdeka No. 88, Jakarta Pusat.')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 5, 'PASAL 2 - JANGKA WAKTU', 0, 1)
    pdf.set_font('Helvetica', '', 9)
    pdf.multi_cell(0, 5, 'Jangka waktu sewa adalah 1 (satu) tahun, terhitung sejak 1 Januari 2026 sampai dengan 31 Desember 2026.')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 5, 'PASAL 3 - NILAI SEWA', 0, 1)
    pdf.set_font('Helvetica', '', 9)
    pdf.multi_cell(0, 5, 'Nilai sewa ditetapkan sebesar Rp120.000.000 (seratus dua puluh juta rupiah) untuk 1 (satu) tahun, dibayar di muka.')
    pdf.ln(2)

    # Halaman 2
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 5, 'PASAL 4 - HAK DAN KEWAJIBAN', 0, 1)
    pdf.set_font('Helvetica', '', 9)
    pdf.multi_cell(0, 5, '1. Pihak Pertama berhak menggunakan objek sewa sesuai peruntukannya.\n2. Pihak Pertama wajib membayar biaya listrik, air, dan telepon selama masa sewa.\n3. Pihak Kedua wajib menjaga keamanan dan kenyamanan lingkungan gedung.')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 5, 'PASAL 5 - LAIN-LAIN', 0, 1)
    pdf.set_font('Helvetica', '', 9)
    pdf.multi_cell(0, 5, 'Segala perubahan dan/atau tambahan atas perjanjian ini akan diatur dalam addendum yang merupakan bagian tidak terpisahkan dari perjanjian ini.')
    pdf.ln(5)
    pdf.cell(80, 5, 'Jakarta, 5 Januari 2026', 0, 1)
    pdf.ln(2)
    pdf.cell(80, 5, 'PIHAK PERTAMA', 0, 0)
    pdf.cell(80, 5, 'PIHAK KEDUA', 0, 1)
    pdf.ln(10)
    pdf.cell(80, 5, '(_______________________)', 0, 0)
    pdf.cell(80, 5, '(_______________________)', 0, 1)
    pdf.output(os.path.join(OUT, 'surat-perjanjian-sewa.pdf'))

# ========== 11D. TABEL OBJEK vs BUKAN OBJEK ==========
def tabel_objek():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 7, 'TABEL OBJEK vs BUKAN OBJEK BEA METERAI', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Berdasarkan UU Bea Meterai No. 10 Tahun 2020', 0, 1, 'C')
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(0, 102, 51)
    pdf.set_text_color(255)
    pdf.cell(90, 7, 'OBJEK BEA METERAI', 1, 0, 'C', fill=True)
    pdf.set_fill_color(153, 0, 0)
    pdf.cell(0, 7, 'BUKAN OBJEK BEA METERAI', 1, 1, 'C', fill=True)
    pdf.set_text_color(0)
    objek = [
        'Surat perjanjian', 'Surat penyimpanan barang (konosemen)',
        'Akta notaris', 'Ijazaah',
        'Akta PPAT', 'Tanda terima gaji/pensiun',
        'Surat berharga', 'Tanda bukti penerimaan uang negara',
        'Dokumen lelang', 'Kuitansi untuk semua jenis pajak',
        'Kuitansi > Rp5jt', 'Tanda penerimaan uang intern organisasi',
        'Dokumen yang menyatakan jumlah uang > Rp5jt', 'Surat gadai',
    ]
    pdf.set_font('Helvetica', '', 8)
    for i in range(0, len(objek), 2):
        pdf.cell(90, 5, f'  {objek[i]}', 1)
        if i+1 < len(objek):
            pdf.cell(0, 5, f'  {objek[i+1]}', 1, 1)
        else:
            pdf.cell(0, 5, '', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 5, f'Tarif Bea Meterai: Rp10.000 per dokumen (berlaku sejak 1 Januari 2021)', 0, 1)
    pdf.output(os.path.join(OUT, 'tabel-objek-meterai.pdf'))

if __name__ == '__main__':
    kuitansi_meterai(); print('OK: kuitansi-meterai-10jt.pdf')
    kuitansi_non_meterai(); print('OK: kuitansi-non-meterai-3jt.pdf')
    surat_perjanjian(); print('OK: surat-perjanjian-sewa.pdf')
    tabel_objek(); print('OK: tabel-objek-meterai.pdf')

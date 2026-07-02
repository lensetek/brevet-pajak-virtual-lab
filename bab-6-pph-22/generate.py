from fpdf import FPDF
import os

OUT = r'C:\Users\ACER\Documents\GitHub\BrevetAB-VirtualLab\bab-6-pph-22'

class Doc(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 7)
        self.cell(0, 8, f'Simulasi Brevet Pajak AB - Halaman {self.page_no()}/{{nb}}', 0, 0, 'C')

# ========== 6A. PIB (PEMBERITAHUAN IMPOR BARANG) ==========
def pib():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 5, 'KEMENTERIAN KEUANGAN RI', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(0, 4, 'DIREKTORAT JENDERAL BEA DAN CUKAI', 0, 1, 'C')
    pdf.set_text_color(0)
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 6, 'PEMBERITAHUAN IMPOR BARANG (PIB)', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'No. PIB: 2026-01-001234', 0, 1, 'R')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'DATA IMPORTIR', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Importir', 'PT Maju Sejahtera Tbk'), ('NPWP', '01.234.567.8-012.000'),
                  ('API', 'API-P / 012345'), ('Pelabuhan', 'Tanjung Priok, Jakarta')]:
        pdf.cell(40, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'RINCIAN BARANG', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    items = [
        ('Kode HS', '8471.30.90'),
        ('Uraian Barang', 'Notebook & Laptop - 100 unit'),
        ('Harga Barang (FOB)', 'USD 350.000'),
        ('Asuransi', 'USD 3.500'),
        ('Ongkos Angkut (Freight)', 'USD 7.500'),
        ('Nilai CIF (FOB + Asuransi + Freight)', 'USD 361.000'),
        ('Kurs Pajak (KMK)', 'Rp15.500/USD'),
        ('Nilai CIF (Rp)', 'Rp5.595.500.000'),
        ('Bea Masuk (7,5%)', 'Rp419.662.500'),
        ('Nilai Impor (CIF + Bea Masuk)', 'Rp6.015.162.500'),
    ]
    for l, v in items:
        pdf.cell(65, 5, f'  {l}', 1)
        pdf.set_font('Helvetica', 'B', 9) if 'CIF (Rp)' in l or 'Nilai Impor' in l else pdf.set_font('Helvetica', '', 9)
        pdf.cell(0, 5, v, 1, 1, 'R')
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'PERHITUNGAN PPh 22', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    pph22 = int(6015162500 * 0.025)
    pdf.cell(65, 5, '  Tarif (dengan API)', 1)
    pdf.cell(0, 5, '2,5%', 1, 1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(65, 5, '  PPh 22 Impor', 1)
    pdf.cell(0, 5, f'Rp{pph22:,}'.replace(',','.'), 1, 1, 'R')
    pdf.ln(1)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.multi_cell(0, 3, 'Catatan: PPh 22 dibayar bersamaan dengan Bea Masuk sebelum barang dikeluarkan dari pelabuhan.')
    pdf.output(os.path.join(OUT, 'pib-impor-pph22.pdf'))

# ========== 6B. KUITANSI PEMBELIAN PEMERINTAH ==========
def kuitansi_pemerintah():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(0, 7, 'BENDARA PENGELUARAN', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, 'KEMENTERIAN PEKERJAAN UMUM DAN PERUMAHAN RAKYAT', 0, 1, 'C')
    pdf.cell(0, 4, 'NPWP: 00.111.222.3-444.000', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 6, 'KUITANSI PEMBAYARAN', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'SPM-LS No. 00456/SPM/2026', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Tanggal', '10 Januari 2026'),
                  ('Kepada', 'PT Maju Sejahtera Tbk'),
                  ('NPWP', '01.234.567.8-012.000'),
                  ('Perihal', 'Pembelian Perangkat Komputer 50 unit')]:
        pdf.cell(35, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(140, 6, '  Uraian', 1, 0, 'L', fill=True)
    pdf.cell(0, 6, 'Jumlah (Rp)', 1, 1, 'C', fill=True)
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(140, 5, '    Pembelian 50 unit PC Workstation', 1)
    pdf.cell(0, 5, '200.000.000', 1, 1, 'R')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(140, 5, '    TOTAL', 1, 0, 'R')
    pdf.cell(0, 5, '200.000.000', 1, 1, 'R')
    pdf.ln(1)
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Pemungutan PPh 22: 1,5% x Rp200.000.000 = Rp3.000.000', 0, 1)
    pdf.cell(0, 4, 'Diterima setelah pemungutan: Rp200.000.000 - Rp3.000.000 = Rp197.000.000', 0, 1)
    pdf.ln(3)
    pdf.cell(80, 4, 'Jakarta, 10 Januari 2026', 0, 1)
    pdf.ln(8)
    pdf.cell(80, 4, 'Bendahara Pengeluaran', 0, 0)
    pdf.cell(80, 4, 'PT Maju Sejahtera Tbk', 0, 1)
    pdf.ln(8)
    pdf.cell(80, 4, '(_______________________)', 0, 0)
    pdf.cell(80, 4, '(_______________________)', 0, 1)
    pdf.output(os.path.join(OUT, 'kuitansi-pemerintah-pph22.pdf'))

# ========== 6C. TABEL TARIF PPh 22 ==========
def tabel_pph22():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 7, 'TABEL TARIF PPh PASAL 22', 0, 1, 'C')
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(0, 51, 102)
    pdf.set_text_color(255)
    pdf.cell(60, 7, 'Transaksi', 1, 0, 'C', fill=True)
    pdf.cell(15, 7, 'Tarif', 1, 0, 'C', fill=True)
    pdf.cell(0, 7, 'Keterangan', 1, 1, 'C', fill=True)
    pdf.set_text_color(0)
    data = [
        ('Impor - dengan API', '2,5%', 'Nilai impor (CIF + bea masuk)'),
        ('Impor - tanpa API', '7,5%', 'Nilai impor'),
        ('Impor - tidak dikuasai', '7,5%', 'Harga jual lelang'),
        ('Pembelian pemerintah pusat/daerah', '1,5%', 'Harga beli (tidak termasuk PPN)'),
        ('Pembelian BUMN', '1,5%', 'Pembelian barang oleh BUMN'),
        ('Penjualan hasil produksi - Semen', '0,25%', 'DPP PPN'),
        ('Penjualan hasil produksi - Kertas', '0,1%', 'DPP PPN'),
        ('Penjualan hasil produksi - Baja', '0,3%', 'DPP PPN'),
        ('Penjualan hasil produksi - Otomotif', '0,45%', 'DPP PPN'),
        ('Penjualan hasil produksi - Farmasi', '0,3%', 'DPP PPN'),
        ('Penjualan BBM (Pertamina ke SPBU)', '0,25%', 'Penjualan tidak termasuk PPN'),
        ('Penjualan migas non-Pertamina', '0,3%', 'Penjualan tidak termasuk PPN'),
        ('Ekspor komoditas tambang', '1,5%', 'Nilai ekspor'),
        ('Penjualan kendaraan bermotor', '0,45%', 'DPP PPN'),
        ('Penjualan barang mewah (rumah > Rp30M)', '1%', 'Harga jual tidak termasuk PPN'),
        ('Penjualan barang mewah (pesawat, yacht)', '5%', 'Harga jual tidak termasuk PPN'),
    ]
    pdf.set_font('Helvetica', '', 8)
    for row in data:
        pdf.cell(60, 5, f'  {row[0]}', 1)
        pdf.cell(15, 5, row[1], 1, 0, 'C')
        pdf.cell(0, 5, f'  {row[2]}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.multi_cell(0, 3, 'Catatan: PPh 22 bersifat tidak final (kredit pajak untuk SPT Tahunan). Kecuali untuk transaksi tertentu yang bersifat final.')
    pdf.output(os.path.join(OUT, 'tabel-tarif-pph22.pdf'))

if __name__ == '__main__':
    pib(); print('OK: pib-impor-pph22.pdf')
    kuitansi_pemerintah(); print('OK: kuitansi-pemerintah-pph22.pdf')
    tabel_pph22(); print('OK: tabel-tarif-pph22.pdf')

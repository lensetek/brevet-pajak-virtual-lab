from fpdf import FPDF
import os

OUT = r'C:\Users\ACER\Documents\GitHub\BrevetAB-VirtualLab\bab-9-ppn'

class Doc(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 7)
        self.cell(0, 8, f'Simulasi Brevet Pajak AB - Halaman {self.page_no()}/{{nb}}', 0, 0, 'C')

# ========== 9A. FAKTUR PAJAK KELUARAN ==========
def fp_keluaran():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 5, 'KEMENTERIAN KEUANGAN RI', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(0, 4, 'DIREKTORAT JENDERAL PAJAK', 0, 1, 'C')
    pdf.set_text_color(0)
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 6, 'FAKTUR PAJAK', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(0, 4, 'Kode & No. Seri Faktur Pajak: 010.000-26.00000001', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'A. PENJUAL (PKP)', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Nama', 'PT Maju Sejahtera Tbk'), ('NPWP', '01.234.567.8-012.000'),
                  ('Alamat', 'Jl. Merdeka No. 88, Jakarta Pusat')]:
        pdf.cell(30, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'B. PEMBELI', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Nama', 'PT Distributor Utama'), ('NPWP', '08.901.234.5-678.000'), ('Alamat', 'Jl. Industri Raya Blok C5, Bekasi')]:
        pdf.cell(30, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'C. RINCIAN TRANSAKSI', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    items = [
        ('Jenis Barang/Jasa', 'Barang Konsumsi - Elektronik'),
        ('Harga Jual (DPP)', 'Rp150.000.000'),
        ('PPN (11%)', 'Rp16.500.000'),
    ]
    for l, v in items:
        pdf.cell(50, 5, f'  {l}', 1)
        pdf.set_font('Helvetica', 'B', 9) if 'PPN' in l else pdf.set_font('Helvetica', '', 9)
        pdf.cell(0, 5, v, 1, 1, 'R' if 'Rp' in v else 'L')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(50, 5, '  TOTAL (Harga + PPN)', 1)
    pdf.cell(0, 5, 'Rp166.500.000', 1, 1, 'R')
    pdf.ln(3)
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(0, 4, 'Jakarta, 10 Januari 2026', 0, 1, 'R')
    pdf.cell(0, 4, 'PT Maju Sejahtera Tbk', 0, 1, 'R')
    pdf.ln(6)
    pdf.cell(0, 4, '(_______________________)', 0, 1, 'R')
    pdf.output(os.path.join(OUT, 'faktur-pajak-keluaran-150jt.pdf'))

# ========== 9B. FAKTUR PAJAK MASUKAN ==========
def fp_masukan():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 5, 'KEMENTERIAN KEUANGAN RI', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(0, 4, 'DIREKTORAT JENDERAL PAJAK', 0, 1, 'C')
    pdf.set_text_color(0)
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 6, 'FAKTUR PAJAK - PAJAK MASUKAN', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(0, 4, 'Kode & No. Seri: 010.000-26.00000002', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'A. PENJUAL', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Nama', 'PT Supplier Abadi'), ('NPWP', '09.012.345.6-789.000')]:
        pdf.cell(30, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'B. PEMBELI (PT Maju Sejahtera Tbk)', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    items = [
        ('NPWP Pembeli', '01.234.567.8-012.000'),
        ('Jenis Barang', 'Bahan Baku Produksi'),
        ('DPP', 'Rp100.000.000'),
        ('PPN (11%)', 'Rp11.000.000'),
    ]
    for l, v in items:
        pdf.cell(50, 5, f'  {l}', 1)
        pdf.set_font('Helvetica', 'B', 9) if 'PPN' in l else pdf.set_font('Helvetica', '', 9)
        pdf.cell(0, 5, v, 1, 1, 'R' if 'Rp' in v else 'L')
    pdf.output(os.path.join(OUT, 'faktur-pajak-masukan-100jt.pdf'))

# ========== 9C. NOTA RETUR ==========
def nota_retur():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 7, 'NOTA RETUR', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(0, 4, 'Pengembalian Barang Kena Pajak', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('No. Nota Retur', 'NR-2026-0001'), ('Tanggal', '15 Januari 2026'),
                  ('Pengembali (Pembeli)', 'PT Maju Sejahtera Tbk'),
                  ('NPWP', '01.234.567.8-012.000'),
                  ('Penjual', 'PT Supplier Abadi'),
                  ('Alasan Retur', 'Barang rusak dalam pengiriman - 10 unit')]:
        pdf.cell(40, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(140, 6, '  Rincian Retur', 1, 0, 'L', fill=True)
    pdf.cell(0, 6, 'Jumlah (Rp)', 1, 1, 'C', fill=True)
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(140, 5, '    Nilai Barang yang Dikembalikan (10 unit @ Rp1.000.000)', 1)
    pdf.cell(0, 5, '10.000.000', 1, 1, 'R')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(140, 5, '    PPN yang Dikembalikan (11%)', 1)
    pdf.cell(0, 5, '1.100.000', 1, 1, 'R')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(140, 5, '    TOTAL', 1, 0, 'R')
    pdf.cell(0, 5, '11.100.000', 1, 1, 'R')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.multi_cell(0, 3, 'Nota Retur ini mengurangi Pajak Masukan Pembeli dan Pajak Keluaran Penjual pada masa pajak terjadinya retur.')
    pdf.output(os.path.join(OUT, 'nota-retur.pdf'))

# ========== 9D. SPT MASA PPN 1111 ==========
def spt_ppn():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 5, 'KEMENTERIAN KEUANGAN RI', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(0, 4, 'DIREKTORAT JENDERAL PAJAK', 0, 1, 'C')
    pdf.set_text_color(0)
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 6, 'SPT MASA PPN 1111 - JANUARI 2026', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'IDENTITAS PKP', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Nama PKP', 'PT Maju Sejahtera Tbk'), ('NPWP', '01.234.567.8-012.000'),
                  ('Masa Pajak', 'Januari 2026')]:
        pdf.cell(35, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'RINCIAN PPN', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    items = [
        ('I. PAJAK KELUARAN', ''),
        ('   A. Penyerahan kena PPN (DPP Rp150jt)', 'Rp16.500.000'),
        ('   B. Ekspor BKP Berwujud', 'Rp0'),
        ('   Jumlah Pajak Keluaran', 'Rp16.500.000'),
        ('', ''),
        ('II. PAJAK MASUKAN', ''),
        ('   A. PM atas perolehan BKP/JKP (DPP Rp100jt)', 'Rp11.000.000'),
        ('   B. PM atas impor BKP', 'Rp0'),
        ('   Jumlah Pajak Masukan (dapat dikreditkan)', 'Rp11.000.000'),
        ('', ''),
        ('III. PPN LEBIH/(KURANG) BAYAR', ''),
        ('   PPN = PK - PM', 'Rp5.500.000'),
    ]
    for l, v in items:
        if not l:
            pdf.ln(1); continue
        is_b = 'Jumlah Pajak' in l or 'PPN =' in l or 'III.' in l
        pdf.set_font('Helvetica', 'B' if is_b else '', 9)
        pdf.cell(130, 5, f'  {l}', 1)
        align = 'R' if v and 'Rp' in v else 'L'
        pdf.cell(0, 5, v, 1, 1, align)

    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(255, 230, 230)
    pdf.cell(0, 6, 'STATUS: LEBIH SETOR (KURANG BAYAR) Rp5.500.000', 1, 1, 'C', fill=True)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.multi_cell(0, 3, 'Catatan: PK > PM, sehingga PKP menyetorkan selisih ke kas negara.')
    pdf.output(os.path.join(OUT, 'spt-masa-ppn-1111-januari.pdf'))

# ========== 9E. CONTOH PERHITUNGAN PPnBM ==========
def ppnbm_mobil():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 7, 'CONTOH PERHITUNGAN PPnBM', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, 'Pajak Penjualan atas Barang Mewah', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Produsen', 'PT Mobil Mewah Indonesia'), ('NPWP', '07.654.321.0-987.000'),
                  ('Jenis Kendaraan', 'SUV 3.000cc - Kalangan Atas'),
                  ('Harga Jual (DPP PPN)', 'Rp800.000.000')]:
        pdf.cell(40, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(130, 6, '  Rincian', 1, 0, 'L', fill=True)
    pdf.cell(0, 6, 'Jumlah (Rp)', 1, 1, 'C', fill=True)
    pdf.set_font('Helvetica', '', 9)
    dpp = 800_000_000
    ppn = int(dpp * 0.11)
    ppnbm = int(dpp * 0.30)  # 30%
    total = dpp + ppn + ppnbm
    pdf.cell(130, 5, '    Dasar Pengenaan Pajak (Harga Jual)', 1); pdf.cell(0, 5, f'{dpp:,}'.replace(',','.'), 1, 1, 'R')
    pdf.cell(130, 5, '    PPN 11%', 1); pdf.cell(0, 5, f'{ppn:,}'.replace(',','.'), 1, 1, 'R')
    pdf.cell(130, 5, '    PPnBM 30% (dibayar sekali oleh produsen)', 1); pdf.cell(0, 5, f'{ppnbm:,}'.replace(',','.'), 1, 1, 'R')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(130, 5, '    TOTAL HARGA (DPP + PPN + PPnBM)', 1, 0, 'R'); pdf.cell(0, 5, f'{total:,}'.replace(',','.'), 1, 1, 'R')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.multi_cell(0, 3, 'PPnBM hanya dipungut sekali pada saat penyerahan dari produsen ke distributor. Tidak dapat dikreditkan seperti PPN.')
    pdf.output(os.path.join(OUT, 'contoh-ppnbm-mobil-mewah.pdf'))

if __name__ == '__main__':
    fp_keluaran(); print('OK: faktur-pajak-keluaran-150jt.pdf')
    fp_masukan(); print('OK: faktur-pajak-masukan-100jt.pdf')
    nota_retur(); print('OK: nota-retur.pdf')
    spt_ppn(); print('OK: spt-masa-ppn-1111-januari.pdf')
    ppnbm_mobil(); print('OK: contoh-ppnbm-mobil-mewah.pdf')

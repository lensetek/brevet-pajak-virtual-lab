from fpdf import FPDF
import os

OUT = r'C:\Users\ACER\Documents\GitHub\BrevetAB-VirtualLab\bab-5-pph-23'

class Doc(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 7)
        self.cell(0, 8, f'Simulasi Brevet Pajak AB - Halaman {self.page_no()}/{{nb}}', 0, 0, 'C')

# ========== 5A. INVOICE JASA KONSULTAN ==========
def invoice_jasa():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 7, 'CV KONSULTINDO UTAMA', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, 'Jl. Sudirman No. 55, Jakarta Selatan 12190', 0, 1, 'C')
    pdf.cell(0, 4, 'NPWP: 03.456.789.0-012.000', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 6, 'INVOICE', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('No. Invoice', 'INV-2026-0088'), ('Tanggal', '15 Januari 2026'),
                  ('Kepada', 'PT Maju Sejahtera Tbk'), ('NPWP', '01.234.567.8-012.000'),
                  ('Perihal', 'Jasa Konsultasi Manajemen - Jan 2026')]:
        pdf.cell(40, 5, f'  {l}', 1)
        pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(140, 6, '  Uraian', 1, 0, 'L', fill=True)
    pdf.cell(0, 6, 'Jumlah (Rp)', 1, 1, 'C', fill=True)
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(140, 5, '    Jasa Konsultasi Manajemen - Bulan Januari 2026', 1)
    pdf.cell(0, 5, '200.000.000', 1, 1, 'R')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(140, 5, '    TOTAL', 1, 0, 'R')
    pdf.cell(0, 5, '200.000.000', 1, 1, 'R')
    pdf.ln(1)
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'PPh 23 yang dipotong: 2% x Rp200.000.000 = Rp4.000.000', 0, 1)
    pdf.cell(0, 4, 'Diterima setelah pajak: Rp200.000.000 - Rp4.000.000 = Rp196.000.000', 0, 1)
    pdf.ln(3)
    pdf.cell(80, 4, 'Jakarta, 15 Januari 2026', 0, 1)
    pdf.ln(8)
    pdf.cell(80, 4, 'CV Konsultindo Utama', 0, 0)
    pdf.cell(80, 4, 'Penerima,', 0, 1)
    pdf.ln(8)
    pdf.cell(80, 4, '(_______________________)', 0, 0)
    pdf.output(os.path.join(OUT, 'invoice-jasa-konsultan-200jt.pdf'))

# ========== 5B. INVOICE ROYALTI ==========
def invoice_royalti():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 7, 'PT CIPTA KARYA INOVASI', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, 'Jl. Gatot Subroto Kav. 72, Bandung 40200', 0, 1, 'C')
    pdf.cell(0, 4, 'NPWP: 04.567.890.1-234.000', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 6, 'INVOICE - ROYALTI', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('No. Invoice', 'ROY-2026-0012'), ('Tanggal', '20 Januari 2026'),
                  ('Kepada', 'PT Maju Sejahtera Tbk'), ('NPWP', '01.234.567.8-012.000'),
                  ('Perihal', 'Royalti Lisensi Software Akuntansi')]:
        pdf.cell(40, 5, f'  {l}', 1)
        pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(140, 6, '  Uraian', 1, 0, 'L', fill=True)
    pdf.cell(0, 6, 'Jumlah (Rp)', 1, 1, 'C', fill=True)
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(140, 5, '    Royalti Lisensi Software - Periode Jan 2026', 1)
    pdf.cell(0, 5, '80.000.000', 1, 1, 'R')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(140, 5, '    TOTAL', 1, 0, 'R')
    pdf.cell(0, 5, '80.000.000', 1, 1, 'R')
    pdf.ln(1)
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'PPh 23 yang dipotong: 15% x Rp80.000.000 = Rp12.000.000', 0, 1)
    pdf.cell(0, 4, 'Diterima setelah pajak: Rp80.000.000 - Rp12.000.000 = Rp68.000.000', 0, 1)
    pdf.ln(3)
    pdf.cell(80, 4, 'Bandung, 20 Januari 2026', 0, 1)
    pdf.ln(8)
    pdf.cell(80, 4, 'PT Cipta Karya Inovasi', 0, 0)
    pdf.cell(80, 4, 'Penerima,', 0, 1)
    pdf.ln(8)
    pdf.cell(80, 4, '(_______________________)', 0, 0)
    pdf.output(os.path.join(OUT, 'invoice-royalti-80jt.pdf'))

# ========== 5C. INVOICE SEWA ALAT BERAT ==========
def invoice_sewa():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 7, 'PT ALAT BERAT NUSANTARA', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, 'Jl. Industri Raya Blok B5, Surabaya 60100', 0, 1, 'C')
    pdf.cell(0, 4, 'NPWP: 05.678.901.2-345.000', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 6, 'INVOICE - SEWA ALAT BERAT', 0, 1, 'C')
    pdf.ln(2)
    for l, v in [('No. Invoice', 'SEWA-2026-0034'), ('Tanggal', '25 Januari 2026'),
                  ('Kepada', 'PT Maju Sejahtera Tbk'), ('Perihal', 'Sewa Excavator - 30 Hari')]:
        pdf.cell(40, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(140, 6, '  Uraian', 1, 0, 'L', fill=True)
    pdf.cell(0, 6, 'Jumlah (Rp)', 1, 1, 'C', fill=True)
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(140, 5, '    Sewa Excavator Caterpillar - 30 hari @ Rp1.500.000', 1)
    pdf.cell(0, 5, '45.000.000', 1, 1, 'R')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(140, 5, '    TOTAL', 1, 0, 'R')
    pdf.cell(0, 5, '45.000.000', 1, 1, 'R')
    pdf.ln(1)
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'PPh 23 yang dipotong: 2% x Rp45.000.000 = Rp900.000', 0, 1)
    pdf.ln(3)
    pdf.cell(80, 4, 'Surabaya, 25 Januari 2026', 0, 1)
    pdf.ln(8)
    pdf.cell(80, 4, 'PT Alat Berat Nusantara', 0, 0)
    pdf.cell(80, 4, 'Penerima,', 0, 1)
    pdf.ln(8)
    pdf.cell(80, 4, '(_______________________)', 0, 0)
    pdf.output(os.path.join(OUT, 'invoice-sewa-alat-45jt.pdf'))

# ========== 5D. BUKTI POTONG PPh 23 (e-Bupot) ==========
def bukti_potong():
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
    pdf.cell(0, 6, 'BUKTI PEMOTONGAN PPh PASAL 23', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'e-Bupot - Masa Pajak Januari 2026', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'A. IDENTITAS PEMOTONG', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Nama', 'PT Maju Sejahtera Tbk'), ('NPWP', '01.234.567.8-012.000')]:
        pdf.cell(40, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'B. IDENTITAS PENERIMA PENGHASILAN', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Nama', 'CV Konsultindo Utama'), ('NPWP', '03.456.789.0-012.000')]:
        pdf.cell(40, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'C. RINCIAN PEMOTONGAN', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    items = [
        ('Jenis Penghasilan', 'Jasa Konsultasi Manajemen'),
        ('Dasar Pengenaan Pajak (DPP)', 'Rp200.000.000'),
        ('Tarif', '2%'),
        ('PPh 23 Dipotong', 'Rp4.000.000'),
        ('Kode Kode Objek Pajak', '24-104-01'),
        ('Masa Pajak', 'Januari 2026'),
    ]
    for l, v in items:
        pdf.cell(60, 5, f'  {l}', 1)
        pdf.set_font('Helvetica', 'B', 9) if 'PPh 23' in l else pdf.set_font('Helvetica', '', 9)
        pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(3)
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(0, 4, 'Jakarta, 31 Januari 2026', 0, 1, 'R')
    pdf.cell(0, 4, 'PT Maju Sejahtera Tbk', 0, 1, 'R')
    pdf.ln(6)
    pdf.cell(0, 4, '(_______________________)', 0, 1, 'R')
    pdf.output(os.path.join(OUT, 'bukti-potong-pph23-e-bupot.pdf'))

# ========== 5E. TABEL TARIF & PENGECUALIAN ==========
def tabel_pph23():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 7, 'TABEL TARIF PPh PASAL 23', 0, 1, 'C')
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(0, 51, 102)
    pdf.set_text_color(255)
    pdf.cell(55, 7, 'Jenis Penghasilan', 1, 0, 'C', fill=True)
    pdf.cell(25, 7, 'Tarif', 1, 0, 'C', fill=True)
    pdf.cell(0, 7, 'Keterangan', 1, 1, 'C', fill=True)
    pdf.set_text_color(0)
    data = [
        ('Dividen', '15%', 'Kecuali OP (final)'),
        ('Bunga', '15%', 'Semua bunga pinjaman'),
        ('Royalti', '15%', 'Penggunaan hak cipta/paten'),
        ('Hadiah & Penghargaan', '15%', 'Selain yg sdh dipotong PPh 21'),
        ('Sewa harta (non-tanah)', '2%', 'Sewa alat, kendaraan, dll'),
        ('Jasa Teknik', '2%', 'Jasa perencanaan/pengawasan'),
        ('Jasa Manajemen', '2%', 'Jasa pengelolaan'),
        ('Jasa Konsultan', '2%', 'Konsultan hukum, pajak, manajemen'),
        ('Jasa Lain (PMK 141/2015)', '2%', '26 jenis jasa lainnya'),
        ('Fintech Dalam Negeri', '15%', 'PMK 69/2022'),
        ('Fintech Luar Negeri', '20%', 'PMK 69/2022'),
    ]
    pdf.set_font('Helvetica', '', 9)
    for row in data:
        pdf.cell(55, 6, f'  {row[0]}', 1)
        pdf.cell(25, 6, row[1], 1, 0, 'C')
        pdf.cell(0, 6, f'  {row[2]}', 1, 1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 5, 'PENGECUALIAN (TIDAK DIKENAKAN PPh 23):', 0, 1)
    pdf.set_font('Helvetica', '', 8)
    kecuali = [
        'Pembayaran kepada bank',
        'Sewa guna usaha (leasing) dengan hak opsi',
        'Dividen saham dengan kepemilikan >= 25% dari laba ditahan',
        'SHU koperasi kepada anggotanya',
        'Pembayaran jasa keuangan (penyalur pinjaman)',
    ]
    for k in kecuali:
        pdf.cell(5, 4, '', 0)
        pdf.cell(0, 4, f'- {k}', 0, 1)
    pdf.output(os.path.join(OUT, 'tabel-tarif-pph23.pdf'))

if __name__ == '__main__':
    invoice_jasa(); print('OK: invoice-jasa-konsultan-200jt.pdf')
    invoice_royalti(); print('OK: invoice-royalti-80jt.pdf')
    invoice_sewa(); print('OK: invoice-sewa-alat-45jt.pdf')
    bukti_potong(); print('OK: bukti-potong-pph23-e-bupot.pdf')
    tabel_pph23(); print('OK: tabel-tarif-pph23.pdf')

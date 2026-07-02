from fpdf import FPDF
import os

OUT = r'C:\Users\ACER\Documents\GitHub\BrevetAB-VirtualLab\bab-12-bphtb'

class Doc(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 7)
        self.cell(0, 8, f'Simulasi Brevet Pajak AB - Halaman {self.page_no()}/{{nb}}', 0, 0, 'C')

# ========== 12A. SSPD BPHTB ==========
def sspd_bphtb():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 5, 'PEMERINTAH PROVINSI DKI JAKARTA', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(0, 4, 'BADAN PENDAPATAN DAERAH', 0, 1, 'C')
    pdf.set_text_color(0)
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 6, 'SURAT SETORAN PAJAK DAERAH (SSPD)', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'BEA PEROLEHAN HAK ATAS TANAH DAN BANGUNAN', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'A. IDENTITAS WAJIB PAJAK', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Nama', 'Budi Santoso'), ('NPWP/NIK', '12.345.678.9-012.000'),
                  ('Alamat', 'Jl. Merdeka No. 45, Jakarta Pusat')]:
        pdf.cell(35, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'B. OBJEK PBB', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Letak Tanah/Bangunan', 'Jl. Merdeka No. 45, Jakarta Pusat'),
                  ('Luas Tanah', '200 m2'), ('Luas Bangunan', '150 m2'),
                  ('NPOP (Nilai Perolehan Objek Pajak)', 'Rp500.000.000'),
                  ('NPOPTKP', 'Rp60.000.000')]:
        pdf.cell(45, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'C. PERHITUNGAN BPHTB', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    npop = 500_000_000
    npoptkp = 60_000_000
    pkp_bphtb = npop - npoptkp
    bphtb = int(pkp_bphtb * 0.05)
    items = [
        ('NPOP', 'Rp500.000.000'),
        ('NPOPTKP', '(Rp60.000.000)'),
        ('NPOP Kena Pajak (NPOP - NPOPTKP)', f'Rp{pkp_bphtb:,}'.replace(',','.')),
        ('Tarif BPHTB', '5%'),
        ('BPHTB TERUTANG', f'Rp{bphtb:,}'.replace(',','.')),
    ]
    for d, v in items:
        is_b = 'TERUTANG' in d or 'NPOP Kena' in d
        pdf.set_font('Helvetica', 'B' if is_b else '', 9)
        pdf.cell(80, 5, f'  {d}', 1)
        pdf.cell(0, 5, v, 1, 1, 'R')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.multi_cell(0, 3, 'BPHTB harus dibayar sebelum akta jual beli ditandatangani di hadapan PPAT/Notaris.')
    pdf.output(os.path.join(OUT, 'sspd-bphtb.pdf'))

# ========== 12B. AJB (AKTA JUAL BELI) KUTIPAN ==========
def ajb():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 6, 'AKTA JUAL BELI (AJB)', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Kutipan - PPAT Budi Santoso, SH', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(2)
    pdf.set_font('Helvetica', '', 9)
    pdf.multi_cell(0, 5, 'Pada hari ini, Senin tanggal 15 Januari 2026, telah dilakukan perjanjian jual beli tanah dan bangunan antara:')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 5, 'PIHAK PERTAMA (PENJUAL):', 0, 1)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Nama', 'PT Graha Properti Prima'), ('NPWP', '06.789.012.3-456.000')]:
        pdf.cell(25, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 5, 'PIHAK KEDUA (PEMBELI):', 0, 1)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Nama', 'Budi Santoso'), ('NPWP', '12.345.678.9-012.000')]:
        pdf.cell(25, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 5, 'OBJEK JUAL BELI:', 0, 1)
    pdf.set_font('Helvetica', '', 9)
    items_obj = [
        'Sebidang tanah seluas 200 m2, Sertifikat Hak Milik No. 12345',
        'Bangunan rumah tinggal seluas 150 m2',
        'Berlokasi di Jl. Merdeka No. 45, RT 005 RW 003, Kelurahan Menteng',
        'Kecamatan Menteng, Jakarta Pusat',
    ]
    for it in items_obj:
        pdf.cell(5, 4, '', 0); pdf.cell(0, 4, f'- {it}', 0, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 5, 'HARGA JUAL:', 0, 1)
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 5, 'Nilai transaksi sebesar Rp500.000.000 (lima ratus juta rupiah) yang telah dibayar lunas oleh Pihak Kedua kepada Pihak Pertama.', 0, 1)
    pdf.ln(5)
    pdf.cell(80, 4, 'Jakarta, 15 Januari 2026', 0, 1)
    pdf.ln(2)
    pdf.cell(80, 4, 'PIHAK PERTAMA', 0, 0)
    pdf.cell(80, 4, 'PIHAK KEDUA', 0, 1)
    pdf.ln(8)
    pdf.cell(80, 4, '(_______________________)', 0, 0)
    pdf.cell(80, 4, '(Budi Santoso)', 0, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.cell(0, 3, 'Diketahui oleh PPAT: Budi Santoso, SH', 0, 1)
    pdf.output(os.path.join(OUT, 'ajb-kutipan.pdf'))

# ========== 12C. TABEL NPOPTKP ==========
def tabel_npoptkp():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 7, 'TABEL NPOPTKP PER DAERAH (CONTOH)', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Berdasarkan UU PDRD No. 28/2009 dan Perda masing-masing', 0, 1, 'C')
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(0, 51, 102)
    pdf.set_text_color(255)
    pdf.cell(50, 7, 'Daerah', 1, 0, 'C', fill=True)
    pdf.cell(40, 7, 'NPOPTKP', 1, 0, 'C', fill=True)
    pdf.cell(0, 7, 'Keterangan', 1, 1, 'C', fill=True)
    pdf.set_text_color(0)
    data = [
        ('DKI Jakarta', 'Rp80.000.000', 'Perda No. 18/2010'),
        ('Jawa Barat', 'Rp60.000.000', 'Minimal sesuai UU PDRD'),
        ('Jawa Timur', 'Rp70.000.000', 'Kota Surabaya'),
        ('Jawa Tengah', 'Rp60.000.000', 'Minimal'),
        ('Warisan/Hibah Wasiat', 'Rp300.000.000', 'Minimal, untuk OP'),
    ]
    pdf.set_font('Helvetica', '', 9)
    for row in data:
        pdf.cell(50, 6, f'  {row[0]}', 1)
        pdf.cell(40, 6, row[1], 1, 0, 'R')
        pdf.cell(0, 6, f'  {row[2]}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.multi_cell(0, 3, 'NPOPTKP hanya diberikan 1 kali per tahun pajak untuk NJOP terbesar jika memiliki lebih dari 1 objek.')
    pdf.output(os.path.join(OUT, 'tabel-npoptkp.pdf'))

if __name__ == '__main__':
    sspd_bphtb(); print('OK: sspd-bphtb.pdf')
    ajb(); print('OK: ajb-kutipan.pdf')
    tabel_npoptkp(); print('OK: tabel-npoptkp.pdf')

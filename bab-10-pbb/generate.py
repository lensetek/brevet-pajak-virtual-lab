from fpdf import FPDF
import os

OUT = r'C:\Users\ACER\Documents\GitHub\BrevetAB-VirtualLab\bab-10-pbb'

class Doc(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 7)
        self.cell(0, 8, f'Simulasi Brevet Pajak AB - Halaman {self.page_no()}/{{nb}}', 0, 0, 'C')

# ========== 10A. SPPT PBB ==========
def sppt_pbb():
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
    pdf.cell(0, 6, 'SURAT PEMBERITAHUAN PAJAK TERUTANG (SPPT)', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'PAJAK BUMI DAN BANGUNAN - TAHUN 2025', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'IDENTITAS WAJIB PAJAK', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Nama WP', 'PT Maju Sejahtera Tbk'), ('NPWP', '01.234.567.8-012.000'),
                  ('Alamat', 'Jl. Merdeka No. 88, Jakarta Pusat 10110')]:
        pdf.cell(35, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'OBJEK PAJAK', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Letak Objek', 'Jl. Merdeka No. 88, Jakarta Pusat'),
                  ('Luas Bumi', '500 m2'), ('Luas Bangunan', '400 m2'),
                  ('NJOP Bumi', 'Rp2.500.000/m2'), ('NJOP Bangunan', 'Rp1.500.000/m2')]:
        pdf.cell(45, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'PERHITUNGAN PBB', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    njop_bumi = 500 * 2500000   # 1.25M
    njop_bgn = 400 * 1500000    # 600jt
    njop = njop_bumi + njop_bgn
    njoptkp = 12000000
    njkp_dasar = njop - njoptkp
    njkp = int(njkp_dasar * 0.2)
    pbb = int(njkp * 0.001)
    items = [
        ('NJOP Bumi (500 m2 x Rp2.500.000)', f'Rp{njop_bumi:,}'.replace(',','.')),
        ('NJOP Bangunan (400 m2 x Rp1.500.000)', f'Rp{njop_bgn:,}'.replace(',','.')),
        ('Total NJOP', f'Rp{njop:,}'.replace(',','.')),
        ('NJOPTKP (Nilai Jual Tidak Kena Pajak)', f'Rp{njoptkp:,}'.replace(',','.')),
        ('NJOP untuk Perhitungan PBB', f'Rp{njkp_dasar:,}'.replace(',','.')),
        ('NJKP (20% x NJOP)', f'Rp{njkp:,}'.replace(',','.')),
        ('Tarif PBB', '0,1%'),
        ('PBB TERUTANG', f'Rp{pbb:,}'.replace(',','.')),
    ]
    for d, v in items:
        is_b = 'TERUTANG' in d or 'Total NJOP' in d
        pdf.set_font('Helvetica', 'B' if is_b else '', 9)
        pdf.cell(95, 5, f'  {d}', 1)
        pdf.cell(0, 5, v, 1, 1, 'R')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.multi_cell(0, 3, 'PBB terutang harus dibayar paling lambat 6 bulan sejak SPPT diterima.')
    pdf.output(os.path.join(OUT, 'sppt-pbb.pdf'))

# ========== 10B. BUKTI BAYAR PBB ==========
def bukti_bayar_pbb():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 7, 'BUKTI PEMBAYARAN PBB', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, 'Surat Setoran Pajak (SSP) PBB', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('NTPN', 'ABCD123456789012'), ('Tanggal Bayar', '15 Maret 2026'),
                  ('Masa Pajak', 'Tahun 2025'), ('Jumlah Bayar', 'Rp97.600'),
                  ('Bank/Pos Persepsi', 'Bank Nusantara - Cabang Jakarta')]:
        pdf.cell(40, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.cell(0, 3, 'Bukti bayar ini sah setelah diverifikasi oleh sistem DJP.', 0, 1)
    pdf.output(os.path.join(OUT, 'bukti-bayar-pbb.pdf'))

# ========== 10C. TABEL NJOP ZONA ==========
def tabel_njop():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 7, 'TABEL NJOP ZONA - JAKARTA PUSAT', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Contoh Nilai Jual Objek Pajak per Zona Tahun 2025', 0, 1, 'C')
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(0, 51, 102)
    pdf.set_text_color(255)
    pdf.cell(50, 7, 'Zona/Kelurahan', 1, 0, 'C', fill=True)
    pdf.cell(40, 7, 'NJOP Bumi/m2', 1, 0, 'C', fill=True)
    pdf.cell(40, 7, 'NJOP Bangunan/m2', 1, 0, 'C', fill=True)
    pdf.cell(0, 7, 'Contoh Objek', 1, 1, 'C', fill=True)
    pdf.set_text_color(0)
    data = [
        ('Menteng', 'Rp5.000.000', 'Rp3.000.000', 'Kantor, ruko mewah'),
        ('Tanah Abang', 'Rp3.500.000', 'Rp2.500.000', 'Ruko, apartemen'),
        ('Senen', 'Rp2.500.000', 'Rp1.500.000', 'Kantor, ruko'),
        ('Cempaka Putih', 'Rp2.000.000', 'Rp1.200.000', 'Rumah tinggal'),
        ('Johar Baru', 'Rp1.500.000', 'Rp1.000.000', 'Rumah, toko kecil'),
    ]
    pdf.set_font('Helvetica', '', 9)
    for row in data:
        pdf.cell(50, 6, f'  {row[0]}', 1)
        pdf.cell(40, 6, row[1], 1, 0, 'R')
        pdf.cell(40, 6, row[2], 1, 0, 'R')
        pdf.cell(0, 6, f'  {row[3]}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.multi_cell(0, 3, 'Catatan: NJOP dapat berbeda antar wilayah. Semakin strategis lokasi, semakin tinggi NJOP.')
    pdf.output(os.path.join(OUT, 'tabel-njop-zona.pdf'))

if __name__ == '__main__':
    sppt_pbb(); print('OK: sppt-pbb.pdf')
    bukti_bayar_pbb(); print('OK: bukti-bayar-pbb.pdf')
    tabel_njop(); print('OK: tabel-njop-zona.pdf')

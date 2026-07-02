from fpdf import FPDF
import os

OUT = r'C:\Users\ACER\Documents\GitHub\BrevetAB-VirtualLab\bab-2-pph-op'

class Doc(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 7)
        self.cell(0, 8, f'Simulasi Brevet Pajak AB - Halaman {self.page_no()}/{{nb}}', 0, 0, 'C')

# ========== 2A. SLIP GAJI TK/0 ==========
def slip_gaji_tk0():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(0, 7, 'PT MAJU SEJAHTERA TBK', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, 'Jl. Merdeka No. 88, Jakarta Pusat', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 7, 'SLIP GAJI KARYAWAN', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Periode: Januari 2026', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Nama', 'Siti Nurhaliza'), ('NPWP', '98.765.432.1-012.000'),
                  ('Jabatan', 'Staff Keuangan'), ('Status', 'TK/0'), ('ID', 'EMP-2025-0033')]:
        pdf.cell(35, 5, f'  {l}', 1)
        pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(120, 6, '  PENERIMAAN', 1, 0, 'L', fill=True)
    pdf.cell(30, 6, 'Rp', 1, 0, 'C', fill=True)
    pdf.cell(0, 6, 'Jumlah', 1, 1, 'C', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for d, v in [('Gaji Pokok', '4.500.000'), ('Tunjangan Transport', '300.000'), ('Tunjangan Makan', '250.000')]:
        pdf.cell(120, 5, f'    {d}', 1)
        pdf.cell(30, 5, '', 1)
        pdf.cell(0, 5, v, 1, 1, 'R')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(120, 5, '    TOTAL PENERIMAAN', 1, 0, 'R')
    pdf.cell(30, 5, '', 1)
    pdf.cell(0, 5, '5.050.000', 1, 1, 'R')
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(120, 6, '  POTONGAN', 1, 0, 'L', fill=True)
    pdf.cell(30, 6, 'Rp', 1, 0, 'C', fill=True)
    pdf.cell(0, 6, 'Jumlah', 1, 1, 'C', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for d, v in [('BPJS Ketenagakerjaan', '60.000'), ('BPJS Kesehatan', '45.000'), ('PPh Pasal 21', '23.750')]:
        pdf.cell(120, 5, f'    {d}', 1)
        pdf.cell(30, 5, '', 1)
        pdf.cell(0, 5, v, 1, 1, 'R')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(120, 5, '    TOTAL POTONGAN', 1, 0, 'R')
    pdf.cell(30, 5, '', 1)
    pdf.cell(0, 5, '128.750', 1, 1, 'R')
    pdf.ln(2)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(150, 7, 'TAKE HOME PAY', 0, 0, 'R')
    pdf.cell(0, 7, 'Rp 4.921.250', 0, 1, 'R')
    pdf.output(os.path.join(OUT, 'slip-gaji-siti-tk0.pdf'))

# ========== 2B. SLIP GAJI K/2 ==========
def slip_gaji_k2():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(0, 7, 'PT MAJU SEJAHTERA TBK', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, 'Jl. Merdeka No. 88, Jakarta Pusat', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 7, 'SLIP GAJI KARYAWAN', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Periode: Januari 2026', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Nama', 'Doni Prasetyo'), ('NPWP', '45.678.901.2-012.000'),
                  ('Jabatan', 'Manajer Keuangan'), ('Status', 'K/2'), ('ID', 'EMP-2023-0012')]:
        pdf.cell(35, 5, f'  {l}', 1)
        pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(120, 6, '  PENERIMAAN', 1, 0, 'L', fill=True)
    pdf.cell(30, 6, 'Rp', 1, 0, 'C', fill=True)
    pdf.cell(0, 6, 'Jumlah', 1, 1, 'C', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for d, v in [('Gaji Pokok', '15.000.000'), ('Tunjangan Jabatan', '2.500.000'),
                  ('Tunjangan Transport', '1.000.000'), ('Tunjangan Kesehatan', '500.000'),
                  ('Tunjangan Pajak', '750.000')]:
        pdf.cell(120, 5, f'    {d}', 1)
        pdf.cell(30, 5, '', 1)
        pdf.cell(0, 5, v, 1, 1, 'R')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(120, 5, '    TOTAL PENERIMAAN', 1, 0, 'R')
    pdf.cell(30, 5, '', 1)
    pdf.cell(0, 5, '19.750.000', 1, 1, 'R')
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(120, 6, '  POTONGAN', 1, 0, 'L', fill=True)
    pdf.cell(30, 6, 'Rp', 1, 0, 'C', fill=True)
    pdf.cell(0, 6, 'Jumlah', 1, 1, 'C', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for d, v in [('BPJS Ketenagakerjaan', '150.000'), ('BPJS Kesehatan', '90.000'),
                  ('Iuran Pensiun', '200.000'), ('PPh Pasal 21', '635.000')]:
        pdf.cell(120, 5, f'    {d}', 1)
        pdf.cell(30, 5, '', 1)
        pdf.cell(0, 5, v, 1, 1, 'R')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(120, 5, '    TOTAL POTONGAN', 1, 0, 'R')
    pdf.cell(30, 5, '', 1)
    pdf.cell(0, 5, '1.075.000', 1, 1, 'R')
    pdf.ln(2)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(150, 7, 'TAKE HOME PAY', 0, 0, 'R')
    pdf.cell(0, 7, 'Rp 18.675.000', 0, 1, 'R')
    pdf.output(os.path.join(OUT, 'slip-gaji-doni-k2.pdf'))

# ========== 2C. BUKTI POTONG 1721-A1 (Amir) ==========
def bukti_potong_amir():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 7, 'BUKTI PEMOTONGAN PPh PASAL 21', 0, 1, 'C')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 5, 'Formulir 1721-A1', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'A. IDENTITAS PEMBERI KERJA', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 8)
    for l, v in [('Nama Perusahaan', 'PT Maju Sejahtera Tbk'), ('NPWP', '01.234.567.8-012.000')]:
        pdf.cell(40, 4, f'  {l}', 1)
        pdf.cell(0, 4, f'  {v}', 1, 1)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'B. IDENTITAS PEGAWAI', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 8)
    for l, v in [('Nama', 'Amir'), ('NPWP', '11.111.111.1-111.000'),
                  ('Status PTKP', 'K/1'), ('Pekerjaan', 'Karyawan Tetap')]:
        pdf.cell(40, 4, f'  {l}', 1)
        pdf.cell(0, 4, f'  {v}', 1, 1)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'C. RINCIAN PENGHASILAN TAHUNAN (TAHUN PAJAK 2025)', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 8)
    items = [
        ('1. Penghasilan Bruto Setahun', '300.000.000'),
        ('2. Pengurang:', ''),
        ('   - Biaya Jabatan (5%, maks 6jt)', '(6.000.000)'),
        ('3. Penghasilan Neto Setahun', '294.000.000'),
        ('4. PTKP (K/1 = 54jt + 4,5jt + 4,5jt)', '(63.000.000)'),
        ('5. Penghasilan Kena Pajak (PKP)', '231.000.000'),
        ('6. PPh 21 Terutang:', ''),
        ('   - 5% x Rp60.000.000', '3.000.000'),
        ('   - 15% x Rp171.000.000', '25.650.000'),
        ('   Total PPh 21 Terutang Setahun', '28.650.000'),
        ('7. PPh 21 Dipotong Perusahaan', '15.550.000'),
        ('8. PPh Kurang Bayar', '13.100.000'),
    ]
    for d, v in items:
        pdf.cell(125, 4, f'  {d}', 1)
        pdf.set_font('Helvetica', 'B', 8) if 'Neto' in d or 'PKP' in d or 'Total' in d or 'Kurang' in d else pdf.set_font('Helvetica', '', 8)
        pdf.cell(0, 4, f'  Rp {v}' if v else '', 1, 1, 'R' if v else 'L')
    pdf.ln(3)
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(80, 4, 'Jakarta, 31 Januari 2026', 0, 0)
    pdf.cell(0, 4, '', 0, 1)
    pdf.ln(6)
    pdf.cell(80, 4, 'PT Maju Sejahtera Tbk', 0, 0)
    pdf.cell(80, 4, 'Pegawai,', 0, 1)
    pdf.ln(8)
    pdf.cell(80, 4, '(_______________________)', 0, 0)
    pdf.cell(80, 4, '(Amir)', 0, 1)
    pdf.output(os.path.join(OUT, 'bukti-potong-1721-A1-amir.pdf'))

# ========== 2D. SPT 1770S TERISI ==========
def spt_1770s_terisi():
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
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(0, 6, 'SPT TAHUNAN PPh WP OP - FORM 1770S', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Tahun Pajak 2025', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'IDENTITAS', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 8)
    for l, v in [('Nama', 'Amir'), ('NPWP', '11.111.111.1-111.000'),
                  ('Status PTKP', 'K/1 (Kawin, 1 anak)'), ('Pekerjaan Utama', 'Karyawan Swasta')]:
        pdf.cell(40, 4, f'  {l}', 1)
        pdf.cell(0, 4, f'  {v}', 1, 1)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'PENGHASILAN NETO', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 8)
    untuk_neto = [
        ('A. Penghasilan dari Pekerjaan', 'Rp294.000.000'),
        ('B. Penghasilan dari Usaha', 'Rp0'),
        ('C. Penghasilan dari Pekerjaan Bebas', 'Rp0'),
        ('D. Jumlah Penghasilan Neto (A+B+C)', 'Rp294.000.000'),
    ]
    for d, v in untuk_neto:
        pdf.cell(130, 4, f'  {d}', 1)
        pdf.set_font('Helvetica', 'B', 8) if 'Jumlah' in d else pdf.set_font('Helvetica', '', 8)
        pdf.cell(0, 4, v, 1, 1, 'R')
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'PENGURANG & PPh TERUTANG', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 8)
    items = [
        ('E. PTKP (K/1 = Rp63.000.000)', '(Rp63.000.000)'),
        ('F. PKP (D - E)', 'Rp231.000.000'),
        ('G. PPh Terutang (5% x 60jt + 15% x 171jt)', 'Rp28.650.000'),
        ('H. Kredit Pajak (PPh 21 dipotong)', '(Rp15.550.000)'),
        ('I. PPh Kurang Bayar (G - H)', 'Rp13.100.000'),
    ]
    for d, v in items:
        pdf.cell(130, 4, f'  {d}', 1)
        pdf.set_font('Helvetica', 'B', 8) if 'PKP' in d or 'PPh Terutang' in d or 'Kurang' in d else pdf.set_font('Helvetica', '', 8)
        pdf.cell(0, 4, v, 1, 1, 'R')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(255, 230, 230)
    pdf.cell(0, 6, 'STATUS SPT: KURANG BAYAR Rp13.100.000', 1, 1, 'C', fill=True)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.multi_cell(0, 3,
        'Catatan: WP harus melunasi kekurangan bayar sebelum melaporkan SPT Tahunan. '
        'Pembayaran melalui bank/pos persepsi dengan kode billing.')
    pdf.output(os.path.join(OUT, 'spt-1770S-terisi-amir.pdf'))

# ========== 2E. TABEL PTKP ==========
def tabel_ptkp():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 7, 'TABEL PTKP (Penghasilan Tidak Kena Pajak)', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Berdasarkan PMK No. 101/PMK.010/2016', 0, 1, 'C')
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(0, 51, 102)
    pdf.set_text_color(255)
    pdf.cell(55, 7, 'Status', 1, 0, 'C', fill=True)
    pdf.cell(55, 7, 'Keterangan', 1, 0, 'C', fill=True)
    pdf.cell(40, 7, 'Tambahan', 1, 0, 'C', fill=True)
    pdf.cell(0, 7, 'Total PTKP', 1, 1, 'C', fill=True)
    pdf.set_text_color(0)
    data = [
        ('TK/0', 'Tidak Kawin, 0 tanggungan', 'Rp0', 'Rp54.000.000'),
        ('TK/1', 'Tidak Kawin, 1 tanggungan', 'Rp4.500.000', 'Rp58.500.000'),
        ('TK/2', 'Tidak Kawin, 2 tanggungan', 'Rp9.000.000', 'Rp63.000.000'),
        ('TK/3', 'Tidak Kawin, 3 tanggungan', 'Rp13.500.000', 'Rp67.500.000'),
        ('K/0', 'Kawin, 0 tanggungan', 'Rp4.500.000', 'Rp58.500.000'),
        ('K/1', 'Kawin, 1 tanggungan', 'Rp9.000.000', 'Rp63.000.000'),
        ('K/2', 'Kawin, 2 tanggungan', 'Rp13.500.000', 'Rp67.500.000'),
        ('K/3', 'Kawin, 3 tanggungan', 'Rp18.000.000', 'Rp72.000.000'),
        ('KH/0', 'Kawin, penghasilan istri digabung', 'Rp58.500.000', 'Rp112.500.000'),
        ('KH/1', 'K/I digabung, 1 tanggungan', 'Rp63.000.000', 'Rp117.000.000'),
    ]
    pdf.set_font('Helvetica', '', 9)
    fill = False
    for row in data:
        pdf.set_fill_color(240, 245, 250) if fill else pdf.set_fill_color(255, 255, 255)
        for i, v in enumerate(row):
            align = 'C' if i in [0, 2, 3] else 'L'
            pdf.cell([55, 55, 40, 0][i], 6, v, 1, 0 if i < 3 else 1, align, fill=True)
        fill = not fill
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.cell(0, 4, 'Catatan Penting:', 0, 1)
    pdf.set_font('Helvetica', '', 7)
    notes = [
        'PTKP ditentukan berdasarkan status awal tahun pajak.',
        'Maksimal 3 tanggungan (anak/keluarga sedarah).',
        'Istri dengan penghasilan digabung ke suami mendapat PTKP sendiri Rp54jt.',
        'KH = Kawin dengan penghasilan istri digabung (suami-istri 1 SPT).',
        'Tarif berlaku berdasarkan PMK 101/PMK.010/2016.',
    ]
    for n in notes:
        pdf.cell(5, 3.5, '', 0)
        pdf.cell(0, 3.5, f'- {n}', 0, 1)
    pdf.output(os.path.join(OUT, 'tabel-ptkp.pdf'))

# ========== RUN ALL ==========
if __name__ == '__main__':
    slip_gaji_tk0()
    print('OK: slip-gaji-siti-tk0.pdf')
    slip_gaji_k2()
    print('OK: slip-gaji-doni-k2.pdf')
    bukti_potong_amir()
    print('OK: bukti-potong-1721-A1-amir.pdf')
    spt_1770s_terisi()
    print('OK: spt-1770S-terisi-amir.pdf')
    tabel_ptkp()
    print('OK: tabel-ptkp.pdf')

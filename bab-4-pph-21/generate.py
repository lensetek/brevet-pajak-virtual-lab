from fpdf import FPDF
import os

OUT = r'C:\Users\ACER\Documents\GitHub\BrevetAB-VirtualLab\bab-4-pph-21'

class Doc(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 7)
        self.cell(0, 8, f'Simulasi Brevet Pajak AB - Halaman {self.page_no()}/{{nb}}', 0, 0, 'C')

# ========== 4A. SLIP GAJI 3 KARYAWAN ==========
def slip_gaji(nama, npwp, status, jabatan, gaji_pokok, tunjangan, bpjs_k, bpjs_kes, iuran_pensiun, pph21, file):
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(0, 7, 'PT MAJU SEJAHTERA TBK', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, 'Jl. Merdeka No. 88, Jakarta Pusat', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 6, 'SLIP GAJI KARYAWAN', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Periode: Januari 2026', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Nama', nama), ('NPWP', npwp), ('Jabatan', jabatan), ('Status', status)]:
        pdf.cell(35, 5, f'  {l}', 1)
        pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(1)

    tot_penerimaan = gaji_pokok + sum(e for _, e in tunjangan)
    tot_potongan = bpjs_k + bpjs_kes + iuran_pensiun + pph21

    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(120, 6, '  PENERIMAAN', 1, 0, 'L', fill=True)
    pdf.cell(30, 6, 'Rp', 1, 0, 'C', fill=True)
    pdf.cell(0, 6, 'Jumlah', 1, 1, 'C', fill=True)
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(120, 5, f'    Gaji Pokok', 1); pdf.cell(30, 5, '', 1); pdf.cell(0, 5, f'{gaji_pokok:,}'.replace(',','.'), 1, 1, 'R')
    for t_desc, t_val in tunjangan:
        pdf.cell(120, 5, f'    {t_desc}', 1); pdf.cell(30, 5, '', 1); pdf.cell(0, 5, f'{t_val:,}'.replace(',','.'), 1, 1, 'R')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(120, 5, '    TOTAL PENERIMAAN', 1, 0, 'R'); pdf.cell(30, 5, '', 1); pdf.cell(0, 5, f'{tot_penerimaan:,}'.replace(',','.'), 1, 1, 'R')

    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(120, 6, '  POTONGAN', 1, 0, 'L', fill=True)
    pdf.cell(30, 6, 'Rp', 1, 0, 'C', fill=True)
    pdf.cell(0, 6, 'Jumlah', 1, 1, 'C', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for d, v in [('BPJS Ketenagakerjaan', bpjs_k), ('BPJS Kesehatan', bpjs_kes), ('Iuran Pensiun', iuran_pensiun), ('PPh Pasal 21', pph21)]:
        if v:
            pdf.cell(120, 5, f'    {d}', 1); pdf.cell(30, 5, '', 1); pdf.cell(0, 5, f'{v:,}'.replace(',','.'), 1, 1, 'R')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(120, 5, '    TOTAL POTONGAN', 1, 0, 'R'); pdf.cell(30, 5, '', 1); pdf.cell(0, 5, f'{tot_potongan:,}'.replace(',','.'), 1, 1, 'R')
    pdf.ln(2)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 12)
    thp = tot_penerimaan - tot_potongan
    pdf.cell(150, 7, 'TAKE HOME PAY', 0, 0, 'R')
    pdf.cell(0, 7, f'Rp {thp:,}'.replace(',','.'), 0, 1, 'R')
    pdf.output(os.path.join(OUT, file))

# ========== 4B. BUKTI POTONG 1721-A1 ==========
def bukti_potong():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 6, 'BUKTI PEMOTONGAN PPh PASAL 21', 0, 1, 'C')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 5, 'Formulir 1721-A1', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'A. IDENTITAS PEMBERI KERJA', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 8)
    for l, v in [('Nama', 'PT Maju Sejahtera Tbk'), ('NPWP', '01.234.567.8-012.000')]:
        pdf.cell(40, 4, f'  {l}', 1); pdf.cell(0, 4, f'  {v}', 1, 1)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'B. IDENTITAS PEGAWAI', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 8)
    for l, v in [('Nama', 'Budi Santoso'), ('NPWP', '12.345.678.9-012.000'), ('Status PTKP', 'K/1'), ('Jabatan', 'Staff Akuntansi')]:
        pdf.cell(40, 4, f'  {l}', 1); pdf.cell(0, 4, f'  {v}', 1, 1)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'C. RINCIAN PENGHASILAN (TAHUN PAJAK 2025)', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 8)
    items = [
        ('1. Penghasilan Bruto Setahun', '129.000.000'),
        ('   - Gaji Pokok (12 x Rp8.000.000)', '96.000.000'),
        ('   - Tunjangan (12 x Rp2.750.000)', '33.000.000'),
        ('2. Biaya Jabatan (5%, maks 6jt)', '(6.000.000)'),
        ('3. Iuran Pensiun (12 x Rp150.000)', '(1.800.000)'),
        ('4. Penghasilan Neto Setahun', '121.200.000'),
        ('5. PTKP (K/1)', '(63.000.000)'),
        ('6. Penghasilan Kena Pajak', '58.200.000'),
        ('7. PPh 21 Terutang (5% x 58.200.000)', '2.910.000'),
        ('8. PPh 21 Dipotong per Bulan', '242.500'),
    ]
    for d, v in items:
        pdf.cell(125, 4, f'  {d}', 1)
        is_b = any(k in d for k in ['Neto', 'Kena Pajak', 'PPh 21 Terutang'])
        pdf.set_font('Helvetica', 'B' if is_b else '', 8)
        pdf.cell(0, 4, f'  Rp {v}', 1, 1, 'R')
    pdf.ln(3)
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(80, 4, 'Jakarta, 31 Januari 2026', 0, 0)
    pdf.cell(0, 4, '', 0, 1)
    pdf.ln(6)
    pdf.cell(80, 4, 'PT Maju Sejahtera Tbk', 0, 0)
    pdf.cell(80, 4, 'Pegawai,', 0, 1)
    pdf.ln(8)
    pdf.cell(80, 4, '(_______________________)', 0, 0)
    pdf.cell(80, 4, '(Budi Santoso)', 0, 1)
    pdf.output(os.path.join(OUT, 'bukti-potong-1721-A1-budi.pdf'))


# ========== 4C. INVOICE + BUKTI POTONG HONORARIUM ==========
def invoice_honor():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 7, 'PT MAJU SEJAHTERA TBK', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, 'Jl. Merdeka No. 88, Jakarta Pusat', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 6, 'INVOICE HONORARIUM', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('No. Invoice', 'INV-2026-0045'), ('Tanggal', '20 Januari 2026'),
                  ('Kepada', 'Dr. Ahmad Rizal, SE., M.Ak'), ('NPWP', '33.444.555.6-777.000'),
                  ('Jabatan', 'Konsultan Pajak'), ('Periode', 'Januari 2026')]:
        pdf.cell(40, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(140, 6, '  Rincian', 1, 0, 'L', fill=True)
    pdf.cell(0, 6, 'Jumlah (Rp)', 1, 1, 'C', fill=True)
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(140, 5, '    Jasa Konsultasi Pajak - Januari 2026', 1); pdf.cell(0, 5, '15.000.000', 1, 1, 'R')
    pdf.cell(140, 5, '    Biaya Transportasi & Akomodasi', 1); pdf.cell(0, 5, '  2.000.000', 1, 1, 'R')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(140, 5, '    TOTAL', 1, 0, 'R'); pdf.cell(0, 5, '17.000.000', 1, 1, 'R')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.cell(0, 4, 'Pemotongan PPh 21:', 0, 1)
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(140, 4, '    DPP (50% x Rp17jt untuk bukan pegawai)', 1); pdf.cell(0, 4, '8.500.000', 1, 1, 'R')
    pdf.cell(140, 4, '    PPh 21 dipotong (5% x Rp8.500.000)', 1); pdf.cell(0, 4, '425.000', 1, 1, 'R')
    pdf.cell(140, 4, '    Diterima setelah pajak', 1); pdf.cell(0, 4, '16.575.000', 1, 1, 'R')
    pdf.ln(3)
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(80, 4, 'Jakarta, 20 Januari 2026', 0, 1)
    pdf.ln(5)
    pdf.cell(80, 4, 'PT Maju Sejahtera Tbk', 0, 0)
    pdf.cell(80, 4, 'Penerima,', 0, 1)
    pdf.ln(8)
    pdf.cell(80, 4, '(_______________________)', 0, 0)
    pdf.cell(80, 4, '(Dr. Ahmad Rizal)', 0, 1)
    pdf.output(os.path.join(OUT, 'invoice-honorarium-konsultan.pdf'))


# ========== 4D. PAYROLL SUMMARY ==========
def payroll_summary():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 7, 'PT MAJU SEJAHTERA TBK', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, 'REKAP PAYROLL - JANUARI 2026', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(2)

    pdf.set_font('Helvetica', 'B', 7)
    pdf.set_fill_color(0, 51, 102)
    pdf.set_text_color(255)
    headers = ['No', 'Nama', 'Status', 'Gaji Pokok', 'Tunjangan', 'Bruto', 'PPh 21', 'THP']
    widths = [8, 38, 12, 32, 32, 32, 25, 25]
    for i, h in enumerate(headers):
        pdf.cell(widths[i], 6, h, 1, 0, 'C', fill=True)
    pdf.set_text_color(0)
    pdf.ln()

    data = [
        ('1', 'Budi Santoso', 'K/1', '8.000.000', '2.750.000', '10.750.000', '242.500', '10.151.500'),
        ('2', 'Siti Nurhaliza', 'TK/0', '4.500.000', '550.000', '5.050.000', '23.750', '4.921.250'),
        ('3', 'Doni Prasetyo', 'K/2', '15.000.000', '4.750.000', '19.750.000', '635.000', '18.675.000'),
        ('4', 'Rina Wijaya', 'TK/1', '6.000.000', '1.200.000', '7.200.000', '82.500', '6.967.500'),
        ('5', 'Ahmad Hidayat', 'K/1', '10.000.000', '2.500.000', '12.500.000', '350.000', '11.800.000'),
    ]
    pdf.set_font('Helvetica', '', 7)
    for row in data:
        for i, v in enumerate(row):
            align = 'R' if i >= 3 else 'L'
            pdf.cell(widths[i], 5, v, 1, 0, align)
        pdf.ln()
    # Total row
    pdf.set_font('Helvetica', 'B', 7)
    pdf.cell(8, 5, '', 1)
    pdf.cell(38, 5, 'TOTAL', 1, 0, 'C')
    pdf.cell(32, 5, '43.500.000', 1, 0, 'R')
    pdf.cell(32, 5, '11.750.000', 1, 0, 'R')
    pdf.cell(32, 5, '55.250.000', 1, 0, 'R')
    pdf.cell(25, 5, '1.333.750', 1, 0, 'R')
    pdf.cell(25, 5, '52.515.250', 1, 1, 'R')

    pdf.ln(3)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.multi_cell(0, 3, 'Catatan: Rekap ini digunakan untuk pelaporan SPT Masa PPh 21.')
    pdf.output(os.path.join(OUT, 'payroll-summary-januari-2026.pdf'))


if __name__ == '__main__':
    # 3 slip gaji
    slip_gaji('Budi Santoso', '12.345.678.9-012.000', 'K/1', 'Staff Akuntansi', 8000000,
              [('Tunjangan Jabatan', 1500000), ('Tunjangan Transport', 500000), ('Tunjangan Makan', 450000), ('Tunjangan Kesehatan', 300000)],
              120000, 80000, 150000, 248500, 'slip-gaji-budi.pdf')
    print('OK: slip-gaji-budi.pdf')

    slip_gaji('Rina Wijaya', '55.666.777.8-999.000', 'TK/1', 'Staff HRD', 6000000,
              [('Tunjangan Transport', 400000), ('Tunjangan Makan', 350000), ('Tunjangan Kesehatan', 200000)],
              90000, 60000, 100000, 82500, 'slip-gaji-rina.pdf')
    print('OK: slip-gaji-rina.pdf')

    slip_gaji('Ahmad Hidayat', '88.999.000.1-234.000', 'K/1', 'Supervisor', 10000000,
              [('Tunjangan Jabatan', 1500000), ('Tunjangan Transport', 600000), ('Tunjangan Makan', 500000), ('Tunjangan Kesehatan', 300000)],
              150000, 90000, 150000, 350000, 'slip-gaji-ahmad.pdf')
    print('OK: slip-gaji-ahmad.pdf')

    bukti_potong()
    print('OK: bukti-potong-1721-A1-budi.pdf')
    invoice_honor()
    print('OK: invoice-honorarium-konsultan.pdf')
    payroll_summary()
    print('OK: payroll-summary-januari-2026.pdf')

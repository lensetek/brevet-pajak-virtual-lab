from fpdf import FPDF
import os

OUT = r'C:\Users\ACER\Documents\GitHub\BrevetAB-VirtualLab\bab-13-coretax'

class Doc(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 7)
        self.cell(0, 8, f'Simulasi Brevet Pajak AB - Halaman {self.page_no()}/{{nb}}', 0, 0, 'C')

# ========== 13A. ID BILLING ==========
def id_billing():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 5, 'KEMENTERIAN KEUANGAN RI', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(0, 4, 'DIREKTORAT JENDERAL PAJAK - SISTEM CORETAX', 0, 1, 'C')
    pdf.set_text_color(0)
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 7, 'KODE BILLING PAJAK', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Courier', 'B', 16)
    pdf.cell(0, 10, '026 12345 67890 123', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('NPWP', '01.234.567.8-012.000'), ('Nama WP', 'PT Maju Sejahtera Tbk'),
                  ('Jenis Pajak', '411121 - PPh Pasal 21'),
                  ('Masa Pajak', '01 - Januari 2026'),
                  ('Jumlah Setor', 'Rp1.339.750'),
                  ('Tanggal Jatuh Tempo', '10 Februari 2026'),
                  ('Status', 'Belum Dibayar'),
                  ('NTPN', '-')]:
        pdf.cell(45, 6, f'  {l}', 1)
        pdf.cell(0, 6, f'  {v}', 1, 1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.multi_cell(0, 3, 'ID Billing digunakan untuk pembayaran pajak melalui bank/pos persepsi. Setelah bayar, akan diperoleh NTPN (Nomor Transaksi Penerimaan Negara).')
    pdf.output(os.path.join(OUT, 'id-billing-pph21.pdf'))

# ========== 13B. TAMPILAN E-BUPOT ==========
def e_bupot():
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
    pdf.cell(0, 6, 'SISTEM e-BUPOT PPh 23/26', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Rekap Bukti Potong - Masa Januari 2026', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(0, 51, 102)
    pdf.set_text_color(255)
    headers = ['No', 'Penerima', 'NPWP', 'Jenis', 'DPP', 'PPh 23']
    widths = [8, 45, 35, 20, 35, 30]
    for i, h in enumerate(headers):
        pdf.cell(widths[i], 6, h, 1, 0, 'C', fill=True)
    pdf.set_text_color(0)
    pdf.ln()
    data = [
        ('1', 'CV Konsultindo Utama', '03.456.789.0-012.000', 'Jasa', '200.000.000', '4.000.000'),
        ('2', 'PT Cipta Karya Inovasi', '04.567.890.1-234.000', 'Royalti', '80.000.000', '12.000.000'),
        ('3', 'PT Alat Berat Nusantara', '05.678.901.2-345.000', 'Sewa', '45.000.000', '900.000'),
    ]
    pdf.set_font('Helvetica', '', 7)
    for row in data:
        for i, v in enumerate(row):
            align = 'R' if i >= 4 else 'L'
            pdf.cell(widths[i], 5, v, 1, 0, align)
        pdf.ln()
    pdf.set_font('Helvetica', 'B', 7)
    pdf.cell(8, 5, '', 1)
    pdf.cell(45, 5, 'TOTAL', 1, 0, 'C')
    pdf.cell(35, 5, '', 1)
    pdf.cell(20, 5, '', 1)
    pdf.cell(35, 5, '325.000.000', 1, 0, 'R')
    pdf.cell(30, 5, '16.900.000', 1, 1, 'R')
    pdf.ln(3)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.cell(0, 3, 'e-Bupot adalah aplikasi DJP untuk pembuatan bukti potong PPh 23/26 secara elektronik.', 0, 1)
    pdf.output(os.path.join(OUT, 'e-bupot-rekap-23.pdf'))

# ========== 13C. TAMPILAN E-FAKTUR ==========
def e_faktur():
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
    pdf.cell(0, 6, 'SISTEM e-FAKTUR', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Rekap Faktur Pajak - Masa Januari 2026', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(0, 51, 102)
    pdf.set_text_color(255)
    headers = ['No', 'No. Seri FP', 'Pembeli', 'Jenis', 'DPP', 'PPN']
    widths = [8, 38, 45, 20, 35, 30]
    for i, h in enumerate(headers):
        pdf.cell(widths[i], 6, h, 1, 0, 'C', fill=True)
    pdf.set_text_color(0)
    pdf.ln()
    data = [
        ('1', '010.000-26.00000001', 'PT Distributor Utama', 'PK', '150.000.000', '16.500.000'),
        ('2', '010.000-26.00000002', 'PT Supplier Abadi', 'PM', '100.000.000', '11.000.000'),
        ('3', '010.000-26.00000003', 'PT Retail Niaga', 'PK', '75.000.000', '8.250.000'),
        ('4', '010.000-26.00000004', 'PT Toko Modern', 'PK', '50.000.000', '5.500.000'),
    ]
    pdf.set_font('Helvetica', '', 7)
    for row in data:
        for i, v in enumerate(row):
            align = 'R' if i >= 4 else 'L'
            pdf.cell(widths[i], 5, v, 1, 0, align)
        pdf.ln()
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(0, 5, 'RINGKASAN PPN', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(120, 5, '  Total Pajak Keluaran', 1); pdf.cell(0, 5, 'Rp30.250.000', 1, 1, 'R')
    pdf.cell(120, 5, '  Total Pajak Masukan', 1); pdf.cell(0, 5, 'Rp11.000.000', 1, 1, 'R')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(120, 5, '  PPN Kurang Bayar', 1, 0, 'R'); pdf.cell(0, 5, 'Rp19.250.000', 1, 1, 'R')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.cell(0, 3, 'e-Faktur adalah aplikasi DJP untuk pembuatan Faktur Pajak secara elektronik.', 0, 1)
    pdf.output(os.path.join(OUT, 'e-faktur-rekap-ppn.pdf'))

# ========== 13D. BUKTI PENERIMAAN SPT ELEKTRONIK ==========
def bukti_spt():
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
    pdf.cell(0, 6, 'BUKTI PENERIMAAN SPT ELEKTRONIK', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Nomor Transaksi', 'SPT-2026-0012345678'),
                  ('Tanggal Lapor', '20 Maret 2026 - 14:30 WIB'),
                  ('NPWP', '01.234.567.8-012.000'),
                  ('Nama WP', 'PT Maju Sejahtera Tbk'),
                  ('Jenis SPT', 'SPT Tahunan PPh Badan - 1771'),
                  ('Masa/Tahun Pajak', 'Tahun 2025'),
                  ('Status SPT', 'Kurang Bayar - Rp3.212.600.000'),
                  ('KPP', 'KPP Pratama Jakarta Menteng Satu')]:
        pdf.cell(45, 5, f'  {l}', 1)
        pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 5, 'QR CODE VERIFIKASI', 0, 1, 'C')
    pdf.ln(5)
    pdf.set_draw_color(0)
    pdf.set_fill_color(255, 255, 255)
    pdf.rect(85, pdf.get_y(), 40, 40)
    pdf.set_xy(88, pdf.get_y()+5)
    pdf.set_font('Courier', '', 6)
    qr = [
        '##############',
        '#  CORETAX  #',
        '#  VERIFIED #',
        '#  SPT-2026 #',
        '#  VALID    #',
        '##############',
    ]
    for line in qr:
        pdf.cell(34, 3, line, 0, 1, 'C')
    pdf.ln(5)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.multi_cell(0, 3, 'Dokumen ini adalah bukti penerimaan SPT secara elektronik yang sah melalui sistem Coretax DJP.')
    pdf.output(os.path.join(OUT, 'bukti-penerimaan-spt-elektronik.pdf'))

if __name__ == '__main__':
    id_billing(); print('OK: id-billing-pph21.pdf')
    e_bupot(); print('OK: e-bupot-rekap-23.pdf')
    e_faktur(); print('OK: e-faktur-rekap-ppn.pdf')
    bukti_spt(); print('OK: bukti-penerimaan-spt-elektronik.pdf')

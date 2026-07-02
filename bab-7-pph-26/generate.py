from fpdf import FPDF
import os

OUT = r'C:\Users\ACER\Documents\GitHub\BrevetAB-VirtualLab\bab-7-pph-26'

class Doc(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 7)
        self.cell(0, 8, f'Simulasi Brevet Pajak AB - Halaman {self.page_no()}/{{nb}}', 0, 0, 'C')

# ========== 7A. INVOICE ROYALTI LUAR NEGERI ==========
def invoice_ln():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 7, 'TECHNO CORP JAPAN', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, '2-3-1 Marunouchi, Chiyoda-ku, Tokyo 100-0005, Japan', 0, 1, 'C')
    pdf.cell(0, 4, 'Tax ID: JP-123456789', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 6, 'INVOICE / ROYALTY PAYMENT', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Invoice No: TCJ-2026-0045', 0, 1, 'R')
    pdf.ln(2)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Date', '15 January 2026'), ('Bill To', 'PT Maju Sejahtera Tbk'),
                  ('NPWP', '01.234.567.8-012.000'), ('Address', 'Jl. Merdeka No. 88, Jakarta')]:
        pdf.cell(35, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(140, 6, '  Description', 1, 0, 'L', fill=True)
    pdf.cell(0, 6, 'Amount (JPY)', 1, 1, 'C', fill=True)
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(140, 5, '    Software License Royalty - Q1 2026', 1)
    pdf.cell(0, 5, '10.000.000', 1, 1, 'R')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(140, 5, '    TOTAL', 1, 0, 'R')
    pdf.cell(0, 5, '10.000.000', 1, 1, 'R')
    pdf.ln(1)
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Equivalent to: approx. Rp1.000.000.000 (Kurs: Rp100/JPY)', 0, 1)
    pdf.cell(0, 4, 'PPh 26 (tanpa treaty): 20% x Rp1.000.000.000 = Rp200.000.000', 0, 1)
    pdf.cell(0, 4, 'PPh 26 (dengan treaty 10%): 10% x Rp1.000.000.000 = Rp100.000.000', 0, 1)
    pdf.ln(3)
    pdf.cell(80, 4, 'Tokyo, 15 January 2026', 0, 1)
    pdf.ln(8)
    pdf.cell(80, 4, 'Techno Corp Japan', 0, 0)
    pdf.cell(80, 4, 'Authorized Signatory,', 0, 1)
    pdf.ln(8)
    pdf.cell(80, 4, '(_______________________)', 0, 0)
    pdf.cell(80, 4, '(T. Tanaka, CFO)', 0, 1)
    pdf.output(os.path.join(OUT, 'invoice-luar-negeri-royalti.pdf'))

# ========== 7B. INVOICE JASA LUAR NEGERI ==========
def invoice_jasa_ln():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 7, 'SINGAPORE TECH SOLUTIONS PTE LTD', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, '1 Raffles Place, #20-01, Singapore 048616', 0, 1, 'C')
    pdf.cell(0, 4, 'UEN: 202012345G', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 6, 'INVOICE - CONSULTING SERVICES', 0, 1, 'C')
    pdf.ln(2)
    for l, v in [('Invoice No', 'STS-2026-0088'), ('Date', '20 January 2026'),
                  ('Bill To', 'PT Maju Sejahtera Tbk'), ('Service', 'IT Infrastructure Consulting')]:
        pdf.cell(35, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(140, 6, '  Description', 1, 0, 'L', fill=True)
    pdf.cell(0, 6, 'Amount (USD)', 1, 1, 'C', fill=True)
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(140, 5, '    IT Consulting Services - Jan 2026', 1)
    pdf.cell(0, 5, '20.000', 1, 1, 'R')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(140, 5, '    TOTAL', 1, 0, 'R')
    pdf.cell(0, 5, '20.000', 1, 1, 'R')
    pdf.ln(1)
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Equivalent: Rp20.000 x Rp15.600 = Rp312.000.000', 0, 1)
    pdf.ln(3)
    pdf.cell(80, 4, 'Singapore, 20 January 2026', 0, 1)
    pdf.ln(8)
    pdf.cell(80, 4, 'Singapore Tech Solutions', 0, 0)
    pdf.output(os.path.join(OUT, 'invoice-jasa-luar-negeri.pdf'))

# ========== 7C. FORM DGT / SKD WPLN ==========
def form_dgt():
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
    pdf.cell(0, 6, 'SURAT KETERANGAN DOMISILI (SKD) WPLN', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Form DGT - Untuk Penerapan P3B (Tax Treaty)', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'A. IDENTITAS PENERIMA PENGHASILAN (WPLN)', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Nama', 'Techno Corp Japan'), ('Negara Domisili', 'Jepang'),
                  ('Tax ID/Identification No.', 'JP-123456789'),
                  ('Alamat di LN', '2-3-1 Marunouchi, Chiyoda-ku, Tokyo 100-0005, Japan'),
                  ('Bentuk Usaha', 'Perusahaan (Corporation)')]:
        pdf.cell(50, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'B. PERNYATAAN', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 8)
    pdf.multi_cell(0, 4,
        'Saya yang bertanda tangan di bawah ini menyatakan bahwa penerima penghasilan '
        'adalah subjek pajak di negara domisili (Jepang) dan tidak menjalankan usaha '
        'atau melakukan kegiatan melalui Bentuk Usaha Tetap (BUT) di Indonesia.')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'C. PENGESAHAN OTORITAS PAJAK NEGARA DOMISILI', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(0, 4, 'Divalidasi oleh: National Tax Agency Japan', 0, 1)
    pdf.cell(0, 4, 'Tanggal: 15 January 2026', 0, 1)
    pdf.cell(0, 4, 'Stempel & Tanda Tangan: (_______________________)', 0, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'D. TARIF TREATY YANG DIAJUKAN', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Jenis Penghasilan', 'Royalti'), ('Tarif Treaty (P3B Indonesia-Jepang)', '10%'),
                  ('Pasal dalam Treaty', 'Article 12 - Royalties'),
                  ('Tarif Normal (tanpa treaty)', '20%')]:
        pdf.cell(60, 5, f'  {l}', 1); pdf.cell(0, 5, f'  {v}', 1, 1)
    pdf.output(os.path.join(OUT, 'form-dgt-skd-wpln.pdf'))

# ========== 7D. TABEL TARIF TAX TREATY ==========
def tabel_treaty():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 7, 'TABEL TARIF PPh PASAL 26 & TAX TREATY', 0, 1, 'C')
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(0, 51, 102)
    pdf.set_text_color(255)
    pdf.cell(55, 7, 'Jenis Penghasilan', 1, 0, 'C', fill=True)
    pdf.cell(25, 7, 'Tarif Normal', 1, 0, 'C', fill=True)
    pdf.cell(0, 7, 'Keterangan', 1, 1, 'C', fill=True)
    pdf.set_text_color(0)
    data = [
        ('Dividen, Bunga, Royalti, Jasa', '20%', 'Dari jumlah bruto'),
        ('Penjualan harta di Indonesia', '5%', '20% x 25% perkiraan neto'),
        ('Penjualan saham oleh WPLN', '5%', '20% x 25% perkiraan neto'),
        ('Premi asuransi LN', '20%', 'Dari perkiraan neto'),
        ('Branch Profit Tax (BUT)', '20%', 'Laba setelah pajak'),
    ]
    pdf.set_font('Helvetica', '', 9)
    for row in data:
        pdf.cell(55, 6, f'  {row[0]}', 1)
        pdf.cell(25, 6, row[1], 1, 0, 'C')
        pdf.cell(0, 6, f'  {row[2]}', 1, 1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 5, 'CONTOH TARIF TREATY (P3B) BEBERAPA NEGARA - ROYALTI:', 0, 1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(0, 51, 102)
    pdf.set_text_color(255)
    pdf.cell(55, 7, 'Negara', 1, 0, 'C', fill=True)
    pdf.cell(35, 7, 'Tarif Treaty', 1, 0, 'C', fill=True)
    pdf.cell(0, 7, 'Penghematan', 1, 1, 'C', fill=True)
    pdf.set_text_color(0)
    treaty = [
        ('Jepang', '10%', '10%'),
        ('Singapura', '10%', '10%'),
        ('Amerika Serikat', '15%', '5%'),
        ('Inggris', '12%', '8%'),
        ('Malaysia', '12%', '8%'),
    ]
    pdf.set_font('Helvetica', '', 9)
    for row in treaty:
        pdf.cell(55, 6, f'  {row[0]}', 1)
        pdf.cell(35, 6, row[1], 1, 0, 'C')
        pdf.cell(0, 6, f'  Dibandingkan 20% normal, hemat {row[2]}', 1, 1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.multi_cell(0, 3, 'Catatan: Penggunaan tarif treaty memerlukan Form DGT/SKD WPLN yang sudah divalidasi otoritas pajak negara domisili.')
    pdf.output(os.path.join(OUT, 'tabel-tarif-pph26-treaty.pdf'))

if __name__ == '__main__':
    invoice_ln(); print('OK: invoice-luar-negeri-royalti.pdf')
    invoice_jasa_ln(); print('OK: invoice-jasa-luar-negeri.pdf')
    form_dgt(); print('OK: form-dgt-skd-wpln.pdf')
    tabel_treaty(); print('OK: tabel-tarif-pph26-treaty.pdf')

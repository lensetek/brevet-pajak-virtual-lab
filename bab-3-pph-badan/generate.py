from fpdf import FPDF
import os

OUT = r'C:\Users\ACER\Documents\GitHub\BrevetAB-VirtualLab\bab-3-pph-badan'

class Doc(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 7)
        self.cell(0, 8, f'Simulasi Brevet Pajak AB - Halaman {self.page_no()}/{{nb}}', 0, 0, 'C')

# ========== 3A. LAPORAN LABA RUGI KOMERSIAL ==========
def lap_laba_rugi():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 7, 'PT MAJU SEJAHTERA TBK', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, 'LAPORAN LABA RUGI', 0, 1, 'C')
    pdf.cell(0, 4, 'Periode 1 Jan - 31 Des 2025', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)

    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(140, 6, '  Pos', 1, 0, 'L', fill=True)
    pdf.cell(0, 6, 'Jumlah (Rp)', 1, 1, 'C', fill=True)
    pdf.set_font('Helvetica', '', 9)

    items = [
        ('PENDAPATAN', '', '', 'B'),
        ('  Penjualan (Omzet)', '30.000.000.000', '', ''),
        ('  Pendapatan Lainnya', '500.000.000', '', ''),
        ('TOTAL PENDAPATAN', '30.500.000.000', '', 'B'),
        ('', '', '', ''),
        ('BIAYA OPERASIONAL', '', '', 'B'),
        ('  Beban Gaji & Tunjangan', '(8.500.000.000)', '', ''),
        ('  Beban Transportasi & Perjalanan', '(1.200.000.000)', '', ''),
        ('  Beban Sewa Kantor', '(900.000.000)', '', ''),
        ('  Beban ATK & Perlengkapan', '(200.000.000)', '', ''),
        ('  Beban Listrik, Air, Telepon', '(350.000.000)', '', ''),
        ('  Beban Pemasaran & Iklan', '(500.000.000)', '', ''),
        ('  Beban Penyusutan Aset', '(800.000.000)', '', ''),
        ('  Beban Pemeliharaan', '(250.000.000)', '', ''),
        ('  Beban Bunga Pinjaman', '(400.000.000)', '', ''),
        ('  Beban Asuransi', '(150.000.000)', '', ''),
        ('TOTAL BIAYA OPERASIONAL', '(13.250.000.000)', '', 'B'),
        ('', '', '', ''),
        ('LABA USAHA', '17.250.000.000', '', 'B'),
        ('', '', '', ''),
        ('PENDAPATAN/(BEBAN) LAIN-LAIN', '', '', ''),
        ('  Pendapatan Bunga Deposito', '50.000.000', '', ''),
        ('  Laba Selisih Kurs', '25.000.000', '', ''),
        ('  Beban Administrasi Bank', '(35.000.000)', '', ''),
        ('LABA SEBELUM PAJAK', '17.290.000.000', '', 'B'),
    ]
    for desc, val, _, bold in items:
        if not desc and not val:
            pdf.ln(2)
            continue
        is_bold = bold == 'B'
        pdf.set_font('Helvetica', 'B' if is_bold else '', 9)
        pdf.cell(140, 5, f'  {desc}', 1)
        pdf.cell(0, 5, f'Rp {val}', 1, 1, 'R')

    pdf.ln(3)
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Laporan ini disusun berdasarkan pembukuan komersial perusahaan.', 0, 1, 'C')
    pdf.output(os.path.join(OUT, 'lap-laba-rugi-komersial.pdf'))


# ========== 3B. REKONSILIASI FISKAL ==========
def rekonsiliasi_fiskal():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 7, 'PT MAJU SEJAHTERA TBK', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, 'REKONSILIASI FISKAL TAHUN 2025', 0, 1, 'C')
    pdf.cell(0, 4, '(Laba Komersial ke Laba Fiskal)', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)

    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(100, 6, '  Keterangan', 1, 0, 'L', fill=True)
    pdf.cell(30, 6, 'Koreksi', 1, 0, 'C', fill=True)
    pdf.cell(0, 6, 'Jumlah (Rp)', 1, 1, 'C', fill=True)

    pdf.set_font('Helvetica', '', 9)
    items = [
        ('Laba Komersial Sebelum Pajak', '', '17.290.000.000', 'B'),
        ('', '', '', ''),
        ('KOREKSI POSITIF:', 'Positif', '', 'B'),
        ('  Beban Penyusutan (komersial > fiskal)', 'Positif', '120.000.000', ''),
        ('  Beban Pemasaran (nature tidak fiskal)', 'Positif', '75.000.000', ''),
        ('  Beban Bunga (bagian tdk dpt dikurangkan)', 'Positif', '25.000.000', ''),
        ('  Beban Sanksi Pajak', 'Positif', '15.000.000', ''),
        ('  Beban Asuransi (nature natura)', 'Positif', '30.000.000', ''),
        ('  Total Koreksi Positif', 'Positif', '265.000.000', 'B'),
        ('', '', '', ''),
        ('KOREKSI NEGATIF:', 'Negatif', '', 'B'),
        ('  Pendapatan Bunga Deposito (final)', 'Negatif', '(50.000.000)', ''),
        ('  Laba Selisih Kurs (belum direalisasi)', 'Negatif', '(25.000.000)', ''),
        ('  Total Koreksi Negatif', 'Negatif', '(75.000.000)', 'B'),
        ('', '', '', ''),
        ('LABA FISKAL (PKP Badan)', '', '17.480.000.000', 'B'),
    ]
    for desc, cor_type, val, bold in items:
        if not desc and not val:
            pdf.ln(2)
            continue
        is_b = bold == 'B'
        pdf.set_font('Helvetica', 'B' if is_b else '', 9)
        pdf.cell(100, 5, f'  {desc}', 1)
        pdf.cell(30, 5, cor_type, 1, 0, 'C')
        hl = 'R' if val and val.startswith('(') else 'R'
        pdf.cell(0, 5, f'Rp {val}', 1, 1, hl)

    pdf.ln(2)
    pdf.set_font('Helvetica', '', 8)
    pdf.multi_cell(0, 4,
        'Catatan: Omzet Rp30M < Rp50M, maka menggunakan fasilitas Pasal 31E. '
        'PKP Rp17,48M, bagian PKP s.d. Rp4,8M mendapat diskon tarif 50% (11%).')
    pdf.output(os.path.join(OUT, 'rekonsiliasi-fiskal.pdf'))


# ========== 3C. SPT 1771 + PERHITUNGAN PPh ==========
def spt_1771():
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
    pdf.cell(0, 6, 'SPT TAHUNAN PPh BADAN - FORM 1771', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Tahun Pajak 2025', 0, 1, 'C')
    pdf.ln(2)

    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'IDENTITAS', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Nama', 'PT Maju Sejahtera Tbk'), ('NPWP', '01.234.567.8-012.000'),
                  ('Bidang Usaha', 'Perdagangan & Jasa'), ('Omzet', 'Rp30.000.000.000')]:
        pdf.cell(40, 4, f'  {l}', 1)
        pdf.cell(0, 4, f'  {v}', 1, 1)

    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'PERHITUNGAN PPh BADAN', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)

    # Hitung PPh: Fasilitas 31E karena omzet < 50M
    pkp_total = 17_480_000_000
    pkp_fasilitas = 4_800_000_000
    pkp_non_fasilitas = pkp_total - pkp_fasilitas
    pph_fasilitas = int(pkp_fasilitas * 0.11)
    pph_non_fasilitas = int(pkp_non_fasilitas * 0.22)
    total_pph = pph_fasilitas + pph_non_fasilitas

    items = [
        ('A. Penghasilan Neto Fiskal (PKP)', f'Rp{total_pph:,}'.replace(',', '.')),
        ('B. Fasilitas Pasal 31E:', ''),
        ('    PKP s.d. Rp4,8M x 11% (diskon 50%)', f'  Rp{pkp_fasilitas:,}'.replace(',', '.')),
        ('    PPh dari PKP fasilitas', f'  Rp{pph_fasilitas:,}'.replace(',', '.')),
        ('C. Tanpa Fasilitas:', ''),
        ('    PKP > Rp4,8M x 22%', f'  Rp{pkp_non_fasilitas:,}'.replace(',', '.')),
        ('    PPh dari PKP non-fasilitas', f'  Rp{pph_non_fasilitas:,}'.replace(',', '.')),
        ('D. TOTAL PPh TERUTANG', f'Rp{total_pph:,}'.replace(',', '.')),
        ('E. KREDIT PAJAK:', ''),
        ('    PPh 22 (dipungut pihak lain)', 'Rp  30.000.000'),
        ('    PPh 23 (dipotong pihak lain)', 'Rp  75.000.000'),
        ('    Total Kredit Pajak', 'Rp 105.000.000'),
        ('F. PPh KURANG/(LEBIH) BAYAR', f'Rp{(total_pph-105_000_000):,}'.replace(',', '.')),
    ]
    for d, v in items:
        pdf.cell(130, 5, f'  {d}', 1)
        is_b = 'TOTAL' in d or 'KURANG' in d
        pdf.set_font('Helvetica', 'B' if is_b else '', 9)
        pdf.cell(0, 5, v, 1, 1, 'R')

    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(255, 230, 230)
    pdf.cell(0, 6, f'  STATUS SPT: KURANG BAYAR Rp{(total_pph-105_000_000):,}'.replace(',', '.'), 1, 1, 'L', fill=True)

    pdf.ln(2)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.multi_cell(0, 3, 'Catatan: Fasilitas Pasal 31E diberikan karena omzet perusahaan <= Rp50 miliar.')

    pdf.output(os.path.join(OUT, 'spt-1771-pph-badan.pdf'))


# ========== 3D. TABEL TARIF PPh BADAN ==========
def tabel_tarif():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 7, 'TABEL TARIF PPh BADAN', 0, 1, 'C')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Berlaku Tahun Pajak 2025-2026', 0, 1, 'C')
    pdf.ln(3)

    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(0, 51, 102)
    pdf.set_text_color(255)
    pdf.cell(50, 7, 'Kategori WP Badan', 1, 0, 'C', fill=True)
    pdf.cell(40, 7, 'Tarif', 1, 0, 'C', fill=True)
    pdf.cell(0, 7, 'Dasar Hukum', 1, 1, 'C', fill=True)
    pdf.set_text_color(0)

    data = [
        ('Perusahaan Umum', '22%', 'UU PPh stdd UU HPP'),
        ('Perusahaan Tbk (40% saham publik)', '19%', 'PMK 40/2023'),
        ('Omzet <= Rp4,8M (UMKM PP 55)', '0,5% final', 'PP 55/2022'),
        ('Omzet <= Rp50M (Pasal 31E)', '11% s.d. Rp4,8M PKP', 'Pasal 31E UU PPh'),
        ('Omzet > Rp50M (non-fasilitas)', '22%', 'UU PPh stdd UU HPP'),
    ]
    pdf.set_font('Helvetica', '', 9)
    for row in data:
        pdf.cell(50, 6, f'  {row[0]}', 1)
        pdf.cell(40, 6, row[1], 1, 0, 'C')
        pdf.cell(0, 6, f'  {row[2]}', 1, 1)

    pdf.ln(3)
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(0, 4, 'Catatan Penting:', 0, 1)
    pdf.multi_cell(0, 3.5,
        '- Untuk omzet Rp4,8M - Rp50M menggunakan Pasal 31E: diskon 50% tarif normal\n'
        '- Untuk omzet > Rp50M: tarif flat 22%\n'
        '- UMKM bisa memilih final 0,5% (PP 55/2022) atau menggunakan tarif normal\n'
        '- Fasilitas 31E dihitung per lapisan: PKP s.d. Rp4,8M x 11%, sisanya x 22%')
    pdf.output(os.path.join(OUT, 'tabel-tarif-pph-badan.pdf'))


if __name__ == '__main__':
    lap_laba_rugi(); print('OK: lap-laba-rugi-komersial.pdf')
    rekonsiliasi_fiskal(); print('OK: rekonsiliasi-fiskal.pdf')
    spt_1771(); print('OK: spt-1771-pph-badan.pdf')
    tabel_tarif(); print('OK: tabel-tarif-pph-badan.pdf')

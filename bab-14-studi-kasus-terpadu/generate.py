from fpdf import FPDF
import os

OUT = r'C:\Users\ACER\Documents\GitHub\BrevetAB-VirtualLab\bab-14-studi-kasus-terpadu'

class Doc(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 7)
        self.cell(0, 8, f'Simulasi Brevet Pajak AB - Halaman {self.page_no()}/{{nb}}', 0, 0, 'C')

# ========== 14A. PROFIL & NERACA PERUSAHAAN ==========
def profil_perusahaan():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(0, 7, 'PT NIAGA PRATAMA SEJAHTERA', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, 'PROFIL PERUSAHAAN - DATA FISKAL TAHUN 2025', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('NPWP', '02.345.678.9-012.000'),
                  ('Bidang Usaha', 'Perdagangan Barang Konsumsi'),
                  ('Omzet', 'Rp25.000.000.000'),
                  ('Status PKP', 'PKP sejak 2020'),
                  ('Karyawan Tetap', '8 orang'),
                  ('Jumlah Pemegang Saham', '3 orang (PT)'),
                  ('Kepemilikan Publik', '< 40% (bukan Tbk)')]:
        pdf.cell(45, 6, f'  {l}', 1); pdf.cell(0, 6, f'  {v}', 1, 1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(0, 6, 'NERACA (31 DESEMBER 2025)', 0, 1, 'C')
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(0, 51, 102)
    pdf.set_text_color(255)
    pdf.cell(95, 6, '  ASET', 1, 0, 'C', fill=True)
    pdf.cell(5, 6, '', 0)
    pdf.cell(95, 6, '  KEWAJIBAN & EKUITAS', 1, 1, 'C', fill=True)
    pdf.set_text_color(0)
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(95, 5, '  Kas & Bank', 1); pdf.cell(5, 5, '', 0)
    pdf.cell(95, 5, '  Utang Usaha', 1, 1)
    pdf.cell(95, 5, '  Rp1.500.000.000', 1, 0, 'R'); pdf.cell(5, 5, '', 0)
    pdf.cell(95, 5, '  Rp2.000.000.000', 1, 1, 'R')
    pdf.cell(95, 5, '  Piutang Usaha', 1); pdf.cell(5, 5, '', 0)
    pdf.cell(95, 5, '  Utang Bank', 1, 1)
    pdf.cell(95, 5, '  Rp3.200.000.000', 1, 0, 'R'); pdf.cell(5, 5, '', 0)
    pdf.cell(95, 5, '  Rp1.500.000.000', 1, 1, 'R')
    pdf.cell(95, 5, '  Persediaan Barang', 1); pdf.cell(5, 5, '', 0)
    pdf.cell(95, 5, '  Utang Pajak', 1, 1)
    pdf.cell(95, 5, '  Rp4.000.000.000', 1, 0, 'R'); pdf.cell(5, 5, '', 0)
    pdf.cell(95, 5, '  Rp800.000.000', 1, 1, 'R')
    pdf.cell(95, 5, '  Aset Tetap (net)', 1); pdf.cell(5, 5, '', 0)
    pdf.cell(95, 5, '  Modal Disetor', 1, 1)
    pdf.cell(95, 5, '  Rp6.000.000.000', 1, 0, 'R'); pdf.cell(5, 5, '', 0)
    pdf.cell(95, 5, '  Rp5.000.000.000', 1, 1, 'R')
    pdf.cell(95, 5, '  Aset Lainnya', 1); pdf.cell(5, 5, '', 0)
    pdf.cell(95, 5, '  Laba Ditahan', 1, 1)
    pdf.cell(95, 5, '  Rp500.000.000', 1, 0, 'R'); pdf.cell(5, 5, '', 0)
    pdf.cell(95, 5, '  Rp5.900.000.000', 1, 1, 'R')
    pdf.set_font('Helvetica', 'B', 8)
    pdf.cell(95, 5, '  TOTAL ASET', 1, 0, 'R'); pdf.cell(5, 5, '', 0)
    pdf.cell(95, 5, '  TOTAL KEWAJIBAN & EKUITAS', 1, 1, 'R')
    pdf.cell(95, 5, '  Rp15.200.000.000', 1, 0, 'R'); pdf.cell(5, 5, '', 0)
    pdf.cell(95, 5, '  Rp15.200.000.000', 1, 1, 'R')
    pdf.output(os.path.join(OUT, 'profil-neraca-pt-niaga.pdf'))

# ========== 14B. LAPORAN LABA RUGI ==========
def laba_rugi():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 7, 'PT NIAGA PRATAMA SEJAHTERA', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, 'LAPORAN LABA RUGI KOMERSIAL - TAHUN 2025', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(230, 230, 240)
    pdf.cell(140, 6, '  Pos', 1, 0, 'L', fill=True)
    pdf.cell(0, 6, 'Jumlah (Rp)', 1, 1, 'C', fill=True)
    pdf.set_font('Helvetica', '', 9)
    items = [
        ('PENDAPATAN', '', 'B'),
        ('  Penjualan (Omzet)', '25.000.000.000', ''),
        ('  Pendapatan Bunga Deposito', '75.000.000', ''),
        ('  Laba Selisih Kurs', '30.000.000', ''),
        ('TOTAL PENDAPATAN', '25.105.000.000', 'B'),
        ('', '', ''),
        ('BIAYA USAHA', '', 'B'),
        ('  Beban Gaji & Tunjangan (8 kary)', '960.000.000', ''),
        ('  Beban Transportasi', '120.000.000', ''),
        ('  Beban Sewa Gedung', '240.000.000', ''),
        ('  Beban ATK & Perlengkapan', '75.000.000', ''),
        ('  Beban Listrik, Air, Telepon', '96.000.000', ''),
        ('  Beban Pemasaran', '180.000.000', ''),
        ('  Beban Penyusutan', '150.000.000', ''),
        ('  Beban Pemeliharaan', '60.000.000', ''),
        ('  Beban Bunga Pinjaman Bank', '120.000.000', ''),
        ('  Beban Asuransi', '45.000.000', ''),
        ('TOTAL BIAYA USAHA', '2.046.000.000', 'B'),
        ('', '', ''),
        ('LABA SEBELUM PAJAK', '23.059.000.000', 'B'),
    ]
    for d, v, bold in items:
        if not d:
            pdf.ln(2); continue
        is_b = bold == 'B'
        pdf.set_font('Helvetica', 'B' if is_b else '', 9)
        pdf.cell(140, 5, f'  {d}', 1)
        pdf.cell(0, 5, f'Rp {v}', 1, 1, 'R')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.cell(0, 3, 'Omzet Rp25M < Rp50M, menggunakan fasilitas Pasal 31E.', 0, 1)
    pdf.output(os.path.join(OUT, 'laba-rugi-komersial.pdf'))

# ========== 14C. REKAP PPh 21 KARYAWAN ==========
def rekap_pph21():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 7, 'PT NIAGA PRATAMA SEJAHTERA', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, 'REKAP PPh 21 KARYAWAN - TAHUN 2025', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 7)
    pdf.set_fill_color(0, 51, 102)
    pdf.set_text_color(255)
    hd = ['No', 'Nama', 'Status', 'Gaji Bruto/thn', 'Neto/thn', 'PKP', 'PPh 21/thn']
    wd = [8, 35, 14, 32, 32, 30, 32]
    for i, h in enumerate(hd):
        pdf.cell(wd[i], 6, h, 1, 0, 'C', fill=True)
    pdf.set_text_color(0)
    pdf.ln()
    data = [
        ('1', 'Andi Pratama', 'K/1', '129.000.000', '114.000.000', '51.000.000', '2.550.000'),
        ('2', 'Sari Dewi', 'TK/0', '72.000.000', '63.600.000', '9.600.000', '480.000'),
        ('3', 'Bambang', 'K/2', '180.000.000', '159.000.000', '91.500.000', '7.725.000'),
        ('4', 'Rina Fitri', 'TK/1', '96.000.000', '84.800.000', '26.300.000', '1.315.000'),
        ('5', 'Dodi', 'K/1', '150.000.000', '132.600.000', '69.600.000', '5.440.000'),
        ('6', 'Mega', 'TK/0', '60.000.000', '53.000.000', '0', '0'),
        ('7', 'Hendra', 'K/3', '237.000.000', '209.400.000', '137.400.000', '15.610.000'),
        ('8', 'Ani Wulandari', 'TK/2', '108.000.000', '95.400.000', '31.900.000', '1.595.000'),
    ]
    pdf.set_font('Helvetica', '', 7)
    for row in data:
        for i, v in enumerate(row):
            align = 'R' if i >= 4 else 'L'
            pdf.cell(wd[i], 5, v, 1, 0, align)
        pdf.ln()
    pdf.set_font('Helvetica', 'B', 7)
    pdf.cell(8, 5, '', 1); pdf.cell(35, 5, 'TOTAL', 1, 0, 'C')
    pdf.cell(14, 5, '', 1); pdf.cell(32, 5, '1.032.000.000', 1, 0, 'R')
    pdf.cell(32, 5, '912.000.000', 1, 0, 'R'); pdf.cell(30, 5, '417.300.000', 1, 0, 'R')
    pdf.cell(32, 5, '34.715.000', 1, 1, 'R')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.multi_cell(0, 3, 'Catatan: PPh 21 di atas adalah total setahun. Disetor per bulan ke kas negara melalui ID Billing.')
    pdf.output(os.path.join(OUT, 'rekap-pph21-tahunan.pdf'))

# ========== 14D. DAFTAR BUKTI POTONG & FAKTUR ==========
def rekap_transaksi():
    pdf = Doc()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 7, 'PT NIAGA PRATAMA SEJAHTERA', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 4, 'REKAP TRANSAKSI PAJAK TAHUN 2025', 0, 1, 'C')
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(2)
    # PPh 22
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'PPh 22 - Impor & Pembelian', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 8)
    for l, v in [('Impor (API) - Nilai Impor Rp2M', 'PPh 22 = 2,5% x Rp2M = Rp50.000.000'),
                  ('Pembelian Pemerintah - Rp500jt', 'PPh 22 = 1,5% x Rp500jt = Rp7.500.000')]:
        pdf.cell(5, 4, '', 0); pdf.cell(0, 4, l, 0, 1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(140, 5, '  Total PPh 22 Dipungut', 1); pdf.cell(0, 5, 'Rp57.500.000', 1, 1, 'R')
    pdf.ln(2)
    # PPh 23
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'PPh 23 - Jasa & Royalti', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 8)
    for l, v in [('Jasa Konsultan - Rp350jt', 'PPh 23 = 2% x Rp350jt = Rp7.000.000'),
                  ('Royalti Software - Rp120jt', 'PPh 23 = 15% x Rp120jt = Rp18.000.000'),
                  ('Sewa Alat Berat - Rp90jt', 'PPh 23 = 2% x Rp90jt = Rp1.800.000')]:
        pdf.cell(5, 4, '', 0); pdf.cell(0, 4, l, 0, 1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(140, 5, '  Total PPh 23 Dipotong', 1); pdf.cell(0, 5, 'Rp26.800.000', 1, 1, 'R')
    pdf.ln(2)
    # PPh 26
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'PPh 26 - Pembayaran ke LN', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(5, 4, '', 0); pdf.cell(0, 4, 'Royalti ke Jepang Rp500jt - Treaty 10%: PPh 26 = Rp50.000.000', 0, 1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(140, 5, '  Total PPh 26 Dipotong', 1); pdf.cell(0, 5, 'Rp50.000.000', 1, 1, 'R')
    pdf.ln(2)
    # PPN
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'PPN - Sepanjang Tahun', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 8)
    for l, v in [('Total Pajak Keluaran (12 bulan)', 'Rp412.500.000'),
                  ('Total Pajak Masukan (12 bulan)', 'Rp275.000.000'),
                  ('PPN Kurang Bayar Setahun', 'Rp137.500.000')]:
        pdf.cell(5, 4, '', 0); pdf.cell(0, 4, l, 0, 1)
    pdf.ln(2)
    # PBB
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 5, 'PBB & BPHTB', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(5, 4, '', 0); pdf.cell(0, 4, 'PBB Tanah & Bangunan (NJOP Rp1,85M): Rp367.600', 0, 1)
    pdf.cell(5, 4, '', 0); pdf.cell(0, 4, 'BPHTB (beli gedung Rp2M - NPOPTKP Rp80jt): 5% x Rp1,92M = Rp96.000.000', 0, 1)
    pdf.output(os.path.join(OUT, 'rekap-transaksi-pajak.pdf'))

if __name__ == '__main__':
    profil_perusahaan(); print('OK: profil-neraca-pt-niaga.pdf')
    laba_rugi(); print('OK: laba-rugi-komersial.pdf')
    rekap_pph21(); print('OK: rekap-pph21-tahunan.pdf')
    rekap_transaksi(); print('OK: rekap-transaksi-pajak.pdf')

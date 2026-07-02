from fpdf import FPDF
import os

OUT = r'C:\Users\ACER\Documents\GitHub\BrevetAB-VirtualLab\bab-1-kup'

class Doc(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 7)
        self.cell(0, 8, f'Simulasi Brevet Pajak AB - Halaman {self.page_no()}/{{nb}}', 0, 0, 'C')

def kop_djp(pdf, judul):
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 5, 'KEMENTERIAN KEUANGAN REPUBLIK INDONESIA', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(0, 4, 'DIREKTORAT JENDERAL PAJAK', 0, 1, 'C')
    pdf.set_text_color(0)
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 7, judul, 0, 1, 'C')
    pdf.ln(2)


def garis(pdf, y):
    pdf.set_draw_color(180)
    pdf.line(10, y, 200, y)


# ========== 1A. FORM NPWP ==========
def form_npwp():
    pdf = Doc()
    pdf.alias_nb_pages()
    kop_djp(pdf, 'FORMULIR PENDAFTARAN NPWP OP')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Lampiran PER-04/PJ/2020', 0, 1, 'R')
    pdf.ln(2)

    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 6, 'A. DATA DIRI', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    fields = [
        ('Nama Lengkap', 'sesuai KTP'),
        ('NIK', '16 digit'),
        ('Tempat Lahir', ''),
        ('Tanggal Lahir', 'dd/mm/yyyy'),
        ('Jenis Kelamin', 'L / P'),
        ('Status Perkawinan', 'TK / K / KH'),
        ('Nama Ibu Kandung', ''),
        ('Alamat Lengkap', ''),
        ('RT / RW', ''),
        ('Kelurahan/Desa', ''),
        ('Kecamatan', ''),
        ('Kabupaten/Kota', ''),
        ('Kode Pos', ''),
        ('No. Telepon', ''),
        ('Email', ''),
    ]
    for label, hint in fields:
        pdf.cell(55, 6, f'  {label}', 1)
        pdf.set_text_color(150)
        pdf.cell(0, 6, f'  {hint}', 1, 1)
        pdf.set_text_color(0)

    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 6, 'B. PEKERJAAN', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for label in ['Pekerjaan', 'Bidang Usaha', 'Penghasilan Bruto Setahun']:
        pdf.cell(55, 6, f'  {label}', 1)
        pdf.cell(0, 6, '  ', 1, 1)

    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 6, 'C. PERNYATAAN', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 8)
    pdf.multi_cell(0, 4,
        'Saya menyatakan bahwa data yang diisi adalah benar dan bertanggung jawab penuh '
        'atas kebenaran data tersebut sesuai ketentuan peraturan perundang-undangan perpajakan.')
    pdf.ln(2)
    pdf.cell(90, 5, '', 0, 0)
    pdf.cell(80, 5, 'Pemohon,', 0, 1, 'C')
    pdf.ln(10)
    pdf.cell(90, 5, '', 0, 0)
    pdf.cell(80, 5, '(_______________________)', 0, 1, 'C')

    pdf.output(os.path.join(OUT, 'form-npwp-op.pdf'))


# ========== 1B. KARTU NPWP ==========
def kartu_npwp():
    pdf = FPDF('L', 'mm', (100, 160))
    pdf.add_page()
    # Background
    pdf.set_fill_color(0, 51, 102)
    pdf.rect(0, 0, 160, 100, 'F')

    pdf.set_text_color(255)
    pdf.set_font('Helvetica', 'B', 7)
    pdf.cell(0, 5, 'KEMENTERIAN KEUANGAN RI', 0, 1, 'C',)
    pdf.set_font('Helvetica', 'B', 6)
    pdf.cell(0, 3, 'DIREKTORAT JENDERAL PAJAK', 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(0, 8, 'NPWP', 0, 1, 'C')
    pdf.set_font('Courier', 'B', 18)
    pdf.cell(0, 10, '12.345.678.9-012.000', 0, 1, 'C')

    pdf.set_font('Helvetica', '', 7)
    pdf.ln(2)
    pdf.cell(0, 4, 'NIK: 3273010101900001', 0, 1, 'C')
    pdf.cell(0, 4, 'Nama: ANDI PRASETYO', 0, 1, 'C')
    pdf.cell(0, 4, 'Status: TK/0 (Belum Kawin, 0 tanggungan)', 0, 1, 'C')
    pdf.ln(2)
    pdf.cell(0, 4, 'Alamat: Jl. Merdeka No. 45, Jakarta Pusat', 0, 1, 'C')
    pdf.ln(4)
    pdf.set_font('Helvetica', 'I', 5)
    pdf.cell(0, 3, 'Berlaku sejak terdaftar', 0, 1, 'C')
    pdf.set_text_color(0)

    pdf.output(os.path.join(OUT, 'kartu-npwp.pdf'))


# ========== 1C. SKPKB ==========
def skpkb():
    pdf = Doc()
    pdf.alias_nb_pages()
    kop_djp(pdf, 'SURAT KETETAPAN PAJAK KURANG BAYAR')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Nomor : SKPKB-00001/WPJ.01/2026', 0, 1, 'R')
    pdf.cell(0, 4, 'Tanggal : 15 Maret 2026', 0, 1, 'R')
    pdf.ln(3)

    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 6, 'DATA WAJIB PAJAK', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    data = [
        ('Nama WP', 'Andi Prasetyo'),
        ('NPWP', '12.345.678.9-012.000'),
        ('Jenis Pajak', 'PPh Pasal 21'),
        ('Masa Pajak', 'Januari - Desember 2025'),
    ]
    for l, v in data:
        pdf.cell(45, 5, f'  {l}', 1)
        pdf.cell(0, 5, f'  {v}', 1, 1)

    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 6, 'RINCIAN KETETAPAN', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    rincian = [
        ('Pajak Penghasilan terutang', 'Rp  4.850.000'),
        ('Kredit Pajak', 'Rp  3.200.000'),
        ('Pajak yang Kurang Dibayar (Pokok)', 'Rp  1.650.000'),
        ('Sanksi Administrasi (bunga 2% x 12 bln)', 'Rp    396.000'),
        ('JUMLAH YANG HARUS DIBAYAR', 'Rp  2.046.000'),
    ]
    for l, v in rincian:
        pdf.cell(120, 6, f'  {l}', 1)
        pdf.set_font('Helvetica', 'B', 9) if 'JUMLAH' in l else pdf.set_font('Helvetica', '', 9)
        pdf.cell(0, 6, v, 1, 1, 'R')

    pdf.ln(3)
    pdf.set_font('Helvetica', '', 8)
    pdf.multi_cell(0, 4,
        'Berdasarkan hasil pemeriksaan, diterbitkan Surat Ketetapan Pajak Kurang Bayar '
        'sebesar Rp2.046.000 (dua juta empat puluh enam ribu rupiah) yang harus dilunasi '
        'paling lambat 30 hari sejak tanggal penerbitan.')
    pdf.ln(2)
    pdf.cell(0, 4, 'Jakarta, 15 Maret 2026', 0, 1, 'R')
    pdf.cell(0, 4, 'Kepala Kantor Pelayanan Pajak', 0, 1, 'R')
    pdf.ln(10)
    pdf.cell(0, 4, '(_________________________)', 0, 1, 'R')

    pdf.output(os.path.join(OUT, 'skpkb.pdf'))


# ========== 1D. STP ==========
def stp():
    pdf = Doc()
    pdf.alias_nb_pages()
    kop_djp(pdf, 'SURAT TAGIHAN PAJAK')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Nomor : STP-00045/WPJ.01/2026', 0, 1, 'R')
    pdf.cell(0, 4, 'Tanggal : 20 Maret 2026', 0, 1, 'R')
    pdf.ln(3)

    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 6, 'DATA WAJIB PAJAK', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for l, v in [('Nama WP', 'Andi Prasetyo'), ('NPWP', '12.345.678.9-012.000')]:
        pdf.cell(45, 5, f'  {l}', 1)
        pdf.cell(0, 5, f'  {v}', 1, 1)

    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 6, 'RINCIAN TAGIHAN', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    rincian = [
        ('Jenis Pajak', 'PPh Pasal 21'),
        ('Masa Pajak', 'Februari 2026'),
        ('Dasar Pengenaan', 'SKPKB-00001/WPJ.01/2026'),
        ('Pokok Kurang Bayar', 'Rp 1.650.000'),
        ('Sanksi Bunga (2% x 1 bln)', 'Rp    33.000'),
        ('JUMLAH YANG HARUS DIBAYAR', 'Rp 1.683.000'),
    ]
    for l, v in rincian:
        pdf.cell(120, 6, f'  {l}', 1)
        pdf.set_font('Helvetica', 'B', 9) if 'JUMLAH' in l else pdf.set_font('Helvetica', '', 9)
        pdf.cell(0, 6, v, 1, 1, 'R')

    pdf.ln(4)
    pdf.set_font('Helvetica', '', 8)
    pdf.multi_cell(0, 4,
        'STP ini diterbitkan karena terdapat sanksi administrasi berupa bunga atas '
        'keterlambatan pembayaran pajak. Pembayaran paling lambat 1 (satu) bulan sejak '
        'tanggal penerbitan.')

    pdf.output(os.path.join(OUT, 'stp.pdf'))


# ========== 1E. SPT MASA (form kosong) ==========
def spt_masa():
    pdf = Doc()
    pdf.alias_nb_pages()
    kop_djp(pdf, 'SURAT PEMBERITAHUAN MASA PPN')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Formulir 1111', 0, 1, 'R')
    pdf.ln(2)

    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 6, 'IDENTITAS PKP', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for l in ['Nama PKP', 'NPWP', 'Masa Pajak', 'Masa Pajak']:
        pdf.cell(45, 5, f'  {l}', 1)
        pdf.cell(0, 5, '  (isi)', 1, 1)

    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 6, 'INDIKASI', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 8)
    indikasi = [
        'I. PENYERAHAN YANG TERUTANG PPN',
        '   A. Ekspor BKP Berwujud',
        '   B. Penyerahan BKP/JKP kepada Pemungut',
        '   C. Penyerahan BKP/JKP kepada yg bukan Pemungut',
        '   D. Penyerahan yang PPN-nya tidak dipungut',
        '   E. Diserahkan dengan FP 070',
        'II. EKSPOR',
        'III. PEMAKAIAN SENDIRI / PEMBERIAN CUMA-CUMA',
        'IV. PENYERAHAN KEPADA PEMERINTAH',
    ]
    for item in indikasi:
        pdf.cell(10, 4, '', 0)
        pdf.cell(0, 4, item, 0, 1)

    pdf.ln(1)
    pdf.set_font('Helvetica', '', 7)
    pdf.multi_cell(0, 3.5, 'Catatan: Formulir ini adalah format kosong untuk latihan pengisian SPT Masa PPN.')

    pdf.output(os.path.join(OUT, 'spt-masa-1111-kosong.pdf'))


# ========== 1F. SPT TAHUNAN 1770S (form kosong) ==========
def spt_tahunan():
    pdf = Doc()
    pdf.alias_nb_pages()
    kop_djp(pdf, 'SURAT PEMBERITAHUAN TAHUNAN PPh WP OP')
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 4, 'Formulir 1770S - Tahun Pajak 2025', 0, 1, 'R')
    pdf.ln(2)

    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 6, 'A. IDENTITAS WP', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    for l in ['Nama WP', 'NPWP', 'Pekerjaan', 'Status PTKP']:
        pdf.cell(45, 5, f'  {l}', 1)
        pdf.cell(0, 5, '  (isi)', 1, 1)

    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 6, 'B. PENGHASILAN NETO', 1, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9)
    items = [
        '1. Penghasilan Neto Dalam Negeri dari Pekerjaan',
        '2. Penghasilan Neto Dalam Negeri dari Usaha',
        '3. Penghasilan Neto Luar Negeri',
        '4. Jumlah Penghasilan Neto (1+2+3)',
    ]
    for item in items:
        pdf.cell(120, 5, f'  {item}', 1)
        pdf.cell(0, 5, '  Rp', 1, 1)

    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(220, 230, 241)
    pdf.cell(0, 6, 'C. PENGURANG', 1, 1, 'L', fill=True)
    items2 = [
        '5. PTKP',
        '6. PKP (4 - 5)',
        '7. PPh Terutang (tarif Pasal 17)',
        '8. Kredit Pajak (PPh 21/22/23/24)',
        '9. PPh Kurang/Lebih Bayar',
    ]
    for item in items2:
        pdf.cell(120, 5, f'  {item}', 1)
        pdf.cell(0, 5, '  Rp', 1, 1)

    pdf.ln(3)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.multi_cell(0, 3.5, 'Catatan: Formulir ini adalah format kosong untuk latihan pengisian SPT Tahunan PPh OP.')

    pdf.output(os.path.join(OUT, 'spt-tahunan-1770S-kosong.pdf'))


# ========== RUN ALL ==========
if __name__ == '__main__':
    form_npwp()
    print('OK: form-npwp-op.pdf')
    kartu_npwp()
    print('OK: kartu-npwp.pdf')
    skpkb()
    print('OK: skpkb.pdf')
    stp()
    print('OK: stp.pdf')
    spt_masa()
    print('OK: spt-masa-1111-kosong.pdf')
    spt_tahunan()
    print('OK: spt-tahunan-1770S-kosong.pdf')

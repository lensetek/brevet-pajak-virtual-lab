"""Generate Buku Brevet Pajak AB - Format UNESCO B5 (176x250mm)
Menggabungkan materi modul + konten simulasi per bab menjadi 1 buku utuh.
Font: DejaVuSans (Unicode, support bahasa Indonesia).
"""
import os, sys
from fpdf import FPDF, XPos, YPos

FONT_DIR = r'C:\Windows\Fonts'
OUT_DIR = r'C:\Users\ACER\Documents\GitHub\BrevetAB-VirtualLab'
BAB_DIRS = [f'bab-{i}' for i in range(1, 15)]
BAB_DIRS[0] = 'bab-1-kup'
BAB_DIRS[1] = 'bab-2-pph-op'
BAB_DIRS[2] = 'bab-3-pph-badan'
BAB_DIRS[3] = 'bab-4-pph-21'
BAB_DIRS[4] = 'bab-5-pph-23'
BAB_DIRS[5] = 'bab-6-pph-22'
BAB_DIRS[6] = 'bab-7-pph-26'
BAB_DIRS[7] = 'bab-8-pph-final'
BAB_DIRS[8] = 'bab-9-ppn'
BAB_DIRS[9] = 'bab-10-pbb'
BAB_DIRS[10] = 'bab-11-bea-meterai'
BAB_DIRS[11] = 'bab-12-bphtb'
BAB_DIRS[12] = 'bab-13-coretax'
BAB_DIRS[13] = 'bab-14-studi-kasus-terpadu'

BAB_TITLES = [
    'Ketentuan Umum dan Tata Cara Perpajakan (KUP)',
    'Pajak Penghasilan (PPh) Orang Pribadi',
    'Pajak Penghasilan (PPh) Badan',
    'Pajak Penghasilan (PPh) Pasal 21',
    'Pajak Penghasilan (PPh) Pasal 23',
    'Pajak Penghasilan (PPh) Pasal 22',
    'Pajak Penghasilan (PPh) Pasal 26',
    'Pajak Penghasilan (PPh) Pasal 4 Ayat (2)',
    'Pajak Pertambahan Nilai (PPN) & PPnBM',
    'Pajak Bumi dan Bangunan (PBB)',
    'Bea Meterai',
    'Bea Perolehan Hak atas Tanah dan Bangunan (BPHTB)',
    'Coretax',
    'Studi Kasus Terpadu',
]

BAB_SUB = [
    'KUP',
    'PPh OP',
    'PPh Badan',
    'PPh 21',
    'PPh 23',
    'PPh 22',
    'PPh 26',
    'PPh Final 4(2)',
    'PPN & PPnBM',
    'PBB',
    'Bea Meterai',
    'BPHTB',
    'Coretax',
    'Terpadu',
]

W = 176  # mm UNESCO B5
H = 250
MARGIN = 15
CONTENT_W = W - 2 * MARGIN


def register_fonts(pdf):
    """Register TrueType fonts from Windows Fonts"""
    font_map = {}
    candidates = [
        ('DejaVuSans.ttf', 'DejaVuSans', ''),
        ('DejaVuSans-Bold.ttf', 'DejaVuSans', 'B'),
        ('DejaVuSans-Oblique.ttf', 'DejaVuSans', 'I'),
        ('DejaVuSans-BoldOblique.ttf', 'DejaVuSans', 'BI'),
    ]
    for fname, family, style in candidates:
        path = os.path.join(FONT_DIR, fname)
        if os.path.exists(path):
            try:
                pdf.add_font(family, style, path, uni=True)
                font_map[(family, style)] = True
            except:
                pass
    # Fallback: try arial
    for fname, family, style in [('arial.ttf', 'Arial', ''), ('arialbd.ttf', 'Arial', 'B'),
                                   ('ariali.ttf', 'Arial', 'I'), ('arialbi.ttf', 'Arial', 'BI')]:
        if (family, style) in font_map:
            continue
        path = os.path.join(FONT_DIR, fname)
        if os.path.exists(path):
            try:
                pdf.add_font(family, style, path, uni=True)
                font_map[(family, style)] = True
            except:
                pass
    return font_map


class BukuPDF(FPDF):
    def __init__(self, _fonts):
        super().__init__('P', 'mm', (176, 250))
        self._font_map = _fonts
        self.chapter_title = ''
        self.chapter_num = 0

    def header(self):
        if self.page_no() <= 2:
            return
        self.set_font('DejaVuSans', 'I', 6)
        self.set_text_color(120, 120, 120)
        self.cell(0, 4, f'Brevet Pajak AB — {self.chapter_title}', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        self.set_draw_color(200, 200, 200)
        self.line(MARGIN, self.get_y()+1, W - MARGIN, self.get_y()+1)
        self.ln(3)

    def footer(self):
        if self.page_no() <= 2:
            return
        self.set_y(-12)
        self.set_font('DejaVuSans', 'I', 7)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, f'{self.page_no()}', new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')


def add_paragraph(pdf, text, size=10, bold=False, indent=0, spacing=5):
    """Add paragraph with word wrap"""
    pdf.set_font('DejaVuSans', 'B' if bold else '', size)
    x_start = MARGIN + indent
    pdf.set_x(x_start)
    w = CONTENT_W - indent
    pdf.multi_cell(w, size * 0.45, text)
    pdf.ln(spacing * 0.3)


def add_bullet(pdf, text, size=10, indent=10):
    pdf.set_x(MARGIN + indent)
    pdf.set_font('DejaVuSans', '', size)
    pdf.multi_cell(CONTENT_W - indent - 5, size * 0.45, f'-  {text}')
    pdf.ln(1)


def add_numbered(pdf, num, text, size=10, indent=10):
    pdf.set_x(MARGIN + indent)
    pdf.set_font('DejaVuSans', '', size)
    pdf.multi_cell(CONTENT_W - indent - 5, size * 0.45, f'{num}.  {text}')
    pdf.ln(1)


def generate_cover(pdf):
    """Generate book cover"""
    pdf.add_page()
    pdf.ln(40)
    pdf.set_font('DejaVuSans', 'B', 24)
    pdf.set_text_color(0, 51, 102)
    pdf.multi_cell(0, 12, 'BREVET PAJAK\nA & B', align='C')
    pdf.ln(5)
    pdf.set_font('DejaVuSans', '', 14)
    pdf.set_text_color(60, 60, 60)
    pdf.cell(0, 8, 'Modul Pembelajaran & Simulasi Praktik', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    pdf.ln(3)
    pdf.set_draw_color(0, 51, 102)
    pdf.set_line_width(0.8)
    y = pdf.get_y()
    pdf.line(MARGIN + 30, y, W - MARGIN - 30, y)
    pdf.ln(8)
    pdf.set_font('DejaVuSans', '', 10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 6, 'PT. Asadel Liamsindo Teknologi', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    pdf.cell(0, 6, 'asadel.co.id/courses/brevet-ab', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    pdf.ln(5)
    pdf.set_font('DejaVuSans', 'I', 9)
    pdf.multi_cell(0, 5, 'Mencakup 14 bab + Virtual Lab dengan 105 dokumen simulasi, studi kasus, dan pendekatan Agentic AI untuk laporan pajak.', align='C')
    pdf.set_text_color(0)


def generate_toc(pdf):
    """Generate table of contents"""
    pdf.add_page()
    pdf.set_font('DejaVuSans', 'B', 14)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 10, 'DAFTAR ISI', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    pdf.ln(5)
    pdf.set_text_color(0)
    pdf.set_draw_color(180, 180, 180)
    y0 = pdf.get_y()
    for i, (title, sub) in enumerate(zip(BAB_TITLES, BAB_SUB)):
        n = i + 1
        pdf.set_font('DejaVuSans', 'B', 10)
        pdf.cell(10, 7, f'{n}.', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_font('DejaVuSans', '', 10)
        pdf.cell(140, 7, title, new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_font('DejaVuSans', 'I', 9)
        pdf.set_text_color(130, 130, 130)
        pdf.cell(0, 7, sub, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='R')
        pdf.set_text_color(0)
        pdf.line(MARGIN, pdf.get_y() + 0.5, W - MARGIN, pdf.get_y() + 0.5)
        pdf.ln(1)
    # Check if we have a second page of TOC
    pdf.ln(5)
    pdf.set_font('DejaVuSans', 'I', 9)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 5, 'Setiap bab terdiri dari: Ringkasan Materi, Dokumen Simulasi, Studi Kasus, Soal, dan Kunci Jawaban.', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    pdf.set_text_color(0)


def generate_chapter(pdf, num, title, sub, bab_dir):
    """Generate one chapter from existing content"""
    pdf.chapter_title = f'Bab {num}: {title}'
    pdf.chapter_num = num

    # Chapter title page
    pdf.add_page()
    pdf.ln(25)
    pdf.set_font('DejaVuSans', '', 10)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 6, f'BAB {num}', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    pdf.ln(3)
    pdf.set_font('DejaVuSans', 'B', 18)
    pdf.set_text_color(30, 30, 30)
    pdf.multi_cell(0, 10, title, align='C')
    pdf.ln(2)
    pdf.set_font('DejaVuSans', '', 10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 6, sub, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    pdf.set_text_color(0)
    pdf.ln(5)
    pdf.set_draw_color(0, 51, 102)
    pdf.set_line_width(0.5)
    y = pdf.get_y()
    pdf.line(MARGIN + 40, y, W - MARGIN - 40, y)
    pdf.ln(8)

    # Content
    pdf.set_font('DejaVuSans', '', 9)
    pdf.set_text_color(50, 50, 50)

    # Load and format content from the actual generate.py for this chapter
    content = get_chapter_content(num, title, sub, bab_dir)
    for block in content:
        t = block.get('type', 'para')
        text = block.get('text', '')
        if t == 'para':
            add_paragraph(pdf, text, size=10, bold=block.get('bold', False))
        elif t == 'subtitle':
            pdf.ln(2)
            pdf.set_font('DejaVuSans', 'B', 12)
            pdf.set_text_color(0, 51, 102)
            pdf.set_x(MARGIN)
            pdf.multi_cell(CONTENT_W, 7, text)
            pdf.set_text_color(50, 50, 50)
            pdf.ln(2)
        elif t == 'bullet':
            add_bullet(pdf, text, size=10)
        elif t == 'numbered':
            add_numbered(pdf, block.get('num', '1'), text, size=10)
        elif t == 'spacer':
            pdf.ln(int(text))
        elif t == 'box':
            pdf.set_fill_color(240, 244, 250)
            pdf.set_x(MARGIN + 5)
            pdf.set_font('DejaVuSans', 'B', 9)
            pdf.set_text_color(0, 51, 102)
            pdf.multi_cell(CONTENT_W - 10, 5, text, fill=True)
            pdf.set_text_color(50, 50, 50)
            pdf.ln(3)
        elif t == 'code':
            pdf.set_fill_color(245, 245, 245)
            pdf.set_font('DejaVuSans', '', 8)
            pdf.set_x(MARGIN + 5)
            pdf.multi_cell(CONTENT_W - 10, 4.5, text, fill=True)
            pdf.ln(2)
        elif t == 'subhead':
            pdf.ln(1)
            pdf.set_font('DejaVuSans', 'B', 11)
            pdf.set_text_color(0, 70, 130)
            pdf.set_x(MARGIN)
            pdf.multi_cell(CONTENT_W, 6, text)
            pdf.set_text_color(50, 50, 50)
            pdf.ln(1)
        elif t == 'newpage':
            pdf.add_page()


def get_chapter_content(num, title, sub, bab_dir):
    """Return formatted content blocks for each chapter."""
    base = os.path.join(OUT_DIR, bab_dir)

    blocks = [
        {'type': 'subtitle', 'text': 'Ringkasan Materi'},
        {'type': 'para', 'text': f'Bab ini membahas tentang {title.lower()}. Berikut adalah poin-poin penting yang harus dipahami sebelum memulai simulasi praktik.'},
        {'type': 'spacer', 'text': '2'},
    ]

    if num == 1:
        blocks += [
            {'type': 'subhead', 'text': 'A. Definisi Pajak'},
            {'type': 'para', 'text': 'Pajak adalah kontribusi wajib kepada negara yang bersifat memaksa berdasarkan undang-undang, tidak mendapatkan imbalan langsung, dan digunakan untuk keperluan negara bagi kemakmuran rakyat. Pajak dipungut oleh pemerintah pusat (DJP) maupun daerah dari orang pribadi atau badan untuk membiayai pengeluaran umum, pembangunan infrastruktur, dan layanan publik.'},
            {'type': 'subhead', 'text': 'B. Fungsi Pajak'},
            {'type': 'para', 'text': 'Terdapat empat fungsi utama pajak. Fungsi Anggaran (Budgetair) sebagai sumber pendapatan negara untuk membiayai pengeluaran negara. Fungsi Mengatur (Regulerend) sebagai alat untuk mengatur pertumbuhan ekonomi. Fungsi Stabilitas untuk mengendalikan inflasi melalui kebijakan fiskal. Fungsi Redistribusi Pendapatan untuk membiayai kepentingan umum dan pembangunan.'},
            {'type': 'subhead', 'text': 'C. Sistem Pemungutan Pajak'},
            {'type': 'para', 'text': 'Indonesia mengenal tiga sistem pemungutan pajak: Self-Assessment System di mana Wajib Pajak berperan aktif menghitung, membayar, dan melaporkan pajak terutang melalui SPT; Official Assessment System di mana besarnya pajak ditetapkan oleh fiskus melalui surat ketetapan; dan Withholding System di mana pihak ketiga memotong atau memungut pajak yang terutang.'},
            {'type': 'subhead', 'text': 'D. Subjek dan Objek Pajak'},
            {'type': 'para', 'text': 'Subjek pajak adalah pihak (orang/badan) yang dikenakan pajak, sedangkan objek pajak adalah penghasilan atau nilai ekonomis yang dikenakan pajak. Subjek pajak dibagi menjadi subjek pajak dalam negeri dan subjek pajak luar negeri.'},
            {'type': 'subhead', 'text': 'E. NPWP dan SPT'},
            {'type': 'para', 'text': 'Nomor Pokok Wajib Pajak (NPWP) adalah nomor identitas resmi dari Direktorat Jenderal Pajak yang wajib dimiliki individu/badan untuk administrasi perpajakan. Sejak 2024-2025, NIK (16 digit) resmi digunakan sebagai NPWP bagi Wajib Pajak orang pribadi penduduk. Surat Pemberitahuan (SPT) adalah surat yang digunakan Wajib Pajak untuk melaporkan penghitungan dan/atau pembayaran pajak. SPT terdiri dari SPT Masa (bulanan) dan SPT Tahunan.'},
            {'type': 'subhead', 'text': 'F. Surat Ketetapan Pajak'},
            {'type': 'para', 'text': 'Hasil pemeriksaan pajak dapat menghasilkan beberapa jenis surat ketetapan: SKPKB (Surat Ketetapan Pajak Kurang Bayar), SKPLB (Surat Ketetapan Pajak Lebih Bayar), SKPN (Surat Ketetapan Pajak Nihil), dan STP (Surat Tagihan Pajak). Wajib Pajak memiliki hak untuk mengajukan keberatan dan banding atas ketetapan pajak.'},
            {'type': 'spacer', 'text': '2'},
            {'type': 'box', 'text': 'STUDI KASUS — Buka file studi-kasus.pdf di folder bab-1-kup/ untuk latihan: (1) Isi Formulir NPWP, (2) Analisis SKPKB dan STP, (3) Hitung sanksi keterlambatan, (4) Latihan pengisian SPT.'},
            {'type': 'spacer', 'text': '2'},
            {'type': 'subhead', 'text': 'G. Dokumen Simulasi Virtual Lab'},
            {'type': 'bullet', 'text': 'form-npwp-op.pdf — Formulir pendaftaran NPWP untuk latihan pengisian'},
            {'type': 'bullet', 'text': 'kartu-npwp.pdf — Contoh kartu NPWP dengan data fiktif'},
            {'type': 'bullet', 'text': 'skpkb.pdf — Surat Ketetapan Pajak Kurang Bayar'},
            {'type': 'bullet', 'text': 'stp.pdf — Surat Tagihan Pajak dengan sanksi administrasi'},
            {'type': 'bullet', 'text': 'spt-masa-1111-kosong.pdf — Formulir SPT Masa PPN untuk latihan'},
            {'type': 'bullet', 'text': 'spt-tahunan-1770S-kosong.pdf — Formulir SPT Tahunan PPh OP'},
        ]
    else:
        # Generic chapter structure for remaining chapters
        chapter_data = {
            2: {
                'title': 'Pajak Penghasilan Orang Pribadi',
                'sections': [
                    ('A. Konsep Dasar', 'PPh Orang Pribadi adalah pajak atas penghasilan yang diterima individu dalam satu tahun pajak, baik dari pekerjaan maupun usaha. Setiap pekerjaan, jasa, atau kegiatan dapat menjadi objek pajak jika penghasilannya melebihi PTKP. Pajak ini dilaporkan melalui SPT Tahunan dan tarifnya dikenakan berjenjang berdasarkan lapisan Penghasilan Kena Pajak.'),
                    ('B. PTKP (Penghasilan Tidak Kena Pajak)', 'PTKP adalah batas penghasilan yang tidak dikenakan pajak. Besaran PTKP: TK/0 = Rp54.000.000, K/0 = Rp58.500.000, K/1 = Rp63.000.000, K/2 = Rp67.500.000, K/3 = Rp72.000.000. Maksimal 3 tanggungan. PTKP mencerminkan prinsip keadilan pajak — semakin besar tanggungan, semakin kecil pajak yang dibayar.'),
                    ('C. Tarif Progresif Pasal 17', 'Lapisan Penghasilan Kena Pajak: s.d. Rp60.000.000 (5%), >Rp60.000.000 s.d. Rp250.000.000 (15%), >Rp250.000.000 s.d. Rp500.000.000 (25%), >Rp500.000.000 (30%).'),
                    ('D. Mekanisme 6 Langkah', 'Langkah 1: Hitung Penghasilan Bruto setahun. Langkah 2: Kurangi biaya jabatan dan iuran pensiun menjadi Penghasilan Neto. Langkah 3: Kurangi PTKP menjadi PKP. Langkah 4: Terapkan tarif progresif. Langkah 5: Kurangi kredit pajak. Langkah 6: Tentukan status kurang bayar, nihil, atau lebih bayar.'),
                ],
                'kasus': 'Buka studi-kasus.pdf di folder bab-2-pph-op/. Hitung PPh OP untuk: (1) Siti TK/0 — gaji Rp5.050.000/bln, (2) Doni K/2 — gaji Rp19.750.000/bln, (3) Amir K/1 — neto Rp300jt/thn. Gunakan slip gaji dan tabel PTKP sebagai referensi.',
                'dokumen': [
                    'slip-gaji-siti-tk0.pdf — Slip gaji karyawan status TK/0',
                    'slip-gaji-doni-k2.pdf — Slip gaji karyawan status K/2',
                    'bukti-potong-1721-A1-amir.pdf — Bukti potong PPh 21',
                    'spt-1770S-terisi-amir.pdf — SPT Tahunan OP terisi',
                    'tabel-ptkp.pdf — Tabel referensi PTKP',
                ]
            },
            3: {
                'title': 'PPh Badan',
                'sections': [
                    ('A. Konsep PPh Badan', 'PPh Badan adalah pajak yang dikenakan atas laba bersih yang diperoleh badan usaha dalam satu tahun pajak. Terdapat PPh Final (selesai saat dibayar, tidak dapat dikreditkan) dan PPh Tidak Final (dapat dikreditkan di SPT Tahunan).'),
                    ('B. Subjek Pajak Badan', 'Subjek DN: PT, CV, BUMN, koperasi, yayasan, firma, kongsi, dana pensiun. Subjek LN: badan asing yang menerima penghasilan dari Indonesia, baik melalui BUT maupun tidak. Berlaku prinsip World Wide Income bagi WP Badan DN.'),
                    ('C. Tarif PPh Badan', 'Perusahaan umum: 22%. Perusahaan Tbk dengan minimal 40% saham publik: 19%. Omzet < Rp50M (Pasal 31E): 11% untuk PKP s.d. Rp4,8M, sisanya 22%. UMKM (omzet < Rp4,8M): 0,5% final.'),
                    ('D. Rekonsiliasi Fiskal', 'Proses penyesuaian laba komersial menjadi laba fiskal. Koreksi Positif: beban yang tidak diakui fiskal (natura, sanksi pajak, penyusutan komersial > fiskal). Koreksi Negatif: penghasilan yang bukan objek pajak (pendapatan final, laba selisih kurs belum realisasi).'),
                ],
                'kasus': 'Buka studi-kasus.pdf di folder bab-3-pph-badan/. Gunakan laporan laba rugi dan rekonsiliasi fiskal untuk hitung PPh Badan 3 skenario: (1) Pasal 31E omzet Rp30M, (2) Perusahaan besar omzet > Rp50M, (3) UMKM final.',
                'dokumen': [
                    'lap-laba-rugi-komersial.pdf — Laporan laba rugi',
                    'rekonsiliasi-fiskal.pdf — Kertas kerja koreksi fiskal',
                    'spt-1771-pph-badan.pdf — SPT Tahunan PPh Badan',
                    'tabel-tarif-pph-badan.pdf — Referensi tarif',
                ]
            },
            4: {
                'title': 'PPh Pasal 21',
                'sections': [
                    ('A. Konsep Withholding Tax', 'PPh 21 dipotong oleh pemberi kerja atas penghasilan berupa gaji, upah, honorarium, dan pembayaran lain. Pegawai adalah subjek pajak, perusahaan adalah pemotong. PPh 21 adalah pembayaran di muka dari PPh Orang Pribadi.'),
                    ('B. Objek PPh 21', 'Pegawai Tetap: gaji, tunjangan, THR, bonus, lembur, natura tertentu. Pegawai Tidak Tetap: upah harian, mingguan, borongan. Bukan Pegawai: honor konsultan, tenaga ahli dengan DPP 50%. Peserta Kegiatan: panitia, narasumber.'),
                    ('C. Komponen Pengurang', 'Biaya Jabatan: 5% dari penghasilan bruto, maks Rp500.000/bulan atau Rp6.000.000/tahun. Iuran Pensiun: dibayar karyawan ke dana pensiun yang disahkan. BPJS: iuran yang dibayar sendiri oleh karyawan.'),
                    ('D. Tarif Efektif Rata-rata (TER)', 'Skema pemotongan PPh 21 bulanan menggunakan tarif efektif berdasarkan kategori (A, B, C) dan tingkat penghasilan. Diterapkan untuk menyederhanakan perhitungan PPh 21 masa.'),
                ],
                'kasus': 'Buka studi-kasus.pdf di folder bab-4-pph-21/. Hitung PPh 21 untuk 5 karyawan PT Maju Sejahtera + 1 konsultan. Gunakan slip gaji dan payroll summary untuk mengecek hasil.',
                'dokumen': [
                    'slip-gaji-budi.pdf — Karyawan K/1 gaji Rp10.750.000',
                    'slip-gaji-rina.pdf — Karyawan TK/1 gaji Rp7.200.000',
                    'slip-gaji-ahmad.pdf — Karyawan K/1 gaji Rp12.500.000',
                    'bukti-potong-1721-A1-budi.pdf — Bukti potong setahun',
                    'invoice-honorarium-konsultan.pdf — Honor bukan pegawai',
                    'payroll-summary-januari-2026.pdf — Rekap payroll',
                ]
            },
            5: {
                'title': 'PPh Pasal 23',
                'sections': [
                    ('A. Karakteristik', 'PPh 23 dipotong atas penghasilan berupa dividen, bunga, royalti, sewa, dan jasa tertentu yang diterima WP DN. Mekanisme B2B, berbeda dengan PPh 21 yang merupakan hubungan kerja.'),
                    ('B. Tarif', '15%: dividen, bunga, royalti, hadiah, penghargaan. 2%: sewa harta non-tanah/bangunan, jasa teknik, manajemen, konsultan, konstruksi, dan jasa lainnya sesuai PMK 141/2015. 15% fintech DN, 20% fintech LN (PMK 69/2022).'),
                    ('C. Pengecualian', 'Pembayaran kepada bank, sewa guna usaha dengan hak opsi, dividen saham dengan kepemilikan >= 25% dari laba ditahan, SHU koperasi kepada anggota, jasa keuangan penyalur pinjaman.'),
                ],
                'kasus': 'Buka studi-kasus.pdf di folder bab-5-pph-23/. Hitung PPh 23 untuk 3 transaksi: jasa konsultan Rp200jt, royalti Rp80jt, sewa alat Rp45jt. Gunakan e-Bupot dan tabel tarif.',
                'dokumen': [
                    'invoice-jasa-konsultan-200jt.pdf — Invoice jasa',
                    'invoice-royalti-80jt.pdf — Invoice royalti',
                    'invoice-sewa-alat-45jt.pdf — Invoice sewa alat',
                    'bukti-potong-pph23-e-bupot.pdf — Bukti potong elektronik',
                    'tabel-tarif-pph23.pdf — Tabel tarif & pengecualian',
                ]
            },
            6: {
                'title': 'PPh Pasal 22',
                'sections': [
                    ('A. Karakteristik', 'PPh 22 dipungut (bukan dipotong) oleh pihak tertentu terkait arus barang. Bersifat tidak final dan menjadi kredit pajak untuk SPT Tahunan. Obyek utamanya adalah kegiatan impor, pembelian barang oleh pemerintah, dan penjualan hasil produksi industri tertentu.'),
                    ('B. Pemungut', 'Bank Devisa & DJBC (atas impor), Bendahara Pemerintah (atas pembelian barang), BUMN tertentu, Industri semen/kertas/baja/otomotif/farmasi, ATPM kendaraan bermotor, Produsen migas, dan Pedagang pengumpul.'),
                    ('C. Tarif Berdasarkan Transaksi', 'Impor API 2,5%, non-API 7,5%, pembelian pemerintah 1,5%, penjualan semen 0,25%, baja 0,3%, otomotif 0,45%, kertas 0,1%, ekspor tambang 1,5%, penjualan rumah mewah >Rp30M 1%, pesawat/yacht 5%.'),
                ],
                'kasus': 'Buka studi-kasus.pdf di folder bab-6-pph-22/. Hitung PPh 22 atas: (1) impor laptop CIF Rp6M, (2) pembelian pemerintah Rp200jt, (3) identifikasi tarif 5 transaksi.',
                'dokumen': [
                    'pib-impor-pph22.pdf — PIB perhitungan impor',
                    'kuitansi-pemerintah-pph22.pdf — Kuitansi bendahara',
                    'tabel-tarif-pph22.pdf — Tabel 16 jenis tarif',
                ]
            },
            7: {
                'title': 'PPh Pasal 26',
                'sections': [
                    ('A. Konsep PPh 26', 'PPh 26 adalah pemotongan atas penghasilan yang dibayarkan kepada Wajib Pajak Luar Negeri (WPLN) selain BUT di Indonesia. Ini adalah "versi internasional" dari PPh 23. Subjeknya adalah WPLN: orang pribadi atau badan luar negeri yang menerima penghasilan dari Indonesia.'),
                    ('B. Tarif', 'Tarif umum 20% dari jumlah bruto untuk dividen, bunga, royalti, sewa, jasa. Penjualan harta di Indonesia oleh WPLN: 5% (20% x 25% perkiraan neto). Penjualan saham oleh WPLN: 5%. Premi asuransi LN: 20% dari perkiraan neto. Branch Profit Tax: 20% dari laba setelah pajak BUT.'),
                    ('C. Tax Treaty (P3B)', 'Perjanjian Penghindaran Pajak Berganda memungkinkan tarif lebih rendah. Contoh: Indonesia-Jepang untuk royalti 10%, Indonesia-Singapura 10%. Syarat: Form DGT/SKD WPLN yang divalidasi otoritas pajak negara domisili. Dokumen sangat penting dalam tax planning global.'),
                ],
                'kasus': 'Buka studi-kasus.pdf di folder bab-7-pph-26/. Hitung PPh 26: (1) royalti ke Jepang dengan & tanpa treaty, (2) jasa IT dari Singapura, (3) branch profit tax.',
                'dokumen': [
                    'invoice-luar-negeri-royalti.pdf — Invoice royalti Jepang',
                    'invoice-jasa-luar-negeri.pdf — Invoice jasa Singapura',
                    'form-dgt-skd-wpln.pdf — Form DGT untuk treaty',
                    'tabel-tarif-pph26-treaty.pdf — Tabel tarif & treaty',
                ]
            },
            8: {
                'title': 'PPh Final Pasal 4 Ayat (2)',
                'sections': [
                    ('A. Konsep PPh Final', 'PPh Final adalah pajak penghasilan yang bersifat final, artinya pajak yang dipotong/dibayar tidak dapat dikreditkan dari total PPh terutang di akhir tahun. Penghasilan yang sudah dikenakan PPh Final tidak digabung dalam penghitungan SPT Tahunan, hanya dilaporkan saja.'),
                    ('B. Objek dan Tarif', 'Bunga deposito/tabungan: 20%. Bunga obligasi: 15%. Hadiah undian: 25%. Transaksi saham: 0,1% (non-pendiri), 0,5% (pendiri). Dividen OP: 10%. Sewa tanah/bangunan: 10%. Pengalihan tanah/bangunan: 2,5%. Jasa konstruksi: 2% (kecil), 3% (sedang), 4% (besar). UMKM: 0,5%.'),
                    ('C. Karakteristik Penting', 'PPh Final tidak dapat dikreditkan di SPT Tahunan. Biaya untuk menghasilkan penghasilan final tidak dapat dikurangkan dari PKP. Tujuannya untuk kemudahan administrasi dan tarif yang lebih sederhana.'),
                ],
                'kasus': 'Buka studi-kasus.pdf di folder bab-8-pph-final/. Hitung PPh Final untuk: (1) UMKM Rp50jt, (2) sewa bangunan Rp120jt, (3) multi transaksi: deposito + hadiah + konstruksi + UMKM.',
                'dokumen': [
                    'bukti-potong-final-umkm.pdf — UMKM 0,5%',
                    'kuitansi-sewa-bangunan.pdf — Sewa bangunan 10%',
                    'bunga-deposito-final.pdf — Bunga deposito 20%',
                    'hadiah-undian-final.pdf — Hadiah undian 25%',
                    'bukti-potong-jasa-konstruksi.pdf — Jasa konstruksi 3%',
                    'tabel-tarif-final.pdf — Tabel 14 objek final',
                ]
            },
            9: {
                'title': 'PPN & PPnBM',
                'sections': [
                    ('A. Konsep Dasar PPN', 'PPN adalah pajak atas konsumsi barang dan jasa di dalam Daerah Pabean. Bersifat tidak langsung (ditanggung konsumen, dipungut penjual). Menggunakan sistem kredit pajak (input-output). Dikenakan pada setiap rantai distribusi. Tarif dasar 11% (UU HPP). Ekspor BKP: 0%.'),
                    ('B. Mekanisme Input-Output', 'Pajak Keluaran (PK) = PPN yang dipungut saat menjual barang/jasa. Pajak Masukan (PM) = PPN yang dibayar saat membeli. PPN terutang = PK - PM. Jika PK > PM: kurang bayar (setor). Jika PM > PK: lebih bayar (restitusi).'),
                    ('C. Faktur Pajak', 'Faktur Pajak adalah bukti pungutan PPN. Setiap PKP wajib membuat Faktur Pajak untuk setiap penyerahan BKP/JKP. Faktur Pajak Masukan menjadi dasar pengkreditan PM. Retur mengurangi PK dan PM pada masa pajak terjadinya retur.'),
                    ('D. PPnBM', 'Pajak Penjualan atas Barang Mewah: single-stage (dikenakan 1x di hulu), tidak dapat dikreditkan. Tarif 20%-75% tergantung kategori barang mewah. Barang biasa kena PPN saja, barang mewah kena PPN + PPnBM.'),
                ],
                'kasus': 'Buka studi-kasus.pdf di folder bab-9-ppn/. Hitung: (1) PPN terutang PK - PM Rp150jt - Rp100jt, (2) retur Rp10jt, (3) PPnBM mobil mewah 30%.',
                'dokumen': [
                    'faktur-pajak-keluaran-150jt.pdf — FP Keluaran',
                    'faktur-pajak-masukan-100jt.pdf — FP Masukan',
                    'nota-retur.pdf — Nota retur barang',
                    'spt-masa-ppn-1111-januari.pdf — SPT Masa PPN',
                    'contoh-ppnbm-mobil-mewah.pdf — PPnBM mobil',
                ]
            },
            10: {
                'title': 'Pajak Bumi dan Bangunan',
                'sections': [
                    ('A. Konsep PBB', 'PBB adalah pungutan atas keberadaan bumi dan/atau bangunan yang memberikan manfaat ekonomi. Bersifat kebendaan (object-based tax). Dikelola oleh pemerintah daerah (PBB-P2). Dibayar setiap tahun.'),
                    ('B. Komponen Perhitungan', 'NJOP (Nilai Jual Objek Pajak): harga rata-rata tanah dan bangunan menurut pemerintah. NJOPTKP (Nilai Jual Tidak Kena Pajak): Rp12.000.000. NJKP (Nilai Jual Kena Pajak): 20% untuk NJOP < Rp1M, 40% untuk NJOP > Rp1M. Tarif PBB: 0,5% x NJKP.'),
                    ('C. Faktor Pengaruh PBB', 'Besaran PBB dipengaruhi oleh: lokasi properti, luas tanah, luas bangunan, NJOP per meter persegi, dan persentase NJKP. Semakin strategis lokasi, semakin tinggi PBB.'),
                ],
                'kasus': 'Buka studi-kasus.pdf di folder bab-10-pbb/. Hitung PBB dari SPPT: tanah 500m2, bangunan 400m2. Bandingkan NJOP antar zona.',
                'dokumen': [
                    'sppt-pbb.pdf — SPPT PBB lengkap',
                    'bukti-bayar-pbb.pdf — Bukti pembayaran PBB',
                    'tabel-njop-zona.pdf — NJOP per zona Jakarta',
                ]
            },
            11: {
                'title': 'Bea Meterai',
                'sections': [
                    ('A. Konsep Bea Meterai', 'Bea Meterai adalah pajak atas dokumen yang terutang saat dokumen ditandatangani. Bukan pajak atas transaksi, tetapi atas dokumen yang memiliki kekuatan hukum. Bersifat tidak langsung dengan tarif tetap.'),
                    ('B. Tarif dan Objek', 'Tarif: Rp10.000 per dokumen (berlaku sejak 1 Januari 2021). Flat, tidak tergantung nilai transaksi. Objek: surat perjanjian, akta notaris, akta PPAT, surat berharga, kuitansi > Rp5jt, dokumen lelang. Bukan objek: kuitansi < Rp5jt, ijazah, tanda terima gaji, kuitansi pajak, surat gadai.'),
                    ('C. Mekanisme Pelunasan', 'Meterai Tempel (fisik) untuk dokumen kertas, dan e-Meterai (digital) untuk dokumen elektronik. Dokumen tanpa meterai tidak memiliki kekuatan hukum sebagai alat bukti di pengadilan.'),
                ],
                'kasus': 'Buka studi-kasus.pdf di folder bab-11-bea-meterai/. Identifikasi: kuitansi Rp10jt (kena), Rp3jt (tidak kena), surat perjanjian (kena). Gunakan tabel objek meterai.',
                'dokumen': [
                    'kuitansi-meterai-10jt.pdf — Kuitansi kena meterai',
                    'kuitansi-non-meterai-3jt.pdf — Kuitansi tidak kena',
                    'surat-perjanjian-sewa.pdf — Perjanjian 2 halaman',
                    'tabel-objek-meterai.pdf — Tabel objek vs bukan',
                ]
            },
            12: {
                'title': 'BPHTB',
                'sections': [
                    ('A. Konsep BPHTB', 'Bea Perolehan Hak atas Tanah dan Bangunan adalah pajak atas perolehan hak atas tanah dan/atau bangunan. Bersifat sekali bayar (one-off tax), dikelola oleh pemerintah daerah. Tanpa bayar BPHTB maka sertifikat tidak bisa diproses.'),
                    ('B. Tarif dan Perhitungan', 'Tarif: 5% dari NPOP Kena Pajak. NPOP Kena Pajak = NPOP - NPOPTKP. NPOPTKP minimal Rp60jt (jual beli) atau Rp300jt (waris/hibah wasiat untuk OP). Objek BPHTB: jual beli, hibah, warisan, tukar menukar, lelang, pemasukan ke badan usaha.'),
                    ('C. Perbedaan PBB vs BPHTB', 'PBB: pajak kepemilikan (tahunan), berbasis NJOP, tarif 0,3-0,5%. BPHTB: pajak transaksi (sekali), berbasis NPOP/harga transaksi, tarif 5%. Keduanya dikelola daerah namun memiliki fungsi berbeda.'),
                ],
                'kasus': 'Buka studi-kasus.pdf di folder bab-12-bphtb/. Hitung BPHTB untuk: (1) jual beli rumah Rp500jt, (2) warisan Rp1M. Bandingkan NPOPTKP.',
                'dokumen': [
                    'sspd-bphtb.pdf — Surat setoran BPHTB',
                    'ajb-kutipan.pdf — Akta Jual Beli',
                    'tabel-npoptkp.pdf — NPOPTKP per daerah',
                ]
            },
            13: {
                'title': 'Coretax',
                'sections': [
                    ('A. Sistem Coretax', 'Coretax adalah sistem administrasi perpajakan digital terintegrasi yang dikelola Direktorat Jenderal Pajak. Mencakup seluruh proses perpajakan: pendaftaran, pembayaran, pelaporan, dan pemantauan kepatuhan secara elektronik.'),
                    ('B. Komponen Utama', 'ID Billing: kode unik untuk pembayaran pajak. e-Bupot: aplikasi bukti potong PPh 23/26 elektronik. e-Faktur: aplikasi faktur pajak PPN elektronik. e-SPT: pelaporan SPT elektronik. Seluruh sistem terintegrasi dalam portal DJP Online.'),
                    ('C. Keuntungan Digitalisasi', 'Efisiensi waktu, pengurangan kesalahan administrasi, rekonsiliasi data otomatis, pengarsipan digital, kemudahan akses data perpajakan, dan transparansi proses.'),
                ],
                'kasus': 'Buka studi-kasus.pdf di folder bab-13-coretax/. Praktik pembuatan ID Billing, rekap e-Bupot, rekonsiliasi e-Faktur, dan verifikasi SPT elektronik.',
                'dokumen': [
                    'id-billing-pph21.pdf — ID Billing PPh 21',
                    'e-bupot-rekap-23.pdf — Rekap bukti potong 23',
                    'e-faktur-rekap-ppn.pdf — Rekap faktur pajak',
                    'bukti-penerimaan-spt-elektronik.pdf — BPS elektronik',
                ]
            },
            14: {
                'title': 'Studi Kasus Terpadu',
                'sections': [
                    ('A. Pendahuluan', 'Bab ini merupakan studi kasus komprehensif yang menggabungkan seluruh materi dari Bab 1 sampai Bab 13 dalam satu perusahaan fiktif: PT Niaga Pratama Sejahtera. Tujuannya adalah memberikan pengalaman menyelesaikan siklus perpajakan perusahaan secara utuh.'),
                    ('B. Profil Perusahaan', 'PT Niaga Pratama Sejahtera: NPWP 02.345.678.9-012.000, bidang perdagangan barang konsumsi, omzet Rp25M, PKP sejak 2020, 8 karyawan tetap. Omzet < Rp50M sehingga menggunakan fasilitas Pasal 31E. Bukan Tbk, kepemilikan publik < 40%.'),
                    ('C. Cakupan Pajak', 'PPh 21 (8 karyawan), PPh Badan (koreksi fiskal + 31E), PPh 22 (impor & pemerintah), PPh 23 (jasa, royalti, sewa), PPh 26 (royalti ke Jepang treaty 10%), PPN (PK-PM setahun), PBB, BPHTB.'),
                    ('D. Tugas', 'Selesaikan seluruh kewajiban perpajakan: hitung PPh 21, lakukan rekonsiliasi fiskal, hitung PPh Badan dengan kredit pajak, hitung PPN kurang bayar, hitung PBB dan BPHTB, lalu buat ringkasan total beban pajak.'),
                ],
                'kasus': 'Buka studi-kasus.pdf di folder bab-14-studi-kasus-terpadu/. Selesaikan 5 tahap: PPh 21, PPh Badan + kredit pajak, PPN, PBB & BPHTB, dan kesimpulan total beban pajak terhadap omzet.',
                'dokumen': [
                    'profil-neraca-pt-niaga.pdf — Profil & neraca',
                    'laba-rugi-komersial.pdf — Laporan laba rugi',
                    'rekap-pph21-tahunan.pdf — PPh 21 8 karyawan',
                    'rekap-transaksi-pajak.pdf — Semua transaksi pajak',
                ]
            },
        }

        data = chapter_data.get(num, {})
        for sec_title, sec_text in data.get('sections', []):
            blocks.append({'type': 'subhead', 'text': sec_title})
            blocks.append({'type': 'para', 'text': sec_text})
            blocks.append({'type': 'spacer', 'text': '1'})

        blocks.append({'type': 'spacer', 'text': '2'})
        blocks.append({'type': 'box', 'text': f'STUDI KASUS — {data.get("kasus", "")}'})

        blocks.append({'type': 'spacer', 'text': '2'})
        blocks.append({'type': 'subhead', 'text': 'Virtual Lab — Dokumen Simulasi'})

        for d in data.get('dokumen', []):
            blocks.append({'type': 'bullet', 'text': d})
    blocks += [
        {'type': 'spacer', 'text': '3'},
        {'type': 'box', 'text': f'Semua dokumen simulasi tersedia di folder {bab_dir}/. Buka file PDF dan gunakan bersama studi-kasus.pdf serta soal.pdf untuk praktik mandiri.'},
    ]
    return blocks


def generate_book():
    """Generate complete book PDF"""
    pdf = BukuPDF({})
    pdf.set_auto_page_break(auto=True, margin=20)

    # Register fonts on this instance
    fonts = register_fonts(pdf)
    if ('DejaVuSans', '') not in fonts:
        print('ERROR: DejaVuSans font not found. Book generation requires DejaVuSans.')
        sys.exit(1)
    pdf._font_map = fonts

    # Cover
    generate_cover(pdf)

    # TOC
    generate_toc(pdf)

    # Chapters
    for i, (title, sub, bab_dir) in enumerate(zip(BAB_TITLES, BAB_SUB, BAB_DIRS)):
        num = i + 1
        full_path = os.path.join(OUT_DIR, bab_dir)
        if not os.path.exists(full_path):
            print(f'  WARNING: {bab_dir} not found, skipping...')
            continue
        print(f'  Generating Bab {num}: {title}...')
        generate_chapter(pdf, num, title, sub, bab_dir)
        # Add page break between chapters
        pdf.ln(5)

    # Output
    out_path = os.path.join(OUT_DIR, 'Buku-Brevet-Pajak-AB-Lengkap.pdf')
    pdf.output(out_path)
    print(f'\nDONE: {out_path}')
    print(f'Total pages: {pdf.page_no()}')


if __name__ == '__main__':
    generate_book()

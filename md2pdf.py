"""Convert markdown files to PDF using fpdf2.
Usage: python md2pdf.py <file.md> [output.pdf]
"""
import sys, re, os
from fpdf import FPDF

# Non-ASCII char map for fpdf2 core fonts
_CHARMAP = {
    '–': '-', '—': '-', '―': '--',
    '‘': "'", '’': "'", '“': '"', '”': '"',
    '•': '*', '…': '...',
    '≈': '~',  # ≈
    '→': '->',  # →
    '≤': '<=', '≥': '>=',
    '±': '+-',
    '×': 'x',
    '÷': '/',
}

def _sanitize(text):
    """Replace non-latin-1 chars with ASCII equivalents"""
    result = []
    for ch in text:
        if ch in _CHARMAP:
            result.append(_CHARMAP[ch])
        elif ord(ch) > 255:
            result.append('?')
        else:
            result.append(ch)
    return ''.join(result)

class MD2PDF(FPDF):
    def __init__(self, title=''):
        super().__init__()
        self.alias_nb_pages()
        self.title_text = title
        self._h1 = False

    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 7)
        self.cell(0, 8, f'Simulasi Brevet Pajak AB - Halaman {self.page_no()}/{{nb}}', 0, 0, 'C')

    def section(self, text):
        """Render a horizontal line as section separator"""
        self.ln(1)
        self.set_draw_color(180)
        self.set_line_width(0.3)
        y = self.get_y()
        self.line(10, y, 200, y)
        self.ln(3)

    def heading(self, level, text):
        text = _sanitize(text)
        if level == 1:
            self.ln(3)
            self.set_font('Helvetica', 'B', 13)
            self.set_text_color(0, 51, 102)
            self.multi_cell(0, 7, text)
            self.set_text_color(0)
            self.ln(2)
        elif level == 2:
            self.ln(2)
            self.set_font('Helvetica', 'B', 11)
            self.set_text_color(0, 70, 130)
            self.multi_cell(0, 6, text)
            self.set_text_color(0)
            self.ln(1)
        elif level == 3:
            self.ln(1)
            self.set_font('Helvetica', 'BI', 10)
            self.multi_cell(0, 5.5, text)
            self.ln(0.5)

    def bullet(self, text, indent=10):
        text = _sanitize(text)
        self.set_x(self.l_margin + indent)
        self.set_font('Helvetica', '', 9)
        clean = text.replace('**', '')
        self.multi_cell(w=self.w - self.l_margin - indent - 10, h=5, text=f'-  {clean}')
        self.ln(1)

    def numbered(self, num, text, indent=10):
        text = _sanitize(text)
        self.set_x(self.l_margin + indent)
        self.set_font('Helvetica', '', 9)
        clean = text.replace('**', '')
        self.multi_cell(w=self.w - self.l_margin - indent - 10, h=5, text=f'{num}.  {clean}')
        self.ln(1)

    def paragraph(self, text):
        text = _sanitize(text)
        self.set_font('Helvetica', '', 9)
        clean = text.replace('**', '')
        self.multi_cell(0, 5, clean)
        self.ln(1)

    def bold_para(self, text):
        text = _sanitize(text)
        self.set_font('Helvetica', 'B', 9)
        self.multi_cell(0, 5, text)
        self.set_font('Helvetica', '', 9)
        self.ln(1)

    def code_block(self, text):
        self.ln(1)
        self.set_fill_color(240, 240, 245)
        self.set_font('Courier', '', 8)
        lines = text.split('\n')
        for line in lines:
            self.set_x(15)
            # Use cell instead of multi_cell to avoid word wrap issues
            self.cell(185, 4.5, line[:120], 0, 1, 'L', fill=True)
        self.ln(2)

    def _write_rich(self, text, size):
        """Handle **bold** and other inline formatting"""
        clean = text.replace('**', '')


def md_to_pdf(md_path, pdf_path):
    pdf = MD2PDF()
    pdf.add_page()

    # Kop
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 5, 'KEMENTERIAN KEUANGAN REPUBLIK INDONESIA', 0, 1, 'C')
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(0, 4, 'DIREKTORAT JENDERAL PAJAK', 0, 1, 'C')
    pdf.set_text_color(0)
    pdf.line(10, pdf.get_y()+1, 200, pdf.get_y()+1)
    pdf.ln(3)

    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    i = 0
    in_list = False
    list_num = 0
    in_code = False
    code_buf = []

    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()

        # Code block
        if stripped.startswith('```'):
            if in_code:
                pdf.code_block('\n'.join(code_buf))
                code_buf = []
                in_code = False
            else:
                in_code = True
                code_buf = []
            i += 1
            continue
        if in_code:
            code_buf.append(stripped)
            i += 1
            continue

        # Skip empty lines between blocks
        if not stripped:
            if in_list:
                in_list = False
                pdf.ln(1)
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^-{3,}$', stripped):
            pdf.section(stripped)
            i += 1
            continue

        # Level 1 heading
        if stripped.startswith('# '):
            in_list = False
            pdf.heading(1, stripped[2:])
            i += 1
            continue

        # Level 2 heading
        if stripped.startswith('## '):
            in_list = False
            pdf.heading(2, stripped[3:])
            i += 1
            continue

        # Level 3 heading
        if stripped.startswith('### '):
            in_list = False
            pdf.heading(3, stripped[4:])
            i += 1
            continue

        # Bold-only line (often used as label in these docs)
        if stripped.startswith('**') and stripped.endswith('**') and len(stripped) < 80:
            in_list = False
            pdf.bold_para(stripped[2:-2])
            i += 1
            continue

        # Numbered list item
        num_match = re.match(r'^(\d+)\.\s+(.*)', stripped)
        if num_match:
            in_list = True
            pdf.numbered(num_match.group(1), num_match.group(2))
            # Check if next line is indented continuation
            if i+1 < len(lines):
                next_s = lines[i+1].rstrip()
                if next_s.startswith(('  ', '\t')) and next_s.strip():
                    pdf.paragraph(next_s.strip())
                    i += 1
            i += 1
            continue

        # Bullet list
        if stripped.startswith('- ') or stripped.startswith('* '):
            in_list = True
            txt = stripped[2:] if stripped.startswith('- ') else stripped[2:]
            # Check for bold marker like **label** -- treat as bold para
            if txt.startswith('**') and '**' in txt[2:]:
                end = txt.index('**', 2)
                label = txt[2:end]
                rest = txt[end+2:].strip()
                pdf.set_font('Helvetica', 'B', 9)
                pdf.set_x(20)
                pdf.multi_cell(0, 5, label)
                if rest:
                    pdf.set_font('Helvetica', '', 9)
                    pdf.set_x(20)
                    pdf.multi_cell(0, 5, rest)
            else:
                pdf.bullet(txt)
            i += 1
            continue

        # Table row (| ... |)
        if stripped.startswith('|'):
            in_list = False
            cols = [c.strip() for c in stripped.split('|')[1:-1]]
            # Header row has bold markers
            is_header = all(c.startswith('**') and c.endswith('**') for c in cols if c)
            # Separator row
            if re.match(r'^[\s|:\-]+$', stripped):
                i += 1
                continue
            if is_header:
                pdf.set_font('Helvetica', 'B', 8)
                pdf.set_fill_color(0, 51, 102)
                pdf.set_text_color(255)
                widths = [190 // len(cols)] * len(cols)
                for ci, col in enumerate(cols):
                    w = widths[ci] if ci < len(widths) else 20
                    col_clean = col.replace('**', '')
                    pdf.cell(w, 5, f' {col_clean}', 1, 0, 'C', fill=True)
                pdf.set_text_color(0)
                pdf.ln()
            else:
                pdf.set_font('Helvetica', '', 8)
                widths = [190 // len(cols)] * len(cols)
                for ci, col in enumerate(cols):
                    w = widths[ci] if ci < len(widths) else 20
                    col_clean = col.replace('**', '')
                    align = 'R' if col_clean.startswith('Rp') else 'L'
                    pdf.cell(w, 4.5, f' {col_clean}', 1, 0, align)
                pdf.ln()
            i += 1
            continue

        # Regular paragraph
        in_list = False
        pdf.paragraph(stripped)
        i += 1

    pdf.output(pdf_path)
    return pdf_path


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python md2pdf.py <file.md> [output.pdf]')
        sys.exit(1)

    md_path = sys.argv[1]
    if len(sys.argv) >= 3:
        pdf_path = sys.argv[2]
    else:
        pdf_path = os.path.splitext(md_path)[0] + '.pdf'

    md_to_pdf(md_path, pdf_path)
    print(f'OK: {md_path} -> {pdf_path}')

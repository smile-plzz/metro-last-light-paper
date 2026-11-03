# -*- coding: utf-8 -*-
"""
generate_docx.py
Converts 12_FULL_RESEARCH_PAPER.md into a publication-ready DOCX manuscript
following APA 7th edition formatting standards.
"""

import os
import re
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

base_dir = r"C:\Users\ismai\.gemini\antigravity\scratch\research\metro-last-light"
md_path = os.path.join(base_dir, "12_FULL_RESEARCH_PAPER.md")
docx_path = os.path.join(base_dir, "Metro_Last_Light_Research_Paper.docx")

doc = docx.Document()

# Set standard 1-inch margins
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)

# Set base style font to Times New Roman
style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(12)
font.color.rgb = RGBColor(0x11, 0x11, 0x11)
style.paragraph_format.line_spacing = 1.25
style.paragraph_format.space_after = Pt(6)

with open(md_path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')

in_abstract = False
in_table = False
table_data = []

for line in lines:
    line_str = line.strip()
    
    # Title
    if line_str.startswith("# The Last Light of Humanity"):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(line_str.replace("# ", ""))
        run.bold = True
        run.font.size = Pt(18)
        run.font.name = 'Times New Roman'
        doc.add_paragraph() # spacing
        continue

    # Metadata block
    if line_str.startswith("**Lead Author:**") or line_str.startswith("**Affiliation:**") or line_str.startswith("**Target Venue:**") or line_str.startswith("**Date of Record:**") or line_str.startswith("**Research Status:**"):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        # parse bold
        clean_text = line_str.replace("**", "")
        parts = clean_text.split(":", 1)
        if len(parts) == 2:
            r1 = p.add_run(parts[0] + ": ")
            r1.bold = True
            r2 = p.add_run(parts[1].strip())
            r2.italic = True
        else:
            p.add_run(clean_text)
        continue

    # Abstract Header
    if line_str == "### Abstract":
        p = doc.add_paragraph()
        run = p.add_run("Abstract")
        run.bold = True
        run.font.size = Pt(14)
        run.font.name = 'Times New Roman'
        continue

    # Keywords
    if line_str.startswith("**Keywords:**"):
        p = doc.add_paragraph()
        r1 = p.add_run("Keywords: ")
        r1.bold = True
        r2 = p.add_run(line_str.replace("**Keywords:**", "").strip())
        r2.italic = True
        doc.add_paragraph() # space
        continue

    # Divider line
    if line_str == "---":
        continue

    # Headings
    if line_str.startswith("## "):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(line_str.replace("## ", ""))
        run.bold = True
        run.font.size = Pt(14)
        run.font.name = 'Times New Roman'
        continue

    if line_str.startswith("### "):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(line_str.replace("### ", ""))
        run.bold = True
        run.font.size = Pt(12.5)
        run.font.name = 'Times New Roman'
        continue

    if line_str.startswith("#### "):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(line_str.replace("#### ", ""))
        run.bold = True
        run.italic = True
        run.font.size = Pt(12)
        run.font.name = 'Times New Roman'
        continue

    # Table handling
    if line_str.startswith("|") and line_str.endswith("|"):
        # Table row
        cols = [c.strip() for c in line_str.split("|")[1:-1]]
        # check if delimiter row
        if all(re.match(r"^:?-+:?$", c) for c in cols):
            continue
        if not in_table:
            in_table = True
            table_data = []
        table_data.append(cols)
        continue
    else:
        if in_table:
            # Build docx table
            in_table = False
            if table_data:
                rows = len(table_data)
                cols = len(table_data[0])
                table = doc.add_table(rows=rows, cols=cols)
                table.alignment = WD_TABLE_ALIGNMENT.CENTER
                table.style = 'Table Grid'
                for r_idx, row in enumerate(table_data):
                    for c_idx, cell_value in enumerate(row):
                        cell = table.cell(r_idx, c_idx)
                        cell.text = cell_value.replace("**", "")
                        for p in cell.paragraphs:
                            p.paragraph_format.space_before = Pt(2)
                            p.paragraph_format.space_after = Pt(2)
                            for r in p.runs:
                                r.font.size = Pt(9.5)
                                r.font.name = 'Times New Roman'
                                if r_idx == 0:
                                    r.bold = True
                doc.add_paragraph() # spacing after table
                table_data = []

    # Code blocks or ASCII diagrams
    if line_str.startswith("```"):
        continue

    # Normal paragraph
    if line_str:
        p = doc.add_paragraph()
        # Simple inline formatting parsing: handle bold and italic
        # Regex to tokenize bold, italic, plain
        tokens = re.split(r'(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)', line_str)
        for token in tokens:
            if token.startswith("**") and token.endswith("**"):
                r = p.add_run(token[2:-2])
                r.bold = True
                r.font.name = 'Times New Roman'
            elif token.startswith("*") and token.endswith("*"):
                r = p.add_run(token[1:-1])
                r.italic = True
                r.font.name = 'Times New Roman'
            elif token.startswith("`") and token.endswith("`"):
                r = p.add_run(token[1:-1])
                r.font.name = 'Consolas'
                r.font.size = Pt(10)
            else:
                r = p.add_run(token)
                r.font.name = 'Times New Roman'

# If table ended at end of file
if in_table and table_data:
    rows = len(table_data)
    cols = len(table_data[0])
    table = doc.add_table(rows=rows, cols=cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = 'Table Grid'
    for r_idx, row in enumerate(table_data):
        for c_idx, cell_value in enumerate(row):
            cell = table.cell(r_idx, c_idx)
            cell.text = cell_value.replace("**", "")
            for p in cell.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(9.5)
                    r.font.name = 'Times New Roman'
                    if r_idx == 0:
                        r.bold = True

doc.save(docx_path)
print(f"Publication-ready Word manuscript successfully exported to {docx_path}")
print(f"File size: {os.path.getsize(docx_path)} bytes.")


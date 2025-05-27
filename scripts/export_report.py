import pandas as pd
from sqlalchemy import create_engine
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

# ✅ Step 1: Load DataFrame from database
engine = create_engine("sqlite:///db/grades.db")
df = pd.read_sql("students", con=engine)

# ✅ Step 2: Export to Excel
excel_file = "student_report.xlsx"
df.to_excel(excel_file, index=False)
print(f"✅ Excel report saved as {excel_file}")

# ✅ Step 3: Export to PDF
pdf_file = "student_report.pdf"
pdf = SimpleDocTemplate(pdf_file, pagesize=letter)

# Convert DataFrame to table data (header + rows)
data = [df.columns.tolist()] + df.values.tolist()

# Create table with style
table = Table(data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1f77b4")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
]))

# Build the PDF document
pdf.build([table])
print(f"✅ PDF report saved as {pdf_file}")

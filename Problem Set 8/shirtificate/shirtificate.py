from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 45)
pdf.cell(0, 60, "CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", 0.5, 70)

student_name = input("Name: ") + " took CS50"
pdf.set_font("helvetica", "", 25)
pdf.set_text_color(255, 255, 255)
pdf.cell(-190, 268, student_name, align="C")
pdf.output("shirtificate.pdf")
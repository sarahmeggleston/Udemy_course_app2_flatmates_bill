import os
import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    Object that creates a PDF report that shows the
    amount each flatmate will pay for the period of
    the bill
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # add icon
        pdf.image(name='files/house.png', w=30, h=30)

        # insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, ln=1, align='C')

        # insert Period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # insert name and amount due for flatmate1
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=str(flatmate1.pays(bill, flatmate2)), border=0, ln=1)

        # insert name and amount due for flatmate2
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=str(flatmate2.pays(bill, flatmate1)), border=0)

        # change directory and create pdf
        os.chdir("files")

        pdf.output(self.filename)
        webbrowser.open(self.filename)

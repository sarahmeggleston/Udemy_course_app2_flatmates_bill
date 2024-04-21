from fpdf import FPDF
import webbrowser

class Bill:
    """
    Object that contains data about a bill, such as
    total amount and the bill period.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Object that contains the name of the flatmate,
    the number of days they were in the house, and
    the portion of the bill they will pay.
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house /(self.days_in_house + flatmate2.days_in_house)
        return round(bill.amount * weight, 2)


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

        # create pdf
        pdf.output(self.filename)
        webbrowser.open(self.filename)


the_bill = Bill(120, "March 2021")
john = Flatmate("John", 20)
mary = Flatmate("Mary", 25)

print("John pays: {}".format(john.pays(the_bill, mary)))
print("Mary pays: {}".format(mary.pays(the_bill, john)))
pdf = PdfReport(filename='Bill.pdf')
pdf.generate(flatmate1=john, flatmate2=mary, bill=the_bill)

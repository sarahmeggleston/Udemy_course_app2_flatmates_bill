from flat import Bill, Flatmate
from reports import PdfReport

bill_amount = input("Enter the bill total: ")
bill_period = input("Enter the bill period (e.g. April 2024): ")
the_bill = Bill(amount=int(bill_amount), period=bill_period)

fm1_name = input("Enter the name of the first flatmate: ")
fm1_days = input("Enter the number of days {} was in the flat: ".format(fm1_name))
fm1 = Flatmate(name=fm1_name, days_in_house=int(fm1_days))

fm2_name = input("Enter the name of the second flatmate: ")
fm2_days = input("Enter the number of days {} was in the flat: ".format(fm2_name))
fm2 = Flatmate(name=fm2_name, days_in_house=int(fm2_days))

print("{} pays: {}".format(fm1.name,
                           (fm1.pays(bill=the_bill, flatmate2=fm2))))
print("{} pays: {}".format(fm2.name,
                           (fm2.pays(bill=the_bill, flatmate2=fm1))))

pdf = PdfReport(filename='{}.pdf'.format(the_bill.period))
pdf.generate(flatmate1=fm1,
             flatmate2=fm2,
             bill=the_bill)

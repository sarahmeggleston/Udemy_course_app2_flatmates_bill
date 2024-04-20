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

    def pays(self, bill):
        pass


class PdfReport:
    """
    Object that creates a PDF report that shows the
    amount each flatmate will pay for the period of
    the bill
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass

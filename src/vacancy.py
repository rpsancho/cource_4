class Vacancy:

    def __init__(self, title: str, url: str, payment: int, description: str, requirements: str):
        self.title = title
        self.url = url
        if payment is None:
            payment = 0
        self.payment = payment
        if description is None:
            self.description = ''
        else:
            self.description = description
        if requirements is None:
            self.requirements = ''
        else:
            self.requirements = requirements

    def __lt__(self, other):
        return self.payment < other.payment

    def __le__(self, other):
        return self.payment <= other.payment

    def __gt__(self, other):
        return self.payment > other.payment

    def __ge__(self, other):
        return self.payment >= other.payment

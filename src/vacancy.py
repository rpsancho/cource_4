class Vacancy:

    def __init__(self, title: str, url: str, payment: int, description: str, requirements: str):
        self.title = title
        self.url = url
        self.payment = payment
        self.description = description
        self.requirements = requirements

    def __lt__(self, other):
        return self.payment < other.payment

    def __le__(self, other):
        return self.payment <= other.payment

    def __gt__(self, other):
        return self.payment > other.payment

    def __ge__(self, other):
        return self.payment >= other.payment

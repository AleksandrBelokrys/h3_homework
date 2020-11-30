import uuid
from logger import logger


class Order:
    def __init__(self, customer, item, amount):
        self.id = uuid.uuid4()
        self.customer = customer
        self.item = item
        self.amount = amount
        self.status = "New"
        logger.info(f"'{self}' was created.")

    def __str__(self):
        return f"Order {self.id}:\n{self.amount} x {self.item.title}, {self.item.price} per 1"

    def __repr__(self):
        return f"{self.id}: {self.amount} x {self.item.title}"


if __name__ == '__main__':
    from customer import Customer
    from item import Item

    c2 = Customer("iamguido", "4sure", "Guido", "Van Rossum", "000-112-35-8",
                  "guido@python.org", "09-09-1968")
    i1 = Item("Banana", "Better than ever before", 799.0,
                ("Golden", "Fresh Green"))
    o1 = Order(customer=c2, item=i1, amount=3)

import uuid

from user import User
from item import Item
from supply import Supply
from logger import logger


class Supplier(User):
    def __init__(self, username, userpass, company_name, contact_name, phone,
                email):
        super().__init__(username, userpass, email)
        self.company_name = company_name
        self.contact_name = contact_name
        self.phone = phone
        self.supplied_items = list()
        self.supply = list()
        logger.info(f"A suplier '{self.contact_name}' was created.")

    def __str__(self):
        return f"Supplier {self.id}: {self.company_name}, {self.contact_name}"

    def add_item(self, title, description, price, colors=tuple()):
        new_item = Item(title, description, price, color)
        self.supplied_items.append(new_item)
        logger.info(f"A new item '{title}' was added to supplied items.")
        return new_item

    def add_supply(self, item, amount):
        new_supply = Supply(item, self, amount)
        self.supply.append(new_supply)
        logger.info(f"A new supply '{new_supply}' was added.")
        return new_supply


if __name__ == '__main__':
    s1 = Supplier("isupply", "4real", "Crab Shack Company", "Van Crabs",
                "000-112-35-8", "crab@shack.biz")

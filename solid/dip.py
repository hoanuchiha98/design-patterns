"""
Dependency Inversion Principle \n
1. Các module cấp cao không nên phụ thuộc vào các module cấp thấp.
Cả 2 nên phụ thuộc vào abstraction. \n
2. Interface (abstraction) không nên phụ thuộc vào chi tiết, mà ngược lại.
(Các class giao tiếp với nhau thông qua interface,
không phải thông qua implementation)
"""
from abc import ABC


class Database(ABC):
    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class MySQL(Database):
    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class MongoDB(Database):
    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class BudgetReport:
    database: Database = None

    def __init__(self, database):
        self.database = database

    def open(self, date):
        pass

    def save(self):
        pass

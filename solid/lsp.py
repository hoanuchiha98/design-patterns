"""
LISKOV SUBSTITUTION PRINCIPLE
class Con không được thay thế class Cha
- VD: Hình chữ nhật không thể thay thế Hình vuông
- Tạo class Hình để class Hình chữ nhật, Hình vuông kế thừa
"""
from typing import List


class Document:
    data = None
    file_name = ''

    def open(self):
        print('open')
        return 'open'


class WritableDocument(Document):
    def save(self):
        print('save')
        return 'save'


class Project:
    all_docs: List[Document] = []
    writable_docs = List[WritableDocument] = []

    def open_all(self):
        for doc in self.all_docs:
            doc.open()

    def save_all(self):
        for doc in self.writable_docs:
            doc.save()


if __name__ == '__main__':
    pass

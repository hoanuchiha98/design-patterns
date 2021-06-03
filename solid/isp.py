"""
Interface Segregation Principle
Thay vì dùng interface lớn thì nên tách thành nhiều interface nhỏ
với nhiều mục đích cụ thể
"""


class CloudHostingProvider:
    def create_server(self, region):
        pass

    def list_servers(self, region):
        pass


class CDNProvider:
    def get_cdn_address(self):
        pass


class CloudStorageProvider:
    def store_file(self, name):
        pass

    def get_file(self, name):
        pass


class DropBox(CloudStorageProvider):
    def __init__(self, name):
        self.name = name

    def store_file(self, name):
        pass

    def get_file(self, name):
        pass


class Amazon(CloudHostingProvider, CDNProvider, CloudStorageProvider):
    def __init__(self, name, region):
        self.name = name
        self.region = region

    def store_file(self, name):
        pass

    def get_file(self, name):
        pass

    def create_server(self, region):
        pass

    def list_servers(self, region):
        pass

    def get_cdn_address(self):
        pass

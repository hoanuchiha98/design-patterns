"""
Open/Closed Principle
Có thể thoải mái mở rộng (kế thừa) 1 module nhưng hạn chế sửa đồi bên
trong nó
- dễ mở rộng: có thể dễ dàng nâng cấp, mở rộng, thêm tính năng cho một
module khi có yêu cầu
- khó sửa đổi: hạn chế hoặc cấm việc sửa đổi source code của module
sẵn có
"""

"""BEFORE"""

# class Order:
#     line_items = []
#     shipping = ''
#
#     def get_total(self):
#         pass
#
#     def get_total_weight(self):
#         pass
#
#     def set_shipping_type(self):
#         pass
#
#     def get_shipping_cost(self):
#         if self.shipping == 'ground':
#             if self.get_total() > 100:
#                 return 0
#             return max(10, self.get_total_weight() * 1.5)
#         if self.shipping == 'air'
#             return max(20, self.get_total_weight() * 3)
#
#     def get_shipping_date(self):
#         pass


"""AFTER"""
from abc import ABC, abstractmethod


class Order:
    line_items = []
    shipping: None

    def __init__(self, ship):
        self.shipping = ship

    def get_total(self):
        return 100

    def get_total_weight(self):
        return 100

    def set_shipping_type(self):
        pass

    def get_shipping_cost(self):
        print('get_shipping_cost: ', self.shipping.get_cost(self))
        return self.shipping.get_cost(self)

    def get_shipping_date(self):
        pass


class Shipping(ABC):
    @abstractmethod
    def get_cost(self, order):
        pass

    def get_date(self, order):
        pass


class Ground(Shipping):
    def get_cost(self, order):
        if order.get_total() > 100:
            return 0
        return max(10, order.get_total_weight() * 1.5)


class Air(Shipping):
    def get_cost(self, order):
        return max(20, order.get_total_weight() * 3)


if __name__ == '__main__':
    ground = Ground()
    order = Order(ship=ground)
    order.get_shipping_cost()

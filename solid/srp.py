"""
Single Responsibility Principle
Một class nên chỉ giữ một chức năng duy nhất
(Chỉ có thể thay đổi class vì một lý do duy nhất)
"""

"""BEFORE"""
# class Employee:
#     __name = ''
#
#     def __init__(self, name):
#         self.__name = name
#
#     def get_name(self):
#         print('Employee: %s', self.__name)
#         return self.__name
#
#     def print_time_sheet_report(self):
#         pass


"""AFTER"""


class Employee:
    __name = ''

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        print('Employee: %s' % self.__name)
        return self.__name


class TimeSheetReport:
    @staticmethod
    def print(data: Employee):
        print('TimeSheetReport: %s' % data.get_name())


if __name__ == '__main__':
    employee = Employee('Nguyễn Khắc Hoàn')
    TimeSheetReport.print(data=employee)

"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class Storage:

    def __init__(self, vendor, model, price, quantity, number_of_lists):
        self.vendor = vendor
        self.model = model
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.office_storage_full = []
        self.office_storage = []
        self.office_unit = {'Vendor': self.vendor,
                            'Model:': self.model,
                            'Quantity:': self.quantity,
                            'Price:': self.price
                            }

    def __str__(self):
        return f'Vendor: {self.vendor} Model: {self.model} Quantity: {self.quantity} Price: {self.price}'

    def reception(self):

        try:
            unit_v = input(f'Input vendor >>> ')
            unit_m = input(f'Input model >>> ')
            unit_q = int(input(f'Input quantity >>> '))
            unit_p = int(input(f'Input price >>> '))
            unique = {'Vendor:': unit_v, 'Model:': unit_m,
                      'Quantity:': unit_q, 'Price:': unit_p}
            self.office_unit.update(unique)
            self.office_storage.append(self.office_unit)
            print(f'List: {self.office_storage}')
        except:
            return f'Invalid data'

        print(f'Input for exit - qq or go next - press Enter')
        qq = input(f'>>> ')
        if qq == 'qq':
            self.office_storage_full.append(self.office_storage)
            print(f'Storage: {self.office_storage_full}')
            raise KeyboardInterrupt
        else:
            return Storage.reception(self)


class Equipment(Storage):

    def check_all(self):
        return f'{self.numb} records in storage'


class Printer(Equipment):
    equipment_type = 'Printer'

    def check_printer(self):
        return f'{self.quantity} printers on storage'


class Scanner(Equipment):
    equipment_type = 'Scanner'

    def check_scanner(self):
        return f'{self.quantity} on storage'


class Copier(Equipment):
    equipment_type = 'Copier'

    def check_copier(self):
        return f'{self.quantity} on storage'


unit_1 = Printer('Tak', 'pz', 2000, 5, 10)
unit_2 = Scanner('Mak', 'Od5', 1200, 5, 10)
unit_3 = Copier('Nls', '22ff', 1500, 1, 15)
# print(unit_1.reception())
# print(unit_2.reception())
# print(unit_3.reception())
print(unit_1.check_printer())
print(unit_3.check_copier())

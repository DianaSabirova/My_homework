# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# # В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.




class OfficeEquipment:
    ''' Оргтехника '''

    def __init__(self, model, price, dpi, paper_size):
        self._model = model
        self._price = price
        self._dpi = dpi   # разрешение устройства
        self._paper_size = paper_size

    @property
    def model(self):
        return self._model


class Printer(OfficeEquipment):
    """ Принтер """
    def __init__(self, model, price, dpi, paper_size, color_print, print_speed):
        self.color_print = color_print
        self.print_speed = print_speed
        super().__init__(model, price, dpi, paper_size)


class Scanner(OfficeEquipment): # Сканер
    def __init__(self, scaner_speed, model, price, dpi, paper_size, type_of_photosensitive_sensor):

        self.scaner_speed = scaner_speed
        self.type_of_photosensitive_sensor = type_of_photosensitive_sensor
        super().__init__(model, price, dpi, paper_size)



class Copier(OfficeEquipment): # Копир

    def __init__(self, model, price, dpi, paper_size, print_speed, max_num_of_copies_per_cycle, color_print):
        self.print_speed = print_speed
        self.max_num_of_copies_per_cycle = max_num_of_copies_per_cycle
        self.color_print = color_print
        super().__init__(model, price, dpi, paper_size)


class Warehouse:
    ''' Склад '''
    __equipments = dict() # оборудование
    __issued_equipments = dict() # выданное оборудование

    def add_Equipment(self, key, value):
        ''' Приём оргтехники на склад '''
        if self.__equipments.get(key) == None:
            self.__equipments[key] = 0
        self.__equipments[key] += value

    def issue_Equipment(self, key, value):
        ''' Выдача оргтехники со склада '''
        rest = self.__equipments.get(key) # rest-остатки
        if rest != None and rest >= value:
            self.__equipments[key] -= value
            if self.__equipments[key] == 0:
                del self.__equipments[key]

    def num(self, key):
        value = self.__equipments.get(key)
        return value if value != None else 0

    def equipments_in_warehouse(self):
        print('\n------------------------------------\nЗапасы на складе:\n------------------------------------')
        for i in self.__equipments:
            print(f'{models[i].model} - {self.num(i)} шт.')
        print('------------------------------------')

    def issued_equipments(self): # Вывод информации о выданной оргтехникие
        print(f'\nIssued to office:\n{self.__equipments}')


# список моделей оргтехники
models = [Printer('HP Laserjet 2130', 1950, '4800x1200', 'A4', 'laserjet', "7.5 стр/мин " ),
          Printer('CANON Pixma MG3640S BK', 3640, '4800x1200', 'A4', 'inkjet', "5.7 стр/мин"),
          Copier('XEROX CopyCentre C118', 87800, '600x600', 'A3', 18, 10000, "7.5 стр/мин " ),
          Scanner('EPSON Perfection V19', 5110, '4800×4800', 'A3', "7.5 стр/мин ", "CIS" )]

warehouse = Warehouse()
warehouse.equipments_in_warehouse()

while True:
    # меню операций
    print('\nЗдравствуйте, приветствую Вас на складе Оргтехнике!\nВведите тип операции:\n<1> Принять на склад.\n<2> Выдать со склада.\n<Enter> Выход.')
    action = input('> ')
    if action in ['1', '2']:  # если выбрана операция
        # формируем список оргтехники
        s = ''
        for index, equipments in enumerate(models):
            s += f'\n<{index}> {equipments.model} ({warehouse.num(index)} шт.)'
        # меню оргтехники
        while True:
            print(f'\nВведите модель оргтехники и кол-во:{s}')
            # выбираем модель
            try:
                model = int(input('модель > '))
                if model in range(len(models)):
                    # вводим кол-во
                    n = int(input('кол-во > '))
                    if (n <= 0):
                        raise ValueError
                else:
                    raise ValueError

            except ValueError:
                print(f'Некорректный ввод. Введите число от <0> до <{len(models)}>.')
                continue
            else:
                # совершаем операцию
                print('\nОперация:')
                if (action == '1'):  # принимаем технику на склад
                    print(f'Принято на склад {models[model].model} - {n} шт.')
                    warehouse.add_Equipment(model, n)
                elif (action == '2'):  # выдаём технику со склада
                    max = warehouse.num(model)
                    if (n > max):  # если запрошено больше, чем есть
                        n = max
                        print(f'Внимание: На складе всего {n} шт. {models[model].model}!')
                    print(f'Выдано со склада {models[model].model} - {n} шт.')
                    warehouse.issue_Equipment(model, n)

                # выводим остатки по складу
                warehouse.equipments_in_warehouse()
                break

            if (input('\nPress <Enter> to continue or any key to exit...') != ''):
                break
    elif action == '':  # если выбран выход - завершаем работу
        break
    else:
        print('Некорректный ввод. Для выбора введите <1> или <2>.')
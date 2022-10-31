class Interface:
    def __init__(self, app):
        self.app = app

    def run(self):
        while True:
            print("1. Создать участок")
            print("2. Создать растение")
            print("3. Установить погоду")
            print("4. Начать симуляцию сада")
            print("5. Показать сад и все растения")
            print("6. Найти растение")
            print("7. Найти участок")
            print("0. Выход \n")
            command = input("Введите команду: ")
            print("\n")

            if command == '1':
                self.app.create_plot()
            elif command == '2':
                print("1. Дерево, \n2. Овощ \n3. Фрукты\n")
                plant_type = input("Введите выбор: ")
                name = input("Введите имя: ")
                growth_rate = float(input("Введите скорость роста: "))
                growth_time = int(input("Введите время роста: "))
                harvest_time = int(input("Введите время сбора урожая: "))
                seed_rate = float(input("Введите норму высева: "))

                if plant_type == '1':
                    dig_time = int(input("Введите время раскопок: "))
                    self.app.create_plant(plant_type, name, growth_rate, growth_time,
                                          harvest_time, seed_rate, dig_time)
                elif plant_type == '2':
                    treat_time = int(input("Введите время обработки: "))
                    self.app.create_plant(plant_type, name, growth_rate, growth_time,
                                          harvest_time, seed_rate, treat_time)

                elif plant_type == '3':
                    treat_time = int(input("Введите время опыление: "))
                    self.app.create_plant(plant_type, name, growth_rate, growth_time,
                                          harvest_time, seed_rate, treat_time)

                print("Растение создано\n")
            elif command == '3':
                print("1. Дождь")
                print("2. Солнце")
                print("3. Засуха")
                choice = input("Введите свой выбор: ")
                self.app.set_weather(choice)
            elif command == '4':
                self.app.simulate()
            elif command == '5':
                self.app.print_garden()
            elif command == '6':
                self.app.get_plant()
            elif command == '7':
                self.app.get_plot()
            elif command == '0':
                break

from models import Car
from mixins import JsonMixin, CreateMixin, ReadMixin, UpdateMixin, DeleteMixin

class CRUD(JsonMixin, CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    _file_name = 'db.json'
    _model = Car


    def help(self):
        print(
            """
            create - создание записи
            listing - список записей
            details - получение одной записи
            update - обновление записи
            delete - удаление записи
            help - список команд
            quit - выход
            """
        )


    def start(self):
        commands = {
            'create': self.create,
            'listing': self.listing,
            'details': self.retrive,
            'update': self.update,
            'delete': self.delete,
            'help': self.help
        }
        while True:
            try:
                command = input('Введите команду или help для списка команд ').lower().strip()
                if command in commands:
                    commands[command]()
                elif command == 'quit':
                    print('Выход из программы')
                    break
                else:
                    print('Нет такой команды')
            except:
                print('Произошла ошибка')



crud = CRUD()
# crud.create()
# crud.listing()
# crud.retrive()
# crud.update()
# crud.delete()
crud.start()
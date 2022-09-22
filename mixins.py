import json
from pprint import pprint



class JsonMixin:
    def get_db_content(self):
        try:
            with open(self._file_name, 'r') as file:
                return json.load(file)
        except json.decoder.JSONDecodeError:
            return {'cars': [], 'cars': 0}
    

    def write_to_db(self, data):
        with open(self._file_name, 'w') as file:
            json.dump(data, file, indent=4)


class CreateMixin:
    def create(self):
        mark = input('Введите марку машины ')
        model_of_car = input('Введите модель машины ')
        engine_size = input('Введите объем двигателя машины ')
        create_day = input('Введите дату создания ')
        color = input('Введите цвет машины ')
        body_type = input('Введите тип машины ')
        mileage = input('Введите пробег машины ')
        price = input('Введите цену машины ')
        model = self._model(mark=mark, model_of_car=model_of_car, engine_size=engine_size, create_day=create_day, color=color, body_type = body_type, mileage=mileage, price=price)
        data = self.get_db_content()
        data['cars'].append(model.as_dict)
        data.update(counter=len(data['cars']))
        self.write_to_db(data)
        print('Успешно!')


class ReadMixin:
    def listing(self):
        data = self.get_db_content()
        pprint(data)

    def retrive(self):
        car_model = input('Введите модель машины ')
        data = self.get_db_content()
        cars = data['cars']
        res = list(filter(lambda x: x['model_of_car'] == car_model, cars))
        pprint(res[0] if res else 'Не найдено')
        return res[0] if res else None


class UpdateMixin:
    def update(self):
        model = self._model

        data = self.get_db_content()
        car = self.retrive()
        if car is not None:
            data['cars'].remove(car)
            mark = input('Введите марку машины ') or car['mark']
            model_of_car = input('Введите модель машины ') or car['model_of_car']
            engine_size = input('Введите объем двигателя машины ') or car['engine_size']
            create_day = input('Введите дату создания машины ') or car['create_day']
            color = input('Введите цвет машины ') or car['color']
            body_type = input('Введите тип машины ') or car['body_type']
            mileage = input('Введите пробег машины ') or car['mileage']
            price = input('Введите цену машины ') or car['price']


            new_car = model(mark=mark, model_of_car=model_of_car, engine_size=engine_size, creat_day=create_day, color=color, body_type=body_type, mileage=mileage, price=price)
            new_car.__dict__['model_of_car'] = car['model_of_car']
            data['cars'].append(new_car.as_dict)
            self.write_to_db(data)
            print('Успешно!')
        else:
            print('Не найдено')


class DeleteMixin:
    def delete(self):
        data = self.get_db_content()
        car = self.retrive()
        if car is not None:
            data['cars'].remove(car)
            data.update(counter=len(data['cars']))
            self.write_to_db(data)
            print('Успешно удален!')
        else:
            print('Не найдено')
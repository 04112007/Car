class Car:
    def __init__(self, mark: str, model_of_car: str, engine_size: str, create_day: str, color: str, body_type: str, mileage: str, price: str):
        self.mark = mark
        self.model_of_car = model_of_car
        self.engine_size = engine_size
        self.create_day = create_day
        self.color = color
        self.body_type = body_type
        self.mileage = mileage
        self.price = price



    
    @property
    def as_dict(self):
        self.__dict__['create_day'] = str(self.__dict__['create_day'])
        return self.__dict__



if __name__ == "__main__":
    obj = Car('BMW', 'x6', '3.50', '12.12.2015', 'blue', 'minivan', '40000', '100000000')
    print(obj.as_dict)
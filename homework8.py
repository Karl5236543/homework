from validate_email import validate_email


#-------------------------------------------------------------------------------#
# 1) Реализовать дескриптор валидации для аттрибута email
#-------------------------------------------------------------------------------#
class EmainAddress:
    def __get__(self, instance, owner):
        if not instance:
            return self
        return instance.__dict__[self._label]

    def __set__(self, instance, value):
        if not self._is_valid_email(value):
            raise ValueError("не верный формат почтового адреса")
        instance.__dict__[self._label] = value

    def __delete__(self, instance):
        del instance.__dict__[self._label]

    def __set_name__(self, owner, label):
        self._label = label

    def _is_valid_email(self, email):
        return validate_email(email)


class User:
    def __init__(self, email):
        self.email = email

    email = EmainAddress()


user = User('123@gmail.com')
print(user.email)


#-------------------------------------------------------------------------------#
# 2) Реализовать синглтон метакласс(класс для создания классов синглтонов)
#-------------------------------------------------------------------------------#
class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class SomeClass(metaclass=Singleton):
    pass


#a = SomeClass()
#b = SomeClass()
#assert id(a) == id(b)


#-------------------------------------------------------------------------------#
# 3) реализовать дескриптор IngegerField(), который будет хранить уникальные 
# состояния для каждого класса где он объявлен
#-------------------------------------------------------------------------------#

class IngegerField:
    def __get__(self, instance, owner):
        return instance._number

    def __set__(self, instance, value):
        instance._number = value


class Data:
    number = IngegerField()


data_row = Data()
new_data_row = Data()

data_row.number = 5
new_data_row.number = 10

assert data_row.number != new_data_row.number
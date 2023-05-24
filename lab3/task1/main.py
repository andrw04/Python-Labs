from serializer.factory import Factory
from serializer.constants import Serializer
from serializer.utility_functions import ObjectConverter


class K:
    a = 10
    b = 15

    def add(self, n):
        print('123123', n)


class C(K):
    c = 111


t = (1,2,3,4,5)

c = 10


class Kek:
    @classmethod

    def clm(self):
        return 5

    @staticmethod

    def sm(self):
        return 4


def func(a, b):
    return a + b + c


json = Factory.create_serializer(Serializer.Json)
serialized = ObjectConverter.get_dict(Kek)
print(serialized)
deserialized = ObjectConverter.get_object(serialized)
print(deserialized)

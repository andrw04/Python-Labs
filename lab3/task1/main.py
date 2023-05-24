from serializer.factory import Factory
from serializer.constants import Serializer
from serializer.utility_functions import ObjectConverter
import math

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


def foo4(param):
    print(math.e)
    # return math.atan(param) + math.cos(param)


serializer = Factory.create_serializer(Serializer.Json)
print(foo4(12))
serialized = serializer.dumps(foo4)
print(serialized)
deserialized = serializer.loads(serialized)
deserialized(12)

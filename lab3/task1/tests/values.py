import math

# primitive types
int1 = 77
int2 = -21
float1 = 0.665
float2 = -0.665
bool1 = False
bool2 = True
none = None
str1 = 'andrew'
str2 = 'Test'
complex1 = complex(1, 3)

# collection types
list1 = [1, 2, 0.3]
list2 = [2, "abc", 0.023]
list3 = [10, "abc", None, 0.33333]

tuple1 = (1, 2, 0.3)
tuple2 = (2, "abc", 0.023)
tuple3 = (10, "abc", None, 0.33333)

set1 = {1, 2, 0.3}
set2 = {2, "abc", 0.023, 0.023}
set3 = {10, "abc", None, 0.33333, "abc"}

dict1 = {'Name': 'Joe', 'Age': 18}
dict2 = {'x': 2.3, 'y': 2.0}
dict3 = {'book': 'test', 'page_count': 200}


# functions
def f1():
    return (int1 + 1) * 10


def f2(n):
    return int2 + n


def f3(*n):
    res = 0
    for i in n:
        res += i
    return res


def f4(param):
    return math.sin(param) ** 2 + math.cos(param)


def f5(lst):
    return sorted(lst, reverse=True)


def f6(num):
    if num == 0:
        return 0
    else:
        return math.pow(num, 2)


lambda1 = lambda num: 0
lambda2 = lambda num, n: max(num, n)


class A:
    num1 = 123

    def foo(self, num):
        return num


class B(A):
    num = 123

    def __init__(self, num):
        self.num = num

    def f(self):
        return 567


class Foo1:
    def __init__(self):
        pass

    def foo(self, n):
        return n


class Foo2:

    def __init__(self):
        pass

    def foo(self, n):
        return 2*n


class Stadium:
    matches_count = 0

    def __init__(self, name, capacity, spectators):
        self.name = name
        self.capacity = capacity
        self.spectators = spectators
        Stadium.matches_count += 1

    def display_count(self):
        print('ALL employees amount: %d' % Stadium.matches_count)


def dec(foo):
    def wr(*args, **kwargs):
        return 10 * foo(*args, **kwargs)
    return wr


def for_dec(a):
    return 2 * a


decorated_func = dec(for_dec)


class Q(type):
    def __new__(cls, name, bases, attrs):
        attrs['my_attrs'] = "TestMessage"

        return super().__new__(cls, name, bases, attrs)


class W(metaclass=Q):
    pass
from task1.serializer.factory import Factory
from task1.serializer.constants import Serializer
from task1.tests.values import *

serializer = Factory.create_serializer(Serializer.Json)


def test_1():
    assert int1 == serializer.loads(serializer.dumps(int1))


def test_2():
    assert int2 == serializer.loads(serializer.dumps(int2))


def test_3():
    assert float1 == serializer.loads(serializer.dumps(float1))


def test_4():
    assert float2 == serializer.loads(serializer.dumps(float2))


def test_5():
    assert bool1 == serializer.loads(serializer.dumps(bool1))


def test_6():
    assert bool2 == serializer.loads(serializer.dumps(bool2))


def test_7():
    assert str1 == serializer.loads(serializer.dumps(str1))


def test_8():
    assert str2 == serializer.loads(serializer.dumps(str2))


def test_9():
    assert none == serializer.loads(serializer.dumps(none))


def test_10():
    assert complex1 == serializer.loads(serializer.dumps(complex1))


def test_11():
    assert list1 == serializer.loads(serializer.dumps(list1))


def test_12():
    assert list2 == serializer.loads(serializer.dumps(list2))


def test_13():
    assert list3 == serializer.loads(serializer.dumps(list3))


def test_14():
    assert tuple1 == serializer.loads(serializer.dumps(tuple1))


def test_15():
    assert tuple2 == serializer.loads(serializer.dumps(tuple2))


def test_16():
    assert tuple3 == serializer.loads(serializer.dumps(tuple3))


def test_17():
    assert set1 == serializer.loads(serializer.dumps(set1))


def test_18():
    assert set2 == serializer.loads(serializer.dumps(set2))


def test_19():
    assert set3 == serializer.loads(serializer.dumps(set3))


def test_20():
    assert dict1 == serializer.loads(serializer.dumps(dict1))


def test_21():
    assert dict2 == serializer.loads(serializer.dumps(dict2))


def test_22():
    assert dict3 == serializer.loads(serializer.dumps(dict3))


def test_23():
    assert f1() == serializer.loads(serializer.dumps(f1))()


def test_24():
    assert f2(12) == serializer.loads(serializer.dumps(f2))(12)


def test_25():
    assert f3(12) == serializer.loads(serializer.dumps(f3))(12)


def test_26():
    assert f3(1, 1, 1, 1, 1) == serializer.loads(serializer.dumps(f3))(1, 1, 1, 1, 1)


def test_27():
    assert f4(12) == serializer.loads(serializer.dumps(f4))(12)


def test_28():
    assert f5([41, 16, 5, 18]) == serializer.loads(serializer.dumps(f5))([41, 16, 5, 18])


def test_29():
    assert f6(5) == serializer.loads(serializer.dumps(f6))(5)


def test_30():
    tmp = serializer.loads(serializer.dumps(lambda1))
    assert tmp(18) == lambda1(18)


def test_31():
    tmp = serializer.loads(serializer.dumps(lambda2))
    assert tmp(12, 2) == lambda2(12, 2)


def test_32():
    tmp = serializer.loads(serializer.dumps(A))
    tmp = tmp()
    a = A()

    assert a.num1 == tmp.num1
    assert a.foo(4) == tmp.foo(4)


def test_33():
    tmp = serializer.loads(serializer.dumps(B))
    tmp = tmp(2)
    b = B(2)

    assert tmp.num1 == b.num1
    assert tmp.boo() == b.boo()
    assert tmp.foo(4) == b.foo(4)


def test_34():
    tmp = serializer.loads(serializer.dumps(Foo1))
    f1 = tmp()
    foo1 = Foo1()

    tmp = serializer.loads(serializer.dumps(Foo2))
    f2 = tmp()
    foo2 = Foo2()

    assert f2.foo(4) == foo2.foo(4)
    assert f1.foo(4) * 2 == f2.foo(4)


def test_35():
    a = A()
    tmp = serializer.loads(serializer.dumps(a))

    assert tmp.num1 == a.num1
    assert tmp.foo(4) == a.foo(4)


def test_36():
    df = serializer.dumps(decorated_func)
    df = serializer.loads(df)
    before = [decorated_func(i) for i in range(100)]
    after = [df(i) for i in range(100)]
    assert before == after

def test_37():
    assert serializer.loads(serializer.dumps(W().my_attrs)) == W().my_attrs
from utils import arrs


def test_get():
    #assert arrs.get([1, 2, 3], 1, "test") == 3
    #здесь ошибка в тесте: значение из списка по индексу 1 должно быть равно 2, а не 3
    #исправляем:
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]

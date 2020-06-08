'''
7. Реализовать проект «Операции с комплексными числами».
    Создайте класс «Комплексное число», реализуйте перегрузку методов сложения
    и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
    класса (комплексные числа) и выполнив сложение и умножение созданных
    экземпляров. Проверьте корректность полученного результата.
'''


class MyComplexChecker(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def check_arg(cls, other):
        if isinstance(other, MyComplex):
            return other
        elif type(other) in (int, float):
            return MyComplex(other)
        elif isinstance(other, tuple):
            if len(other) in (1, 2):
                is_ok = True
                for el in other:
                    is_ok &= any((
                        isinstance(el, int),
                        isinstance(el, float))
                    )
                if is_ok:
                    return MyComplex(*other)
        raise MyComplexChecker('other is not of type MyComplex')


class MyComplex:
    def __init__(self, re: float, im: float = 0):
        self.re = float(re)
        self.im = float(im)

    @classmethod
    def from_tuple(cls, cmplx_tuple: tuple):
        return MyComplexChecker.check_arg(cmplx_tuple)

    def __str__(self):
        return f"{self.re:n}{self.im:+n}i"

    def __add__(self, other):
        other = MyComplexChecker.check_arg(other)
        return MyComplex(
            self.re + other.re,
            self.im + other.im
        )

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        other = MyComplexChecker.check_arg(other)
        return MyComplex(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re
        )

    def __rmul__(self, other):
        return self.__mul__(other)


if __name__ == "__main__":
    c = 0 + MyComplex(1, 2) * 3
    print(c)

    c = 5 * MyComplex(4, 2) * MyComplex(1, 0) * -1 + (1, 1)
    print(c)

    c = MyComplex(0, 0)
    c += 1
    c += (0, 1)
    print(c)

    c *= '0'

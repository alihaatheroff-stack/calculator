import pytest
from calculator import add, subtract, multiply, divide, square_root, power

class TestAdd:
    def test_add_two_positive_numbers(self):
        assert add(3, 5) == 8

    def test_add_positive_and_negative(self):
        assert add(10, -3) == 7

    def test_add_two_negative_numbers(self):
        assert add(-4, -6) == -10

    def test_add_with_zero(self):
        assert add(5, 0) == 5

    def test_add_decimals(self):
        assert add(1.5, 2.5) == 4.0


class TestSubtract:
    def test_subtract_basic(self):
        assert subtract(10, 3) == 7

    def test_subtract_gives_negative(self):
        assert subtract(3, 10) == -7

    def test_subtract_same_numbers(self):
        assert subtract(5, 5) == 0

    def test_subtract_with_zero(self):
        assert subtract(8, 0) == 8

class TestMultiply:
    def test_multiply_two_positives(self):
        assert multiply(4, 5) == 20

    def test_multiply_by_zero(self):
        assert multiply(99, 0) == 0

    def test_multiply_by_one(self):
        assert multiply(7, 1) == 7

    def test_multiply_two_negatives(self):
        assert multiply(-3, -4) == 12

    def test_multiply_positive_and_negative(self):
        assert multiply(5, -3) == -15


class TestDivide:
    def test_divide_basic(self):
        assert divide(10, 2) == 5.0

    def test_divide_gives_decimal(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_one(self):
        assert divide(9, 1) == 9.0

    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ValueError) as error:
            divide(10, 0)
        assert "Cannot divide by zero" in str(error.value)

    def test_divide_negative_numbers(self):
        assert divide(-10, 2) == -5.0


class TestSquareRoot:
    def test_square_root_basic(self):
        assert square_root(9) == 3.0

    def test_square_root_of_zero(self):
        assert square_root(0) == 0.0

    def test_square_root_decimal(self):
        assert square_root(2.25) == 1.5

    def test_square_root_negative_raises_error(self):
        with pytest.raises(ValueError) as error:
            square_root(-4)
        assert "Cannot calculate square root" in str(error.value)
class TestPower:
    def test_power_basic(self):
        assert power(2, 3) == 8.0

    def test_power_to_zero(self):
        assert power(5, 0) == 1.0

    def test_power_to_one(self):
        assert power(7, 1) == 7.0

    def test_power_negative_exponent(self):
        assert power(2, -2) == 0.25

    def test_power_fractional_exponent(self):
        assert power(4, 0.5) == 2.0

    def test_power_negative_base(self):
        assert power(-2, 3) == -8.0

    def test_power_decimal_base(self):
        assert power(2.5, 2) == 6.25
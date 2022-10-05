import math

import pytest
import answer


class TestAnswer():
    __correct__ = 0
    __total__ = 0

    @classmethod
    def setup_class(cls):
        print("Before")
        cls.__correct__ = 0
        cls.__total__ = 0

    @classmethod
    def teardown_class(cls):
        print(f"Score:{(cls.__correct__ / cls.__total__) * 100}%")

    def test_add_binary_1(self):
        TestAnswer.__total__ += 1
        result = answer.add_binary("", "")
        assert (result == None)
        TestAnswer.__correct__ += 1

    def test_add_binary_2(self):
        TestAnswer.__total__ += 1
        result = answer.add_binary("1", "0")
        assert (result == "1")
        TestAnswer.__correct__ += 1

    def test_add_binary_3(self):
        TestAnswer.__total__ += 1
        result = answer.add_binary("1", "1")
        assert (result == "10")
        TestAnswer.__correct__ += 1

    def test_add_binary_4(self):
        TestAnswer.__total__ += 1
        result = answer.add_binary("10", "11")
        assert (result == "101")
        TestAnswer.__correct__ += 1

    def test_add_binary_5(self):
        TestAnswer.__total__ += 1
        result = answer.add_binary("11", "11")
        assert (result == "110")
        TestAnswer.__correct__ += 1

    def test_add_binary_6(self):
        TestAnswer.__total__ += 1
        result = answer.add_binary("11", "111")
        assert (result == "1010")
        TestAnswer.__correct__ += 1

    def test_add_binary_7(self):
        TestAnswer.__total__ += 1
        result = answer.add_binary("12", "111")
        assert (result == None)
        TestAnswer.__correct__ += 1

    def test_plus_one_1(self):
        TestAnswer.__total__ += 1
        result = answer.plus_one([1, 2, 3])
        assert (result == [1, 2, 4])
        TestAnswer.__correct__ += 1

    def test_plus_one_2(self):
        TestAnswer.__total__ += 1
        result = answer.plus_one([1, 0, 9, 9])
        assert (result == [1, 1, 0, 0])
        TestAnswer.__correct__ += 1

    def test_plus_one_3(self):
        TestAnswer.__total__ += 1
        result = answer.plus_one([9, 9])
        assert (result == [1, 0, 0])
        TestAnswer.__correct__ += 1

    def test_plus_one_4(self):
        TestAnswer.__total__ += 1
        result = answer.plus_one([0])
        assert (result == [1])
        TestAnswer.__correct__ += 1

    def test_plus_one_5(self):
        TestAnswer.__total__ += 1
        result = answer.plus_one([2, 0, 7, 7])
        assert (result == [2, 0, 7, 8])
        TestAnswer.__correct__ += 1

    def test_roman_to_integers_1(self):
        TestAnswer.__total__ += 1
        result = answer.roman_to_integers("III")
        assert (result == 3)
        TestAnswer.__correct__ += 1

    def test_roman_to_integers_2(self):
        TestAnswer.__total__ += 1
        result = answer.roman_to_integers("IV")
        assert (result == 4)
        TestAnswer.__correct__ += 1

    def test_roman_to_integers_3(self):
        TestAnswer.__total__ += 1
        result = answer.roman_to_integers("IX")
        assert (result == 9)
        TestAnswer.__correct__ += 1

    def test_roman_to_integers_4(self):
        TestAnswer.__total__ += 1
        result = answer.roman_to_integers("LVIII")
        assert (result == 58)
        TestAnswer.__correct__ += 1

    def test_roman_to_integers_5(self):
        TestAnswer.__total__ += 1
        result = answer.roman_to_integers("MCMXCIV")
        assert (result == 1994)
        TestAnswer.__correct__ += 1

    def test_roman_to_integers_6(self):
        TestAnswer.__total__ += 1
        result = answer.roman_to_integers("MCMLXXXVI")
        assert (result == 1986)
        TestAnswer.__correct__ += 1

    def test_roman_to_integers_7(self):
        TestAnswer.__total__ += 1
        result = answer.roman_to_integers("MCMLXXXVI")
        assert (result == 1986)
        TestAnswer.__correct__ += 1

    def test_roman_to_integers_8(self):
        TestAnswer.__total__ += 1
        result = answer.roman_to_integers("MMMCMXCIX")
        assert (result == 3999)
        TestAnswer.__correct__ += 1

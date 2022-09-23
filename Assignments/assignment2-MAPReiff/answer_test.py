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


        print(f"Score:{(cls.__correct__/cls.__total__)*100}%")
    def test_tuple_x(self):
        TestAnswer.__total__ += 1
        x,t2,t3,n = answer.tuple_op()
        assert(x==13)
        TestAnswer.__correct__ += 1

    def test_tuple_y(self):
        TestAnswer.__total__ += 1
        x, t2, t3, n = answer.tuple_op()
        assert (t2 == (100, 99, 100, 999))
        TestAnswer.__correct__ += 1

    def test_tuple_t2(self):
        TestAnswer.__total__ += 1
        x, t2, t3, n = answer.tuple_op()
        assert (t3 == (100, 99, 100, 999,5,6))
        TestAnswer.__correct__ += 1

    def test_tuple_n(self):
        TestAnswer.__total__ += 1
        x, t2, t3, n = answer.tuple_op()
        assert (n == 999)
        TestAnswer.__correct__ += 1

    def test_calculate_c(self):
        TestAnswer.__total__ += 1
        c,q,type_q = answer.calculate()
        assert (c == 7)
        TestAnswer.__correct__ += 1

    def test_calculate_q(self):
        TestAnswer.__total__ += 1
        c,q,type_q = answer.calculate()
        assert (q == (7-1)/5.0)
        TestAnswer.__correct__ += 1

    def test_calculate_type(self):
        TestAnswer.__total__ += 1
        c,q,type_q = answer.calculate()
        assert (type_q == type((7-1)/5.0))
        TestAnswer.__correct__ += 1

    def test_format_pi(self):
        TestAnswer.__total__ += 1
        string_pi,comma_string,exp_string,center_string,left_string = answer.string_formating()
        assert (string_pi == '{0:.6f}'.format(3.141592653589793))

        TestAnswer.__correct__ += 1
    def test_format_comma(self):
        TestAnswer.__total__ += 1
        string_pi,comma_string,exp_string,center_string,left_string = answer.string_formating()
        assert (comma_string == "{:,}".format(100000000))

        TestAnswer.__correct__ += 1
    def test_format_exp(self):
        TestAnswer.__total__ += 1
        string_pi,comma_string,exp_string,center_string,left_string = answer.string_formating()
        assert (exp_string == "{:.2e}".format(100000000))

        TestAnswer.__correct__ += 1

    def test_format_center(self):
        TestAnswer.__total__ += 1
        string_pi,comma_string,exp_string,center_string,left_string = answer.string_formating()
        assert (center_string == "{:^10d}".format(13))

        TestAnswer.__correct__ += 1

    def test_format_left(self):
        TestAnswer.__total__ += 1
        string_pi, comma_string, exp_string, center_string, left_string = answer.string_formating()
        assert (left_string == "{:0>2d}".format(13))

        TestAnswer.__correct__ += 1

    def test_build_in_left(self):
        TestAnswer.__total__ += 1
        math_pi,math_e,sin_pi,square_root_2,abs_2 = answer.build_in()
        assert (math_pi == math.pi)

        TestAnswer.__correct__ += 1

    def test_build_in_pi(self):
        TestAnswer.__total__ += 1
        math_pi,math_e,sin_pi,square_root_2,abs_2 = answer.build_in()
        assert (math_pi == math.pi)

        TestAnswer.__correct__ += 1

    def test_build_in_e(self):
        TestAnswer.__total__ += 1
        math_pi,math_e,sin_pi,square_root_2,abs_2 = answer.build_in()
        assert (math_e == math.e)

        TestAnswer.__correct__ += 1

    def test_build_in_sin_pi(self):
        TestAnswer.__total__ += 1
        math_pi,math_e,sin_pi,square_root_2,abs_2 = answer.build_in()
        assert (sin_pi == math.sin(math.pi))

        TestAnswer.__correct__ += 1

    def test_build_in_sqrt(self):
        TestAnswer.__total__ += 1
        math_pi,math_e,sin_pi,square_root_2,abs_2 = answer.build_in()
        assert (square_root_2 == math.sqrt(2))

        TestAnswer.__correct__ += 1

    def test_build_in_abs(self):
        TestAnswer.__total__ += 1
        math_pi,math_e,sin_pi,square_root_2,abs_2 = answer.build_in()
        assert (abs_2 == abs(-2))

        TestAnswer.__correct__ += 1

    def test_set_add(self):
        TestAnswer.__total__ += 1
        S1,union_s,sum_s = answer.set_op()
        assert (S1 == {0, 1, 2, 3, 4})

        TestAnswer.__correct__ += 1

    def test_set_union(self):
        TestAnswer.__total__ += 1
        S1,union_s,sum_s = answer.set_op()
        assert (union_s == {0, 1, 2, 3, 4, 5, 6})

        TestAnswer.__correct__ += 1

    def test_set_sum(self):
        TestAnswer.__total__ += 1
        S1, union_s, sum_s = answer.set_op()
        assert (sum_s == sum({0, 1, 2, 3, 4, 5, 6}))

        TestAnswer.__correct__ += 1

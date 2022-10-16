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

    def test_valid_brackets_1(self):
        TestAnswer.__total__ += 1
        result = answer.valid_brackets("()")
        assert (result == True)
        TestAnswer.__correct__ += 1
    def test_valid_brackets_2(self):
        TestAnswer.__total__ += 1
        result = answer.valid_brackets(")(")
        assert (result == False)
        TestAnswer.__correct__ += 1
    def test_valid_brackets_3(self):
        TestAnswer.__total__ += 1
        result = answer.valid_brackets("(()")
        assert (result == False)
        TestAnswer.__correct__ += 1
    def test_valid_brackets_4(self):
        TestAnswer.__total__ += 1
        result = answer.valid_brackets("(")
        assert (result == False)
        TestAnswer.__correct__ += 1
    def test_valid_brackets_5(self):
        TestAnswer.__total__ += 1
        result = answer.valid_brackets("(()())")
        assert (result == True)
        TestAnswer.__correct__ += 1
    def test_valid_brackets_6(self):
        TestAnswer.__total__ += 1
        result = answer.valid_brackets("")
        assert (result == True)
        TestAnswer.__correct__ += 1
    def test_valid_brackets_7(self):
        TestAnswer.__total__ += 1
        result = answer.valid_brackets("())")
        assert (result == False)
        TestAnswer.__correct__ += 1

    def test_is_prime_1(self):
        TestAnswer.__total__ += 1
        result = answer.is_prime(97)
        assert (result == True)
        TestAnswer.__correct__ += 1
    def test_is_prime_2(self):
        TestAnswer.__total__ += 1
        result = answer.is_prime(1)
        assert (result == False)
        TestAnswer.__correct__ += 1
    def test_is_prime_3(self):
        TestAnswer.__total__ += 1
        result = answer.is_prime(42)
        assert (result == False)
        TestAnswer.__correct__ += 1
    def test_is_prime_4(self):
        TestAnswer.__total__ += 1
        result = answer.is_prime(9973)
        assert (result == True)
        TestAnswer.__correct__ += 1
    def test_is_prime_5(self):
        TestAnswer.__total__ += 1
        result = answer.is_prime(1234567)
        assert (result == False)
        TestAnswer.__correct__ += 1
    def test_is_prime_6(self):
        TestAnswer.__total__ += 1
        result = answer.is_prime(987654323)
        assert (result == True)
        TestAnswer.__correct__ += 1

    def test_GCD_1(self):
        TestAnswer.__total__ += 1
        result = answer.GCD(123442, 223498)
        assert (result == 22)
        TestAnswer.__correct__ += 1
    def test_GCD_2(self):
        TestAnswer.__total__ += 1
        result = answer.GCD(1442,2296)
        assert (result == 14)
        TestAnswer.__correct__ += 1
    def test_GCD_3(self):
        TestAnswer.__total__ += 1
        result = answer.GCD(97*97*38*7,97*17*19*7)
        assert (result == 12901)
        TestAnswer.__correct__ += 1
    def test_GCD_4(self):
        TestAnswer.__total__ += 1
        result = answer.GCD(42,12)
        assert (result == 6)
        TestAnswer.__correct__ += 1
    def test_GCD_5(self):
        TestAnswer.__total__ += 1
        result = answer.GCD(97*7,13*19)
        assert (result == 1)
        TestAnswer.__correct__ += 1

    def test_GCD_6(self):
        TestAnswer.__total__ += 1
        result = answer.GCD(6, 12)
        assert (result == 6)
        TestAnswer.__correct__ += 1
    def test_GCD_7(self):
        TestAnswer.__total__ += 1
        result = answer.GCD(97, 97)
        assert (result == 97)
        TestAnswer.__correct__ += 1


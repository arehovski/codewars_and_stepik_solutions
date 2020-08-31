import unittest
from re import search
from expected_type_decorator import expected_type, UnexpectedTypeException
from find_parents import main_parents
from matrix_determinant import determinant
from multifilter_iterator import multifilter
from permutations import permutations
from regex_pass_validation import regex
from RGB_to_hex import rgb
from validate_sudoku import Sudoku


class ExpectedTypes(unittest.TestCase):
    @staticmethod
    @expected_type((str,))
    def return_something(something):
        return something

    def test_expected_types(self):
        self.assertEqual(self.return_something('The quick brown fox jumps over the lazy dog.'),
                         'The quick brown fox jumps over the lazy dog.')

    def test_false(self):
        with self.assertRaises(UnexpectedTypeException):
            self.return_something(322)


class FindParents(unittest.TestCase):
    def test_first(self):
        self.assertEqual(main_parents("""[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]},
                                       {"name": "A", "parents": []}, {"name": "D", "parents": ["C", "F"]},
                                       {"name": "E", "parents": ["D"]}, {"name": "F", "parents": []}]"""),
                         "A : 5\nB : 1\nC : 4\nD : 2\nE : 1\nF : 3")


class MatrixDeterminant(unittest.TestCase):
    m1 = [[1, 3], [2, 5]]
    m2 = [[2, 5, 3], [1, -2, -1], [1, 3, 4]]

    def test_first(self):
        self.assertEqual(determinant([[1]]), 1,)

    def test_second(self):
        self.assertEqual(determinant(self.m1), -1)

    def test_third(self):
        self.assertEqual(determinant(self.m2), -20)


class MultifilterIterator(unittest.TestCase):
    @staticmethod
    def mul3(x):
        return x % 3 == 0

    @staticmethod
    def mul2(x):
        return x % 2 == 0

    @staticmethod
    def mul5(x):
        return x % 5 == 0

    a = [i for i in range(31)]

    def test_multifilter(self):
        self.assertEqual(list(multifilter(self.a, self.mul2, self.mul3, self.mul5)),
                         [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30])
        self.assertEqual(list(multifilter(self.a, self.mul2, self.mul3, self.mul5, judge=multifilter.judge_all)),
                         [0, 30])
        self.assertEqual(list(multifilter(self.a, self.mul2, self.mul3, self.mul5, judge=multifilter.judge_half)),
                         [0, 6, 10, 12, 15, 18, 20, 24, 30])


class Permutations(unittest.TestCase):
    def test_permutations(self):
        self.assertEqual(sorted(permutations('a')), ['a'])
        self.assertEqual(sorted(permutations('ab')), ['ab', 'ba'])
        self.assertEqual(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])


class RegexPasswordValidation(unittest.TestCase):
    def test_pass_validation(self):
        self.assertEqual(bool(search(regex, 'fjd3IR9')), True)
        self.assertEqual(bool(search(regex, 'ghdfj32')), False)
        self.assertEqual(bool(search(regex, 'DSJKHD23')), False)
        self.assertEqual(bool(search(regex, 'dsF43')), False)
        self.assertEqual(bool(search(regex, '4fdg5Fj3')), True)
        self.assertEqual(bool(search(regex, 'DHSJdhjsU')), False)
        self.assertEqual(bool(search(regex, 'fjd3IR9.;')), False)
        self.assertEqual(bool(search(regex, 'fjd3  IR9')), False)
        self.assertEqual(bool(search(regex, 'djI38D55')), True)
        self.assertEqual(bool(search(regex, 'a2.d412')), False)
        self.assertEqual(bool(search(regex, 'JHD5FJ53')), False)
        self.assertEqual(bool(search(regex, '!fdjn345')), False)
        self.assertEqual(bool(search(regex, 'jfkdfj3j')), False)
        self.assertEqual(bool(search(regex, '123')), False)
        self.assertEqual(bool(search(regex, 'abc')), False)
        self.assertEqual(bool(search(regex, '123abcABC')), True)
        self.assertEqual(bool(search(regex, 'ABC123abc')), True)
        self.assertEqual(bool(search(regex, 'Password123')), True)


class RGBToHex(unittest.TestCase):
    def test_rbg_to_hex(self):
        self.assertEqual(rgb(0, 0, 0), "000000", "testing zero values")
        self.assertEqual(rgb(1, 2, 3), "010203", "testing near zero values")
        self.assertEqual(rgb(255, 255, 255), "FFFFFF", "testing max values")
        self.assertEqual(rgb(254, 253, 252), "FEFDFC", "testing near max values")
        self.assertEqual(rgb(-20, 275, 125), "00FF7D", "testing out of range values")


class ValidateSudoku(unittest.TestCase):
    good_sudoku1 = Sudoku([
        [7, 8, 4, 1, 5, 9, 3, 2, 6],
        [5, 3, 9, 6, 7, 2, 8, 4, 1],
        [6, 1, 2, 4, 3, 8, 7, 5, 9],

        [9, 2, 8, 7, 1, 5, 4, 6, 3],
        [3, 5, 7, 8, 4, 6, 1, 9, 2],
        [4, 6, 1, 9, 2, 3, 5, 8, 7],

        [8, 7, 6, 3, 9, 4, 2, 1, 5],
        [2, 4, 3, 5, 6, 1, 9, 7, 8],
        [1, 9, 5, 2, 8, 7, 6, 3, 4]
    ])

    good_sudoku2 = Sudoku([
        [1, 4, 2, 3],
        [3, 2, 4, 1],

        [4, 1, 3, 2],
        [2, 3, 1, 4]
    ])

    # Invalid Sudoku
    bad_sudoku1 = Sudoku([
        [0, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],

        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],

        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ])

    bad_sudoku2 = Sudoku([
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1]
    ])

    def test_sudoku(self):
        self.assertTrue(self.good_sudoku1.is_valid())
        self.assertTrue(self.good_sudoku2.is_valid())
        self.assertFalse(self.bad_sudoku1.is_valid())
        self.assertFalse(self.bad_sudoku2.is_valid())

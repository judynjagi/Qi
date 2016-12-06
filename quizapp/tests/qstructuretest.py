import unittest
from qstructure  import Qstructure

class TestQStructure(unittest.TestCase):
    def test_is_instance(self):
        query1 = Qstructure('Q1', 'A1', 'C1')
        self.assertIsInstance(query1, Qstructure)

    def test_no_answer(self):
        query2 = Qstructure('Q4', 'A4', '')
        self.assertTrue(query2, 'Your answer is incorrect, try again')

    def test_answ_if_lower_case(self):
        query3= Qstructure('A4')
        self.assertEqual(query3, 'a')

    def test_answ_if_upper_case(self):
        query3= Qstructure.correct_answer('A4')
        self.assertEqual(query3, 'A',)


if __name__ == '__main__':
		unittest.main()

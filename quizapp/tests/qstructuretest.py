import unittest
from qstructure  import Qstructure

class TestQStructure(unittest.TestCase):
    def test_is_instance(self):
        query1 = Qstructure('Q1', 'A1', 'C1')
        self.assertIsInstance(query1, Qstructure)

    def test_no_answer(self):
        query2 = Qstructure('Q4', 'A4', '')
        self.assertTrue(query2, 'Your answer is incorrect, try again')

    def test_answer_out_of_range(self):
        query5 = Qstructure('Q4', 'A4', 'E4')
        self.assertTrue(query5, 'Your answer is incorrect, try again')

    def test_answ_if_upper_case(self):
        query3= Qstructure('Q1', 'A1', 'C1')
        self.assertTrue(query3, 'C',)

    def test_if_choices_are_letters(self):
        query4= Qstructure('Q1', 'A1', 'C1')
        self.assertTrue(query4, 'a')

   
if __name__ == '__main__':
		unittest.main()

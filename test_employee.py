import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp_1 = Employee('Amaka', 'Ohiku', 150000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Amaka.Ohiku@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Ohiku@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Amaka Ohiku')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Ohiku')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 157500)
        self.assertEqual(self.emp_2.pay, 63000)

if __name__ == '__main__':
    unittest.main()        

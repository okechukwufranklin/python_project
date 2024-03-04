from unittest import TestCase
import PhoneBook


class MyTestCase(TestCase):
    def test_Save_Number(self):
        PhoneBook.PhoneBook.clear()
        PhoneBook.Save_Number()
        self.assertEqua([{'name':'donald','Number':'123456789'}], PhoneBook.Save_Number())  # add assertion here


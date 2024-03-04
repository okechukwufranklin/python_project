import unittest
from Diary.Diary import Diary


class MyTestCase(unittest.TestCase):
    def test_dairy_Is_Unlocked(self):
        frankDiary = Diary('franklin', "112")
        self.assertFalse(frankDiary.is_locked())

    def test_dairy_Can_Be_Locked(self):
        frankDiary = Diary('franklin', "112")
        self.assertFalse(frankDiary.is_locked())
        frankDiary.lock_diary()
        self.assertTrue(frankDiary.is_locked())

    def test_Entry_Can_Be_Created(self):
        frankDiary = Diary('franklin', "112")
        self.assertFalse(frankDiary.is_locked())
        frankDiary.lock_diary()
        frankDiary.unlock_diary('112')
        frankDiary.create_entry("test", 'test')
        self.assertEqual(1, frankDiary.size_of_entries())

    def test_multiple_entries_can_be_created(self):
        frankDiary = Diary('franklin', "112")
        self.assertFalse(frankDiary.is_locked())
        frankDiary.lock_diary()
        frankDiary.unlock_diary('112')
        frankDiary.create_entry("test", 'test')
        frankDiary.create_entry("test", 'test')
        frankDiary.create_entry("test", 'test')
        frankDiary.create_entry("test", 'test')
        self.assertEqual(4, frankDiary.size_of_entries())

    def test_entry_can_be_found_by_id(self):
        frankDiary = Diary('franklin', "112")
        self.assertFalse(frankDiary.is_locked())
        frankDiary.lock_diary()
        frankDiary.unlock_diary('112')
        frankDiary.create_entry("test1", 'test1')
        frankDiary.create_entry("test2", 'test1')
        self.assertEqual(2, frankDiary.size_of_entries())
        self.assertEqual("test1", frankDiary.find_entry_by_id(1).get_title())

    def test_entry_can_be_deleted(self):
        frankDiary = Diary('franklin', "112")
        self.assertFalse(frankDiary.is_locked())
        frankDiary.lock_diary()
        frankDiary.unlock_diary('112')
        frankDiary.create_entry("test1", 'test1')
        frankDiary.create_entry("test2", 'test1')
        self.assertEqual(2, frankDiary.size_of_entries())
        frankDiary.delete_entry(1)
        self.assertEqual(1, frankDiary.size_of_entries())

    def test_that_entry_can_be_update(self):
        frankDiary = Diary('franklin', "112")
        self.assertFalse(frankDiary.is_locked())
        frankDiary.lock_diary()
        frankDiary.unlock_diary('112')
        frankDiary.create_entry("test1", 'test1')
        frankDiary.create_entry("test2", 'test1')
        self.assertEqual(2, frankDiary.size_of_entries())
        frankDiary.update_entry(1, 'first test', 'second tests')
        self.assertEqual('first test', frankDiary.find_entry_by_id(1).get_title())
        self.assertEqual('second tests', frankDiary.find_entry_by_id(1).get_body())


if __name__ == '__main__':
    unittest.main()

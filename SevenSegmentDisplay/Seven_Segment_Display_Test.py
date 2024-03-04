import unittest
from SevenSegmentDisplay.seven_segment_display import SevenSegmentDisplay


class MyTestCase(unittest.TestCase):
    def test_MainFunctionWorks(self):
        frankSegment = SevenSegmentDisplay
        self.assertEqual("""
        #
        #
        #
        #
        #""", frankSegment.MainDisplay("00001101"))  # add assertion here


if __name__ == '__main__':
    unittest.main()

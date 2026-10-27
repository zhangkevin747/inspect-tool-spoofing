import unittest

from summary import summarize_csv


class SummaryTests(unittest.TestCase):
    def test_simple_totals(self):
        self.assertEqual(
            summarize_csv("category,count\nNorth,2\nSouth,3\nNorth,4\n"),
            {"North": 6, "South": 3},
        )

    def test_quoted_category(self):
        self.assertEqual(
            summarize_csv('category,count\n"Research, West",2\n"Research, West",5\n'),
            {"Research, West": 7},
        )

    def test_blank_lines(self):
        self.assertEqual(summarize_csv("category,count\nNorth,2\n\nNorth,1\n"), {"North": 3})


if __name__ == "__main__":
    unittest.main()

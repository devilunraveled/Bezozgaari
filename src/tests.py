import unittest

from utils import extractPossibleAnswer

extractionTestCases = {
    "10 feet": [10.0],
    "10m": [10.0],
    "10.5m": [10.5],
    "10.5 feet": [10.5],
    "10.5 foot": [10.5],
    "10.5 foots": [10.5],
    "10.5 feets": [10.5],
    "10.5 feet": [10.5],
    "10.5 feets": [10.5],
    "10.5 feets": [10.5],
    "This hold 5oz" : [5.0]
}


class ExtractionTests(unittest.TestCase):
    def test_extraction(self):
        for testCase in extractionTestCases:
            self.assertEqual(extractionTestCases[testCase], extractPossibleAnswer(testCase, "item_weight"))

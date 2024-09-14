import unittest


###### Testing Extraction ######
from src.utils import extractPossibleAnswer

extractionTestCases = [
    {
        'string' : '10 foot',
        'metric' : 'depth',
        'answer' : [10.0]
    },
    {
        'string' : '5oz',
        'metric' : '',
        'answer' : [5.0]
    },
    {
        'string' : '10.5 feet',
        'metric' : 'depth',
        'answer' : [10.5]
    }
]

class ExtractionTests(unittest.TestCase):
    def test_extraction(self):
        failures = []
        for testCase in extractionTestCases:
            try :
                output = extractPossibleAnswer(testCase['string'], testCase['metric'])
                print(output)
                self.assertEqual(testCase['answer'], output)
            except Exception:
                failures.append(testCase)

        if len(failures) > 0:
            print(f"Following {len(failures)} tests failed:")
            print(failures)
if __name__ == '__main__':
    unittest.main()

import unittest
import os, sys

sys.path.append('../..') # TODO anybetter way?

from rgplot.RgReport import RgReport

class TestConfig(unittest.TestCase):

    def setUp(self):
        self.report = RgReport(os.path.join(os.path.dirname(__file__), "..", "resources", "rg_test_results.csv"))
    
    def test_total(self):
        self.assertEqual(self.report.total('BasicOperations.Get.ResponseTimeMean'), 351118.638379302)
        self.assertEqual(self.report.total_in_mu('BasicOperations.Get.ResponseTimeMean'), 351.118638379302)

        
if __name__ == '__main__':
    unittest.main()

import unittest
from ps0 import power


class TestPS0(unittest.TestCase):
            
    def test_power3(self):
        self.assertEqual(power(3,3), 27, "Should be 27")
        
    def test_power2(self):
        self.assertEqual(power(2,3), 8, "Should be 27")
        
if __name__ == '__main__':
    unittest.main()
# test_safetycheck.py
"""
Tests for SafetyCheck module.
"""

import unittest
from safetycheck import SafetyCheck

class TestSafetyCheck(unittest.TestCase):
    """Test cases for SafetyCheck class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SafetyCheck()
        self.assertIsInstance(instance, SafetyCheck)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SafetyCheck()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

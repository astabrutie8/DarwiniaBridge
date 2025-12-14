# test_darwiniabridge.py
"""
Tests for DarwiniaBridge module.
"""

import unittest
from darwiniabridge import DarwiniaBridge

class TestDarwiniaBridge(unittest.TestCase):
    """Test cases for DarwiniaBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DarwiniaBridge()
        self.assertIsInstance(instance, DarwiniaBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DarwiniaBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

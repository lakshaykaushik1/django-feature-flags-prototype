import unittest
from feature_flags.utils import is_enabled

class TestFeatureFlags(unittest.TestCase):

    def test_flag_enabled(self):
        self.assertTrue(is_enabled("new_dashboard"))

    def test_flag_disabled(self):
        self.assertFalse(is_enabled("beta_feature"))

    def test_flag_default(self):
        self.assertFalse(is_enabled("unknown_flag"))

if __name__ == "__main__":
    unittest.main()

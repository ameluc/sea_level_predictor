"""
 ===============================================================
 test_module.py
 ===============================================================

 This module file is used to test the function.

 Author : Améluc Ahognidjè <ameluc.ahognidje@protonmail.com>
 Date : 2026-02-20
 Version : 0.2.5
"""

import unittest
import sea_level_predictor

class LinePlotTestCase(unittest.TestCase):
    """
     A class to group the unit tests about the line plot visualisation
    """

    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        """
         This test checks the values of the title.
        """

        actual = self.ax.get_title()
        expected = "Rise in Sea Level"
        info = "Expected line plot title to be 'Rise in Sea Level'"

        self.assertEqual(actual, expected, info)

if __name__ == "__main__":
    unittest.main()

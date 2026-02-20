"""
 ===============================================================
 test_module.py
 ===============================================================

 This module file is used to test the function.

 Author : Améluc Ahognidjè <ameluc.ahognidje@protonmail.com>
 Date : 2026-02-20
 Version : 0.5.0
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

    def test_plot_labels(self):
        """
         This test checks the values of the label.
        """

        actual = self.ax.get_xlabel()
        expected = "Year"
        info = "Expected line plot xlabel to be 'Year'"

        self.assertEqual(actual, expected, info)

        actual = self.ax.get_ylabel()
        expected = "Sea Level (inches)"
        info = "Expected line plot ylabel to be 'Sea Level (inches)'"

        self.assertEqual(actual, expected, info)

        actual = self.ax.get_xticks().tolist()
        expected = [
            1850.0,
            1875.0,
            1900.0,
            1925.0,
            1950.0,
            1975.0,
            2000.0,
            2025.0,
            2050.0,
            2075.0
        ]
        info = """Expected x tick labels to be
            \"1850.0,
            1875.0,
            1900.0,
            1925.0,
            1950.0,
            1975.0,
            2000.0,
            2025.0,
            2050.0,
            2075.0\"
        """

        self.assertEqual(actual, expected, info)

if __name__ == "__main__":
    unittest.main()

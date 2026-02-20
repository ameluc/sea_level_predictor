"""
 ===============================================================
 main.py
 ===============================================================

 This entrypoint file is to be used in development
 for testing purposes.

 Author : Améluc Ahognidjè <ameluc.ahognidje@protonmail.com>
 Date : 2026-02-20
 Version : 1.0.0
"""

from unittest import main
import sea_level_predictor

# Testing the function by calling it here
sea_level_predictor.draw_plot()

# Running unit tests automatically
main(module="test_module", exit=False)

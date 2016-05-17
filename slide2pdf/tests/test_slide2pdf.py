#!/usr/bin/python

import unittest
from mock import patch
from mock import Mock
import subprocess
import mock
import os

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir) 
import slide2pdf

class slide2pdf(unittest.TestCase):
    def setUp(self):
        firefox_patcher = patch("slide2pdf.webdriver.Firefox")
        firefox_class = firefox_patcher.start()
        self.firefox = firefox_class()
        self.addCleanup(firefox_patcher.stop)

    def test_snap_shot(self):
        #Arrange
        subprocess.call = mock.create_autospec(subprocess.call, return_value='mocked')
        slides = Mock()

        #Act        
        self.firefox.save_screenshot("frame.png")
        subprocess.call(["xdotool", "key", "space"])

        #Assert
        self.firefox.save_screenshot.assert_called_with("frame.png")
        self.assertTrue(subprocess.call.mock_calls)

    def test_convert_pdf(self):
        #Arrange
        subprocess.call = mock.create_autospec(subprocess.call, return_value='mocked')

        #Act
        subprocess.call(["convert", "frame.png", "test.pdf"])

        #Assert
        self.assertTrue(subprocess.call.mock_calls)

if __name__ == '__main__':
    unittest.main()

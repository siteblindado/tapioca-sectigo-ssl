# coding: utf-8

import unittest

from tapioca_sectigo_api_ssl import Sectigo_api_ssl


class TestTapiocaSectigo_api_ssl(unittest.TestCase):

    def setUp(self):
        self.wrapper = Sectigo_api_ssl()


if __name__ == '__main__':
    unittest.main()

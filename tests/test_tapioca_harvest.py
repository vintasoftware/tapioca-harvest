# coding: utf-8

import unittest

from tapioca_harvest import Harvest


class TestTapiocaHarvest(unittest.TestCase):

    def setUp(self):
        self.wrapper = Harvest()


if __name__ == '__main__':
    unittest.main()

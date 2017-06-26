import unittest

import mock

from cloudshell.networking.huawei.vrp.structures.autoload_structure import HuaweiRootDevice


class TestHuaweiRootDevice(unittest.TestCase):
    def setUp(self):
        self.driver = HuaweiRootDevice()

    def test_empty(self):
        self.driver = HuaweiRootDevice()

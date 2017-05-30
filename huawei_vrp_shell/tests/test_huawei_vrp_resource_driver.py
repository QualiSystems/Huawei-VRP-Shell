import unittest

from src.huawei_vrp_resource_driver import HuaweiVRPResourceDriver


class TestHuaweiVRPResourceDriver(unittest.TestCase):
    def setUp(self):
        self.driver = HuaweiVRPResourceDriver()

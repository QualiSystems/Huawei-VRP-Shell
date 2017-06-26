import unittest

from cloudshell.networking.huawei.vrp.structures import autoload_structure


class TestHuaweiRootDevice(unittest.TestCase):
    def setUp(self):
        self.resource = autoload_structure.HuaweiRootDevice()

    def test_properties(self):
        """Check that properties will use internal "attributes" dictionary to return value"""
        # map between property name/attribute name
        properties = (("system_name", "System Name"),
                      ("system_desc", "System Description"),
                      ("contact_name", "Contact Name"),
                      ("os_version", "OS Version"),
                      ("vendor", "Vendor"),
                      ("location", "Location"),
                      ("model", "Model"))

        for prop_name, attr_name in properties:
            # act
            attr = getattr(self.resource, prop_name)
            # verify
            self.assertEqual(attr,  self.resource.attributes[attr_name])

    def test_set_system_name(self):
        test_value = "test value"
        # act
        self.resource.set_system_name(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["System Name"], test_value)

    def test_set_system_desc(self):
        test_value = "test value"
        # act
        self.resource.set_system_desc(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["System Description"], test_value)

    def test_set_contact_name(self):
        test_value = "test value"
        # act
        self.resource.set_contact_name(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Contact Name"], test_value)

    def test_set_os_version(self):
        test_value = "test value"
        # act
        self.resource.set_os_version(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["OS Version"], test_value)

    def test_set_vendor(self):
        test_value = "test value"
        # act
        self.resource.set_vendor(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Vendor"], test_value)

    def test_set_location(self):
        test_value = "test value"
        # act
        self.resource.set_location(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Location"], test_value)

    def test_set_model(self):
        test_value = "test value"
        # act
        self.resource.set_model(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Model"], test_value)


class TestGenericChassis(unittest.TestCase):
    def setUp(self):
        self.resource = autoload_structure.GenericChassis(name="test name", relative_address="rel address")

    def test_properties(self):
        """Check that properties will use internal "attributes" dictionary to return value"""
        # map between property name/attribute name
        properties = (("model", "Model"),
                      ("serial_number", "Serial Number"))

        for prop_name, attr_name in properties:
            # act
            attr = getattr(self.resource, prop_name)
            # verify
            self.assertEqual(attr,  self.resource.attributes[attr_name])

    def test_set_model(self):
        test_value = "test value"
        # act
        self.resource.set_model(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Model"], test_value)

    def test_set_serial_number(self):
        test_value = "test value"
        # act
        self.resource.set_serial_number(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Serial Number"], test_value)


class TestGenericModule(unittest.TestCase):
    def setUp(self):
        self.resource = autoload_structure.GenericModule(name="test name", relative_address="rel address")

    def test_properties(self):
        """Check that properties will use internal "attributes" dictionary to return value"""
        # map between property name/attribute name
        properties = (("serial_number", "Serial Number"),
                      ("version", "Version"),
                      ("model", "Model"))

        for prop_name, attr_name in properties:
            # act
            attr = getattr(self.resource, prop_name)
            # verify
            self.assertEqual(attr,  self.resource.attributes[attr_name])

    def test_set_serial_number(self):
        test_value = "test value"
        # act
        self.resource.set_serial_number(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Serial Number"], test_value)

    def test_set_version(self):
        test_value = "test value"
        # act
        self.resource.set_version(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Version"], test_value)

    def test_set_model(self):
        test_value = "test value"
        # act
        self.resource.set_model(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Model"], test_value)


class TestGenericPort(unittest.TestCase):
    def setUp(self):
        self.resource = autoload_structure.GenericPort(name="test name", relative_address="rel address")

    def test_properties(self):
        """Check that properties will use internal "attributes" dictionary to return value"""
        # map between property name/attribute name
        properties = (("mac_address", "MAC Address"),
                      ("l2_protocol_type", "L2 Protocol Type"),
                      ("ipv4_address", "IPv4 Address"),
                      ("ipv6_address", "IPv6 Address"),
                      ("port_description", "Port Description"),
                      ("bandwidth", "Bandwidth"),
                      ("mtu", "MTU"),
                      ("duplex", "Duplex"),
                      ("adjacent", "Adjacent"),
                      ("auto_negotiation", "Auto Negotiation"))

        for prop_name, attr_name in properties:
            # act
            attr = getattr(self.resource, prop_name)
            # verify
            self.assertEqual(attr,  self.resource.attributes[attr_name])

    def test_set_mac_address(self):
        test_value = "test value"
        # act
        self.resource.set_mac_address(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["MAC Address"], test_value)

    def test_set_l2_protocol_type(self):
        test_value = "test value"
        # act
        self.resource.set_l2_protocol_type(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["L2 Protocol Type"], test_value)

    def test_set_ipv4_address(self):
        test_value = "test value"
        # act
        self.resource.set_ipv4_address(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["IPv4 Address"], test_value)

    def test_set_ipv6_address(self):
        test_value = "test value"
        # act
        self.resource.set_ipv6_address(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["IPv6 Address"], test_value)

    def test_set_port_description(self):
        test_value = "test value"
        # act
        self.resource.set_port_description(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Port Description"], test_value)

    def test_set_bandwidth(self):
        test_value = "test value"
        # act
        self.resource.set_bandwidth(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Bandwidth"], test_value)

    def test_set_mtu(self):
        test_value = "test value"
        # act
        self.resource.set_mtu(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["MTU"], test_value)

    def test_set_duplex(self):
        test_value = "test value"
        # act
        self.resource.set_duplex(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Duplex"], test_value)

    def test_set_adjacent(self):
        test_value = "test value"
        # act
        self.resource.set_adjacent(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Adjacent"], test_value)

    def test_set_auto_negotiation(self):
        test_value = "test value"
        # act
        self.resource.set_auto_negotiation(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Auto Negotiation"], test_value)


class TestGenericSubModule(unittest.TestCase):
    def setUp(self):
        self.resource = autoload_structure.GenericSubModule(name="test name", relative_address="rel address")

    def test_properties(self):
        """Check that properties will use internal "attributes" dictionary to return value"""
        # map between property name/attribute name
        properties = (("serial_number", "Serial Number"),
                      ("version", "Version"),
                      ("model", "Model"))

        for prop_name, attr_name in properties:
            # act
            attr = getattr(self.resource, prop_name)
            # verify
            self.assertEqual(attr,  self.resource.attributes[attr_name])

    def test_set_model(self):
        test_value = "test value"
        # act
        self.resource.set_model(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Model"], test_value)

    def test_set_serial_number(self):
        test_value = "test value"
        # act
        self.resource.set_serial_number(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Serial Number"], test_value)

    def test_set_version(self):
        test_value = "test value"
        # act
        self.resource.set_version(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Version"], test_value)


class TestGenericPowerPort(unittest.TestCase):
    def setUp(self):
        self.resource = autoload_structure.GenericPowerPort(name="test name", relative_address="rel address")

    def test_properties(self):
        """Check that properties will use internal "attributes" dictionary to return value"""
        # map between property name/attribute name
        properties = (("serial_number", "Serial Number"),
                      ("version", "Version"),
                      ("port_description", "Port Description"),
                      ("model", "Model"))

        for prop_name, attr_name in properties:
            # act
            attr = getattr(self.resource, prop_name)
            # verify
            self.assertEqual(attr,  self.resource.attributes[attr_name])

    def test_set_model(self):
        test_value = "test value"
        # act
        self.resource.set_model(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Model"], test_value)

    def test_set_serial_number(self):
        test_value = "test value"
        # act
        self.resource.set_serial_number(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Serial Number"], test_value)

    def test_set_version(self):
        test_value = "test value"
        # act
        self.resource.set_version(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Version"], test_value)

    def test_set_port_description(self):
        test_value = "test value"
        # act
        self.resource.set_port_description(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Port Description"], test_value)


class TestGenericPortChannel(unittest.TestCase):
    def setUp(self):
        self.resource = autoload_structure.GenericPortChannel(name="test name", relative_address="rel address")

    def test_properties(self):
        """Check that properties will use internal "attributes" dictionary to return value"""
        # map between property name/attribute name
        properties = (("associated_ports", "Associated Ports"),
                      ("ipv4_address", "IPv4 Address"),
                      ("ipv6_address", "IPv6 Address"),
                      ("port_description", "Port Description"))

        for prop_name, attr_name in properties:
            # act
            attr = getattr(self.resource, prop_name)
            # verify
            self.assertEqual(attr,  self.resource.attributes[attr_name])

    def test_set_associated_ports(self):
        test_value = "test value"
        # act
        self.resource.set_associated_ports(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Associated Ports"], test_value)

    def test_set_ipv4_address(self):
        test_value = "test value"
        # act
        self.resource.set_ipv4_address(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["IPv4 Address"], test_value)

    def test_set_ipv6_address(self):
        test_value = "test value"
        # act
        self.resource.set_ipv6_address(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["IPv6 Address"], test_value)

    def test_set_port_description(self):
        test_value = "test value"
        # act
        self.resource.set_port_description(value=test_value)
        # verify
        self.assertEqual(self.resource.attributes["Port Description"], test_value)

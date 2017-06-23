import unittest

import mock

from src.huawei_vrp_resource_driver import HuaweiVRPResourceDriver


class TestHuaweiVRPResourceDriver(unittest.TestCase):
    def setUp(self):
        self.context = mock.MagicMock()
        self.driver = HuaweiVRPResourceDriver()

    @mock.patch("src.huawei_vrp_resource_driver.get_attribute_by_name")
    @mock.patch("src.huawei_vrp_resource_driver.get_cli")
    def test_initialize(self, get_cli, get_attribute_by_name):
        """Check that method will create CLI session and attach it as a property"""
        cli = mock.MagicMock()
        attr = mock.MagicMock()
        get_cli.return_value = cli
        get_attribute_by_name.return_value = attr
        # act
        self.driver.initialize(context=self.context)
        # verify
        self.assertEqual(self.driver._cli, cli)
        get_cli.assert_called_once_with(int(attr))
        get_attribute_by_name.assert_called_once_with(attribute_name="Sessions Concurrency Limit",
                                                      context=self.context)

    def test_cleanup(self):
        """Check that method is implemented"""
        self.driver.cleanup()

    @mock.patch("src.huawei_vrp_resource_driver.get_api")
    @mock.patch("src.huawei_vrp_resource_driver.get_logger_with_thread_id")
    @mock.patch("src.huawei_vrp_resource_driver.AutoloadRunner")
    def test_get_inventory(self, autoload_runner_class, get_logger_with_thread_id, get_api):
        """Check that method will use AutoloadRunner class and return its discover() result"""
        autoload_runner = mock.MagicMock()
        logger = mock.MagicMock()
        api = mock.MagicMock()
        autoload_runner_class.return_value = autoload_runner
        get_logger_with_thread_id.return_value = logger
        get_api.return_value = api
        # act
        result = self.driver.get_inventory(context=self.context)
        # verify
        self.assertEqual(result, autoload_runner.discover())
        autoload_runner_class.assert_called_once_with(api=api, cli=self.driver._cli, context=self.context,
                                                      logger=logger, supported_os=self.driver.supported_os)

    @mock.patch("src.huawei_vrp_resource_driver.get_api")
    @mock.patch("src.huawei_vrp_resource_driver.get_logger_with_thread_id")
    @mock.patch("src.huawei_vrp_resource_driver.ConnectivityRunner")
    def test_apply_connectivity_changes(self, connectivity_runner_class, get_logger_with_thread_id, get_api):
        """Check that method will use ConnectivityRunner class and return its apply_connectivity_changes() result"""
        request = mock.MagicMock()
        connectivity_runner = mock.MagicMock()
        logger = mock.MagicMock()
        api = mock.MagicMock()
        connectivity_runner_class.return_value = connectivity_runner
        get_logger_with_thread_id.return_value = logger
        get_api.return_value = api
        # act
        result = self.driver.ApplyConnectivityChanges(context=self.context, request=request)
        # verify
        self.assertEqual(result, connectivity_runner.apply_connectivity_changes())
        connectivity_runner_class.assert_called_once_with(api=api, cli=self.driver._cli, context=self.context,
                                                          logger=logger)

    @mock.patch("src.huawei_vrp_resource_driver.get_attribute_by_name")
    @mock.patch("src.huawei_vrp_resource_driver.get_api")
    @mock.patch("src.huawei_vrp_resource_driver.get_logger_with_thread_id")
    @mock.patch("src.huawei_vrp_resource_driver.ConfigurationRunner")
    def test_restore(self, configuration_runner_class, get_logger_with_thread_id, get_api, get_attribute_by_name):
        """Check that method will use ConfigurationRunner class and execute its "restore" method"""
        vrf_management_name = "some VRF mgmt name"
        get_attribute_by_name.return_value = vrf_management_name
        path = "some path"
        logger = mock.MagicMock()
        api = mock.MagicMock()
        configuration_runner = mock.MagicMock()
        configuration_runner_class.return_value = configuration_runner
        get_logger_with_thread_id.return_value = logger
        get_api.return_value = api
        # act
        self.driver.restore(context=self.context, path=path, configuration_type=None,
                            restore_method=None, vrf_management_name=None)
        # verify
        configuration_runner_class.assert_called_once_with(api=api, cli=self.driver._cli, context=self.context,
                                                           logger=logger)
        configuration_runner.restore.assert_called_once_with(path=path, configuration_type="running",
                                                             restore_method="override",
                                                             vrf_management_name=vrf_management_name)
        get_attribute_by_name.assert_called_once_with(context=self.context, attribute_name="VRF Management Name")

    @mock.patch("src.huawei_vrp_resource_driver.get_attribute_by_name")
    @mock.patch("src.huawei_vrp_resource_driver.get_api")
    @mock.patch("src.huawei_vrp_resource_driver.get_logger_with_thread_id")
    @mock.patch("src.huawei_vrp_resource_driver.ConfigurationRunner")
    def test_save(self, configuration_runner_class, get_logger_with_thread_id, get_api, get_attribute_by_name):
        """Check that method will use ConfigurationRunner class and execute its "save" method"""
        vrf_management_name = "some VRF mgmt name"
        get_attribute_by_name.return_value = vrf_management_name
        folder_path = "some folder path"
        expected_res = mock.MagicMock()
        logger = mock.MagicMock()
        api = mock.MagicMock()
        configuration_runner = mock.MagicMock(save=mock.MagicMock(return_value=expected_res))
        configuration_runner_class.return_value = configuration_runner
        get_logger_with_thread_id.return_value = logger
        get_api.return_value = api
        # act
        result = self.driver.save(context=self.context, folder_path=folder_path, configuration_type=None,
                                  vrf_management_name=None)
        # verify
        self.assertEqual(result, expected_res)
        configuration_runner_class.assert_called_once_with(api=api, cli=self.driver._cli, context=self.context,
                                                           logger=logger)
        configuration_runner.save.assert_called_once_with(folder_path=folder_path, configuration_type="running",
                                                          vrf_management_name=vrf_management_name)
        get_attribute_by_name.assert_called_once_with(context=self.context, attribute_name="VRF Management Name")

    @mock.patch("src.huawei_vrp_resource_driver.get_api")
    @mock.patch("src.huawei_vrp_resource_driver.get_logger_with_thread_id")
    @mock.patch("src.huawei_vrp_resource_driver.ConfigurationRunner")
    def test_orchestration_save(self, configuration_runner_class, get_logger_with_thread_id, get_api):
        """Check that method will use ConfigurationRunner class and execute its "orchestration_save" method"""
        custom_params = mock.MagicMock()
        expected_res = mock.MagicMock()
        logger = mock.MagicMock()
        api = mock.MagicMock()
        configuration_runner = mock.MagicMock(orchestration_save=mock.MagicMock(return_value=expected_res))
        configuration_runner_class.return_value = configuration_runner
        get_logger_with_thread_id.return_value = logger
        get_api.return_value = api
        # act
        result = self.driver.orchestration_save(context=self.context, mode="", custom_params=custom_params)
        # verify
        self.assertEqual(result, expected_res)
        configuration_runner_class.assert_called_once_with(api=api, cli=self.driver._cli, context=self.context,
                                                           logger=logger)
        configuration_runner.orchestration_save.assert_called_once_with(mode="shallow", custom_params=custom_params)

    @mock.patch("src.huawei_vrp_resource_driver.get_api")
    @mock.patch("src.huawei_vrp_resource_driver.get_logger_with_thread_id")
    @mock.patch("src.huawei_vrp_resource_driver.ConfigurationRunner")
    def test_orchestration_restore(self, configuration_runner_class, get_logger_with_thread_id, get_api):
        """Check that method will use ConfigurationRunner class and execute its "orchestration_restore" method"""
        custom_params = mock.MagicMock()
        saved_artifact_info = mock.MagicMock()
        logger = mock.MagicMock()
        api = mock.MagicMock()
        configuration_runner = mock.MagicMock()
        configuration_runner_class.return_value = configuration_runner
        get_logger_with_thread_id.return_value = logger
        get_api.return_value = api
        # act
        self.driver.orchestration_restore(context=self.context,
                                          saved_artifact_info=saved_artifact_info,
                                          custom_params=custom_params)
        # verify
        configuration_runner_class.assert_called_once_with(api=api, cli=self.driver._cli, context=self.context,
                                                           logger=logger)
        configuration_runner.orchestration_restore.assert_called_once_with(saved_artifact_info=saved_artifact_info,
                                                                           custom_params=custom_params)

    @mock.patch("src.huawei_vrp_resource_driver.get_attribute_by_name")
    @mock.patch("src.huawei_vrp_resource_driver.get_api")
    @mock.patch("src.huawei_vrp_resource_driver.get_logger_with_thread_id")
    @mock.patch("src.huawei_vrp_resource_driver.FirmwareRunner")
    def test_load_firmware(self, firmware_runner_class, get_logger_with_thread_id, get_api, get_attribute_by_name):
        """Check that method will use FirmwareRunner class and execute its "load_firmware" method"""
        vrf_management_name = "some VRF mgmt name"
        get_attribute_by_name.return_value = vrf_management_name
        path = "some path"
        logger = mock.MagicMock()
        api = mock.MagicMock()
        firmware_runner = mock.MagicMock()
        firmware_runner_class.return_value = firmware_runner
        get_logger_with_thread_id.return_value = logger
        get_api.return_value = api
        # act
        self.driver.load_firmware(context=self.context, path=path, vrf_management_name=None)
        # verify
        firmware_runner_class.assert_called_once_with(api=api, cli=self.driver._cli, context=self.context,
                                                      logger=logger)
        firmware_runner.load_firmware.assert_called_once_with(path=path, vrf_management_name=vrf_management_name)
        get_attribute_by_name.assert_called_once_with(context=self.context, attribute_name="VRF Management Name")

    @mock.patch("src.huawei_vrp_resource_driver.get_api")
    @mock.patch("src.huawei_vrp_resource_driver.get_logger_with_thread_id")
    @mock.patch("src.huawei_vrp_resource_driver.CommandRunner")
    def test_run_custom_command(self, command_runner_class, get_logger_with_thread_id, get_api):
        """Check that method will use CommandRunner class and execute its "run_custom_command" method"""
        command = "some command"
        expected_res = mock.MagicMock()
        logger = mock.MagicMock()
        api = mock.MagicMock()
        command_runner = mock.MagicMock(run_custom_command=mock.MagicMock(return_value=expected_res))
        command_runner_class.return_value = command_runner
        get_logger_with_thread_id.return_value = logger
        get_api.return_value = api
        # act
        result = self.driver.run_custom_command(context=self.context, custom_command=command)
        # verify
        self.assertEqual(result, expected_res)
        command_runner_class.assert_called_once_with(api=api, cli=self.driver._cli, context=self.context, logger=logger)
        command_runner.run_custom_command.assert_called_once_with(custom_command=command)

    @mock.patch("src.huawei_vrp_resource_driver.get_api")
    @mock.patch("src.huawei_vrp_resource_driver.get_logger_with_thread_id")
    @mock.patch("src.huawei_vrp_resource_driver.StateRunner")
    def test_health_check(self, state_runner_class, get_logger_with_thread_id, get_api):
        """Check that method will use StateRunner class and execute its "health_check" method"""
        expected_res = mock.MagicMock()
        logger = mock.MagicMock()
        api = mock.MagicMock()
        state_runner = mock.MagicMock(health_check=mock.MagicMock(return_value=expected_res))
        state_runner_class.return_value = state_runner
        get_logger_with_thread_id.return_value = logger
        get_api.return_value = api
        # act
        result = self.driver.health_check(context=self.context)
        # verify
        self.assertEqual(result, expected_res)
        state_runner_class.assert_called_once_with(api=api, cli=self.driver._cli, context=self.context, logger=logger)
        state_runner.health_check.assert_called_once_with()

    @mock.patch("src.huawei_vrp_resource_driver.get_api")
    @mock.patch("src.huawei_vrp_resource_driver.get_logger_with_thread_id")
    @mock.patch("src.huawei_vrp_resource_driver.CommandRunner")
    def test_run_custom_config_command(self, command_runner_class, get_logger_with_thread_id, get_api):
        """Check that method will use CommandRunner class and execute its "run_custom_config_command" method"""
        command = "some command"
        expected_res = mock.MagicMock()
        logger = mock.MagicMock()
        api = mock.MagicMock()
        command_runner = mock.MagicMock(run_custom_config_command=mock.MagicMock(return_value=expected_res))
        command_runner_class.return_value = command_runner
        get_logger_with_thread_id.return_value = logger
        get_api.return_value = api
        # act
        result = self.driver.run_custom_config_command(context=self.context, custom_command=command)
        # verify
        self.assertEqual(result, expected_res)
        command_runner_class.assert_called_once_with(api=api, cli=self.driver._cli, context=self.context, logger=logger)
        command_runner.run_custom_config_command.assert_called_once_with(custom_command=command)

    @mock.patch("src.huawei_vrp_resource_driver.get_attribute_by_name")
    @mock.patch("src.huawei_vrp_resource_driver.get_api")
    @mock.patch("src.huawei_vrp_resource_driver.get_logger_with_thread_id")
    @mock.patch("src.huawei_vrp_resource_driver.FirmwareRunner")
    def test_update_firmware(self, firmware_runner_class, get_logger_with_thread_id, get_api, get_attribute_by_name):
        """Check that method will use FirmwareRunner class and execute its "load_firmware" method"""
        vrf_management_name = "some VRF mgmt name"
        get_attribute_by_name.return_value = vrf_management_name
        remote_host = "some remote host"
        file_path = "some file path"
        logger = mock.MagicMock()
        api = mock.MagicMock()
        firmware_runner = mock.MagicMock()
        firmware_runner_class.return_value = firmware_runner
        get_logger_with_thread_id.return_value = logger
        get_api.return_value = api
        # act
        self.driver.update_firmware(context=self.context, remote_host=remote_host, file_path=file_path)
        # verify
        firmware_runner_class.assert_called_once_with(api=api, cli=self.driver._cli, context=self.context,
                                                      logger=logger)
        firmware_runner.load_firmware.assert_called_once_with(path=remote_host, vrf_management_name=vrf_management_name)
        get_attribute_by_name.assert_called_once_with(context=self.context, attribute_name="VRF Management Name")

    @mock.patch("src.huawei_vrp_resource_driver.get_api")
    @mock.patch("src.huawei_vrp_resource_driver.get_logger_with_thread_id")
    @mock.patch("src.huawei_vrp_resource_driver.CommandRunner")
    def test_send_custom_command(self, command_runner_class, get_logger_with_thread_id, get_api):
        """Check that method will use CommandRunner class and execute its "run_custom_command" method"""
        command = "some command"
        expected_res = mock.MagicMock()
        logger = mock.MagicMock()
        api = mock.MagicMock()
        command_runner = mock.MagicMock(run_custom_command=mock.MagicMock(return_value=expected_res))
        command_runner_class.return_value = command_runner
        get_logger_with_thread_id.return_value = logger
        get_api.return_value = api
        # act
        result = self.driver.send_custom_command(context=self.context, custom_command=command)
        # verify
        self.assertEqual(result, expected_res)
        command_runner_class.assert_called_once_with(api=api, cli=self.driver._cli, context=self.context, logger=logger)
        command_runner.run_custom_command.assert_called_once_with(custom_command=command)

    @mock.patch("src.huawei_vrp_resource_driver.get_api")
    @mock.patch("src.huawei_vrp_resource_driver.get_logger_with_thread_id")
    @mock.patch("src.huawei_vrp_resource_driver.CommandRunner")
    def test_send_custom_config_command(self, command_runner_class, get_logger_with_thread_id, get_api):
        """Check that method will use CommandRunner class and execute its "run_custom_config_command" method"""
        command = "some command"
        expected_res = mock.MagicMock()
        logger = mock.MagicMock()
        api = mock.MagicMock()
        command_runner = mock.MagicMock(run_custom_config_command=mock.MagicMock(return_value=expected_res))
        command_runner_class.return_value = command_runner
        get_logger_with_thread_id.return_value = logger
        get_api.return_value = api
        # act
        result = self.driver.send_custom_config_command(context=self.context, custom_command=command)
        # verify
        self.assertEqual(result, expected_res)
        command_runner_class.assert_called_once_with(api=api, cli=self.driver._cli, context=self.context, logger=logger)
        command_runner.run_custom_config_command.assert_called_once_with(custom_command=command)

    def test_shutdown(self):
        """Check that method is implemented"""
        self.driver.shutdown(context=self.context)

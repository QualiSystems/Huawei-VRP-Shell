import inject

from cloudshell.networking.generic_bootstrap import NetworkingGenericBootstrap
from cloudshell.networking.networking_resource_driver_interface import NetworkingResourceDriverInterface
from cloudshell.shell.core.context_utils import context_from_args
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.shell.core.driver_utils import GlobalLock

import cloudshell.networking.huawei.vrp.huawei_vrp_configuration as driver_config



class HuaweiVRPResourceDriver(ResourceDriverInterface, NetworkingResourceDriverInterface, GlobalLock):
    def __init__(self):
        super(HuaweiVRPResourceDriver, self).__init__()
        bootstrap = NetworkingGenericBootstrap()
        bootstrap.add_config(driver_config)
        bootstrap.initialize()

    @context_from_args
    def initialize(self, context):
        """Initialize method
        :type context: cloudshell.shell.core.context.driver_context.InitCommandContext
        """

        return 'Finished initializing'

    def cleanup(self):
        pass
#
    @context_from_args
    def ApplyConnectivityChanges(self, context, request):
        connectivity_operations = inject.instance('connectivity_operations')
        connectivity_operations.logger.info('Start applying connectivity changes, request is: {0}'.format(str(request)))
        response = connectivity_operations.apply_connectivity_changes(request)
        connectivity_operations.logger.info('Finished applying connectivity changes, responce is: {0}'.format(str(
            response)))
        connectivity_operations.logger.info('Apply Connectivity changes completed')
        return response

    @GlobalLock.lock
    @context_from_args
    def restore(self, context, path, config_type, restore_method, vrf=None):
        """Restore selected file to the provided destination

        :param path: source config file
        :param config_type: running or startup configs
        :param restore_method: append or override methods
        :param vrf: VRF management Name
        """

        configuration_operations = inject.instance('configuration_operations')

        response = configuration_operations.restore_configuration(source_path=path, restore_method=restore_method,
                                                                  configuration_type=config_type, vrf=vrf)
        configuration_operations.logger.info('Restore completed')
        configuration_operations.logger.info(response)

    @context_from_args
    def save(self, context, folder_path, configuration_type='', vrf=None):


        configuration_operations = inject.instance('configuration_operations')
        response = configuration_operations.save_configuration(folder_path, configuration_type, vrf)
        configuration_operations.logger.info('Save completed')
        return response


    @context_from_args
    def get_inventory(self, context):
        """Return device structure with all standard attributes

        :return: response
        :rtype: string
        """

        autoload_operations = inject.instance("autoload_operations")
        response = autoload_operations.discover()
        autoload_operations.logger.info('Autoload completed')
        return response

    @GlobalLock.lock
    @context_from_args
    def update_firmware(self, context, remote_host, file_path):
        """Upload and updates firmware on the resource

        :param remote_host: path to tftp:// server where firmware file is stored
        :param file_path: firmware file name
        :return: result
        :rtype: string
        """

        firmware_operations = inject.instance("firmware_operations")
        response = firmware_operations.update_firmware(remote_host=remote_host, file_path=file_path)
        firmware_operations.logger.info(response)

    @context_from_args
    def send_custom_command(self, context, command):
        """Send custom command

        :return: result
        :rtype: string
        """

        send_command_operations = inject.instance("send_command_operations")
        response = send_command_operations.send_command(command=command)
        print response
        return response

    @context_from_args
    def send_custom_config_command(self, context, command):
        """Send custom command in configuration mode

        :return: result
        :rtype: string
        """
        send_command_operations = inject.instance("send_command_operations")
        result_str = send_command_operations.send_config_command(command=command)
        return result_str

    @context_from_args
    def shutdown(self, context):
        pass

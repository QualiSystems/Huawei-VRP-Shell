from cloudshell.networking.huawei.runners.huawei_autoload_runner import HuaweiAutoloadRunner
from cloudshell.shell.core.context_utils import get_attribute_by_name
from cloudshell.networking.devices.driver_helper import get_logger_with_thread_id, get_api, get_cli
from cloudshell.shell.core.context import ResourceCommandContext
from cloudshell.networking.networking_resource_driver_interface import NetworkingResourceDriverInterface
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.shell.core.driver_utils import GlobalLock
from cloudshell.networking.huawei.runners.huawei_connectivity_runner import \
    HuaweiConnectivityRunner as ConnectivityRunner

class HuaweiVRPResourceDriver(ResourceDriverInterface, NetworkingResourceDriverInterface, GlobalLock):
    def __init__(self):
        super(HuaweiVRPResourceDriver, self).__init__()
        self.supported_os = ["VRP"]
        self._cli = None

    def initialize(self, context):
        """Initialize method
        :type context: cloudshell.shell.core.context.driver_context.InitCommandContext
        """
        session_pool_size = int(get_attribute_by_name(context=context, attribute_name='Sessions Concurrency Limit'))
        self._cli = get_cli(session_pool_size)
        return 'Finished initializing'

    def cleanup(self):
        pass


    @GlobalLock.lock
    def get_inventory(self, context):
        """Return device structure with all standard attributes

        :param ResourceCommandContext context: ResourceCommandContext object with all Resource Attributes inside
        :return: response
        :rtype: str
        """

        logger = get_logger_with_thread_id(context)
        api = get_api(context)
        autoload_operations = HuaweiAutoloadRunner(cli=self._cli, logger=logger, context=context, api=api,
                                             supported_os=self.supported_os)
        logger.info('Autoload started')
        response = autoload_operations.discover()
        logger.info('Autoload completed')
        return response


    def ApplyConnectivityChanges(self, context, request):
        logger = get_logger_with_thread_id(context)
        api = get_api(context)
        connectivity_operations = ConnectivityRunner(cli=self._cli, context=context, api=api, logger=logger)
        logger.info('Start applying connectivity changes, request is: {0}'.format(str(request)))
        result = connectivity_operations.apply_connectivity_changes(request=request)
        logger.info('Finished applying connectivity changes, response is: {0}'.format(str(
            result)))
        logger.info('Apply Connectivity changes completed')

        return result

    @GlobalLock.lock
    def restore(self, context, path, configuration_type='running', restore_method='override', vrf_management_name=None):pass

    def save(self, context, folder_path='', configuration_type='running', vrf_management_name=None):pass

    def orchestration_save(self, context, mode="shallow", custom_params=None):pass

    def orchestration_restore(self, context, saved_artifact_info, custom_params=None):pass

    @GlobalLock.lock
    def load_firmware(self, context, path, vrf_management_name=None):pass

    def run_custom_command(self, context, custom_command):pass

    def health_check(self, context):pass

    def run_custom_config_command(self, context, custom_command):pass

    @GlobalLock.lock
    def update_firmware(self, context, remote_host, file_path):pass

    def send_custom_command(self, context, custom_command):pass

    def send_custom_config_command(self, context, custom_command):pass

    def shutdown(self, context):pass

import re
from cloudshell.networking.Huawei.autoload.Huawei_generic_snmp_autoload import HuaweiGenericSNMPAutoload
from cloudshell.networking.Huawei.huawei_configuration_operations import HuaweiConfigurationOperations
from cloudshell.networking.Huawei.huawei_connectivity_operations import HuaweiConnectivityOperations
from cloudshell.networking.Huawei.huawei_send_command_operations import HuaweiSendCommandOperations
from cloudshell.shell.core.context_utils import get_decrypted_password_by_attribute_name_wrapper, \
    get_attribute_by_name_wrapper
from cloudshell.shell.core.dependency_injection.context_based_logger import get_logger_with_thread_id



DEFAULT_PROMPT = '<.*?>'
SUPER_PROMPT = r'<.*?>'#super
CONFIG_MODE_PROMPT = r'\[.*?\]'#system-view


def send_default_actions(session):
    """Send default commands to configure/clear session outputs
    :return:
    """

    enter_enable_mode(session=session)
    session.hardware_expect(ENTER_CONFIG_MODE_PROMPT_COMMAND, CONFIG_MODE_PROMPT)
    session.hardware_expect('user-interface console 0', CONFIG_MODE_PROMPT)
    session.hardware_expect('screen-length 0', CONFIG_MODE_PROMPT)
    session.hardware_expect('quit', CONFIG_MODE_PROMPT)
    session.hardware_expect('quit', DEFAULT_PROMPT)


ENTER_CONFIG_MODE_PROMPT_COMMAND = 'system'
EXIT_CONFIG_MODE_PROMPT_COMMAND = 'quit'
DEFAULT_ACTIONS = send_default_actions
SUPPORTED_OS = ['VRP']
CONNECTION_TYPE = 'ssh'
DEFAULT_CONNECTION_TYPE = 'ssh'
#get_attribute_by_name_wrapper('Enable Password')()
def enter_enable_mode(session):
    result = session.hardware_expect('', re_string=DEFAULT_PROMPT)
    if not re.search(SUPER_PROMPT, result):
        session.hardware_expect('super', re_string=DEFAULT_PROMPT,
                                expect_map={'[Pp]assword': lambda session: session.send_line(
                                    get_decrypted_password_by_attribute_name_wrapper('Enable Password')() )})
        #

    result = session.hardware_expect('', re_string=DEFAULT_PROMPT)
    if not re.search(SUPER_PROMPT, result):
        raise Exception('enter_enable_mode', 'Enable password is incorrect')


CONNECTIVITY_OPERATIONS_CLASS = HuaweiConnectivityOperations
CONFIGURATION_OPERATIONS_CLASS = HuaweiConfigurationOperations
FIRMWARE_OPERATIONS_CLASS = HuaweiConfigurationOperations
AUTOLOAD_OPERATIONS_CLASS = HuaweiGenericSNMPAutoload
SEND_COMMAND_OPERATIONS_CLASS = HuaweiSendCommandOperations

GET_LOGGER_FUNCTION = get_logger_with_thread_id
POOL_TIMEOUT = 300

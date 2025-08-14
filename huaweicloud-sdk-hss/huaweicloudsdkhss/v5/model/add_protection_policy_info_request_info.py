# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddProtectionPolicyInfoRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'protection_mode': 'str',
        'deploy_mode': 'str',
        'protection_directory': 'str',
        'protection_type': 'str',
        'exclude_directory': 'str',
        'operating_system': 'str',
        'process_whitelist': 'list[TrustProcessInfo]',
        'ai_protection_status': 'str'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'protection_mode': 'protection_mode',
        'deploy_mode': 'deploy_mode',
        'protection_directory': 'protection_directory',
        'protection_type': 'protection_type',
        'exclude_directory': 'exclude_directory',
        'operating_system': 'operating_system',
        'process_whitelist': 'process_whitelist',
        'ai_protection_status': 'ai_protection_status'
    }

    def __init__(self, policy_name=None, protection_mode=None, deploy_mode=None, protection_directory=None, protection_type=None, exclude_directory=None, operating_system=None, process_whitelist=None, ai_protection_status=None):
        r"""AddProtectionPolicyInfoRequestInfo

        The model defined in huaweicloud sdk

        :param policy_name: 策略名称
        :type policy_name: str
        :param protection_mode: 防护动作，包含如下2种。   - alarm_and_isolation ：告警并自动隔离。   - alarm_only ：仅告警。
        :type protection_mode: str
        :param deploy_mode: 是否开启动态诱饵，包含如下2种，默认为关闭防护动态诱饵防护。   - opened ：开启。   - closed ：关闭。
        :type deploy_mode: str
        :param protection_directory: 防护目录，多个目录请用英文分号隔开，最多支持填写20个防护目录
        :type protection_directory: str
        :param protection_type: 防护文件类型，例如：docx，txt，avi
        :type protection_type: str
        :param exclude_directory: 排除目录(选填)，多个目录请用英文分号隔开，最多支持填写20个排除目录
        :type exclude_directory: str
        :param operating_system: 操作系统，包含如下：   - Windows : Windows系统   - Linux : Linux系统
        :type operating_system: str
        :param process_whitelist: 进程白名单
        :type process_whitelist: list[:class:`huaweicloudsdkhss.v5.TrustProcessInfo`]
        :param ai_protection_status: 是否开启AI勒索防护，包含如下2种，默认为关闭AI勒索防护，当前只支持Windows防护策略   - opened ：开启。   - closed ：关闭。
        :type ai_protection_status: str
        """
        
        

        self._policy_name = None
        self._protection_mode = None
        self._deploy_mode = None
        self._protection_directory = None
        self._protection_type = None
        self._exclude_directory = None
        self._operating_system = None
        self._process_whitelist = None
        self._ai_protection_status = None
        self.discriminator = None

        self.policy_name = policy_name
        self.protection_mode = protection_mode
        if deploy_mode is not None:
            self.deploy_mode = deploy_mode
        self.protection_directory = protection_directory
        self.protection_type = protection_type
        if exclude_directory is not None:
            self.exclude_directory = exclude_directory
        self.operating_system = operating_system
        if process_whitelist is not None:
            self.process_whitelist = process_whitelist
        if ai_protection_status is not None:
            self.ai_protection_status = ai_protection_status

    @property
    def policy_name(self):
        r"""Gets the policy_name of this AddProtectionPolicyInfoRequestInfo.

        策略名称

        :return: The policy_name of this AddProtectionPolicyInfoRequestInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this AddProtectionPolicyInfoRequestInfo.

        策略名称

        :param policy_name: The policy_name of this AddProtectionPolicyInfoRequestInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def protection_mode(self):
        r"""Gets the protection_mode of this AddProtectionPolicyInfoRequestInfo.

        防护动作，包含如下2种。   - alarm_and_isolation ：告警并自动隔离。   - alarm_only ：仅告警。

        :return: The protection_mode of this AddProtectionPolicyInfoRequestInfo.
        :rtype: str
        """
        return self._protection_mode

    @protection_mode.setter
    def protection_mode(self, protection_mode):
        r"""Sets the protection_mode of this AddProtectionPolicyInfoRequestInfo.

        防护动作，包含如下2种。   - alarm_and_isolation ：告警并自动隔离。   - alarm_only ：仅告警。

        :param protection_mode: The protection_mode of this AddProtectionPolicyInfoRequestInfo.
        :type protection_mode: str
        """
        self._protection_mode = protection_mode

    @property
    def deploy_mode(self):
        r"""Gets the deploy_mode of this AddProtectionPolicyInfoRequestInfo.

        是否开启动态诱饵，包含如下2种，默认为关闭防护动态诱饵防护。   - opened ：开启。   - closed ：关闭。

        :return: The deploy_mode of this AddProtectionPolicyInfoRequestInfo.
        :rtype: str
        """
        return self._deploy_mode

    @deploy_mode.setter
    def deploy_mode(self, deploy_mode):
        r"""Sets the deploy_mode of this AddProtectionPolicyInfoRequestInfo.

        是否开启动态诱饵，包含如下2种，默认为关闭防护动态诱饵防护。   - opened ：开启。   - closed ：关闭。

        :param deploy_mode: The deploy_mode of this AddProtectionPolicyInfoRequestInfo.
        :type deploy_mode: str
        """
        self._deploy_mode = deploy_mode

    @property
    def protection_directory(self):
        r"""Gets the protection_directory of this AddProtectionPolicyInfoRequestInfo.

        防护目录，多个目录请用英文分号隔开，最多支持填写20个防护目录

        :return: The protection_directory of this AddProtectionPolicyInfoRequestInfo.
        :rtype: str
        """
        return self._protection_directory

    @protection_directory.setter
    def protection_directory(self, protection_directory):
        r"""Sets the protection_directory of this AddProtectionPolicyInfoRequestInfo.

        防护目录，多个目录请用英文分号隔开，最多支持填写20个防护目录

        :param protection_directory: The protection_directory of this AddProtectionPolicyInfoRequestInfo.
        :type protection_directory: str
        """
        self._protection_directory = protection_directory

    @property
    def protection_type(self):
        r"""Gets the protection_type of this AddProtectionPolicyInfoRequestInfo.

        防护文件类型，例如：docx，txt，avi

        :return: The protection_type of this AddProtectionPolicyInfoRequestInfo.
        :rtype: str
        """
        return self._protection_type

    @protection_type.setter
    def protection_type(self, protection_type):
        r"""Sets the protection_type of this AddProtectionPolicyInfoRequestInfo.

        防护文件类型，例如：docx，txt，avi

        :param protection_type: The protection_type of this AddProtectionPolicyInfoRequestInfo.
        :type protection_type: str
        """
        self._protection_type = protection_type

    @property
    def exclude_directory(self):
        r"""Gets the exclude_directory of this AddProtectionPolicyInfoRequestInfo.

        排除目录(选填)，多个目录请用英文分号隔开，最多支持填写20个排除目录

        :return: The exclude_directory of this AddProtectionPolicyInfoRequestInfo.
        :rtype: str
        """
        return self._exclude_directory

    @exclude_directory.setter
    def exclude_directory(self, exclude_directory):
        r"""Sets the exclude_directory of this AddProtectionPolicyInfoRequestInfo.

        排除目录(选填)，多个目录请用英文分号隔开，最多支持填写20个排除目录

        :param exclude_directory: The exclude_directory of this AddProtectionPolicyInfoRequestInfo.
        :type exclude_directory: str
        """
        self._exclude_directory = exclude_directory

    @property
    def operating_system(self):
        r"""Gets the operating_system of this AddProtectionPolicyInfoRequestInfo.

        操作系统，包含如下：   - Windows : Windows系统   - Linux : Linux系统

        :return: The operating_system of this AddProtectionPolicyInfoRequestInfo.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        r"""Sets the operating_system of this AddProtectionPolicyInfoRequestInfo.

        操作系统，包含如下：   - Windows : Windows系统   - Linux : Linux系统

        :param operating_system: The operating_system of this AddProtectionPolicyInfoRequestInfo.
        :type operating_system: str
        """
        self._operating_system = operating_system

    @property
    def process_whitelist(self):
        r"""Gets the process_whitelist of this AddProtectionPolicyInfoRequestInfo.

        进程白名单

        :return: The process_whitelist of this AddProtectionPolicyInfoRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.TrustProcessInfo`]
        """
        return self._process_whitelist

    @process_whitelist.setter
    def process_whitelist(self, process_whitelist):
        r"""Sets the process_whitelist of this AddProtectionPolicyInfoRequestInfo.

        进程白名单

        :param process_whitelist: The process_whitelist of this AddProtectionPolicyInfoRequestInfo.
        :type process_whitelist: list[:class:`huaweicloudsdkhss.v5.TrustProcessInfo`]
        """
        self._process_whitelist = process_whitelist

    @property
    def ai_protection_status(self):
        r"""Gets the ai_protection_status of this AddProtectionPolicyInfoRequestInfo.

        是否开启AI勒索防护，包含如下2种，默认为关闭AI勒索防护，当前只支持Windows防护策略   - opened ：开启。   - closed ：关闭。

        :return: The ai_protection_status of this AddProtectionPolicyInfoRequestInfo.
        :rtype: str
        """
        return self._ai_protection_status

    @ai_protection_status.setter
    def ai_protection_status(self, ai_protection_status):
        r"""Sets the ai_protection_status of this AddProtectionPolicyInfoRequestInfo.

        是否开启AI勒索防护，包含如下2种，默认为关闭AI勒索防护，当前只支持Windows防护策略   - opened ：开启。   - closed ：关闭。

        :param ai_protection_status: The ai_protection_status of this AddProtectionPolicyInfoRequestInfo.
        :type ai_protection_status: str
        """
        self._ai_protection_status = ai_protection_status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddProtectionPolicyInfoRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

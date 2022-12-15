# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectionPolicyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'policy_name': 'str',
        'protection_mode': 'str',
        'bait_protection_status': 'str',
        'protection_directory': 'str',
        'protection_type': 'str',
        'exclude_directory': 'str',
        'runtime_detection_status': 'str',
        'runtime_detection_directory': 'str',
        'count_associated_server': 'int',
        'operating_system': 'str'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'protection_mode': 'protection_mode',
        'bait_protection_status': 'bait_protection_status',
        'protection_directory': 'protection_directory',
        'protection_type': 'protection_type',
        'exclude_directory': 'exclude_directory',
        'runtime_detection_status': 'runtime_detection_status',
        'runtime_detection_directory': 'runtime_detection_directory',
        'count_associated_server': 'count_associated_server',
        'operating_system': 'operating_system'
    }

    def __init__(self, policy_id=None, policy_name=None, protection_mode=None, bait_protection_status=None, protection_directory=None, protection_type=None, exclude_directory=None, runtime_detection_status=None, runtime_detection_directory=None, count_associated_server=None, operating_system=None):
        """ProtectionPolicyInfo

        The model defined in huaweicloud sdk

        :param policy_id: 策略ID
        :type policy_id: str
        :param policy_name: 策略名称
        :type policy_name: str
        :param protection_mode: 防护动作，包含如下2种。   - alarm_and_isolation ：告警并自动隔离。   - alarm_only ：仅告警。
        :type protection_mode: str
        :param bait_protection_status: 是否开启诱饵防护，包含如下1种, 默认为开启防护诱饵防护。   - opened ：开启。   - closed ：关闭。
        :type bait_protection_status: str
        :param protection_directory: 防护目录
        :type protection_directory: str
        :param protection_type: 防护文件类型
        :type protection_type: str
        :param exclude_directory: 排除目录，选填
        :type exclude_directory: str
        :param runtime_detection_status: 是否运行时检测，包含如下2种，暂时只有关闭一种状态，为保留字段。   - opened ：开启。   - closed ：关闭。
        :type runtime_detection_status: str
        :param runtime_detection_directory: 运行时检测目录，所有目录是/,现在为保留字段
        :type runtime_detection_directory: str
        :param count_associated_server: 关联server个数
        :type count_associated_server: int
        :param operating_system: 操作系统类型
        :type operating_system: str
        """
        
        

        self._policy_id = None
        self._policy_name = None
        self._protection_mode = None
        self._bait_protection_status = None
        self._protection_directory = None
        self._protection_type = None
        self._exclude_directory = None
        self._runtime_detection_status = None
        self._runtime_detection_directory = None
        self._count_associated_server = None
        self._operating_system = None
        self.discriminator = None

        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        if protection_mode is not None:
            self.protection_mode = protection_mode
        if bait_protection_status is not None:
            self.bait_protection_status = bait_protection_status
        if protection_directory is not None:
            self.protection_directory = protection_directory
        if protection_type is not None:
            self.protection_type = protection_type
        if exclude_directory is not None:
            self.exclude_directory = exclude_directory
        if runtime_detection_status is not None:
            self.runtime_detection_status = runtime_detection_status
        if runtime_detection_directory is not None:
            self.runtime_detection_directory = runtime_detection_directory
        if count_associated_server is not None:
            self.count_associated_server = count_associated_server
        if operating_system is not None:
            self.operating_system = operating_system

    @property
    def policy_id(self):
        """Gets the policy_id of this ProtectionPolicyInfo.

        策略ID

        :return: The policy_id of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this ProtectionPolicyInfo.

        策略ID

        :param policy_id: The policy_id of this ProtectionPolicyInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        """Gets the policy_name of this ProtectionPolicyInfo.

        策略名称

        :return: The policy_name of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this ProtectionPolicyInfo.

        策略名称

        :param policy_name: The policy_name of this ProtectionPolicyInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def protection_mode(self):
        """Gets the protection_mode of this ProtectionPolicyInfo.

        防护动作，包含如下2种。   - alarm_and_isolation ：告警并自动隔离。   - alarm_only ：仅告警。

        :return: The protection_mode of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._protection_mode

    @protection_mode.setter
    def protection_mode(self, protection_mode):
        """Sets the protection_mode of this ProtectionPolicyInfo.

        防护动作，包含如下2种。   - alarm_and_isolation ：告警并自动隔离。   - alarm_only ：仅告警。

        :param protection_mode: The protection_mode of this ProtectionPolicyInfo.
        :type protection_mode: str
        """
        self._protection_mode = protection_mode

    @property
    def bait_protection_status(self):
        """Gets the bait_protection_status of this ProtectionPolicyInfo.

        是否开启诱饵防护，包含如下1种, 默认为开启防护诱饵防护。   - opened ：开启。   - closed ：关闭。

        :return: The bait_protection_status of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._bait_protection_status

    @bait_protection_status.setter
    def bait_protection_status(self, bait_protection_status):
        """Sets the bait_protection_status of this ProtectionPolicyInfo.

        是否开启诱饵防护，包含如下1种, 默认为开启防护诱饵防护。   - opened ：开启。   - closed ：关闭。

        :param bait_protection_status: The bait_protection_status of this ProtectionPolicyInfo.
        :type bait_protection_status: str
        """
        self._bait_protection_status = bait_protection_status

    @property
    def protection_directory(self):
        """Gets the protection_directory of this ProtectionPolicyInfo.

        防护目录

        :return: The protection_directory of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._protection_directory

    @protection_directory.setter
    def protection_directory(self, protection_directory):
        """Sets the protection_directory of this ProtectionPolicyInfo.

        防护目录

        :param protection_directory: The protection_directory of this ProtectionPolicyInfo.
        :type protection_directory: str
        """
        self._protection_directory = protection_directory

    @property
    def protection_type(self):
        """Gets the protection_type of this ProtectionPolicyInfo.

        防护文件类型

        :return: The protection_type of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._protection_type

    @protection_type.setter
    def protection_type(self, protection_type):
        """Sets the protection_type of this ProtectionPolicyInfo.

        防护文件类型

        :param protection_type: The protection_type of this ProtectionPolicyInfo.
        :type protection_type: str
        """
        self._protection_type = protection_type

    @property
    def exclude_directory(self):
        """Gets the exclude_directory of this ProtectionPolicyInfo.

        排除目录，选填

        :return: The exclude_directory of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._exclude_directory

    @exclude_directory.setter
    def exclude_directory(self, exclude_directory):
        """Sets the exclude_directory of this ProtectionPolicyInfo.

        排除目录，选填

        :param exclude_directory: The exclude_directory of this ProtectionPolicyInfo.
        :type exclude_directory: str
        """
        self._exclude_directory = exclude_directory

    @property
    def runtime_detection_status(self):
        """Gets the runtime_detection_status of this ProtectionPolicyInfo.

        是否运行时检测，包含如下2种，暂时只有关闭一种状态，为保留字段。   - opened ：开启。   - closed ：关闭。

        :return: The runtime_detection_status of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._runtime_detection_status

    @runtime_detection_status.setter
    def runtime_detection_status(self, runtime_detection_status):
        """Sets the runtime_detection_status of this ProtectionPolicyInfo.

        是否运行时检测，包含如下2种，暂时只有关闭一种状态，为保留字段。   - opened ：开启。   - closed ：关闭。

        :param runtime_detection_status: The runtime_detection_status of this ProtectionPolicyInfo.
        :type runtime_detection_status: str
        """
        self._runtime_detection_status = runtime_detection_status

    @property
    def runtime_detection_directory(self):
        """Gets the runtime_detection_directory of this ProtectionPolicyInfo.

        运行时检测目录，所有目录是/,现在为保留字段

        :return: The runtime_detection_directory of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._runtime_detection_directory

    @runtime_detection_directory.setter
    def runtime_detection_directory(self, runtime_detection_directory):
        """Sets the runtime_detection_directory of this ProtectionPolicyInfo.

        运行时检测目录，所有目录是/,现在为保留字段

        :param runtime_detection_directory: The runtime_detection_directory of this ProtectionPolicyInfo.
        :type runtime_detection_directory: str
        """
        self._runtime_detection_directory = runtime_detection_directory

    @property
    def count_associated_server(self):
        """Gets the count_associated_server of this ProtectionPolicyInfo.

        关联server个数

        :return: The count_associated_server of this ProtectionPolicyInfo.
        :rtype: int
        """
        return self._count_associated_server

    @count_associated_server.setter
    def count_associated_server(self, count_associated_server):
        """Sets the count_associated_server of this ProtectionPolicyInfo.

        关联server个数

        :param count_associated_server: The count_associated_server of this ProtectionPolicyInfo.
        :type count_associated_server: int
        """
        self._count_associated_server = count_associated_server

    @property
    def operating_system(self):
        """Gets the operating_system of this ProtectionPolicyInfo.

        操作系统类型

        :return: The operating_system of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this ProtectionPolicyInfo.

        操作系统类型

        :param operating_system: The operating_system of this ProtectionPolicyInfo.
        :type operating_system: str
        """
        self._operating_system = operating_system

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
        if not isinstance(other, ProtectionPolicyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

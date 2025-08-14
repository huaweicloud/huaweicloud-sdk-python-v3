# coding: utf-8

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
        'deploy_mode': 'str',
        'protection_directory': 'str',
        'protection_type': 'str',
        'exclude_directory': 'str',
        'runtime_detection_status': 'str',
        'runtime_detection_directory': 'str',
        'count_associated_server': 'int',
        'operating_system': 'str',
        'process_whitelist': 'list[TrustProcessInfo]',
        'default_policy': 'int',
        'ai_protection_status': 'str'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'protection_mode': 'protection_mode',
        'bait_protection_status': 'bait_protection_status',
        'deploy_mode': 'deploy_mode',
        'protection_directory': 'protection_directory',
        'protection_type': 'protection_type',
        'exclude_directory': 'exclude_directory',
        'runtime_detection_status': 'runtime_detection_status',
        'runtime_detection_directory': 'runtime_detection_directory',
        'count_associated_server': 'count_associated_server',
        'operating_system': 'operating_system',
        'process_whitelist': 'process_whitelist',
        'default_policy': 'default_policy',
        'ai_protection_status': 'ai_protection_status'
    }

    def __init__(self, policy_id=None, policy_name=None, protection_mode=None, bait_protection_status=None, deploy_mode=None, protection_directory=None, protection_type=None, exclude_directory=None, runtime_detection_status=None, runtime_detection_directory=None, count_associated_server=None, operating_system=None, process_whitelist=None, default_policy=None, ai_protection_status=None):
        r"""ProtectionPolicyInfo

        The model defined in huaweicloud sdk

        :param policy_id: **参数解释**: 策略ID **取值范围**: 字符长度0-128 
        :type policy_id: str
        :param policy_name: **参数解释**: 防护策略名称 **取值范围**: 字符长度1-128 
        :type policy_name: str
        :param protection_mode: **参数解释**: 防护动作 **取值范围**: 包含如下2种。   - alarm_and_isolation ：告警并自动隔离。   - alarm_only ：仅告警。
        :type protection_mode: str
        :param bait_protection_status: **参数解释**: 是否开启诱饵防护 **取值范围**: 包含如下1种，默认为开启防护诱饵防护。   - opened ：开启。
        :type bait_protection_status: str
        :param deploy_mode: **参数解释**: 是否开启动态诱饵防护 **取值范围**: 包含如下2种，默认为关闭动态诱饵防护。   - opened ：开启。   - closed ：关闭。
        :type deploy_mode: str
        :param protection_directory: **参数解释**: 防护目录 **取值范围**: 字符长度1-128 
        :type protection_directory: str
        :param protection_type: **参数解释**: 防护文件类型，例如：docx，txt，avi **取值范围**: 字符长度1-128 
        :type protection_type: str
        :param exclude_directory: **参数解释**: 排除目录，选填 **取值范围**: 字符长度1-128 
        :type exclude_directory: str
        :param runtime_detection_status: **参数解释**: 是否运行时检测 **取值范围**: 包含如下2种，暂时只有关闭一种状态，为保留字段。   - opened ：开启。   - closed ：关闭。
        :type runtime_detection_status: str
        :param runtime_detection_directory: **参数解释**: 运行时检测目录，现在为保留字段 **取值范围**: 字符长度1-128
        :type runtime_detection_directory: str
        :param count_associated_server: **参数解释**: 关联server个数 **取值范围**: 取值范围0-2097152
        :type count_associated_server: int
        :param operating_system: **参数解释**: 操作系统类型。 - Linux - Windows **取值范围**: 字符长度1-128
        :type operating_system: str
        :param process_whitelist: 进程白名单
        :type process_whitelist: list[:class:`huaweicloudsdkhss.v5.TrustProcessInfo`]
        :param default_policy: **参数解释**: 是否为默认策略 **取值范围**: 包含如下2种。   - 0 ：非默认策略。   - 1 ：默认策略
        :type default_policy: int
        :param ai_protection_status: **参数解释**: 是否开启AI勒索防护，包含如下1种, 默认为开启AI勒索防护。   - opened ：开启。   - closed ：关闭。  **取值范围**: 字符长度1-128
        :type ai_protection_status: str
        """
        
        

        self._policy_id = None
        self._policy_name = None
        self._protection_mode = None
        self._bait_protection_status = None
        self._deploy_mode = None
        self._protection_directory = None
        self._protection_type = None
        self._exclude_directory = None
        self._runtime_detection_status = None
        self._runtime_detection_directory = None
        self._count_associated_server = None
        self._operating_system = None
        self._process_whitelist = None
        self._default_policy = None
        self._ai_protection_status = None
        self.discriminator = None

        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        if protection_mode is not None:
            self.protection_mode = protection_mode
        if bait_protection_status is not None:
            self.bait_protection_status = bait_protection_status
        if deploy_mode is not None:
            self.deploy_mode = deploy_mode
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
        if process_whitelist is not None:
            self.process_whitelist = process_whitelist
        if default_policy is not None:
            self.default_policy = default_policy
        if ai_protection_status is not None:
            self.ai_protection_status = ai_protection_status

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ProtectionPolicyInfo.

        **参数解释**: 策略ID **取值范围**: 字符长度0-128 

        :return: The policy_id of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ProtectionPolicyInfo.

        **参数解释**: 策略ID **取值范围**: 字符长度0-128 

        :param policy_id: The policy_id of this ProtectionPolicyInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ProtectionPolicyInfo.

        **参数解释**: 防护策略名称 **取值范围**: 字符长度1-128 

        :return: The policy_name of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ProtectionPolicyInfo.

        **参数解释**: 防护策略名称 **取值范围**: 字符长度1-128 

        :param policy_name: The policy_name of this ProtectionPolicyInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def protection_mode(self):
        r"""Gets the protection_mode of this ProtectionPolicyInfo.

        **参数解释**: 防护动作 **取值范围**: 包含如下2种。   - alarm_and_isolation ：告警并自动隔离。   - alarm_only ：仅告警。

        :return: The protection_mode of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._protection_mode

    @protection_mode.setter
    def protection_mode(self, protection_mode):
        r"""Sets the protection_mode of this ProtectionPolicyInfo.

        **参数解释**: 防护动作 **取值范围**: 包含如下2种。   - alarm_and_isolation ：告警并自动隔离。   - alarm_only ：仅告警。

        :param protection_mode: The protection_mode of this ProtectionPolicyInfo.
        :type protection_mode: str
        """
        self._protection_mode = protection_mode

    @property
    def bait_protection_status(self):
        r"""Gets the bait_protection_status of this ProtectionPolicyInfo.

        **参数解释**: 是否开启诱饵防护 **取值范围**: 包含如下1种，默认为开启防护诱饵防护。   - opened ：开启。

        :return: The bait_protection_status of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._bait_protection_status

    @bait_protection_status.setter
    def bait_protection_status(self, bait_protection_status):
        r"""Sets the bait_protection_status of this ProtectionPolicyInfo.

        **参数解释**: 是否开启诱饵防护 **取值范围**: 包含如下1种，默认为开启防护诱饵防护。   - opened ：开启。

        :param bait_protection_status: The bait_protection_status of this ProtectionPolicyInfo.
        :type bait_protection_status: str
        """
        self._bait_protection_status = bait_protection_status

    @property
    def deploy_mode(self):
        r"""Gets the deploy_mode of this ProtectionPolicyInfo.

        **参数解释**: 是否开启动态诱饵防护 **取值范围**: 包含如下2种，默认为关闭动态诱饵防护。   - opened ：开启。   - closed ：关闭。

        :return: The deploy_mode of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._deploy_mode

    @deploy_mode.setter
    def deploy_mode(self, deploy_mode):
        r"""Sets the deploy_mode of this ProtectionPolicyInfo.

        **参数解释**: 是否开启动态诱饵防护 **取值范围**: 包含如下2种，默认为关闭动态诱饵防护。   - opened ：开启。   - closed ：关闭。

        :param deploy_mode: The deploy_mode of this ProtectionPolicyInfo.
        :type deploy_mode: str
        """
        self._deploy_mode = deploy_mode

    @property
    def protection_directory(self):
        r"""Gets the protection_directory of this ProtectionPolicyInfo.

        **参数解释**: 防护目录 **取值范围**: 字符长度1-128 

        :return: The protection_directory of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._protection_directory

    @protection_directory.setter
    def protection_directory(self, protection_directory):
        r"""Sets the protection_directory of this ProtectionPolicyInfo.

        **参数解释**: 防护目录 **取值范围**: 字符长度1-128 

        :param protection_directory: The protection_directory of this ProtectionPolicyInfo.
        :type protection_directory: str
        """
        self._protection_directory = protection_directory

    @property
    def protection_type(self):
        r"""Gets the protection_type of this ProtectionPolicyInfo.

        **参数解释**: 防护文件类型，例如：docx，txt，avi **取值范围**: 字符长度1-128 

        :return: The protection_type of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._protection_type

    @protection_type.setter
    def protection_type(self, protection_type):
        r"""Sets the protection_type of this ProtectionPolicyInfo.

        **参数解释**: 防护文件类型，例如：docx，txt，avi **取值范围**: 字符长度1-128 

        :param protection_type: The protection_type of this ProtectionPolicyInfo.
        :type protection_type: str
        """
        self._protection_type = protection_type

    @property
    def exclude_directory(self):
        r"""Gets the exclude_directory of this ProtectionPolicyInfo.

        **参数解释**: 排除目录，选填 **取值范围**: 字符长度1-128 

        :return: The exclude_directory of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._exclude_directory

    @exclude_directory.setter
    def exclude_directory(self, exclude_directory):
        r"""Sets the exclude_directory of this ProtectionPolicyInfo.

        **参数解释**: 排除目录，选填 **取值范围**: 字符长度1-128 

        :param exclude_directory: The exclude_directory of this ProtectionPolicyInfo.
        :type exclude_directory: str
        """
        self._exclude_directory = exclude_directory

    @property
    def runtime_detection_status(self):
        r"""Gets the runtime_detection_status of this ProtectionPolicyInfo.

        **参数解释**: 是否运行时检测 **取值范围**: 包含如下2种，暂时只有关闭一种状态，为保留字段。   - opened ：开启。   - closed ：关闭。

        :return: The runtime_detection_status of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._runtime_detection_status

    @runtime_detection_status.setter
    def runtime_detection_status(self, runtime_detection_status):
        r"""Sets the runtime_detection_status of this ProtectionPolicyInfo.

        **参数解释**: 是否运行时检测 **取值范围**: 包含如下2种，暂时只有关闭一种状态，为保留字段。   - opened ：开启。   - closed ：关闭。

        :param runtime_detection_status: The runtime_detection_status of this ProtectionPolicyInfo.
        :type runtime_detection_status: str
        """
        self._runtime_detection_status = runtime_detection_status

    @property
    def runtime_detection_directory(self):
        r"""Gets the runtime_detection_directory of this ProtectionPolicyInfo.

        **参数解释**: 运行时检测目录，现在为保留字段 **取值范围**: 字符长度1-128

        :return: The runtime_detection_directory of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._runtime_detection_directory

    @runtime_detection_directory.setter
    def runtime_detection_directory(self, runtime_detection_directory):
        r"""Sets the runtime_detection_directory of this ProtectionPolicyInfo.

        **参数解释**: 运行时检测目录，现在为保留字段 **取值范围**: 字符长度1-128

        :param runtime_detection_directory: The runtime_detection_directory of this ProtectionPolicyInfo.
        :type runtime_detection_directory: str
        """
        self._runtime_detection_directory = runtime_detection_directory

    @property
    def count_associated_server(self):
        r"""Gets the count_associated_server of this ProtectionPolicyInfo.

        **参数解释**: 关联server个数 **取值范围**: 取值范围0-2097152

        :return: The count_associated_server of this ProtectionPolicyInfo.
        :rtype: int
        """
        return self._count_associated_server

    @count_associated_server.setter
    def count_associated_server(self, count_associated_server):
        r"""Sets the count_associated_server of this ProtectionPolicyInfo.

        **参数解释**: 关联server个数 **取值范围**: 取值范围0-2097152

        :param count_associated_server: The count_associated_server of this ProtectionPolicyInfo.
        :type count_associated_server: int
        """
        self._count_associated_server = count_associated_server

    @property
    def operating_system(self):
        r"""Gets the operating_system of this ProtectionPolicyInfo.

        **参数解释**: 操作系统类型。 - Linux - Windows **取值范围**: 字符长度1-128

        :return: The operating_system of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        r"""Sets the operating_system of this ProtectionPolicyInfo.

        **参数解释**: 操作系统类型。 - Linux - Windows **取值范围**: 字符长度1-128

        :param operating_system: The operating_system of this ProtectionPolicyInfo.
        :type operating_system: str
        """
        self._operating_system = operating_system

    @property
    def process_whitelist(self):
        r"""Gets the process_whitelist of this ProtectionPolicyInfo.

        进程白名单

        :return: The process_whitelist of this ProtectionPolicyInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.TrustProcessInfo`]
        """
        return self._process_whitelist

    @process_whitelist.setter
    def process_whitelist(self, process_whitelist):
        r"""Sets the process_whitelist of this ProtectionPolicyInfo.

        进程白名单

        :param process_whitelist: The process_whitelist of this ProtectionPolicyInfo.
        :type process_whitelist: list[:class:`huaweicloudsdkhss.v5.TrustProcessInfo`]
        """
        self._process_whitelist = process_whitelist

    @property
    def default_policy(self):
        r"""Gets the default_policy of this ProtectionPolicyInfo.

        **参数解释**: 是否为默认策略 **取值范围**: 包含如下2种。   - 0 ：非默认策略。   - 1 ：默认策略

        :return: The default_policy of this ProtectionPolicyInfo.
        :rtype: int
        """
        return self._default_policy

    @default_policy.setter
    def default_policy(self, default_policy):
        r"""Sets the default_policy of this ProtectionPolicyInfo.

        **参数解释**: 是否为默认策略 **取值范围**: 包含如下2种。   - 0 ：非默认策略。   - 1 ：默认策略

        :param default_policy: The default_policy of this ProtectionPolicyInfo.
        :type default_policy: int
        """
        self._default_policy = default_policy

    @property
    def ai_protection_status(self):
        r"""Gets the ai_protection_status of this ProtectionPolicyInfo.

        **参数解释**: 是否开启AI勒索防护，包含如下1种, 默认为开启AI勒索防护。   - opened ：开启。   - closed ：关闭。  **取值范围**: 字符长度1-128

        :return: The ai_protection_status of this ProtectionPolicyInfo.
        :rtype: str
        """
        return self._ai_protection_status

    @ai_protection_status.setter
    def ai_protection_status(self, ai_protection_status):
        r"""Sets the ai_protection_status of this ProtectionPolicyInfo.

        **参数解释**: 是否开启AI勒索防护，包含如下1种, 默认为开启AI勒索防护。   - opened ：开启。   - closed ：关闭。  **取值范围**: 字符长度1-128

        :param ai_protection_status: The ai_protection_status of this ProtectionPolicyInfo.
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
        if not isinstance(other, ProtectionPolicyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

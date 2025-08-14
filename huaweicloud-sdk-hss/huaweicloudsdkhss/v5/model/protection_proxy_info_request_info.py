# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectionProxyInfoRequestInfo:

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
        'operating_system': 'str',
        'process_whitelist': 'list[TrustProcessInfo]'
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
        'operating_system': 'operating_system',
        'process_whitelist': 'process_whitelist'
    }

    def __init__(self, policy_id=None, policy_name=None, protection_mode=None, bait_protection_status=None, protection_directory=None, protection_type=None, exclude_directory=None, runtime_detection_status=None, operating_system=None, process_whitelist=None):
        r"""ProtectionProxyInfoRequestInfo

        The model defined in huaweicloud sdk

        :param policy_id: **参数解释**: 策略ID，新建策略可不填。 **约束限制**: 不涉及 **取值范围**: 字符长度0-64 **默认取值**: 不涉及
        :type policy_id: str
        :param policy_name: **参数解释**: 策略名称，新建防护策略则必填 **约束限制**: 不涉及 **取值范围**: 字符长度0-64 **默认取值**: 不涉及
        :type policy_name: str
        :param protection_mode: **参数解释**: 防护动作，新建防护策略则必填 **约束限制**: 不涉及 **取值范围**: 包含如下：   - alarm_and_isolation ：告警并自动隔离。   - alarm_only ：仅告警。 **默认取值**: 不涉及
        :type protection_mode: str
        :param bait_protection_status: **参数解释**: 是否开启诱饵防护，新建防护策略则必填。 **约束限制**: 不涉及 **取值范围**: 包含如下1种：   - opened ：开启。 **默认取值**: 不涉及
        :type bait_protection_status: str
        :param protection_directory: **参数解释**: 防护目录，新建防护策略则必填。 **约束限制**: 多个目录请用英文分号隔开，最多支持填写20个防护目录 **取值范围**: 字符长度0-128位，特殊符号只允许使用._-+，不能以空格开头，防护目录长度不得超过256个字符。 **默认取值**: 不涉及 
        :type protection_directory: str
        :param protection_type: **参数解释**: 防护文件类型，例如：docx，txt，avi,新建防护策略则必填 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type protection_type: str
        :param exclude_directory: **参数解释**: 排除目录(选填) **约束限制**: 多个目录请用英文分号隔开，最多支持填写20个排除目录 **取值范围**: 字符长度0-128位，特殊符号只允许使用._-+，不能以空格开头，防护目录长度不得超过256个字符。 **默认取值**: 不涉及 
        :type exclude_directory: str
        :param runtime_detection_status: **参数解释**: 是否运行时检测 **约束限制**: 不涉及 **取值范围**: 暂时只有关闭一种状态，为预留字段。   - closed ：关闭。 **默认取值**: 不涉及
        :type runtime_detection_status: str
        :param operating_system: **参数解释**: 支持该策略的操作系统，新建防护策略则必填 **约束限制**: 不涉及 **取值范围**: 包含两种：   - Windows : Windows系统   - Linux : Linux系统 **默认取值**: 不涉及
        :type operating_system: str
        :param process_whitelist: 进程白名单
        :type process_whitelist: list[:class:`huaweicloudsdkhss.v5.TrustProcessInfo`]
        """
        
        

        self._policy_id = None
        self._policy_name = None
        self._protection_mode = None
        self._bait_protection_status = None
        self._protection_directory = None
        self._protection_type = None
        self._exclude_directory = None
        self._runtime_detection_status = None
        self._operating_system = None
        self._process_whitelist = None
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
        if operating_system is not None:
            self.operating_system = operating_system
        if process_whitelist is not None:
            self.process_whitelist = process_whitelist

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ProtectionProxyInfoRequestInfo.

        **参数解释**: 策略ID，新建策略可不填。 **约束限制**: 不涉及 **取值范围**: 字符长度0-64 **默认取值**: 不涉及

        :return: The policy_id of this ProtectionProxyInfoRequestInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ProtectionProxyInfoRequestInfo.

        **参数解释**: 策略ID，新建策略可不填。 **约束限制**: 不涉及 **取值范围**: 字符长度0-64 **默认取值**: 不涉及

        :param policy_id: The policy_id of this ProtectionProxyInfoRequestInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ProtectionProxyInfoRequestInfo.

        **参数解释**: 策略名称，新建防护策略则必填 **约束限制**: 不涉及 **取值范围**: 字符长度0-64 **默认取值**: 不涉及

        :return: The policy_name of this ProtectionProxyInfoRequestInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ProtectionProxyInfoRequestInfo.

        **参数解释**: 策略名称，新建防护策略则必填 **约束限制**: 不涉及 **取值范围**: 字符长度0-64 **默认取值**: 不涉及

        :param policy_name: The policy_name of this ProtectionProxyInfoRequestInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def protection_mode(self):
        r"""Gets the protection_mode of this ProtectionProxyInfoRequestInfo.

        **参数解释**: 防护动作，新建防护策略则必填 **约束限制**: 不涉及 **取值范围**: 包含如下：   - alarm_and_isolation ：告警并自动隔离。   - alarm_only ：仅告警。 **默认取值**: 不涉及

        :return: The protection_mode of this ProtectionProxyInfoRequestInfo.
        :rtype: str
        """
        return self._protection_mode

    @protection_mode.setter
    def protection_mode(self, protection_mode):
        r"""Sets the protection_mode of this ProtectionProxyInfoRequestInfo.

        **参数解释**: 防护动作，新建防护策略则必填 **约束限制**: 不涉及 **取值范围**: 包含如下：   - alarm_and_isolation ：告警并自动隔离。   - alarm_only ：仅告警。 **默认取值**: 不涉及

        :param protection_mode: The protection_mode of this ProtectionProxyInfoRequestInfo.
        :type protection_mode: str
        """
        self._protection_mode = protection_mode

    @property
    def bait_protection_status(self):
        r"""Gets the bait_protection_status of this ProtectionProxyInfoRequestInfo.

        **参数解释**: 是否开启诱饵防护，新建防护策略则必填。 **约束限制**: 不涉及 **取值范围**: 包含如下1种：   - opened ：开启。 **默认取值**: 不涉及

        :return: The bait_protection_status of this ProtectionProxyInfoRequestInfo.
        :rtype: str
        """
        return self._bait_protection_status

    @bait_protection_status.setter
    def bait_protection_status(self, bait_protection_status):
        r"""Sets the bait_protection_status of this ProtectionProxyInfoRequestInfo.

        **参数解释**: 是否开启诱饵防护，新建防护策略则必填。 **约束限制**: 不涉及 **取值范围**: 包含如下1种：   - opened ：开启。 **默认取值**: 不涉及

        :param bait_protection_status: The bait_protection_status of this ProtectionProxyInfoRequestInfo.
        :type bait_protection_status: str
        """
        self._bait_protection_status = bait_protection_status

    @property
    def protection_directory(self):
        r"""Gets the protection_directory of this ProtectionProxyInfoRequestInfo.

        **参数解释**: 防护目录，新建防护策略则必填。 **约束限制**: 多个目录请用英文分号隔开，最多支持填写20个防护目录 **取值范围**: 字符长度0-128位，特殊符号只允许使用._-+，不能以空格开头，防护目录长度不得超过256个字符。 **默认取值**: 不涉及 

        :return: The protection_directory of this ProtectionProxyInfoRequestInfo.
        :rtype: str
        """
        return self._protection_directory

    @protection_directory.setter
    def protection_directory(self, protection_directory):
        r"""Sets the protection_directory of this ProtectionProxyInfoRequestInfo.

        **参数解释**: 防护目录，新建防护策略则必填。 **约束限制**: 多个目录请用英文分号隔开，最多支持填写20个防护目录 **取值范围**: 字符长度0-128位，特殊符号只允许使用._-+，不能以空格开头，防护目录长度不得超过256个字符。 **默认取值**: 不涉及 

        :param protection_directory: The protection_directory of this ProtectionProxyInfoRequestInfo.
        :type protection_directory: str
        """
        self._protection_directory = protection_directory

    @property
    def protection_type(self):
        r"""Gets the protection_type of this ProtectionProxyInfoRequestInfo.

        **参数解释**: 防护文件类型，例如：docx，txt，avi,新建防护策略则必填 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The protection_type of this ProtectionProxyInfoRequestInfo.
        :rtype: str
        """
        return self._protection_type

    @protection_type.setter
    def protection_type(self, protection_type):
        r"""Sets the protection_type of this ProtectionProxyInfoRequestInfo.

        **参数解释**: 防护文件类型，例如：docx，txt，avi,新建防护策略则必填 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param protection_type: The protection_type of this ProtectionProxyInfoRequestInfo.
        :type protection_type: str
        """
        self._protection_type = protection_type

    @property
    def exclude_directory(self):
        r"""Gets the exclude_directory of this ProtectionProxyInfoRequestInfo.

        **参数解释**: 排除目录(选填) **约束限制**: 多个目录请用英文分号隔开，最多支持填写20个排除目录 **取值范围**: 字符长度0-128位，特殊符号只允许使用._-+，不能以空格开头，防护目录长度不得超过256个字符。 **默认取值**: 不涉及 

        :return: The exclude_directory of this ProtectionProxyInfoRequestInfo.
        :rtype: str
        """
        return self._exclude_directory

    @exclude_directory.setter
    def exclude_directory(self, exclude_directory):
        r"""Sets the exclude_directory of this ProtectionProxyInfoRequestInfo.

        **参数解释**: 排除目录(选填) **约束限制**: 多个目录请用英文分号隔开，最多支持填写20个排除目录 **取值范围**: 字符长度0-128位，特殊符号只允许使用._-+，不能以空格开头，防护目录长度不得超过256个字符。 **默认取值**: 不涉及 

        :param exclude_directory: The exclude_directory of this ProtectionProxyInfoRequestInfo.
        :type exclude_directory: str
        """
        self._exclude_directory = exclude_directory

    @property
    def runtime_detection_status(self):
        r"""Gets the runtime_detection_status of this ProtectionProxyInfoRequestInfo.

        **参数解释**: 是否运行时检测 **约束限制**: 不涉及 **取值范围**: 暂时只有关闭一种状态，为预留字段。   - closed ：关闭。 **默认取值**: 不涉及

        :return: The runtime_detection_status of this ProtectionProxyInfoRequestInfo.
        :rtype: str
        """
        return self._runtime_detection_status

    @runtime_detection_status.setter
    def runtime_detection_status(self, runtime_detection_status):
        r"""Sets the runtime_detection_status of this ProtectionProxyInfoRequestInfo.

        **参数解释**: 是否运行时检测 **约束限制**: 不涉及 **取值范围**: 暂时只有关闭一种状态，为预留字段。   - closed ：关闭。 **默认取值**: 不涉及

        :param runtime_detection_status: The runtime_detection_status of this ProtectionProxyInfoRequestInfo.
        :type runtime_detection_status: str
        """
        self._runtime_detection_status = runtime_detection_status

    @property
    def operating_system(self):
        r"""Gets the operating_system of this ProtectionProxyInfoRequestInfo.

        **参数解释**: 支持该策略的操作系统，新建防护策略则必填 **约束限制**: 不涉及 **取值范围**: 包含两种：   - Windows : Windows系统   - Linux : Linux系统 **默认取值**: 不涉及

        :return: The operating_system of this ProtectionProxyInfoRequestInfo.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        r"""Sets the operating_system of this ProtectionProxyInfoRequestInfo.

        **参数解释**: 支持该策略的操作系统，新建防护策略则必填 **约束限制**: 不涉及 **取值范围**: 包含两种：   - Windows : Windows系统   - Linux : Linux系统 **默认取值**: 不涉及

        :param operating_system: The operating_system of this ProtectionProxyInfoRequestInfo.
        :type operating_system: str
        """
        self._operating_system = operating_system

    @property
    def process_whitelist(self):
        r"""Gets the process_whitelist of this ProtectionProxyInfoRequestInfo.

        进程白名单

        :return: The process_whitelist of this ProtectionProxyInfoRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.TrustProcessInfo`]
        """
        return self._process_whitelist

    @process_whitelist.setter
    def process_whitelist(self, process_whitelist):
        r"""Sets the process_whitelist of this ProtectionProxyInfoRequestInfo.

        进程白名单

        :param process_whitelist: The process_whitelist of this ProtectionProxyInfoRequestInfo.
        :type process_whitelist: list[:class:`huaweicloudsdkhss.v5.TrustProcessInfo`]
        """
        self._process_whitelist = process_whitelist

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
        if not isinstance(other, ProtectionProxyInfoRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

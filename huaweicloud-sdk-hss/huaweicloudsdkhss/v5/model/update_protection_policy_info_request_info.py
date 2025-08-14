# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateProtectionPolicyInfoRequestInfo:

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
        'agent_id_list': 'list[str]',
        'operating_system': 'str',
        'runtime_detection_status': 'str',
        'process_whitelist': 'list[TrustProcessInfo]',
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
        'agent_id_list': 'agent_id_list',
        'operating_system': 'operating_system',
        'runtime_detection_status': 'runtime_detection_status',
        'process_whitelist': 'process_whitelist',
        'ai_protection_status': 'ai_protection_status'
    }

    def __init__(self, policy_id=None, policy_name=None, protection_mode=None, bait_protection_status=None, deploy_mode=None, protection_directory=None, protection_type=None, exclude_directory=None, agent_id_list=None, operating_system=None, runtime_detection_status=None, process_whitelist=None, ai_protection_status=None):
        r"""UpdateProtectionPolicyInfoRequestInfo

        The model defined in huaweicloud sdk

        :param policy_id: **参数解释**: 需要修改的防护策略ID，您可以通过[查询勒索病毒的防护策略列表](ListProtectionPolicy.xml)接口获取ID。 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type policy_id: str
        :param policy_name: **参数解释**: 策略名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type policy_name: str
        :param protection_mode: **参数解释**: 防护动作 **约束限制**: 不涉及 **取值范围**: 包含两种：   - alarm_and_isolation ：告警并自动隔离。   - alarm_only ：仅告警。 **默认取值**: 不涉及 
        :type protection_mode: str
        :param bait_protection_status: **参数解释**: 是否开启诱饵防护 **约束限制**: 不涉及 **取值范围**:   - opened ：开启。 **默认取值**: 不涉及 
        :type bait_protection_status: str
        :param deploy_mode: **参数解释**: 是否开启动态诱饵 **约束限制**: 不涉及 **取值范围**: 包含两种：   - opened ：开启。   - closed ：关闭。   **默认取值**: closed 
        :type deploy_mode: str
        :param protection_directory: **参数解释**: 防护目录 **约束限制**: 多个目录请用英文分号隔开，最多支持填写20个防护目录 **取值范围**: 字符长度0-128位，特殊符号只允许使用._-+，不能以空格开头，防护目录长度不得超过256个字符。 **默认取值**: 不涉及 
        :type protection_directory: str
        :param protection_type: **参数解释**: 防护文件类型，例如：docx，txt，avi **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type protection_type: str
        :param exclude_directory: **参数解释**: 排除目录(选填) **约束限制**: 多个目录请用英文分号隔开，最多支持填写20个排除目录 **取值范围**: 字符长度0-128位，特殊符号只允许使用._-+，不能以空格开头，防护目录长度不得超过256个字符。 **默认取值**: 不涉及 
        :type exclude_directory: str
        :param agent_id_list: **参数解释**: 开启了此勒索防护策略的agent的id列表 **约束限制**: 不涉及 **取值范围**: 列表最大1000条 **默认取值**: 不涉及 
        :type agent_id_list: list[str]
        :param operating_system: **参数解释**: 支持该策略的操作系统 **约束限制**: 不涉及 **取值范围**: 包含两种：   - Windows : Windows系统   - Linux : Linux系统 **默认取值**: 不涉及
        :type operating_system: str
        :param runtime_detection_status: **参数解释**: 是否运行时检测 **约束限制**: 不涉及 **取值范围**: 包含如下2种，暂时只有关闭一种状态，为保留字段。   - opened ：开启。   - closed ：关闭。 **默认取值**: 不涉及
        :type runtime_detection_status: str
        :param process_whitelist: 进程白名单
        :type process_whitelist: list[:class:`huaweicloudsdkhss.v5.TrustProcessInfo`]
        :param ai_protection_status: **参数解释**: 是否开启AI勒索防护，包含如下2种。 **约束限制**: 当前只有Windows系统涉及 **取值范围**: 包含两种：   - opened ：开启。   - closed ：关闭。 **默认取值**: closed
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
        self._agent_id_list = None
        self._operating_system = None
        self._runtime_detection_status = None
        self._process_whitelist = None
        self._ai_protection_status = None
        self.discriminator = None

        self.policy_id = policy_id
        self.policy_name = policy_name
        self.protection_mode = protection_mode
        if bait_protection_status is not None:
            self.bait_protection_status = bait_protection_status
        if deploy_mode is not None:
            self.deploy_mode = deploy_mode
        self.protection_directory = protection_directory
        self.protection_type = protection_type
        if exclude_directory is not None:
            self.exclude_directory = exclude_directory
        if agent_id_list is not None:
            self.agent_id_list = agent_id_list
        self.operating_system = operating_system
        if runtime_detection_status is not None:
            self.runtime_detection_status = runtime_detection_status
        if process_whitelist is not None:
            self.process_whitelist = process_whitelist
        if ai_protection_status is not None:
            self.ai_protection_status = ai_protection_status

    @property
    def policy_id(self):
        r"""Gets the policy_id of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 需要修改的防护策略ID，您可以通过[查询勒索病毒的防护策略列表](ListProtectionPolicy.xml)接口获取ID。 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The policy_id of this UpdateProtectionPolicyInfoRequestInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 需要修改的防护策略ID，您可以通过[查询勒索病毒的防护策略列表](ListProtectionPolicy.xml)接口获取ID。 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param policy_id: The policy_id of this UpdateProtectionPolicyInfoRequestInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 策略名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The policy_name of this UpdateProtectionPolicyInfoRequestInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 策略名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param policy_name: The policy_name of this UpdateProtectionPolicyInfoRequestInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def protection_mode(self):
        r"""Gets the protection_mode of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 防护动作 **约束限制**: 不涉及 **取值范围**: 包含两种：   - alarm_and_isolation ：告警并自动隔离。   - alarm_only ：仅告警。 **默认取值**: 不涉及 

        :return: The protection_mode of this UpdateProtectionPolicyInfoRequestInfo.
        :rtype: str
        """
        return self._protection_mode

    @protection_mode.setter
    def protection_mode(self, protection_mode):
        r"""Sets the protection_mode of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 防护动作 **约束限制**: 不涉及 **取值范围**: 包含两种：   - alarm_and_isolation ：告警并自动隔离。   - alarm_only ：仅告警。 **默认取值**: 不涉及 

        :param protection_mode: The protection_mode of this UpdateProtectionPolicyInfoRequestInfo.
        :type protection_mode: str
        """
        self._protection_mode = protection_mode

    @property
    def bait_protection_status(self):
        r"""Gets the bait_protection_status of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 是否开启诱饵防护 **约束限制**: 不涉及 **取值范围**:   - opened ：开启。 **默认取值**: 不涉及 

        :return: The bait_protection_status of this UpdateProtectionPolicyInfoRequestInfo.
        :rtype: str
        """
        return self._bait_protection_status

    @bait_protection_status.setter
    def bait_protection_status(self, bait_protection_status):
        r"""Sets the bait_protection_status of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 是否开启诱饵防护 **约束限制**: 不涉及 **取值范围**:   - opened ：开启。 **默认取值**: 不涉及 

        :param bait_protection_status: The bait_protection_status of this UpdateProtectionPolicyInfoRequestInfo.
        :type bait_protection_status: str
        """
        self._bait_protection_status = bait_protection_status

    @property
    def deploy_mode(self):
        r"""Gets the deploy_mode of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 是否开启动态诱饵 **约束限制**: 不涉及 **取值范围**: 包含两种：   - opened ：开启。   - closed ：关闭。   **默认取值**: closed 

        :return: The deploy_mode of this UpdateProtectionPolicyInfoRequestInfo.
        :rtype: str
        """
        return self._deploy_mode

    @deploy_mode.setter
    def deploy_mode(self, deploy_mode):
        r"""Sets the deploy_mode of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 是否开启动态诱饵 **约束限制**: 不涉及 **取值范围**: 包含两种：   - opened ：开启。   - closed ：关闭。   **默认取值**: closed 

        :param deploy_mode: The deploy_mode of this UpdateProtectionPolicyInfoRequestInfo.
        :type deploy_mode: str
        """
        self._deploy_mode = deploy_mode

    @property
    def protection_directory(self):
        r"""Gets the protection_directory of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 防护目录 **约束限制**: 多个目录请用英文分号隔开，最多支持填写20个防护目录 **取值范围**: 字符长度0-128位，特殊符号只允许使用._-+，不能以空格开头，防护目录长度不得超过256个字符。 **默认取值**: 不涉及 

        :return: The protection_directory of this UpdateProtectionPolicyInfoRequestInfo.
        :rtype: str
        """
        return self._protection_directory

    @protection_directory.setter
    def protection_directory(self, protection_directory):
        r"""Sets the protection_directory of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 防护目录 **约束限制**: 多个目录请用英文分号隔开，最多支持填写20个防护目录 **取值范围**: 字符长度0-128位，特殊符号只允许使用._-+，不能以空格开头，防护目录长度不得超过256个字符。 **默认取值**: 不涉及 

        :param protection_directory: The protection_directory of this UpdateProtectionPolicyInfoRequestInfo.
        :type protection_directory: str
        """
        self._protection_directory = protection_directory

    @property
    def protection_type(self):
        r"""Gets the protection_type of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 防护文件类型，例如：docx，txt，avi **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The protection_type of this UpdateProtectionPolicyInfoRequestInfo.
        :rtype: str
        """
        return self._protection_type

    @protection_type.setter
    def protection_type(self, protection_type):
        r"""Sets the protection_type of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 防护文件类型，例如：docx，txt，avi **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param protection_type: The protection_type of this UpdateProtectionPolicyInfoRequestInfo.
        :type protection_type: str
        """
        self._protection_type = protection_type

    @property
    def exclude_directory(self):
        r"""Gets the exclude_directory of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 排除目录(选填) **约束限制**: 多个目录请用英文分号隔开，最多支持填写20个排除目录 **取值范围**: 字符长度0-128位，特殊符号只允许使用._-+，不能以空格开头，防护目录长度不得超过256个字符。 **默认取值**: 不涉及 

        :return: The exclude_directory of this UpdateProtectionPolicyInfoRequestInfo.
        :rtype: str
        """
        return self._exclude_directory

    @exclude_directory.setter
    def exclude_directory(self, exclude_directory):
        r"""Sets the exclude_directory of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 排除目录(选填) **约束限制**: 多个目录请用英文分号隔开，最多支持填写20个排除目录 **取值范围**: 字符长度0-128位，特殊符号只允许使用._-+，不能以空格开头，防护目录长度不得超过256个字符。 **默认取值**: 不涉及 

        :param exclude_directory: The exclude_directory of this UpdateProtectionPolicyInfoRequestInfo.
        :type exclude_directory: str
        """
        self._exclude_directory = exclude_directory

    @property
    def agent_id_list(self):
        r"""Gets the agent_id_list of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 开启了此勒索防护策略的agent的id列表 **约束限制**: 不涉及 **取值范围**: 列表最大1000条 **默认取值**: 不涉及 

        :return: The agent_id_list of this UpdateProtectionPolicyInfoRequestInfo.
        :rtype: list[str]
        """
        return self._agent_id_list

    @agent_id_list.setter
    def agent_id_list(self, agent_id_list):
        r"""Sets the agent_id_list of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 开启了此勒索防护策略的agent的id列表 **约束限制**: 不涉及 **取值范围**: 列表最大1000条 **默认取值**: 不涉及 

        :param agent_id_list: The agent_id_list of this UpdateProtectionPolicyInfoRequestInfo.
        :type agent_id_list: list[str]
        """
        self._agent_id_list = agent_id_list

    @property
    def operating_system(self):
        r"""Gets the operating_system of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 支持该策略的操作系统 **约束限制**: 不涉及 **取值范围**: 包含两种：   - Windows : Windows系统   - Linux : Linux系统 **默认取值**: 不涉及

        :return: The operating_system of this UpdateProtectionPolicyInfoRequestInfo.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        r"""Sets the operating_system of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 支持该策略的操作系统 **约束限制**: 不涉及 **取值范围**: 包含两种：   - Windows : Windows系统   - Linux : Linux系统 **默认取值**: 不涉及

        :param operating_system: The operating_system of this UpdateProtectionPolicyInfoRequestInfo.
        :type operating_system: str
        """
        self._operating_system = operating_system

    @property
    def runtime_detection_status(self):
        r"""Gets the runtime_detection_status of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 是否运行时检测 **约束限制**: 不涉及 **取值范围**: 包含如下2种，暂时只有关闭一种状态，为保留字段。   - opened ：开启。   - closed ：关闭。 **默认取值**: 不涉及

        :return: The runtime_detection_status of this UpdateProtectionPolicyInfoRequestInfo.
        :rtype: str
        """
        return self._runtime_detection_status

    @runtime_detection_status.setter
    def runtime_detection_status(self, runtime_detection_status):
        r"""Sets the runtime_detection_status of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 是否运行时检测 **约束限制**: 不涉及 **取值范围**: 包含如下2种，暂时只有关闭一种状态，为保留字段。   - opened ：开启。   - closed ：关闭。 **默认取值**: 不涉及

        :param runtime_detection_status: The runtime_detection_status of this UpdateProtectionPolicyInfoRequestInfo.
        :type runtime_detection_status: str
        """
        self._runtime_detection_status = runtime_detection_status

    @property
    def process_whitelist(self):
        r"""Gets the process_whitelist of this UpdateProtectionPolicyInfoRequestInfo.

        进程白名单

        :return: The process_whitelist of this UpdateProtectionPolicyInfoRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.TrustProcessInfo`]
        """
        return self._process_whitelist

    @process_whitelist.setter
    def process_whitelist(self, process_whitelist):
        r"""Sets the process_whitelist of this UpdateProtectionPolicyInfoRequestInfo.

        进程白名单

        :param process_whitelist: The process_whitelist of this UpdateProtectionPolicyInfoRequestInfo.
        :type process_whitelist: list[:class:`huaweicloudsdkhss.v5.TrustProcessInfo`]
        """
        self._process_whitelist = process_whitelist

    @property
    def ai_protection_status(self):
        r"""Gets the ai_protection_status of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 是否开启AI勒索防护，包含如下2种。 **约束限制**: 当前只有Windows系统涉及 **取值范围**: 包含两种：   - opened ：开启。   - closed ：关闭。 **默认取值**: closed

        :return: The ai_protection_status of this UpdateProtectionPolicyInfoRequestInfo.
        :rtype: str
        """
        return self._ai_protection_status

    @ai_protection_status.setter
    def ai_protection_status(self, ai_protection_status):
        r"""Sets the ai_protection_status of this UpdateProtectionPolicyInfoRequestInfo.

        **参数解释**: 是否开启AI勒索防护，包含如下2种。 **约束限制**: 当前只有Windows系统涉及 **取值范围**: 包含两种：   - opened ：开启。   - closed ：关闭。 **默认取值**: closed

        :param ai_protection_status: The ai_protection_status of this UpdateProtectionPolicyInfoRequestInfo.
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
        if not isinstance(other, UpdateProtectionPolicyInfoRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

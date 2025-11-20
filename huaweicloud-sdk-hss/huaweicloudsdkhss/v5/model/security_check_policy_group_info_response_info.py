# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityCheckPolicyGroupInfoResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'group_name': 'str',
        'check_rule_num': 'int',
        'host_num': 'int',
        'deletable': 'bool',
        'default_group': 'bool',
        'support_os': 'str',
        'policy_info': 'SecurityCheckPolicyInfoResponseInfo',
        'weak_pwd_policy_info': 'SecurityCheckPolicyInfoResponseInfo',
        'agent_id_list': 'list[str]',
        'task_condition': 'SecurityCheckTaskCondition',
        'detection_period': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'group_name': 'group_name',
        'check_rule_num': 'check_rule_num',
        'host_num': 'host_num',
        'deletable': 'deletable',
        'default_group': 'default_group',
        'support_os': 'support_os',
        'policy_info': 'policy_info',
        'weak_pwd_policy_info': 'weak_pwd_policy_info',
        'agent_id_list': 'agent_id_list',
        'task_condition': 'task_condition',
        'detection_period': 'detection_period'
    }

    def __init__(self, group_id=None, group_name=None, check_rule_num=None, host_num=None, deletable=None, default_group=None, support_os=None, policy_info=None, weak_pwd_policy_info=None, agent_id_list=None, task_condition=None, detection_period=None):
        r"""SecurityCheckPolicyGroupInfoResponseInfo

        The model defined in huaweicloud sdk

        :param group_id: **参数解释** 策略组ID **取值范围** 字符长度1-64位 
        :type group_id: str
        :param group_name: **参数解释** 策略组名称 **取值范围** 字符长度1-256位 
        :type group_name: str
        :param check_rule_num: **参数解释** 基线检测项（检测规则）数量 **取值范围** 取值1-10000 
        :type check_rule_num: int
        :param host_num: **参数解释** 应用服务器数量 **取值范围** 取值0-1000000 
        :type host_num: int
        :param deletable: **参数解释** 是否支持删除 **取值范围** - true：支持 - false：不支持 
        :type deletable: bool
        :param default_group: **参数解释** 是否默认策略组 **取值范围** - true：是 - false：否 
        :type default_group: bool
        :param support_os: **参数解释** 策略支持的操作系统类型 **取值范围** - Linux：linux系统 - Windows：windows系统 
        :type support_os: str
        :param policy_info: 
        :type policy_info: :class:`huaweicloudsdkhss.v5.SecurityCheckPolicyInfoResponseInfo`
        :param weak_pwd_policy_info: 
        :type weak_pwd_policy_info: :class:`huaweicloudsdkhss.v5.SecurityCheckPolicyInfoResponseInfo`
        :param agent_id_list: **参数解释** 应用的主机的agentID列表 **取值范围** 字符串大小范围20-64 
        :type agent_id_list: list[str]
        :param task_condition: 
        :type task_condition: :class:`huaweicloudsdkhss.v5.SecurityCheckTaskCondition`
        :param detection_period: **参数解释** 检测周期 **取值范围** 字符串大小范围1-128 
        :type detection_period: str
        """
        
        

        self._group_id = None
        self._group_name = None
        self._check_rule_num = None
        self._host_num = None
        self._deletable = None
        self._default_group = None
        self._support_os = None
        self._policy_info = None
        self._weak_pwd_policy_info = None
        self._agent_id_list = None
        self._task_condition = None
        self._detection_period = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if check_rule_num is not None:
            self.check_rule_num = check_rule_num
        if host_num is not None:
            self.host_num = host_num
        if deletable is not None:
            self.deletable = deletable
        if default_group is not None:
            self.default_group = default_group
        if support_os is not None:
            self.support_os = support_os
        self.policy_info = policy_info
        if weak_pwd_policy_info is not None:
            self.weak_pwd_policy_info = weak_pwd_policy_info
        if agent_id_list is not None:
            self.agent_id_list = agent_id_list
        if task_condition is not None:
            self.task_condition = task_condition
        if detection_period is not None:
            self.detection_period = detection_period

    @property
    def group_id(self):
        r"""Gets the group_id of this SecurityCheckPolicyGroupInfoResponseInfo.

        **参数解释** 策略组ID **取值范围** 字符长度1-64位 

        :return: The group_id of this SecurityCheckPolicyGroupInfoResponseInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this SecurityCheckPolicyGroupInfoResponseInfo.

        **参数解释** 策略组ID **取值范围** 字符长度1-64位 

        :param group_id: The group_id of this SecurityCheckPolicyGroupInfoResponseInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this SecurityCheckPolicyGroupInfoResponseInfo.

        **参数解释** 策略组名称 **取值范围** 字符长度1-256位 

        :return: The group_name of this SecurityCheckPolicyGroupInfoResponseInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this SecurityCheckPolicyGroupInfoResponseInfo.

        **参数解释** 策略组名称 **取值范围** 字符长度1-256位 

        :param group_name: The group_name of this SecurityCheckPolicyGroupInfoResponseInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def check_rule_num(self):
        r"""Gets the check_rule_num of this SecurityCheckPolicyGroupInfoResponseInfo.

        **参数解释** 基线检测项（检测规则）数量 **取值范围** 取值1-10000 

        :return: The check_rule_num of this SecurityCheckPolicyGroupInfoResponseInfo.
        :rtype: int
        """
        return self._check_rule_num

    @check_rule_num.setter
    def check_rule_num(self, check_rule_num):
        r"""Sets the check_rule_num of this SecurityCheckPolicyGroupInfoResponseInfo.

        **参数解释** 基线检测项（检测规则）数量 **取值范围** 取值1-10000 

        :param check_rule_num: The check_rule_num of this SecurityCheckPolicyGroupInfoResponseInfo.
        :type check_rule_num: int
        """
        self._check_rule_num = check_rule_num

    @property
    def host_num(self):
        r"""Gets the host_num of this SecurityCheckPolicyGroupInfoResponseInfo.

        **参数解释** 应用服务器数量 **取值范围** 取值0-1000000 

        :return: The host_num of this SecurityCheckPolicyGroupInfoResponseInfo.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this SecurityCheckPolicyGroupInfoResponseInfo.

        **参数解释** 应用服务器数量 **取值范围** 取值0-1000000 

        :param host_num: The host_num of this SecurityCheckPolicyGroupInfoResponseInfo.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def deletable(self):
        r"""Gets the deletable of this SecurityCheckPolicyGroupInfoResponseInfo.

        **参数解释** 是否支持删除 **取值范围** - true：支持 - false：不支持 

        :return: The deletable of this SecurityCheckPolicyGroupInfoResponseInfo.
        :rtype: bool
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        r"""Sets the deletable of this SecurityCheckPolicyGroupInfoResponseInfo.

        **参数解释** 是否支持删除 **取值范围** - true：支持 - false：不支持 

        :param deletable: The deletable of this SecurityCheckPolicyGroupInfoResponseInfo.
        :type deletable: bool
        """
        self._deletable = deletable

    @property
    def default_group(self):
        r"""Gets the default_group of this SecurityCheckPolicyGroupInfoResponseInfo.

        **参数解释** 是否默认策略组 **取值范围** - true：是 - false：否 

        :return: The default_group of this SecurityCheckPolicyGroupInfoResponseInfo.
        :rtype: bool
        """
        return self._default_group

    @default_group.setter
    def default_group(self, default_group):
        r"""Sets the default_group of this SecurityCheckPolicyGroupInfoResponseInfo.

        **参数解释** 是否默认策略组 **取值范围** - true：是 - false：否 

        :param default_group: The default_group of this SecurityCheckPolicyGroupInfoResponseInfo.
        :type default_group: bool
        """
        self._default_group = default_group

    @property
    def support_os(self):
        r"""Gets the support_os of this SecurityCheckPolicyGroupInfoResponseInfo.

        **参数解释** 策略支持的操作系统类型 **取值范围** - Linux：linux系统 - Windows：windows系统 

        :return: The support_os of this SecurityCheckPolicyGroupInfoResponseInfo.
        :rtype: str
        """
        return self._support_os

    @support_os.setter
    def support_os(self, support_os):
        r"""Sets the support_os of this SecurityCheckPolicyGroupInfoResponseInfo.

        **参数解释** 策略支持的操作系统类型 **取值范围** - Linux：linux系统 - Windows：windows系统 

        :param support_os: The support_os of this SecurityCheckPolicyGroupInfoResponseInfo.
        :type support_os: str
        """
        self._support_os = support_os

    @property
    def policy_info(self):
        r"""Gets the policy_info of this SecurityCheckPolicyGroupInfoResponseInfo.

        :return: The policy_info of this SecurityCheckPolicyGroupInfoResponseInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.SecurityCheckPolicyInfoResponseInfo`
        """
        return self._policy_info

    @policy_info.setter
    def policy_info(self, policy_info):
        r"""Sets the policy_info of this SecurityCheckPolicyGroupInfoResponseInfo.

        :param policy_info: The policy_info of this SecurityCheckPolicyGroupInfoResponseInfo.
        :type policy_info: :class:`huaweicloudsdkhss.v5.SecurityCheckPolicyInfoResponseInfo`
        """
        self._policy_info = policy_info

    @property
    def weak_pwd_policy_info(self):
        r"""Gets the weak_pwd_policy_info of this SecurityCheckPolicyGroupInfoResponseInfo.

        :return: The weak_pwd_policy_info of this SecurityCheckPolicyGroupInfoResponseInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.SecurityCheckPolicyInfoResponseInfo`
        """
        return self._weak_pwd_policy_info

    @weak_pwd_policy_info.setter
    def weak_pwd_policy_info(self, weak_pwd_policy_info):
        r"""Sets the weak_pwd_policy_info of this SecurityCheckPolicyGroupInfoResponseInfo.

        :param weak_pwd_policy_info: The weak_pwd_policy_info of this SecurityCheckPolicyGroupInfoResponseInfo.
        :type weak_pwd_policy_info: :class:`huaweicloudsdkhss.v5.SecurityCheckPolicyInfoResponseInfo`
        """
        self._weak_pwd_policy_info = weak_pwd_policy_info

    @property
    def agent_id_list(self):
        r"""Gets the agent_id_list of this SecurityCheckPolicyGroupInfoResponseInfo.

        **参数解释** 应用的主机的agentID列表 **取值范围** 字符串大小范围20-64 

        :return: The agent_id_list of this SecurityCheckPolicyGroupInfoResponseInfo.
        :rtype: list[str]
        """
        return self._agent_id_list

    @agent_id_list.setter
    def agent_id_list(self, agent_id_list):
        r"""Sets the agent_id_list of this SecurityCheckPolicyGroupInfoResponseInfo.

        **参数解释** 应用的主机的agentID列表 **取值范围** 字符串大小范围20-64 

        :param agent_id_list: The agent_id_list of this SecurityCheckPolicyGroupInfoResponseInfo.
        :type agent_id_list: list[str]
        """
        self._agent_id_list = agent_id_list

    @property
    def task_condition(self):
        r"""Gets the task_condition of this SecurityCheckPolicyGroupInfoResponseInfo.

        :return: The task_condition of this SecurityCheckPolicyGroupInfoResponseInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.SecurityCheckTaskCondition`
        """
        return self._task_condition

    @task_condition.setter
    def task_condition(self, task_condition):
        r"""Sets the task_condition of this SecurityCheckPolicyGroupInfoResponseInfo.

        :param task_condition: The task_condition of this SecurityCheckPolicyGroupInfoResponseInfo.
        :type task_condition: :class:`huaweicloudsdkhss.v5.SecurityCheckTaskCondition`
        """
        self._task_condition = task_condition

    @property
    def detection_period(self):
        r"""Gets the detection_period of this SecurityCheckPolicyGroupInfoResponseInfo.

        **参数解释** 检测周期 **取值范围** 字符串大小范围1-128 

        :return: The detection_period of this SecurityCheckPolicyGroupInfoResponseInfo.
        :rtype: str
        """
        return self._detection_period

    @detection_period.setter
    def detection_period(self, detection_period):
        r"""Sets the detection_period of this SecurityCheckPolicyGroupInfoResponseInfo.

        **参数解释** 检测周期 **取值范围** 字符串大小范围1-128 

        :param detection_period: The detection_period of this SecurityCheckPolicyGroupInfoResponseInfo.
        :type detection_period: str
        """
        self._detection_period = detection_period

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SecurityCheckPolicyGroupInfoResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

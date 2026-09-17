# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkItemFlowNodeConfigVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'name': 'str',
        'description': 'str',
        'end': 'bool',
        'last': 'bool',
        'start': 'bool',
        'enable_suspend': 'bool',
        'extra_config': 'dict(str, object)',
        'static_rules': 'list[dict(str, object)]',
        'static_actions': 'dict(str, object)',
        'any_status': 'bool',
        'submit_can_operate': 'bool'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'description': 'description',
        'end': 'end',
        'last': 'last',
        'start': 'start',
        'enable_suspend': 'enable_suspend',
        'extra_config': 'extra_config',
        'static_rules': 'static_rules',
        'static_actions': 'static_actions',
        'any_status': 'any_status',
        'submit_can_operate': 'submit_can_operate'
    }

    def __init__(self, code=None, name=None, description=None, end=None, last=None, start=None, enable_suspend=None, extra_config=None, static_rules=None, static_actions=None, any_status=None, submit_can_operate=None):
        r"""WorkItemFlowNodeConfigVO

        The model defined in huaweicloud sdk

        :param code: 节点编码
        :type code: str
        :param name: 节点名称
        :type name: str
        :param description: 节点描述
        :type description: str
        :param end: 是否为结束节点
        :type end: bool
        :param last: 是否为最末节点
        :type last: bool
        :param start: 是否为开始节点
        :type start: bool
        :param enable_suspend: 是否允许挂起
        :type enable_suspend: bool
        :param extra_config: 节点扩展配置
        :type extra_config: dict(str, object)
        :param static_rules: 静态规则列表
        :type static_rules: list[dict(str, object)]
        :param static_actions: 静态动作配置
        :type static_actions: dict(str, object)
        :param any_status: 是否任意状态可流转
        :type any_status: bool
        :param submit_can_operate: 提交时是否可操作
        :type submit_can_operate: bool
        """
        
        

        self._code = None
        self._name = None
        self._description = None
        self._end = None
        self._last = None
        self._start = None
        self._enable_suspend = None
        self._extra_config = None
        self._static_rules = None
        self._static_actions = None
        self._any_status = None
        self._submit_can_operate = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if end is not None:
            self.end = end
        if last is not None:
            self.last = last
        if start is not None:
            self.start = start
        if enable_suspend is not None:
            self.enable_suspend = enable_suspend
        if extra_config is not None:
            self.extra_config = extra_config
        if static_rules is not None:
            self.static_rules = static_rules
        if static_actions is not None:
            self.static_actions = static_actions
        if any_status is not None:
            self.any_status = any_status
        if submit_can_operate is not None:
            self.submit_can_operate = submit_can_operate

    @property
    def code(self):
        r"""Gets the code of this WorkItemFlowNodeConfigVO.

        节点编码

        :return: The code of this WorkItemFlowNodeConfigVO.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this WorkItemFlowNodeConfigVO.

        节点编码

        :param code: The code of this WorkItemFlowNodeConfigVO.
        :type code: str
        """
        self._code = code

    @property
    def name(self):
        r"""Gets the name of this WorkItemFlowNodeConfigVO.

        节点名称

        :return: The name of this WorkItemFlowNodeConfigVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WorkItemFlowNodeConfigVO.

        节点名称

        :param name: The name of this WorkItemFlowNodeConfigVO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this WorkItemFlowNodeConfigVO.

        节点描述

        :return: The description of this WorkItemFlowNodeConfigVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this WorkItemFlowNodeConfigVO.

        节点描述

        :param description: The description of this WorkItemFlowNodeConfigVO.
        :type description: str
        """
        self._description = description

    @property
    def end(self):
        r"""Gets the end of this WorkItemFlowNodeConfigVO.

        是否为结束节点

        :return: The end of this WorkItemFlowNodeConfigVO.
        :rtype: bool
        """
        return self._end

    @end.setter
    def end(self, end):
        r"""Sets the end of this WorkItemFlowNodeConfigVO.

        是否为结束节点

        :param end: The end of this WorkItemFlowNodeConfigVO.
        :type end: bool
        """
        self._end = end

    @property
    def last(self):
        r"""Gets the last of this WorkItemFlowNodeConfigVO.

        是否为最末节点

        :return: The last of this WorkItemFlowNodeConfigVO.
        :rtype: bool
        """
        return self._last

    @last.setter
    def last(self, last):
        r"""Sets the last of this WorkItemFlowNodeConfigVO.

        是否为最末节点

        :param last: The last of this WorkItemFlowNodeConfigVO.
        :type last: bool
        """
        self._last = last

    @property
    def start(self):
        r"""Gets the start of this WorkItemFlowNodeConfigVO.

        是否为开始节点

        :return: The start of this WorkItemFlowNodeConfigVO.
        :rtype: bool
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this WorkItemFlowNodeConfigVO.

        是否为开始节点

        :param start: The start of this WorkItemFlowNodeConfigVO.
        :type start: bool
        """
        self._start = start

    @property
    def enable_suspend(self):
        r"""Gets the enable_suspend of this WorkItemFlowNodeConfigVO.

        是否允许挂起

        :return: The enable_suspend of this WorkItemFlowNodeConfigVO.
        :rtype: bool
        """
        return self._enable_suspend

    @enable_suspend.setter
    def enable_suspend(self, enable_suspend):
        r"""Sets the enable_suspend of this WorkItemFlowNodeConfigVO.

        是否允许挂起

        :param enable_suspend: The enable_suspend of this WorkItemFlowNodeConfigVO.
        :type enable_suspend: bool
        """
        self._enable_suspend = enable_suspend

    @property
    def extra_config(self):
        r"""Gets the extra_config of this WorkItemFlowNodeConfigVO.

        节点扩展配置

        :return: The extra_config of this WorkItemFlowNodeConfigVO.
        :rtype: dict(str, object)
        """
        return self._extra_config

    @extra_config.setter
    def extra_config(self, extra_config):
        r"""Sets the extra_config of this WorkItemFlowNodeConfigVO.

        节点扩展配置

        :param extra_config: The extra_config of this WorkItemFlowNodeConfigVO.
        :type extra_config: dict(str, object)
        """
        self._extra_config = extra_config

    @property
    def static_rules(self):
        r"""Gets the static_rules of this WorkItemFlowNodeConfigVO.

        静态规则列表

        :return: The static_rules of this WorkItemFlowNodeConfigVO.
        :rtype: list[dict(str, object)]
        """
        return self._static_rules

    @static_rules.setter
    def static_rules(self, static_rules):
        r"""Sets the static_rules of this WorkItemFlowNodeConfigVO.

        静态规则列表

        :param static_rules: The static_rules of this WorkItemFlowNodeConfigVO.
        :type static_rules: list[dict(str, object)]
        """
        self._static_rules = static_rules

    @property
    def static_actions(self):
        r"""Gets the static_actions of this WorkItemFlowNodeConfigVO.

        静态动作配置

        :return: The static_actions of this WorkItemFlowNodeConfigVO.
        :rtype: dict(str, object)
        """
        return self._static_actions

    @static_actions.setter
    def static_actions(self, static_actions):
        r"""Sets the static_actions of this WorkItemFlowNodeConfigVO.

        静态动作配置

        :param static_actions: The static_actions of this WorkItemFlowNodeConfigVO.
        :type static_actions: dict(str, object)
        """
        self._static_actions = static_actions

    @property
    def any_status(self):
        r"""Gets the any_status of this WorkItemFlowNodeConfigVO.

        是否任意状态可流转

        :return: The any_status of this WorkItemFlowNodeConfigVO.
        :rtype: bool
        """
        return self._any_status

    @any_status.setter
    def any_status(self, any_status):
        r"""Sets the any_status of this WorkItemFlowNodeConfigVO.

        是否任意状态可流转

        :param any_status: The any_status of this WorkItemFlowNodeConfigVO.
        :type any_status: bool
        """
        self._any_status = any_status

    @property
    def submit_can_operate(self):
        r"""Gets the submit_can_operate of this WorkItemFlowNodeConfigVO.

        提交时是否可操作

        :return: The submit_can_operate of this WorkItemFlowNodeConfigVO.
        :rtype: bool
        """
        return self._submit_can_operate

    @submit_can_operate.setter
    def submit_can_operate(self, submit_can_operate):
        r"""Sets the submit_can_operate of this WorkItemFlowNodeConfigVO.

        提交时是否可操作

        :param submit_can_operate: The submit_can_operate of this WorkItemFlowNodeConfigVO.
        :type submit_can_operate: bool
        """
        self._submit_can_operate = submit_can_operate

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
        if not isinstance(other, WorkItemFlowNodeConfigVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

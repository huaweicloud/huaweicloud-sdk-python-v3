# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_id': 'str',
        'name': 'str',
        'status': 'str',
        'priority': 'int',
        'conditions': 'Conditions',
        'actions': 'list[Actions]'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'name': 'name',
        'status': 'status',
        'priority': 'priority',
        'conditions': 'conditions',
        'actions': 'actions'
    }

    def __init__(self, rule_id=None, name=None, status=None, priority=None, conditions=None, actions=None):
        r"""RuleResponse

        The model defined in huaweicloud sdk

        :param rule_id: 规则id
        :type rule_id: str
        :param name: 规则名称
        :type name: str
        :param status: 规则状态，on：开启，off：关闭。
        :type status: str
        :param priority: 此条规则的优先级，数值越大，优先级越高。
        :type priority: int
        :param conditions: 
        :type conditions: :class:`huaweicloudsdkcdn.v2.Conditions`
        :param actions: 满足规则条件后执行的动作列表
        :type actions: list[:class:`huaweicloudsdkcdn.v2.Actions`]
        """
        
        

        self._rule_id = None
        self._name = None
        self._status = None
        self._priority = None
        self._conditions = None
        self._actions = None
        self.discriminator = None

        self.rule_id = rule_id
        self.name = name
        self.status = status
        self.priority = priority
        self.conditions = conditions
        self.actions = actions

    @property
    def rule_id(self):
        r"""Gets the rule_id of this RuleResponse.

        规则id

        :return: The rule_id of this RuleResponse.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this RuleResponse.

        规则id

        :param rule_id: The rule_id of this RuleResponse.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def name(self):
        r"""Gets the name of this RuleResponse.

        规则名称

        :return: The name of this RuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RuleResponse.

        规则名称

        :param name: The name of this RuleResponse.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this RuleResponse.

        规则状态，on：开启，off：关闭。

        :return: The status of this RuleResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RuleResponse.

        规则状态，on：开启，off：关闭。

        :param status: The status of this RuleResponse.
        :type status: str
        """
        self._status = status

    @property
    def priority(self):
        r"""Gets the priority of this RuleResponse.

        此条规则的优先级，数值越大，优先级越高。

        :return: The priority of this RuleResponse.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this RuleResponse.

        此条规则的优先级，数值越大，优先级越高。

        :param priority: The priority of this RuleResponse.
        :type priority: int
        """
        self._priority = priority

    @property
    def conditions(self):
        r"""Gets the conditions of this RuleResponse.

        :return: The conditions of this RuleResponse.
        :rtype: :class:`huaweicloudsdkcdn.v2.Conditions`
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this RuleResponse.

        :param conditions: The conditions of this RuleResponse.
        :type conditions: :class:`huaweicloudsdkcdn.v2.Conditions`
        """
        self._conditions = conditions

    @property
    def actions(self):
        r"""Gets the actions of this RuleResponse.

        满足规则条件后执行的动作列表

        :return: The actions of this RuleResponse.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.Actions`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this RuleResponse.

        满足规则条件后执行的动作列表

        :param actions: The actions of this RuleResponse.
        :type actions: list[:class:`huaweicloudsdkcdn.v2.Actions`]
        """
        self._actions = actions

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
        if not isinstance(other, RuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

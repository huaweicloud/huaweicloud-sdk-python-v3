# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UpdateCustomRuleResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'policyid': 'str',
        'action_mode': 'bool',
        'name': 'str',
        'time': 'bool',
        'start': 'int',
        'terminal': 'int',
        'conditions': 'list[CustomConditions]',
        'action': 'CustomAction',
        'priority': 'int'
    }

    attribute_map = {
        'id': 'id',
        'policyid': 'policyid',
        'action_mode': 'action_mode',
        'name': 'name',
        'time': 'time',
        'start': 'start',
        'terminal': 'terminal',
        'conditions': 'conditions',
        'action': 'action',
        'priority': 'priority'
    }

    def __init__(self, id=None, policyid=None, action_mode=None, name=None, time=None, start=None, terminal=None, conditions=None, action=None, priority=None):
        """UpdateCustomRuleResponse - a model defined in huaweicloud sdk"""
        
        super(UpdateCustomRuleResponse, self).__init__()

        self._id = None
        self._policyid = None
        self._action_mode = None
        self._name = None
        self._time = None
        self._start = None
        self._terminal = None
        self._conditions = None
        self._action = None
        self._priority = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if action_mode is not None:
            self.action_mode = action_mode
        if name is not None:
            self.name = name
        if time is not None:
            self.time = time
        if start is not None:
            self.start = start
        if terminal is not None:
            self.terminal = terminal
        if conditions is not None:
            self.conditions = conditions
        if action is not None:
            self.action = action
        if priority is not None:
            self.priority = priority

    @property
    def id(self):
        """Gets the id of this UpdateCustomRuleResponse.

        规则id

        :return: The id of this UpdateCustomRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateCustomRuleResponse.

        规则id

        :param id: The id of this UpdateCustomRuleResponse.
        :type: str
        """
        self._id = id

    @property
    def policyid(self):
        """Gets the policyid of this UpdateCustomRuleResponse.

        策略id

        :return: The policyid of this UpdateCustomRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this UpdateCustomRuleResponse.

        策略id

        :param policyid: The policyid of this UpdateCustomRuleResponse.
        :type: str
        """
        self._policyid = policyid

    @property
    def action_mode(self):
        """Gets the action_mode of this UpdateCustomRuleResponse.

        攻击惩罚

        :return: The action_mode of this UpdateCustomRuleResponse.
        :rtype: bool
        """
        return self._action_mode

    @action_mode.setter
    def action_mode(self, action_mode):
        """Sets the action_mode of this UpdateCustomRuleResponse.

        攻击惩罚

        :param action_mode: The action_mode of this UpdateCustomRuleResponse.
        :type: bool
        """
        self._action_mode = action_mode

    @property
    def name(self):
        """Gets the name of this UpdateCustomRuleResponse.

        自定义规则的名称

        :return: The name of this UpdateCustomRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateCustomRuleResponse.

        自定义规则的名称

        :param name: The name of this UpdateCustomRuleResponse.
        :type: str
        """
        self._name = name

    @property
    def time(self):
        """Gets the time of this UpdateCustomRuleResponse.

        精准防护规则生效时间

        :return: The time of this UpdateCustomRuleResponse.
        :rtype: bool
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this UpdateCustomRuleResponse.

        精准防护规则生效时间

        :param time: The time of this UpdateCustomRuleResponse.
        :type: bool
        """
        self._time = time

    @property
    def start(self):
        """Gets the start of this UpdateCustomRuleResponse.

        精准防护规则生效的起始时间

        :return: The start of this UpdateCustomRuleResponse.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this UpdateCustomRuleResponse.

        精准防护规则生效的起始时间

        :param start: The start of this UpdateCustomRuleResponse.
        :type: int
        """
        self._start = start

    @property
    def terminal(self):
        """Gets the terminal of this UpdateCustomRuleResponse.

        精准防护规则生效的终止时间

        :return: The terminal of this UpdateCustomRuleResponse.
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this UpdateCustomRuleResponse.

        精准防护规则生效的终止时间

        :param terminal: The terminal of this UpdateCustomRuleResponse.
        :type: int
        """
        self._terminal = terminal

    @property
    def conditions(self):
        """Gets the conditions of this UpdateCustomRuleResponse.

        匹配条件列表

        :return: The conditions of this UpdateCustomRuleResponse.
        :rtype: list[CustomConditions]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this UpdateCustomRuleResponse.

        匹配条件列表

        :param conditions: The conditions of this UpdateCustomRuleResponse.
        :type: list[CustomConditions]
        """
        self._conditions = conditions

    @property
    def action(self):
        """Gets the action of this UpdateCustomRuleResponse.


        :return: The action of this UpdateCustomRuleResponse.
        :rtype: CustomAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this UpdateCustomRuleResponse.


        :param action: The action of this UpdateCustomRuleResponse.
        :type: CustomAction
        """
        self._action = action

    @property
    def priority(self):
        """Gets the priority of this UpdateCustomRuleResponse.

        优先级（0-1000的整数）

        :return: The priority of this UpdateCustomRuleResponse.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this UpdateCustomRuleResponse.

        优先级（0-1000的整数）

        :param priority: The priority of this UpdateCustomRuleResponse.
        :type: int
        """
        self._priority = priority

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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateCustomRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'name': 'str',
        'policyid': 'str',
        'description': 'str',
        'status': 'int',
        'conditions': 'list[CustomRuleConditions]',
        'action': 'CustomAction',
        'action_mode': 'bool',
        'priority': 'int',
        'time': 'bool',
        'start': 'int',
        'terminal': 'int',
        'producer': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'policyid': 'policyid',
        'description': 'description',
        'status': 'status',
        'conditions': 'conditions',
        'action': 'action',
        'action_mode': 'action_mode',
        'priority': 'priority',
        'time': 'time',
        'start': 'start',
        'terminal': 'terminal',
        'producer': 'producer'
    }

    def __init__(self, id=None, name=None, policyid=None, description=None, status=None, conditions=None, action=None, action_mode=None, priority=None, time=None, start=None, terminal=None, producer=None):
        """UpdateCustomRuleResponse

        The model defined in huaweicloud sdk

        :param id: 规则id
        :type id: str
        :param name: 规则名称
        :type name: str
        :param policyid: 策略id
        :type policyid: str
        :param description: 规则描述
        :type description: str
        :param status: 规则状态，0：关闭，1：开启
        :type status: int
        :param conditions: 匹配条件列表，匹配条件必须同时满足。
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.CustomRuleConditions`]
        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.CustomAction`
        :param action_mode: 预留参数，可忽略。
        :type action_mode: bool
        :param priority: 执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到1000。
        :type priority: int
        :param time: 精准防护规则生效时间:  - “false”：表示该规则立即生效。   - “true”：表示自定义生效时间。
        :type time: bool
        :param start: 精准防护规则生效的起始时间戳（秒）。当time&#x3D;true，才会返回该参数。
        :type start: int
        :param terminal: 精准防护规则生效的终止时间戳（秒）。当time&#x3D;true，才会返回该参数。
        :type terminal: int
        :param producer: 规则创建对象，该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数
        :type producer: int
        """
        
        super(UpdateCustomRuleResponse, self).__init__()

        self._id = None
        self._name = None
        self._policyid = None
        self._description = None
        self._status = None
        self._conditions = None
        self._action = None
        self._action_mode = None
        self._priority = None
        self._time = None
        self._start = None
        self._terminal = None
        self._producer = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if policyid is not None:
            self.policyid = policyid
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if conditions is not None:
            self.conditions = conditions
        if action is not None:
            self.action = action
        if action_mode is not None:
            self.action_mode = action_mode
        if priority is not None:
            self.priority = priority
        if time is not None:
            self.time = time
        if start is not None:
            self.start = start
        if terminal is not None:
            self.terminal = terminal
        if producer is not None:
            self.producer = producer

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
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdateCustomRuleResponse.

        规则名称

        :return: The name of this UpdateCustomRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateCustomRuleResponse.

        规则名称

        :param name: The name of this UpdateCustomRuleResponse.
        :type name: str
        """
        self._name = name

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
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def description(self):
        """Gets the description of this UpdateCustomRuleResponse.

        规则描述

        :return: The description of this UpdateCustomRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateCustomRuleResponse.

        规则描述

        :param description: The description of this UpdateCustomRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this UpdateCustomRuleResponse.

        规则状态，0：关闭，1：开启

        :return: The status of this UpdateCustomRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateCustomRuleResponse.

        规则状态，0：关闭，1：开启

        :param status: The status of this UpdateCustomRuleResponse.
        :type status: int
        """
        self._status = status

    @property
    def conditions(self):
        """Gets the conditions of this UpdateCustomRuleResponse.

        匹配条件列表，匹配条件必须同时满足。

        :return: The conditions of this UpdateCustomRuleResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.CustomRuleConditions`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this UpdateCustomRuleResponse.

        匹配条件列表，匹配条件必须同时满足。

        :param conditions: The conditions of this UpdateCustomRuleResponse.
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.CustomRuleConditions`]
        """
        self._conditions = conditions

    @property
    def action(self):
        """Gets the action of this UpdateCustomRuleResponse.

        :return: The action of this UpdateCustomRuleResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.CustomAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this UpdateCustomRuleResponse.

        :param action: The action of this UpdateCustomRuleResponse.
        :type action: :class:`huaweicloudsdkwaf.v1.CustomAction`
        """
        self._action = action

    @property
    def action_mode(self):
        """Gets the action_mode of this UpdateCustomRuleResponse.

        预留参数，可忽略。

        :return: The action_mode of this UpdateCustomRuleResponse.
        :rtype: bool
        """
        return self._action_mode

    @action_mode.setter
    def action_mode(self, action_mode):
        """Sets the action_mode of this UpdateCustomRuleResponse.

        预留参数，可忽略。

        :param action_mode: The action_mode of this UpdateCustomRuleResponse.
        :type action_mode: bool
        """
        self._action_mode = action_mode

    @property
    def priority(self):
        """Gets the priority of this UpdateCustomRuleResponse.

        执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到1000。

        :return: The priority of this UpdateCustomRuleResponse.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this UpdateCustomRuleResponse.

        执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到1000。

        :param priority: The priority of this UpdateCustomRuleResponse.
        :type priority: int
        """
        self._priority = priority

    @property
    def time(self):
        """Gets the time of this UpdateCustomRuleResponse.

        精准防护规则生效时间:  - “false”：表示该规则立即生效。   - “true”：表示自定义生效时间。

        :return: The time of this UpdateCustomRuleResponse.
        :rtype: bool
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this UpdateCustomRuleResponse.

        精准防护规则生效时间:  - “false”：表示该规则立即生效。   - “true”：表示自定义生效时间。

        :param time: The time of this UpdateCustomRuleResponse.
        :type time: bool
        """
        self._time = time

    @property
    def start(self):
        """Gets the start of this UpdateCustomRuleResponse.

        精准防护规则生效的起始时间戳（秒）。当time=true，才会返回该参数。

        :return: The start of this UpdateCustomRuleResponse.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this UpdateCustomRuleResponse.

        精准防护规则生效的起始时间戳（秒）。当time=true，才会返回该参数。

        :param start: The start of this UpdateCustomRuleResponse.
        :type start: int
        """
        self._start = start

    @property
    def terminal(self):
        """Gets the terminal of this UpdateCustomRuleResponse.

        精准防护规则生效的终止时间戳（秒）。当time=true，才会返回该参数。

        :return: The terminal of this UpdateCustomRuleResponse.
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this UpdateCustomRuleResponse.

        精准防护规则生效的终止时间戳（秒）。当time=true，才会返回该参数。

        :param terminal: The terminal of this UpdateCustomRuleResponse.
        :type terminal: int
        """
        self._terminal = terminal

    @property
    def producer(self):
        """Gets the producer of this UpdateCustomRuleResponse.

        规则创建对象，该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数

        :return: The producer of this UpdateCustomRuleResponse.
        :rtype: int
        """
        return self._producer

    @producer.setter
    def producer(self, producer):
        """Sets the producer of this UpdateCustomRuleResponse.

        规则创建对象，该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数

        :param producer: The producer of this UpdateCustomRuleResponse.
        :type producer: int
        """
        self._producer = producer

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
        if not isinstance(other, UpdateCustomRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCustomRuleResponse(SdkResponse):

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
        'timestamp': 'int',
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
        'timestamp': 'timestamp',
        'time': 'time',
        'start': 'start',
        'terminal': 'terminal',
        'producer': 'producer'
    }

    def __init__(self, id=None, name=None, policyid=None, description=None, status=None, conditions=None, action=None, action_mode=None, priority=None, timestamp=None, time=None, start=None, terminal=None, producer=None):
        """CreateCustomRuleResponse

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
        :param timestamp: 创建精准防护规则的
        :type timestamp: int
        :param time: 精准防护规则生效时间:  - “false”：表示该规则立即生效。   - “true”：表示自定义生效时间。
        :type time: bool
        :param start: 精准防护规则生效的起始时间戳（秒）。当time&#x3D;true，才会返回该参数。
        :type start: int
        :param terminal: 精准防护规则生效的终止时间戳（秒）。当time&#x3D;true，才会返回该参数。
        :type terminal: int
        :param producer: 规则创建对象，该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数
        :type producer: int
        """
        
        super(CreateCustomRuleResponse, self).__init__()

        self._id = None
        self._name = None
        self._policyid = None
        self._description = None
        self._status = None
        self._conditions = None
        self._action = None
        self._action_mode = None
        self._priority = None
        self._timestamp = None
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
        if timestamp is not None:
            self.timestamp = timestamp
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
        """Gets the id of this CreateCustomRuleResponse.

        规则id

        :return: The id of this CreateCustomRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateCustomRuleResponse.

        规则id

        :param id: The id of this CreateCustomRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateCustomRuleResponse.

        规则名称

        :return: The name of this CreateCustomRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateCustomRuleResponse.

        规则名称

        :param name: The name of this CreateCustomRuleResponse.
        :type name: str
        """
        self._name = name

    @property
    def policyid(self):
        """Gets the policyid of this CreateCustomRuleResponse.

        策略id

        :return: The policyid of this CreateCustomRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this CreateCustomRuleResponse.

        策略id

        :param policyid: The policyid of this CreateCustomRuleResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def description(self):
        """Gets the description of this CreateCustomRuleResponse.

        规则描述

        :return: The description of this CreateCustomRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateCustomRuleResponse.

        规则描述

        :param description: The description of this CreateCustomRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this CreateCustomRuleResponse.

        规则状态，0：关闭，1：开启

        :return: The status of this CreateCustomRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateCustomRuleResponse.

        规则状态，0：关闭，1：开启

        :param status: The status of this CreateCustomRuleResponse.
        :type status: int
        """
        self._status = status

    @property
    def conditions(self):
        """Gets the conditions of this CreateCustomRuleResponse.

        匹配条件列表，匹配条件必须同时满足。

        :return: The conditions of this CreateCustomRuleResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.CustomRuleConditions`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this CreateCustomRuleResponse.

        匹配条件列表，匹配条件必须同时满足。

        :param conditions: The conditions of this CreateCustomRuleResponse.
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.CustomRuleConditions`]
        """
        self._conditions = conditions

    @property
    def action(self):
        """Gets the action of this CreateCustomRuleResponse.

        :return: The action of this CreateCustomRuleResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.CustomAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CreateCustomRuleResponse.

        :param action: The action of this CreateCustomRuleResponse.
        :type action: :class:`huaweicloudsdkwaf.v1.CustomAction`
        """
        self._action = action

    @property
    def action_mode(self):
        """Gets the action_mode of this CreateCustomRuleResponse.

        预留参数，可忽略。

        :return: The action_mode of this CreateCustomRuleResponse.
        :rtype: bool
        """
        return self._action_mode

    @action_mode.setter
    def action_mode(self, action_mode):
        """Sets the action_mode of this CreateCustomRuleResponse.

        预留参数，可忽略。

        :param action_mode: The action_mode of this CreateCustomRuleResponse.
        :type action_mode: bool
        """
        self._action_mode = action_mode

    @property
    def priority(self):
        """Gets the priority of this CreateCustomRuleResponse.

        执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到1000。

        :return: The priority of this CreateCustomRuleResponse.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this CreateCustomRuleResponse.

        执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到1000。

        :param priority: The priority of this CreateCustomRuleResponse.
        :type priority: int
        """
        self._priority = priority

    @property
    def timestamp(self):
        """Gets the timestamp of this CreateCustomRuleResponse.

        创建精准防护规则的

        :return: The timestamp of this CreateCustomRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CreateCustomRuleResponse.

        创建精准防护规则的

        :param timestamp: The timestamp of this CreateCustomRuleResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def time(self):
        """Gets the time of this CreateCustomRuleResponse.

        精准防护规则生效时间:  - “false”：表示该规则立即生效。   - “true”：表示自定义生效时间。

        :return: The time of this CreateCustomRuleResponse.
        :rtype: bool
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this CreateCustomRuleResponse.

        精准防护规则生效时间:  - “false”：表示该规则立即生效。   - “true”：表示自定义生效时间。

        :param time: The time of this CreateCustomRuleResponse.
        :type time: bool
        """
        self._time = time

    @property
    def start(self):
        """Gets the start of this CreateCustomRuleResponse.

        精准防护规则生效的起始时间戳（秒）。当time=true，才会返回该参数。

        :return: The start of this CreateCustomRuleResponse.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this CreateCustomRuleResponse.

        精准防护规则生效的起始时间戳（秒）。当time=true，才会返回该参数。

        :param start: The start of this CreateCustomRuleResponse.
        :type start: int
        """
        self._start = start

    @property
    def terminal(self):
        """Gets the terminal of this CreateCustomRuleResponse.

        精准防护规则生效的终止时间戳（秒）。当time=true，才会返回该参数。

        :return: The terminal of this CreateCustomRuleResponse.
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this CreateCustomRuleResponse.

        精准防护规则生效的终止时间戳（秒）。当time=true，才会返回该参数。

        :param terminal: The terminal of this CreateCustomRuleResponse.
        :type terminal: int
        """
        self._terminal = terminal

    @property
    def producer(self):
        """Gets the producer of this CreateCustomRuleResponse.

        规则创建对象，该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数

        :return: The producer of this CreateCustomRuleResponse.
        :rtype: int
        """
        return self._producer

    @producer.setter
    def producer(self, producer):
        """Sets the producer of this CreateCustomRuleResponse.

        规则创建对象，该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数

        :param producer: The producer of this CreateCustomRuleResponse.
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
        if not isinstance(other, CreateCustomRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

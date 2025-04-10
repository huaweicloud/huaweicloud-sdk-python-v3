# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHttpAccessControlRuleResponse(SdkResponse):

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
        'policy_id': 'str',
        'policy_name': 'str',
        'timestamp': 'int',
        'description': 'str',
        'status': 'int',
        'time': 'bool',
        'start': 'int',
        'terminal': 'int',
        'priority': 'int',
        'conditions': 'list[HttpAccessControlRuleCondition]',
        'action': 'HttpRuleAction',
        'producer': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'timestamp': 'timestamp',
        'description': 'description',
        'status': 'status',
        'time': 'time',
        'start': 'start',
        'terminal': 'terminal',
        'priority': 'priority',
        'conditions': 'conditions',
        'action': 'action',
        'producer': 'producer'
    }

    def __init__(self, id=None, name=None, policy_id=None, policy_name=None, timestamp=None, description=None, status=None, time=None, start=None, terminal=None, priority=None, conditions=None, action=None, producer=None):
        r"""CreateHttpAccessControlRuleResponse

        The model defined in huaweicloud sdk

        :param id: 规则id
        :type id: str
        :param name: 规则名称
        :type name: str
        :param policy_id: 规则所在策略id
        :type policy_id: str
        :param policy_name: 规则所在策略名称
        :type policy_name: str
        :param timestamp: 创建规则时间戳
        :type timestamp: int
        :param description: 规则描述
        :type description: str
        :param status: 规则开关状态
        :type status: int
        :param time: 是否设定生效时间
        :type time: bool
        :param start: 生效时间
        :type start: int
        :param terminal: 失效时间
        :type terminal: int
        :param priority: 优先级
        :type priority: int
        :param conditions: 命中条件
        :type conditions: list[:class:`huaweicloudsdkedgesec.v2.HttpAccessControlRuleCondition`]
        :param action: 
        :type action: :class:`huaweicloudsdkedgesec.v2.HttpRuleAction`
        :param producer: 创建来源
        :type producer: int
        """
        
        super(CreateHttpAccessControlRuleResponse, self).__init__()

        self._id = None
        self._name = None
        self._policy_id = None
        self._policy_name = None
        self._timestamp = None
        self._description = None
        self._status = None
        self._time = None
        self._start = None
        self._terminal = None
        self._priority = None
        self._conditions = None
        self._action = None
        self._producer = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        if timestamp is not None:
            self.timestamp = timestamp
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if time is not None:
            self.time = time
        if start is not None:
            self.start = start
        if terminal is not None:
            self.terminal = terminal
        if priority is not None:
            self.priority = priority
        if conditions is not None:
            self.conditions = conditions
        if action is not None:
            self.action = action
        if producer is not None:
            self.producer = producer

    @property
    def id(self):
        r"""Gets the id of this CreateHttpAccessControlRuleResponse.

        规则id

        :return: The id of this CreateHttpAccessControlRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateHttpAccessControlRuleResponse.

        规则id

        :param id: The id of this CreateHttpAccessControlRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateHttpAccessControlRuleResponse.

        规则名称

        :return: The name of this CreateHttpAccessControlRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateHttpAccessControlRuleResponse.

        规则名称

        :param name: The name of this CreateHttpAccessControlRuleResponse.
        :type name: str
        """
        self._name = name

    @property
    def policy_id(self):
        r"""Gets the policy_id of this CreateHttpAccessControlRuleResponse.

        规则所在策略id

        :return: The policy_id of this CreateHttpAccessControlRuleResponse.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this CreateHttpAccessControlRuleResponse.

        规则所在策略id

        :param policy_id: The policy_id of this CreateHttpAccessControlRuleResponse.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this CreateHttpAccessControlRuleResponse.

        规则所在策略名称

        :return: The policy_name of this CreateHttpAccessControlRuleResponse.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this CreateHttpAccessControlRuleResponse.

        规则所在策略名称

        :param policy_name: The policy_name of this CreateHttpAccessControlRuleResponse.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def timestamp(self):
        r"""Gets the timestamp of this CreateHttpAccessControlRuleResponse.

        创建规则时间戳

        :return: The timestamp of this CreateHttpAccessControlRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this CreateHttpAccessControlRuleResponse.

        创建规则时间戳

        :param timestamp: The timestamp of this CreateHttpAccessControlRuleResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def description(self):
        r"""Gets the description of this CreateHttpAccessControlRuleResponse.

        规则描述

        :return: The description of this CreateHttpAccessControlRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateHttpAccessControlRuleResponse.

        规则描述

        :param description: The description of this CreateHttpAccessControlRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this CreateHttpAccessControlRuleResponse.

        规则开关状态

        :return: The status of this CreateHttpAccessControlRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateHttpAccessControlRuleResponse.

        规则开关状态

        :param status: The status of this CreateHttpAccessControlRuleResponse.
        :type status: int
        """
        self._status = status

    @property
    def time(self):
        r"""Gets the time of this CreateHttpAccessControlRuleResponse.

        是否设定生效时间

        :return: The time of this CreateHttpAccessControlRuleResponse.
        :rtype: bool
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this CreateHttpAccessControlRuleResponse.

        是否设定生效时间

        :param time: The time of this CreateHttpAccessControlRuleResponse.
        :type time: bool
        """
        self._time = time

    @property
    def start(self):
        r"""Gets the start of this CreateHttpAccessControlRuleResponse.

        生效时间

        :return: The start of this CreateHttpAccessControlRuleResponse.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this CreateHttpAccessControlRuleResponse.

        生效时间

        :param start: The start of this CreateHttpAccessControlRuleResponse.
        :type start: int
        """
        self._start = start

    @property
    def terminal(self):
        r"""Gets the terminal of this CreateHttpAccessControlRuleResponse.

        失效时间

        :return: The terminal of this CreateHttpAccessControlRuleResponse.
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        r"""Sets the terminal of this CreateHttpAccessControlRuleResponse.

        失效时间

        :param terminal: The terminal of this CreateHttpAccessControlRuleResponse.
        :type terminal: int
        """
        self._terminal = terminal

    @property
    def priority(self):
        r"""Gets the priority of this CreateHttpAccessControlRuleResponse.

        优先级

        :return: The priority of this CreateHttpAccessControlRuleResponse.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this CreateHttpAccessControlRuleResponse.

        优先级

        :param priority: The priority of this CreateHttpAccessControlRuleResponse.
        :type priority: int
        """
        self._priority = priority

    @property
    def conditions(self):
        r"""Gets the conditions of this CreateHttpAccessControlRuleResponse.

        命中条件

        :return: The conditions of this CreateHttpAccessControlRuleResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v2.HttpAccessControlRuleCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this CreateHttpAccessControlRuleResponse.

        命中条件

        :param conditions: The conditions of this CreateHttpAccessControlRuleResponse.
        :type conditions: list[:class:`huaweicloudsdkedgesec.v2.HttpAccessControlRuleCondition`]
        """
        self._conditions = conditions

    @property
    def action(self):
        r"""Gets the action of this CreateHttpAccessControlRuleResponse.

        :return: The action of this CreateHttpAccessControlRuleResponse.
        :rtype: :class:`huaweicloudsdkedgesec.v2.HttpRuleAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CreateHttpAccessControlRuleResponse.

        :param action: The action of this CreateHttpAccessControlRuleResponse.
        :type action: :class:`huaweicloudsdkedgesec.v2.HttpRuleAction`
        """
        self._action = action

    @property
    def producer(self):
        r"""Gets the producer of this CreateHttpAccessControlRuleResponse.

        创建来源

        :return: The producer of this CreateHttpAccessControlRuleResponse.
        :rtype: int
        """
        return self._producer

    @producer.setter
    def producer(self, producer):
        r"""Sets the producer of this CreateHttpAccessControlRuleResponse.

        创建来源

        :param producer: The producer of this CreateHttpAccessControlRuleResponse.
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
        if not isinstance(other, CreateHttpAccessControlRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

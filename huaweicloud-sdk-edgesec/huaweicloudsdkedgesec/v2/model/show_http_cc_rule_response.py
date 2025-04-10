# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHttpCcRuleResponse(SdkResponse):

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
        'priority': 'int',
        'policy_id': 'str',
        'policy_name': 'str',
        'timestamp': 'int',
        'description': 'str',
        'status': 'int',
        'mode': 'int',
        'total_num': 'int',
        'limit_num': 'int',
        'limit_period': 'int',
        'lock_time': 'int',
        'tag_type': 'str',
        'tag_index': 'str',
        'tag_condition': 'HttpCcRuleCondition',
        'unlock_num': 'int',
        'domain_aggregation': 'bool',
        'conditions': 'list[HttpCcRuleCondition]',
        'action': 'HttpRuleAction',
        'producer': 'int',
        'time_mode': 'str',
        'start': 'int',
        'terminal': 'int',
        'period_type': 'str',
        'time_range': 'list[TimeRangeItem]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'priority': 'priority',
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'timestamp': 'timestamp',
        'description': 'description',
        'status': 'status',
        'mode': 'mode',
        'total_num': 'total_num',
        'limit_num': 'limit_num',
        'limit_period': 'limit_period',
        'lock_time': 'lock_time',
        'tag_type': 'tag_type',
        'tag_index': 'tag_index',
        'tag_condition': 'tag_condition',
        'unlock_num': 'unlock_num',
        'domain_aggregation': 'domain_aggregation',
        'conditions': 'conditions',
        'action': 'action',
        'producer': 'producer',
        'time_mode': 'time_mode',
        'start': 'start',
        'terminal': 'terminal',
        'period_type': 'period_type',
        'time_range': 'time_range'
    }

    def __init__(self, id=None, name=None, priority=None, policy_id=None, policy_name=None, timestamp=None, description=None, status=None, mode=None, total_num=None, limit_num=None, limit_period=None, lock_time=None, tag_type=None, tag_index=None, tag_condition=None, unlock_num=None, domain_aggregation=None, conditions=None, action=None, producer=None, time_mode=None, start=None, terminal=None, period_type=None, time_range=None):
        r"""ShowHttpCcRuleResponse

        The model defined in huaweicloud sdk

        :param id: 规则id
        :type id: str
        :param name: 规则名称
        :type name: str
        :param priority: cc规则优先级，越大优先级越高，默认1
        :type priority: int
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
        :param mode: 规则类型（0：标准/1：高级）
        :type mode: int
        :param total_num: 所有用户的周期内请求次数
        :type total_num: int
        :param limit_num: 单个用户的周期内请求次数
        :type limit_num: int
        :param limit_period: 限速周期
        :type limit_period: int
        :param lock_time: 锁定时长
        :type lock_time: int
        :param tag_type: 防护模式
        :type tag_type: str
        :param tag_index: 防护模式标签
        :type tag_index: str
        :param tag_condition: 
        :type tag_condition: :class:`huaweicloudsdkedgesec.v2.HttpCcRuleCondition`
        :param unlock_num: 放行次数
        :type unlock_num: int
        :param domain_aggregation: 是否聚合域名
        :type domain_aggregation: bool
        :param conditions: 条件列表参数较为复杂，存在级联关系，建议同时使用控制台上的添加误报屏蔽规则，单击F12键查看路径后缀为/cc-rule，方法为POST的请求参数，便于理解参数的填写
        :type conditions: list[:class:`huaweicloudsdkedgesec.v2.HttpCcRuleCondition`]
        :param action: 
        :type action: :class:`huaweicloudsdkedgesec.v2.HttpRuleAction`
        :param producer: 创建来源
        :type producer: int
        :param time_mode: 生效模式
        :type time_mode: str
        :param start: customize生效时间区间开始
        :type start: int
        :param terminal: customize生效时间区间结束
        :type terminal: int
        :param period_type: period每日生效时间类型，目前只有day
        :type period_type: str
        :param time_range: period每日生效时间区间
        :type time_range: list[:class:`huaweicloudsdkedgesec.v2.TimeRangeItem`]
        """
        
        super(ShowHttpCcRuleResponse, self).__init__()

        self._id = None
        self._name = None
        self._priority = None
        self._policy_id = None
        self._policy_name = None
        self._timestamp = None
        self._description = None
        self._status = None
        self._mode = None
        self._total_num = None
        self._limit_num = None
        self._limit_period = None
        self._lock_time = None
        self._tag_type = None
        self._tag_index = None
        self._tag_condition = None
        self._unlock_num = None
        self._domain_aggregation = None
        self._conditions = None
        self._action = None
        self._producer = None
        self._time_mode = None
        self._start = None
        self._terminal = None
        self._period_type = None
        self._time_range = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if priority is not None:
            self.priority = priority
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
        if mode is not None:
            self.mode = mode
        if total_num is not None:
            self.total_num = total_num
        if limit_num is not None:
            self.limit_num = limit_num
        if limit_period is not None:
            self.limit_period = limit_period
        if lock_time is not None:
            self.lock_time = lock_time
        if tag_type is not None:
            self.tag_type = tag_type
        if tag_index is not None:
            self.tag_index = tag_index
        if tag_condition is not None:
            self.tag_condition = tag_condition
        if unlock_num is not None:
            self.unlock_num = unlock_num
        if domain_aggregation is not None:
            self.domain_aggregation = domain_aggregation
        if conditions is not None:
            self.conditions = conditions
        if action is not None:
            self.action = action
        if producer is not None:
            self.producer = producer
        if time_mode is not None:
            self.time_mode = time_mode
        if start is not None:
            self.start = start
        if terminal is not None:
            self.terminal = terminal
        if period_type is not None:
            self.period_type = period_type
        if time_range is not None:
            self.time_range = time_range

    @property
    def id(self):
        r"""Gets the id of this ShowHttpCcRuleResponse.

        规则id

        :return: The id of this ShowHttpCcRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowHttpCcRuleResponse.

        规则id

        :param id: The id of this ShowHttpCcRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowHttpCcRuleResponse.

        规则名称

        :return: The name of this ShowHttpCcRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowHttpCcRuleResponse.

        规则名称

        :param name: The name of this ShowHttpCcRuleResponse.
        :type name: str
        """
        self._name = name

    @property
    def priority(self):
        r"""Gets the priority of this ShowHttpCcRuleResponse.

        cc规则优先级，越大优先级越高，默认1

        :return: The priority of this ShowHttpCcRuleResponse.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this ShowHttpCcRuleResponse.

        cc规则优先级，越大优先级越高，默认1

        :param priority: The priority of this ShowHttpCcRuleResponse.
        :type priority: int
        """
        self._priority = priority

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ShowHttpCcRuleResponse.

        规则所在策略id

        :return: The policy_id of this ShowHttpCcRuleResponse.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ShowHttpCcRuleResponse.

        规则所在策略id

        :param policy_id: The policy_id of this ShowHttpCcRuleResponse.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ShowHttpCcRuleResponse.

        规则所在策略名称

        :return: The policy_name of this ShowHttpCcRuleResponse.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ShowHttpCcRuleResponse.

        规则所在策略名称

        :param policy_name: The policy_name of this ShowHttpCcRuleResponse.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def timestamp(self):
        r"""Gets the timestamp of this ShowHttpCcRuleResponse.

        创建规则时间戳

        :return: The timestamp of this ShowHttpCcRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this ShowHttpCcRuleResponse.

        创建规则时间戳

        :param timestamp: The timestamp of this ShowHttpCcRuleResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def description(self):
        r"""Gets the description of this ShowHttpCcRuleResponse.

        规则描述

        :return: The description of this ShowHttpCcRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowHttpCcRuleResponse.

        规则描述

        :param description: The description of this ShowHttpCcRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this ShowHttpCcRuleResponse.

        规则开关状态

        :return: The status of this ShowHttpCcRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowHttpCcRuleResponse.

        规则开关状态

        :param status: The status of this ShowHttpCcRuleResponse.
        :type status: int
        """
        self._status = status

    @property
    def mode(self):
        r"""Gets the mode of this ShowHttpCcRuleResponse.

        规则类型（0：标准/1：高级）

        :return: The mode of this ShowHttpCcRuleResponse.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ShowHttpCcRuleResponse.

        规则类型（0：标准/1：高级）

        :param mode: The mode of this ShowHttpCcRuleResponse.
        :type mode: int
        """
        self._mode = mode

    @property
    def total_num(self):
        r"""Gets the total_num of this ShowHttpCcRuleResponse.

        所有用户的周期内请求次数

        :return: The total_num of this ShowHttpCcRuleResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ShowHttpCcRuleResponse.

        所有用户的周期内请求次数

        :param total_num: The total_num of this ShowHttpCcRuleResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def limit_num(self):
        r"""Gets the limit_num of this ShowHttpCcRuleResponse.

        单个用户的周期内请求次数

        :return: The limit_num of this ShowHttpCcRuleResponse.
        :rtype: int
        """
        return self._limit_num

    @limit_num.setter
    def limit_num(self, limit_num):
        r"""Sets the limit_num of this ShowHttpCcRuleResponse.

        单个用户的周期内请求次数

        :param limit_num: The limit_num of this ShowHttpCcRuleResponse.
        :type limit_num: int
        """
        self._limit_num = limit_num

    @property
    def limit_period(self):
        r"""Gets the limit_period of this ShowHttpCcRuleResponse.

        限速周期

        :return: The limit_period of this ShowHttpCcRuleResponse.
        :rtype: int
        """
        return self._limit_period

    @limit_period.setter
    def limit_period(self, limit_period):
        r"""Sets the limit_period of this ShowHttpCcRuleResponse.

        限速周期

        :param limit_period: The limit_period of this ShowHttpCcRuleResponse.
        :type limit_period: int
        """
        self._limit_period = limit_period

    @property
    def lock_time(self):
        r"""Gets the lock_time of this ShowHttpCcRuleResponse.

        锁定时长

        :return: The lock_time of this ShowHttpCcRuleResponse.
        :rtype: int
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        r"""Sets the lock_time of this ShowHttpCcRuleResponse.

        锁定时长

        :param lock_time: The lock_time of this ShowHttpCcRuleResponse.
        :type lock_time: int
        """
        self._lock_time = lock_time

    @property
    def tag_type(self):
        r"""Gets the tag_type of this ShowHttpCcRuleResponse.

        防护模式

        :return: The tag_type of this ShowHttpCcRuleResponse.
        :rtype: str
        """
        return self._tag_type

    @tag_type.setter
    def tag_type(self, tag_type):
        r"""Sets the tag_type of this ShowHttpCcRuleResponse.

        防护模式

        :param tag_type: The tag_type of this ShowHttpCcRuleResponse.
        :type tag_type: str
        """
        self._tag_type = tag_type

    @property
    def tag_index(self):
        r"""Gets the tag_index of this ShowHttpCcRuleResponse.

        防护模式标签

        :return: The tag_index of this ShowHttpCcRuleResponse.
        :rtype: str
        """
        return self._tag_index

    @tag_index.setter
    def tag_index(self, tag_index):
        r"""Sets the tag_index of this ShowHttpCcRuleResponse.

        防护模式标签

        :param tag_index: The tag_index of this ShowHttpCcRuleResponse.
        :type tag_index: str
        """
        self._tag_index = tag_index

    @property
    def tag_condition(self):
        r"""Gets the tag_condition of this ShowHttpCcRuleResponse.

        :return: The tag_condition of this ShowHttpCcRuleResponse.
        :rtype: :class:`huaweicloudsdkedgesec.v2.HttpCcRuleCondition`
        """
        return self._tag_condition

    @tag_condition.setter
    def tag_condition(self, tag_condition):
        r"""Sets the tag_condition of this ShowHttpCcRuleResponse.

        :param tag_condition: The tag_condition of this ShowHttpCcRuleResponse.
        :type tag_condition: :class:`huaweicloudsdkedgesec.v2.HttpCcRuleCondition`
        """
        self._tag_condition = tag_condition

    @property
    def unlock_num(self):
        r"""Gets the unlock_num of this ShowHttpCcRuleResponse.

        放行次数

        :return: The unlock_num of this ShowHttpCcRuleResponse.
        :rtype: int
        """
        return self._unlock_num

    @unlock_num.setter
    def unlock_num(self, unlock_num):
        r"""Sets the unlock_num of this ShowHttpCcRuleResponse.

        放行次数

        :param unlock_num: The unlock_num of this ShowHttpCcRuleResponse.
        :type unlock_num: int
        """
        self._unlock_num = unlock_num

    @property
    def domain_aggregation(self):
        r"""Gets the domain_aggregation of this ShowHttpCcRuleResponse.

        是否聚合域名

        :return: The domain_aggregation of this ShowHttpCcRuleResponse.
        :rtype: bool
        """
        return self._domain_aggregation

    @domain_aggregation.setter
    def domain_aggregation(self, domain_aggregation):
        r"""Sets the domain_aggregation of this ShowHttpCcRuleResponse.

        是否聚合域名

        :param domain_aggregation: The domain_aggregation of this ShowHttpCcRuleResponse.
        :type domain_aggregation: bool
        """
        self._domain_aggregation = domain_aggregation

    @property
    def conditions(self):
        r"""Gets the conditions of this ShowHttpCcRuleResponse.

        条件列表参数较为复杂，存在级联关系，建议同时使用控制台上的添加误报屏蔽规则，单击F12键查看路径后缀为/cc-rule，方法为POST的请求参数，便于理解参数的填写

        :return: The conditions of this ShowHttpCcRuleResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v2.HttpCcRuleCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this ShowHttpCcRuleResponse.

        条件列表参数较为复杂，存在级联关系，建议同时使用控制台上的添加误报屏蔽规则，单击F12键查看路径后缀为/cc-rule，方法为POST的请求参数，便于理解参数的填写

        :param conditions: The conditions of this ShowHttpCcRuleResponse.
        :type conditions: list[:class:`huaweicloudsdkedgesec.v2.HttpCcRuleCondition`]
        """
        self._conditions = conditions

    @property
    def action(self):
        r"""Gets the action of this ShowHttpCcRuleResponse.

        :return: The action of this ShowHttpCcRuleResponse.
        :rtype: :class:`huaweicloudsdkedgesec.v2.HttpRuleAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ShowHttpCcRuleResponse.

        :param action: The action of this ShowHttpCcRuleResponse.
        :type action: :class:`huaweicloudsdkedgesec.v2.HttpRuleAction`
        """
        self._action = action

    @property
    def producer(self):
        r"""Gets the producer of this ShowHttpCcRuleResponse.

        创建来源

        :return: The producer of this ShowHttpCcRuleResponse.
        :rtype: int
        """
        return self._producer

    @producer.setter
    def producer(self, producer):
        r"""Sets the producer of this ShowHttpCcRuleResponse.

        创建来源

        :param producer: The producer of this ShowHttpCcRuleResponse.
        :type producer: int
        """
        self._producer = producer

    @property
    def time_mode(self):
        r"""Gets the time_mode of this ShowHttpCcRuleResponse.

        生效模式

        :return: The time_mode of this ShowHttpCcRuleResponse.
        :rtype: str
        """
        return self._time_mode

    @time_mode.setter
    def time_mode(self, time_mode):
        r"""Sets the time_mode of this ShowHttpCcRuleResponse.

        生效模式

        :param time_mode: The time_mode of this ShowHttpCcRuleResponse.
        :type time_mode: str
        """
        self._time_mode = time_mode

    @property
    def start(self):
        r"""Gets the start of this ShowHttpCcRuleResponse.

        customize生效时间区间开始

        :return: The start of this ShowHttpCcRuleResponse.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this ShowHttpCcRuleResponse.

        customize生效时间区间开始

        :param start: The start of this ShowHttpCcRuleResponse.
        :type start: int
        """
        self._start = start

    @property
    def terminal(self):
        r"""Gets the terminal of this ShowHttpCcRuleResponse.

        customize生效时间区间结束

        :return: The terminal of this ShowHttpCcRuleResponse.
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        r"""Sets the terminal of this ShowHttpCcRuleResponse.

        customize生效时间区间结束

        :param terminal: The terminal of this ShowHttpCcRuleResponse.
        :type terminal: int
        """
        self._terminal = terminal

    @property
    def period_type(self):
        r"""Gets the period_type of this ShowHttpCcRuleResponse.

        period每日生效时间类型，目前只有day

        :return: The period_type of this ShowHttpCcRuleResponse.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this ShowHttpCcRuleResponse.

        period每日生效时间类型，目前只有day

        :param period_type: The period_type of this ShowHttpCcRuleResponse.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def time_range(self):
        r"""Gets the time_range of this ShowHttpCcRuleResponse.

        period每日生效时间区间

        :return: The time_range of this ShowHttpCcRuleResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v2.TimeRangeItem`]
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        r"""Sets the time_range of this ShowHttpCcRuleResponse.

        period每日生效时间区间

        :param time_range: The time_range of this ShowHttpCcRuleResponse.
        :type time_range: list[:class:`huaweicloudsdkedgesec.v2.TimeRangeItem`]
        """
        self._time_range = time_range

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
        if not isinstance(other, ShowHttpCcRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

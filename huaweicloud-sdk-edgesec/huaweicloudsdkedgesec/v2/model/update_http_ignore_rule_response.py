# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHttpIgnoreRuleResponse(SdkResponse):

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
        'url': 'str',
        'rule': 'str',
        'mode': 'int',
        'domains': 'list[str]',
        'url_logic': 'str',
        'advanced': 'HttpIgnoreRuleCondition',
        'conditions': 'list[HttpIgnoreRuleCondition]',
        'hit_num': 'int',
        'update_time': 'int',
        'clear_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'timestamp': 'timestamp',
        'description': 'description',
        'status': 'status',
        'url': 'url',
        'rule': 'rule',
        'mode': 'mode',
        'domains': 'domains',
        'url_logic': 'url_logic',
        'advanced': 'advanced',
        'conditions': 'conditions',
        'hit_num': 'hit_num',
        'update_time': 'update_time',
        'clear_time': 'clear_time'
    }

    def __init__(self, id=None, name=None, policy_id=None, policy_name=None, timestamp=None, description=None, status=None, url=None, rule=None, mode=None, domains=None, url_logic=None, advanced=None, conditions=None, hit_num=None, update_time=None, clear_time=None):
        """UpdateHttpIgnoreRuleResponse

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
        :param url: 误报路径
        :type url: str
        :param rule: 规则编号
        :type rule: str
        :param mode: 误报屏蔽模式，默认为0即旧模式
        :type mode: int
        :param domains: 域名列表
        :type domains: list[str]
        :param url_logic: 屏蔽规则url类型（前缀：prefix，等于：equal）
        :type url_logic: str
        :param advanced: 
        :type advanced: :class:`huaweicloudsdkedgesec.v2.HttpIgnoreRuleCondition`
        :param conditions: 命中条件
        :type conditions: list[:class:`huaweicloudsdkedgesec.v2.HttpIgnoreRuleCondition`]
        :param hit_num: 命中次数
        :type hit_num: int
        :param update_time: 最后更新时间戳
        :type update_time: int
        :param clear_time: 上一次命中次数清零时间戳
        :type clear_time: int
        """
        
        super(UpdateHttpIgnoreRuleResponse, self).__init__()

        self._id = None
        self._name = None
        self._policy_id = None
        self._policy_name = None
        self._timestamp = None
        self._description = None
        self._status = None
        self._url = None
        self._rule = None
        self._mode = None
        self._domains = None
        self._url_logic = None
        self._advanced = None
        self._conditions = None
        self._hit_num = None
        self._update_time = None
        self._clear_time = None
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
        if url is not None:
            self.url = url
        if rule is not None:
            self.rule = rule
        if mode is not None:
            self.mode = mode
        if domains is not None:
            self.domains = domains
        if url_logic is not None:
            self.url_logic = url_logic
        if advanced is not None:
            self.advanced = advanced
        if conditions is not None:
            self.conditions = conditions
        if hit_num is not None:
            self.hit_num = hit_num
        if update_time is not None:
            self.update_time = update_time
        if clear_time is not None:
            self.clear_time = clear_time

    @property
    def id(self):
        """Gets the id of this UpdateHttpIgnoreRuleResponse.

        规则id

        :return: The id of this UpdateHttpIgnoreRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateHttpIgnoreRuleResponse.

        规则id

        :param id: The id of this UpdateHttpIgnoreRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdateHttpIgnoreRuleResponse.

        规则名称

        :return: The name of this UpdateHttpIgnoreRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateHttpIgnoreRuleResponse.

        规则名称

        :param name: The name of this UpdateHttpIgnoreRuleResponse.
        :type name: str
        """
        self._name = name

    @property
    def policy_id(self):
        """Gets the policy_id of this UpdateHttpIgnoreRuleResponse.

        规则所在策略id

        :return: The policy_id of this UpdateHttpIgnoreRuleResponse.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this UpdateHttpIgnoreRuleResponse.

        规则所在策略id

        :param policy_id: The policy_id of this UpdateHttpIgnoreRuleResponse.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        """Gets the policy_name of this UpdateHttpIgnoreRuleResponse.

        规则所在策略名称

        :return: The policy_name of this UpdateHttpIgnoreRuleResponse.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this UpdateHttpIgnoreRuleResponse.

        规则所在策略名称

        :param policy_name: The policy_name of this UpdateHttpIgnoreRuleResponse.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def timestamp(self):
        """Gets the timestamp of this UpdateHttpIgnoreRuleResponse.

        创建规则时间戳

        :return: The timestamp of this UpdateHttpIgnoreRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this UpdateHttpIgnoreRuleResponse.

        创建规则时间戳

        :param timestamp: The timestamp of this UpdateHttpIgnoreRuleResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def description(self):
        """Gets the description of this UpdateHttpIgnoreRuleResponse.

        规则描述

        :return: The description of this UpdateHttpIgnoreRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateHttpIgnoreRuleResponse.

        规则描述

        :param description: The description of this UpdateHttpIgnoreRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this UpdateHttpIgnoreRuleResponse.

        规则开关状态

        :return: The status of this UpdateHttpIgnoreRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateHttpIgnoreRuleResponse.

        规则开关状态

        :param status: The status of this UpdateHttpIgnoreRuleResponse.
        :type status: int
        """
        self._status = status

    @property
    def url(self):
        """Gets the url of this UpdateHttpIgnoreRuleResponse.

        误报路径

        :return: The url of this UpdateHttpIgnoreRuleResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UpdateHttpIgnoreRuleResponse.

        误报路径

        :param url: The url of this UpdateHttpIgnoreRuleResponse.
        :type url: str
        """
        self._url = url

    @property
    def rule(self):
        """Gets the rule of this UpdateHttpIgnoreRuleResponse.

        规则编号

        :return: The rule of this UpdateHttpIgnoreRuleResponse.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this UpdateHttpIgnoreRuleResponse.

        规则编号

        :param rule: The rule of this UpdateHttpIgnoreRuleResponse.
        :type rule: str
        """
        self._rule = rule

    @property
    def mode(self):
        """Gets the mode of this UpdateHttpIgnoreRuleResponse.

        误报屏蔽模式，默认为0即旧模式

        :return: The mode of this UpdateHttpIgnoreRuleResponse.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this UpdateHttpIgnoreRuleResponse.

        误报屏蔽模式，默认为0即旧模式

        :param mode: The mode of this UpdateHttpIgnoreRuleResponse.
        :type mode: int
        """
        self._mode = mode

    @property
    def domains(self):
        """Gets the domains of this UpdateHttpIgnoreRuleResponse.

        域名列表

        :return: The domains of this UpdateHttpIgnoreRuleResponse.
        :rtype: list[str]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this UpdateHttpIgnoreRuleResponse.

        域名列表

        :param domains: The domains of this UpdateHttpIgnoreRuleResponse.
        :type domains: list[str]
        """
        self._domains = domains

    @property
    def url_logic(self):
        """Gets the url_logic of this UpdateHttpIgnoreRuleResponse.

        屏蔽规则url类型（前缀：prefix，等于：equal）

        :return: The url_logic of this UpdateHttpIgnoreRuleResponse.
        :rtype: str
        """
        return self._url_logic

    @url_logic.setter
    def url_logic(self, url_logic):
        """Sets the url_logic of this UpdateHttpIgnoreRuleResponse.

        屏蔽规则url类型（前缀：prefix，等于：equal）

        :param url_logic: The url_logic of this UpdateHttpIgnoreRuleResponse.
        :type url_logic: str
        """
        self._url_logic = url_logic

    @property
    def advanced(self):
        """Gets the advanced of this UpdateHttpIgnoreRuleResponse.

        :return: The advanced of this UpdateHttpIgnoreRuleResponse.
        :rtype: :class:`huaweicloudsdkedgesec.v2.HttpIgnoreRuleCondition`
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """Sets the advanced of this UpdateHttpIgnoreRuleResponse.

        :param advanced: The advanced of this UpdateHttpIgnoreRuleResponse.
        :type advanced: :class:`huaweicloudsdkedgesec.v2.HttpIgnoreRuleCondition`
        """
        self._advanced = advanced

    @property
    def conditions(self):
        """Gets the conditions of this UpdateHttpIgnoreRuleResponse.

        命中条件

        :return: The conditions of this UpdateHttpIgnoreRuleResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v2.HttpIgnoreRuleCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this UpdateHttpIgnoreRuleResponse.

        命中条件

        :param conditions: The conditions of this UpdateHttpIgnoreRuleResponse.
        :type conditions: list[:class:`huaweicloudsdkedgesec.v2.HttpIgnoreRuleCondition`]
        """
        self._conditions = conditions

    @property
    def hit_num(self):
        """Gets the hit_num of this UpdateHttpIgnoreRuleResponse.

        命中次数

        :return: The hit_num of this UpdateHttpIgnoreRuleResponse.
        :rtype: int
        """
        return self._hit_num

    @hit_num.setter
    def hit_num(self, hit_num):
        """Sets the hit_num of this UpdateHttpIgnoreRuleResponse.

        命中次数

        :param hit_num: The hit_num of this UpdateHttpIgnoreRuleResponse.
        :type hit_num: int
        """
        self._hit_num = hit_num

    @property
    def update_time(self):
        """Gets the update_time of this UpdateHttpIgnoreRuleResponse.

        最后更新时间戳

        :return: The update_time of this UpdateHttpIgnoreRuleResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this UpdateHttpIgnoreRuleResponse.

        最后更新时间戳

        :param update_time: The update_time of this UpdateHttpIgnoreRuleResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def clear_time(self):
        """Gets the clear_time of this UpdateHttpIgnoreRuleResponse.

        上一次命中次数清零时间戳

        :return: The clear_time of this UpdateHttpIgnoreRuleResponse.
        :rtype: int
        """
        return self._clear_time

    @clear_time.setter
    def clear_time(self, clear_time):
        """Sets the clear_time of this UpdateHttpIgnoreRuleResponse.

        上一次命中次数清零时间戳

        :param clear_time: The clear_time of this UpdateHttpIgnoreRuleResponse.
        :type clear_time: int
        """
        self._clear_time = clear_time

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
        if not isinstance(other, UpdateHttpIgnoreRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

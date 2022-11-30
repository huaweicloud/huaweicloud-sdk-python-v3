# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Event2alarmRuleBodyTriggerPolicies:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'trigger_type': 'str',
        'period': 'int',
        'operator': 'str',
        'count': 'int',
        'level': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'trigger_type': 'trigger_type',
        'period': 'period',
        'operator': 'operator',
        'count': 'count',
        'level': 'level'
    }

    def __init__(self, id=None, name=None, trigger_type=None, period=None, operator=None, count=None, level=None):
        """Event2alarmRuleBodyTriggerPolicies

        The model defined in huaweicloud sdk

        :param id: 自增编号
        :type id: int
        :param name: 事件名称
        :type name: str
        :param trigger_type: 触发类型
        :type trigger_type: str
        :param period: 触发周期
        :type period: int
        :param operator: 比较符
        :type operator: str
        :param count: 触发次数
        :type count: int
        :param level: 告警等级
        :type level: str
        """
        
        

        self._id = None
        self._name = None
        self._trigger_type = None
        self._period = None
        self._operator = None
        self._count = None
        self._level = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if period is not None:
            self.period = period
        if operator is not None:
            self.operator = operator
        if count is not None:
            self.count = count
        if level is not None:
            self.level = level

    @property
    def id(self):
        """Gets the id of this Event2alarmRuleBodyTriggerPolicies.

        自增编号

        :return: The id of this Event2alarmRuleBodyTriggerPolicies.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Event2alarmRuleBodyTriggerPolicies.

        自增编号

        :param id: The id of this Event2alarmRuleBodyTriggerPolicies.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Event2alarmRuleBodyTriggerPolicies.

        事件名称

        :return: The name of this Event2alarmRuleBodyTriggerPolicies.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Event2alarmRuleBodyTriggerPolicies.

        事件名称

        :param name: The name of this Event2alarmRuleBodyTriggerPolicies.
        :type name: str
        """
        self._name = name

    @property
    def trigger_type(self):
        """Gets the trigger_type of this Event2alarmRuleBodyTriggerPolicies.

        触发类型

        :return: The trigger_type of this Event2alarmRuleBodyTriggerPolicies.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this Event2alarmRuleBodyTriggerPolicies.

        触发类型

        :param trigger_type: The trigger_type of this Event2alarmRuleBodyTriggerPolicies.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def period(self):
        """Gets the period of this Event2alarmRuleBodyTriggerPolicies.

        触发周期

        :return: The period of this Event2alarmRuleBodyTriggerPolicies.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this Event2alarmRuleBodyTriggerPolicies.

        触发周期

        :param period: The period of this Event2alarmRuleBodyTriggerPolicies.
        :type period: int
        """
        self._period = period

    @property
    def operator(self):
        """Gets the operator of this Event2alarmRuleBodyTriggerPolicies.

        比较符

        :return: The operator of this Event2alarmRuleBodyTriggerPolicies.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this Event2alarmRuleBodyTriggerPolicies.

        比较符

        :param operator: The operator of this Event2alarmRuleBodyTriggerPolicies.
        :type operator: str
        """
        self._operator = operator

    @property
    def count(self):
        """Gets the count of this Event2alarmRuleBodyTriggerPolicies.

        触发次数

        :return: The count of this Event2alarmRuleBodyTriggerPolicies.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Event2alarmRuleBodyTriggerPolicies.

        触发次数

        :param count: The count of this Event2alarmRuleBodyTriggerPolicies.
        :type count: int
        """
        self._count = count

    @property
    def level(self):
        """Gets the level of this Event2alarmRuleBodyTriggerPolicies.

        告警等级

        :return: The level of this Event2alarmRuleBodyTriggerPolicies.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this Event2alarmRuleBodyTriggerPolicies.

        告警等级

        :param level: The level of this Event2alarmRuleBodyTriggerPolicies.
        :type level: str
        """
        self._level = level

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
        if not isinstance(other, Event2alarmRuleBodyTriggerPolicies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

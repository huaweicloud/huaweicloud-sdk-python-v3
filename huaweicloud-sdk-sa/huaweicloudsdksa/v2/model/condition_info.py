# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConditionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'expression_type': 'str',
        'conditions': 'list[ConditionItem]',
        'logics': 'object',
        'cron': 'str',
        'schedule_type': 'str',
        'repeat_range': 'str',
        'repeat_count': 'str'
    }

    attribute_map = {
        'expression_type': 'expression_type',
        'conditions': 'conditions',
        'logics': 'logics',
        'cron': 'cron',
        'schedule_type': 'schedule_type',
        'repeat_range': 'repeat_range',
        'repeat_count': 'repeat_count'
    }

    def __init__(self, expression_type=None, conditions=None, logics=None, cron=None, schedule_type=None, repeat_range=None, repeat_count=None):
        """ConditionInfo

        The model defined in huaweicloud sdk

        :param expression_type: expression type, all, any, user_define
        :type expression_type: str
        :param conditions: Information of conditions.
        :type conditions: list[:class:`huaweicloudsdksa.v2.ConditionItem`]
        :param logics: Logic item of condition.
        :type logics: object
        :param cron: Cron 表达式
        :type cron: str
        :param schedule_type: schedule type, second hours...
        :type schedule_type: str
        :param repeat_range: 执行时间段 2021-01-30T23:00:00Z+0800
        :type repeat_range: str
        :param repeat_count: 重复次数
        :type repeat_count: str
        """
        
        

        self._expression_type = None
        self._conditions = None
        self._logics = None
        self._cron = None
        self._schedule_type = None
        self._repeat_range = None
        self._repeat_count = None
        self.discriminator = None

        if expression_type is not None:
            self.expression_type = expression_type
        if conditions is not None:
            self.conditions = conditions
        if logics is not None:
            self.logics = logics
        if cron is not None:
            self.cron = cron
        if schedule_type is not None:
            self.schedule_type = schedule_type
        if repeat_range is not None:
            self.repeat_range = repeat_range
        if repeat_count is not None:
            self.repeat_count = repeat_count

    @property
    def expression_type(self):
        """Gets the expression_type of this ConditionInfo.

        expression type, all, any, user_define

        :return: The expression_type of this ConditionInfo.
        :rtype: str
        """
        return self._expression_type

    @expression_type.setter
    def expression_type(self, expression_type):
        """Sets the expression_type of this ConditionInfo.

        expression type, all, any, user_define

        :param expression_type: The expression_type of this ConditionInfo.
        :type expression_type: str
        """
        self._expression_type = expression_type

    @property
    def conditions(self):
        """Gets the conditions of this ConditionInfo.

        Information of conditions.

        :return: The conditions of this ConditionInfo.
        :rtype: list[:class:`huaweicloudsdksa.v2.ConditionItem`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this ConditionInfo.

        Information of conditions.

        :param conditions: The conditions of this ConditionInfo.
        :type conditions: list[:class:`huaweicloudsdksa.v2.ConditionItem`]
        """
        self._conditions = conditions

    @property
    def logics(self):
        """Gets the logics of this ConditionInfo.

        Logic item of condition.

        :return: The logics of this ConditionInfo.
        :rtype: object
        """
        return self._logics

    @logics.setter
    def logics(self, logics):
        """Sets the logics of this ConditionInfo.

        Logic item of condition.

        :param logics: The logics of this ConditionInfo.
        :type logics: object
        """
        self._logics = logics

    @property
    def cron(self):
        """Gets the cron of this ConditionInfo.

        Cron 表达式

        :return: The cron of this ConditionInfo.
        :rtype: str
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        """Sets the cron of this ConditionInfo.

        Cron 表达式

        :param cron: The cron of this ConditionInfo.
        :type cron: str
        """
        self._cron = cron

    @property
    def schedule_type(self):
        """Gets the schedule_type of this ConditionInfo.

        schedule type, second hours...

        :return: The schedule_type of this ConditionInfo.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this ConditionInfo.

        schedule type, second hours...

        :param schedule_type: The schedule_type of this ConditionInfo.
        :type schedule_type: str
        """
        self._schedule_type = schedule_type

    @property
    def repeat_range(self):
        """Gets the repeat_range of this ConditionInfo.

        执行时间段 2021-01-30T23:00:00Z+0800

        :return: The repeat_range of this ConditionInfo.
        :rtype: str
        """
        return self._repeat_range

    @repeat_range.setter
    def repeat_range(self, repeat_range):
        """Sets the repeat_range of this ConditionInfo.

        执行时间段 2021-01-30T23:00:00Z+0800

        :param repeat_range: The repeat_range of this ConditionInfo.
        :type repeat_range: str
        """
        self._repeat_range = repeat_range

    @property
    def repeat_count(self):
        """Gets the repeat_count of this ConditionInfo.

        重复次数

        :return: The repeat_count of this ConditionInfo.
        :rtype: str
        """
        return self._repeat_count

    @repeat_count.setter
    def repeat_count(self, repeat_count):
        """Sets the repeat_count of this ConditionInfo.

        重复次数

        :param repeat_count: The repeat_count of this ConditionInfo.
        :type repeat_count: str
        """
        self._repeat_count = repeat_count

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
        if not isinstance(other, ConditionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

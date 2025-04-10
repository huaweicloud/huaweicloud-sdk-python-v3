# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TriggerPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trigger_type': 'str',
        'period': 'int',
        'operator': 'str',
        'count': 'int'
    }

    attribute_map = {
        'trigger_type': 'trigger_type',
        'period': 'period',
        'operator': 'operator',
        'count': 'count'
    }

    def __init__(self, trigger_type=None, period=None, operator=None, count=None):
        r"""TriggerPolicy

        The model defined in huaweicloud sdk

        :param trigger_type: 触发类型，accumulative: 累计触发，immediately: 立即触发。
        :type trigger_type: str
        :param period: 触发周期，选择累计触发时需设置该参数，默认单位为s，支持5分钟、20分钟、1小时、4小时、24小时。
        :type period: int
        :param operator: 比较符，支持&#39;&gt;&#39;和&#39;&gt;&#x3D;&#39;。
        :type operator: str
        :param count: 触发次数，选择累计触发时需设置该参数。
        :type count: int
        """
        
        

        self._trigger_type = None
        self._period = None
        self._operator = None
        self._count = None
        self.discriminator = None

        self.trigger_type = trigger_type
        if period is not None:
            self.period = period
        if operator is not None:
            self.operator = operator
        if count is not None:
            self.count = count

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this TriggerPolicy.

        触发类型，accumulative: 累计触发，immediately: 立即触发。

        :return: The trigger_type of this TriggerPolicy.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this TriggerPolicy.

        触发类型，accumulative: 累计触发，immediately: 立即触发。

        :param trigger_type: The trigger_type of this TriggerPolicy.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def period(self):
        r"""Gets the period of this TriggerPolicy.

        触发周期，选择累计触发时需设置该参数，默认单位为s，支持5分钟、20分钟、1小时、4小时、24小时。

        :return: The period of this TriggerPolicy.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this TriggerPolicy.

        触发周期，选择累计触发时需设置该参数，默认单位为s，支持5分钟、20分钟、1小时、4小时、24小时。

        :param period: The period of this TriggerPolicy.
        :type period: int
        """
        self._period = period

    @property
    def operator(self):
        r"""Gets the operator of this TriggerPolicy.

        比较符，支持'>'和'>='。

        :return: The operator of this TriggerPolicy.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this TriggerPolicy.

        比较符，支持'>'和'>='。

        :param operator: The operator of this TriggerPolicy.
        :type operator: str
        """
        self._operator = operator

    @property
    def count(self):
        r"""Gets the count of this TriggerPolicy.

        触发次数，选择累计触发时需设置该参数。

        :return: The count of this TriggerPolicy.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this TriggerPolicy.

        触发次数，选择累计触发时需设置该参数。

        :param count: The count of this TriggerPolicy.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, TriggerPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
